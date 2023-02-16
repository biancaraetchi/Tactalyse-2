from datetime import datetime
import os
from flask import Blueprint, request, make_response
from flask import render_template
from flask_simplelogin import login_required
from werkzeug.utils import secure_filename
import config
from app.players import excel_service
from app.players.players_model import Players
import app.players.scouting_service
import app.players.radar_service
import pandas as pd
from app.players.dates_model import DatesModel
import app.players.pdf_service
import uuid
import shutil
import app.players.scouting_compare_service
import app.players.radar_compare_service

player_controller = Blueprint('player_controller', __name__)
YEARS_FRAME = [3, 4]

comparitive = False

LEAGUES = ['Premier League', 'Championship', 'La Liga', 'Eredivisie', 'Ligue 1', 'Serie A', 'Bundesliga']
POSITIONS = ['Goalkeeper','Full Back','Center Back','Defensive Midfielder', 'Attacking Midfielder', 'Winger', 'Striker'
             ]
seasons = ['2022-2023']

@player_controller.route('/', methods = ['GET'])
@login_required
def index():
    return render_template('LeagueForm.html', positions=POSITIONS, leagues = LEAGUES)

@player_controller.route('/create-report-form-1', methods = ['GET'])
@login_required
def league_file_upload_form():
    return render_template('LeagueForm.html', positions=POSITIONS, leagues = LEAGUES)

@player_controller.route('/create-report-form-2', methods = ['POST'])
@login_required
def player_form():
    id = uuid.uuid1()
    position = request.form.get("position")
    excel = request.files['excel']
    excel_df = excel_service.header_adder(pd.ExcelFile(excel).parse())

    # create a folder with id name
    path = os.getcwd()
    dir = ""
    print(path)
    try:
        if path[0] == '/':
            dir = path + config.DIRECTORY_FOR_FILE_SAVE_UNIX
            dir = dir + str(id)
        else:
            dir = path + config.DIRECTORY_FOR_FILE_SAVE_WINDOWS
            dir = dir + str(id)

        os.mkdir(dir)
    except FileExistsError:
        os.rmdir(dir)
        os.mkdir(dir)

    # save excel to this folder
    excel_df.to_excel(os.path.join(dir, secure_filename(excel.filename)))
    stats = app.players.radar_service.fetch_stat_list(excel_df, position)


    # Load Names from Excel File to an array
    i = 0
    names = []
    for named in stats.index:
        names.append(named)
        i += 1

    return render_template('PlayerForm.html', id = id ,names = names,
                           time_frames=YEARS_FRAME, position = position, filename = excel.filename, seasons = seasons)


@player_controller.route('/create-report-form-3', methods = ['POST'])
@login_required
def generate_graphs():

    league_file_name = request.form.get("league_file_name")
    league = request.form.get("league")
    id = request.form.get("id")
    name = request.form.get("name")
    position = request.form.get("position")
    height = request.form.get("height")
    agent = request.form.get("agent")
    club = request.form.get("club")
    dob = datetime.strptime(request.form.get("dob"), '%Y-%m-%d')
    country = request.form.get("country")
    signing_date = datetime.strptime(request.form.get("signing-date"), '%Y-%m-%d')
    end_date = datetime.strptime(request.form.get("end-date"), '%Y-%m-%d')
    time_frame = request.form.get("time_frame")
    player_file = request.files['excel']
    profile_picture = request.files['profile-pic']
    dates = DatesModel()
    dates.year_frame = time_frame
    dates.year = signing_date.year
    dates.month = signing_date.month
    dates.day = signing_date.day
    season = request.form.get('season')

    compare = False

    if request.form.get("compare"):
        compare = True

    folder_dir = ""
    path = os.getcwd()

    if path[0] == '/':
        folder_dir = path + config.DIRECTORY_FOR_FILE_SAVE_UNIX
        folder_dir = folder_dir + str(id)
        league_file_path = folder_dir + '/' +secure_filename(league_file_name)
    else:
        folder_dir = path+config.DIRECTORY_FOR_FILE_SAVE_WINDOWS
        folder_dir = folder_dir + str(id)
        league_file_path = folder_dir + '\\'+secure_filename(league_file_name)

    print(league_file_path)
    stats = app.players.radar_service.fetch_stat_list(pd.ExcelFile(league_file_path).parse(), position)
    filename = ''
    if not compare:
        app.players.scouting_service.run(player_file.stream.read(), dates,end_date, folder_dir)
        filename = app.players.radar_service.run(position, folder_dir, name, stats, season)

    else:
        app.players.scouting_compare_service.run(player_file.stream.read(),request.files["excel2"].stream.read() ,dates,end_date, folder_dir)
        filename = app.players.radar_compare_service.run(position,folder_dir,name,request.form.get("name2"),stats,season)

    profile_picture.save(os.path.join(folder_dir, secure_filename(profile_picture.filename)))
    print(filename + ": generated radar plot")

    return  render_template('RadarPlotGenerated.html',name=name,position=position,height=height,dob=request.form.get("dob"),
                     agent=agent,club=club,country=country, league= league, id = id , filename = filename, profile_filename = profile_picture.filename)


@player_controller.route('/create-report-form-4', methods = ['POST'])
@login_required
def generate_pdf():

    player = Players(name= request.form.get("name"),position=request.form.get("position"),height=request.form.get("height"),dob=datetime.strptime(request.form.get("dob"), '%Y-%m-%d'),
                     agent=request.form.get("agent"),club=request.form.get("club"),country=request.form.get("country"), league= request.form.get("league"))
    folder_dir = ""
    path = os.getcwd()

    if path[0] == '/':
        folder_dir = path + config.DIRECTORY_FOR_FILE_SAVE_UNIX
        folder_dir = folder_dir + str(request.form.get("id"))
    else:
        folder_dir = path + config.DIRECTORY_FOR_FILE_SAVE_WINDOWS
        folder_dir = folder_dir + str(request.form.get("id"))

    pdf = app.players.pdf_service.generate(player, os.path.join(folder_dir, secure_filename(request.form.get("profile_filename"))),
                                           request.form.get("filename"), folder_dir)
    response = make_response(pdf)
    response.headers.set('Content-Disposition', 'attachment', filename=player.name + '.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    shutil.rmtree(folder_dir)

    return response
