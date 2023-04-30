# Tactalyse-2
Repository for the Tactalyse-2 project, part of the Software Engineering course. For this project, we need to generate pdfs with different types of graphs, based on data submitted by the user on the API call.

## PDF-Generator: How to run
To install the pre-requisites for the project, you have to have python installed on your system. If you have it, run `pip3 install -r requirements.txt` from the root folder.

To run the project through a Docker container, run `docker build -t test-image .` and then start the project on your localhost:5000 by running `docker run -p 5000:5000 test-image`. To perform API calls, we would recommend working with a tool such as Postman. There is one endpoint that runs our app - `/pdf`. You need the following query parameters: `league-file`, `player-file`, `player-name`. Inside `app/pdf_generator/resources/test_data` you will find a league file - `ENG2.xlsx` and multiple player files following the `Player stats {first name initial} {last name}.xlsx` format. Upload any of them as query parameters to Postman and add the `player-name` field as well.

For quick access and report generation, we have set up a test file with all the necessary resources already loaded, `test_main.py`. To run it as a python script, run `python -u "d:\Uni work\SoftwareEng\Tactalyse-2\test_main.py"` from the root folder.
    
