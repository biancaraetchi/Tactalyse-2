from .pdf import PDF


def generate_basic_pdf(league_df, player_name, main_pos, plot, line_plot):
    pdf = PDF()

    pdf.set_info(player_name, league_df, main_pos)

    pdf.alias_nb_pages()
    pdf.set_font('Arial', '', 12)
    pdf.set_draw_color(250, 51, 10)
    pdf.set_fill_color(255, 230, 230)
    pdf.set_title(player_name)
    pdf.add_page()

    pdf.print_title()
    pdf.print_basic_player_info()
    pdf.print_chapter('Radar Chart', 'This graph showcases general player statistics.')
    pdf.print_plot(plot)
    pdf.print_chapter('Line Plots', 'These plots showcase player statistics over time.')
    pdf.print_plot(line_plot)
    return pdf.output(dest='S')
