from unittest import TestCase
from main import DataBaseReader
import base


class TestDataBaseReader(TestCase):
    def test_use_case3(self):
        if DataBaseReader.get_labs_of_the_teacher(401) != [
            [601, 'Homework 3', 'Some sort of content about Fitch-notation.\nС переводом на русский?..'],
            [602, 'Homework 4', 'Binary logic. Sounds breathtaking...']
        ]:
            self.fail()
        self.assertEqual(DataBaseReader.what_is_lab(602), [[602, 'Homework 4', 'Binary logic. Sounds breathtaking...'],
                                                           [[602, 501, 0, '21.12.2021'], [602, 504, 1, '27.12.2021']]])

    def test_use_case6(self):
        self.assertEqual(DataBaseReader.get_deliv_labs_for_the_lab(601), [701, 703])
        self.assertEqual(DataBaseReader.deliv_lab_information(701),
                         [701, 301, 'Лень придумывать 1', '5', 'No SQRT', '01.11.2021'])
        DataBaseReader.teacher_sets_mark(701, '0', 'nice try')
        self.assertEqual(DataBaseReader.deliv_lab_information(701),
                         [701, 301, 'Лень придумывать 1', '0', 'nice try', '01.11.2021'])

    def test_use_case9(self):
        self.assertEqual(DataBaseReader.get_all_deliv_labs_of_the_student(301),
                         [[701, 301, 'Лень придумывать 1', '5', 'No SQRT', '01.11.2021'],
                         [702, 301, 'Лень придумывать 2', '10', '', '01.11.2021']])
        self.assertEqual(DataBaseReader.deliv_lab_information(701),
                         [701, 301, 'Лень придумывать 1', '5', 'No SQRT', '01.11.2021'])

    def test_use_case2(self):
        self.assertEqual(DataBaseReader.get_gps_of_the_teacher(403), [502, 505])
        DataBaseReader.teacher_creates_new_lab("cool", [[502, 1, "dunno"]], "aaaa")
        self.assertEqual(base.labs[-1], [610, "cool", "aaaa"])
        self.assertEqual(base.lab_gd[-1], [610, 502, 1, "dunno"])

    def test_use_case4_5(self):
        DataBaseReader.delete_lab(601)
        self.assertEqual((base.labs[0]), [602, 'Homework 4', 'Binary logic. Sounds breathtaking...'])
        self.assertEqual(base.lab_gd[0], [602, 501, 0, '21.12.2021'])
        self.assertEqual([702, 301, 'Лень придумывать 2', '10', '', '01.11.2021'], base.del_labs[0])
        self.assertEqual([702, 604], base.lab_del_lab[0])

    def test_use_case8(self):
        self.assertEqual(DataBaseReader.get_groups_of_the_student(302), [201, 204])
        self.assertEqual(DataBaseReader.get_labs_for_the_group(201), [601, 602, 604, 605, 606])
        DataBaseReader.add_deliv_lab(302, 602, "hi", "wat dis")
        self.assertEqual(base.del_labs[-1], [710, 302, "hi", "", "", "wat dis"])
        self.assertEqual(base.lab_del_lab[-1], [710, 602])
