import unittest
from utils import data_processing
from exceptions import *


class TestDataProcessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        function_name = "data_processing"
        cls.base_msg = f"\n Verifique se sua função `{function_name}` está %s."

    def test_negative_titles_error(self):
        """
        Testa se a funçao data_processing
        levanta a exeção NegativeTitlesError
        da maneira correta
        """

        data = {
            "name": "França",
            "titles": -3,
            "top_scorer": "Zidane",
            "fifa_code": "FRA",
            "first_cup": "2022-10-18"
        }
        msg = self.base_msg % "levantando a mensagem de erro correta"

        with self.assertRaises(NegativeTitlesError) as err:
            data_processing(data)

        self.assertEqual(str(err.exception), 'titles cannot be negative', msg)

        data = {
            "name": "França",
            "titles": -1,
            "top_scorer": "Zidane",
            "fifa_code": "FRA",
            "first_cup": "2018-10-18"
        }
        msg = self.base_msg % "levantando a mensagem de erro correta"

        with self.assertRaises(NegativeTitlesError) as err:
            data_processing(data)

        self.assertEqual(str(err.exception), 'titles cannot be negative', msg)


    def test_invalid_year_cup_error(self):
        """
        Testa se a funçao data_processing
        levanta a exeção InvalidYearCupError
        da maneira correta
        """

        data = {
            "name": "França",
            "titles": 3,
            "top_scorer": "Zidane",
            "fifa_code": "FRA",
            "first_cup": "1932-10-18"
        }
        msg = self.base_msg % "levantando a mensagem de erro correta"

        with self.assertRaises(InvalidYearCupError) as err:
            data_processing(data)

        self.assertEqual(str(err.exception), 'there was no world cup this year', msg)
        data = {
            "name": "França",
            "titles": 3,
            "top_scorer": "Zidane",
            "fifa_code": "FRA",
            "first_cup": "2023-10-18"
        }
        msg = self.base_msg % "levantando a mensagem de erro correta"

        with self.assertRaises(InvalidYearCupError) as err:
            data_processing(data)

        self.assertEqual(str(err.exception), 'there was no world cup this year', msg)


    def test_impossible_titles_error(self):
        """
        Testa se a funçao data_processing
        levanta a exeção ImpossibleTitlesError
        da maneira correta
        """

        data = {
            "name": "França",
            "titles": 9,
            "top_scorer": "Zidane",
            "fifa_code": "FRA",
            "first_cup": "2002-10-18",
        }
        msg = self.base_msg % "levantando a mensagem de erro correta"

        with self.assertRaises(ImpossibleTitlesError) as err:
            data_processing(data)

        self.assertEqual(str(err.exception), 'impossible to have more titles than disputed cups', msg)

        data = {
            "name": "França",
            "titles": 3,
            "top_scorer": "Zidane",
            "fifa_code": "FRA",
            "first_cup": "2018-10-18",
        }
        msg = self.base_msg % "levantando a mensagem de erro correta"

        with self.assertRaises(ImpossibleTitlesError) as err:
            data_processing(data)

        self.assertEqual(str(err.exception), 'impossible to have more titles than disputed cups', msg)
