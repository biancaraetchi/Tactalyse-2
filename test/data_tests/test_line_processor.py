from app.data.preprocessors.line_processor import LineProcessor
import unittest
import os
import pandas as pd


class TestLineProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Change the CWD to the root folder
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        os.chdir(root_dir)

    def setUp(self):
        self.processor = LineProcessor()

    def test_get_stats_GK(self):
        gk_stats = ["Total actions / successful",
                    "Passes / accurate",
                    "Long passes / accurate",
                    "Dribbles / successful",
                    "Duels / won",
                    "Aerial duels / won",
                    "Interceptions",
                    "Defensive duels / won",
                    "Loose ball duels / won",
                    "Sliding tackles / successful",
                    "Clearances",
                    "Fouls",
                    "Yellow cards",
                    "Red cards",
                    "Fouls suffered",
                    "Received passes",
                    "Conceded goals",
                    "xCG",
                    "Shots against",
                    "Exits",
                    "Goal kicks",
                    "Short goal kicks",
                    "Long goal kicks"]
        result = self.processor.get_columns_line_plots('GK').to_list()
        self.assertEqual(gk_stats, result)

    def test_get_stats_FB(self):
        fb_stats = ["Total actions / successful",
                    "Passes / accurate",
                    "Long passes / accurate",
                    "Crosses / accurate",
                    "Dribbles / successful",
                    "Duels / won",
                    "Aerial duels / won",
                    "Interceptions",
                    "Losses / own half",
                    "Recoveries / opp. half",
                    "Defensive duels / won",
                    "Loose ball duels / won",
                    "Sliding tackles / successful",
                    "Clearances",
                    "Fouls",
                    "Yellow cards",
                    "Red cards",
                    "Shot assists",
                    "Offensive duels / won",
                    "Touches in penalty area",
                    "Progressive runs",
                    "Fouls suffered",
                    "Through passes / accurate",
                    "xA",
                    "Second assists",
                    "Passes to final third / accurate",
                    "Passes to penalty area / accurate",
                    "Received passes",
                    "Forward passes / accurate",
                    "Back passes / accurate",
                    "Exits",
                    "Passes to GK / accurate"]
        result = self.processor.get_columns_line_plots('FB').to_list()
        self.assertEqual(fb_stats, result)

    def test_get_stats_CB(self):
        cb_stats = ["Total actions / successful",
                    "Passes / accurate",
                    "Long passes / accurate",
                    "Dribbles / successful",
                    "Duels / won",
                    "Aerial duels / won",
                    "Interceptions",
                    "Losses / own half",
                    "Recoveries / opp. half",
                    "Defensive duels / won",
                    "Loose ball duels / won",
                    "Sliding tackles / successful",
                    "Clearances",
                    "Fouls",
                    "Yellow cards",
                    "Red cards",
                    "Shot assists",
                    "Offensive duels / won",
                    "Fouls suffered",
                    "Through passes / accurate",
                    "Passes to final third / accurate",
                    "Passes to penalty area / accurate",
                    "Received passes",
                    "Forward passes / accurate",
                    "Back passes / accurate",
                    "Exits",
                    "Passes to GK / accurate"]
        result = self.processor.get_columns_line_plots('CB').to_list()
        self.assertEqual(cb_stats, result)

    def test_get_stats_DM(self):
        dm_stats = ["Total actions / successful",
                    "Passes / accurate",
                    "Long passes / accurate",
                    "Dribbles / successful",
                    "Duels / won",
                    "Aerial duels / won",
                    "Interceptions",
                    "Losses / own half",
                    "Recoveries / opp. half",
                    "Defensive duels / won",
                    "Loose ball duels / won",
                    "Sliding tackles / successful",
                    "Clearances",
                    "Fouls",
                    "Yellow cards",
                    "Red cards",
                    "Shot assists",
                    "Offensive duels / won",
                    "Fouls suffered",
                    "Through passes / accurate",
                    "Passes to final third / accurate",
                    "Passes to penalty area / accurate",
                    "Received passes",
                    "Forward passes / accurate",
                    "Back passes / accurate",
                    "Exits",
                    "Passes to GK / accurate"]
        result = self.processor.get_columns_line_plots('DM').to_list()
        self.assertEqual(dm_stats, result)

    def test_get_stats_AM(self):
        am_stats = ["Total actions / successful",
                    "Goals",
                    "Assists",
                    "Shots / on target",
                    "xG",
                    "Passes / accurate",
                    "Crosses / accurate",
                    "Dribbles / successful",
                    "Duels / won",
                    "Aerial duels / won",
                    "Interceptions",
                    "Losses / own half",
                    "Recoveries / opp. half",
                    "Defensive duels / won",
                    "Loose ball duels / won",
                    "Sliding tackles / successful",
                    "Clearances",
                    "Fouls",
                    "Yellow cards",
                    "Red cards",
                    "Shot assists",
                    "Offensive duels / won",
                    "Touches in penalty area",
                    "Progressive runs",
                    "Fouls suffered",
                    "Through passes / accurate",
                    "xA",
                    "Second assists",
                    "Passes to final third / accurate",
                    "Passes to penalty area / accurate",
                    "Received passes",
                    "Forward passes / accurate",
                    "Back passes / accurate"]
        result = self.processor.get_columns_line_plots('AM').to_list()
        self.assertEqual(am_stats, result)

    def test_get_stats_WI(self):
        wi_stats = ["Total actions / successful",
                    "Goals",
                    "Assists",
                    "Shots / on target",
                    "xG",
                    "Passes / accurate",
                    "Crosses / accurate",
                    "Dribbles / successful",
                    "Duels / won",
                    "Aerial duels / won",
                    "Interceptions",
                    "Losses / own half",
                    "Recoveries / opp. half",
                    "Defensive duels / won",
                    "Loose ball duels / won",
                    "Sliding tackles / successful",
                    "Clearances",
                    "Fouls",
                    "Yellow cards",
                    "Red cards",
                    "Shot assists",
                    "Offensive duels / won",
                    "Touches in penalty area",
                    "Progressive runs",
                    "Fouls suffered",
                    "Through passes / accurate",
                    "xA",
                    "Second assists",
                    "Passes to final third / accurate",
                    "Passes to penalty area / accurate",
                    "Received passes"]
        result = self.processor.get_columns_line_plots('WI').to_list()
        self.assertEqual(wi_stats, result)

    def test_get_stats_ST(self):
        st_stats = ["Total actions / successful",
                    "Goals",
                    "Assists",
                    "Shots / on target",
                    "xG",
                    "Passes / accurate",
                    "Crosses / accurate",
                    "Dribbles / successful",
                    "Duels / won",
                    "Aerial duels / won",
                    "Interceptions",
                    "Losses / own half",
                    "Recoveries / opp. half",
                    "Defensive duels / won",
                    "Loose ball duels / won",
                    "Sliding tackles / successful",
                    "Clearances",
                    "Fouls",
                    "Yellow cards",
                    "Red cards",
                    "Shot assists",
                    "Offensive duels / won",
                    "Touches in penalty area",
                    "Progressive runs",
                    "Fouls suffered",
                    "Through passes / accurate",
                    "xA",
                    "Second assists",
                    "Passes to final third / accurate",
                    "Passes to penalty area / accurate",
                    "Received passes"]
        result = self.processor.get_columns_line_plots('ST').to_list()
        self.assertEqual(st_stats, result)


if __name__ == "__main__":
    unittest.main()
