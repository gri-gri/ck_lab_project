class LabDelivery:
    def __init__(self, id_: int, student_id: int, content: str, mark: str):
        self.id = id_
        self.student_id = student_id
        self.content = content
        self.mark = mark


class Lab:
    def __init__(self, id_: int, name: str, ids_of_lab_deliveries: list):
        self.id = id_
        self.name = name
        self.ids_of_lab_deliveries = ids_of_lab_deliveries


class GroupAndDiscipline:
    def __init__(self, id_: int, group: str, discipline: str, ids_of_labs: list):
        self.id = id_
        self.group = group
        self.discipline = discipline
        self.ids_of_labs = ids_of_labs


class Person:
    def __init__(self, id_: int, status: str, name: str, tabel_number: str, ids_of_groups_and_disciplines: list):
        self.id = id_
        self.status = status
        self.name = name
        self.tabel_number = tabel_number
        self.ids_of_groups_and_disciplines = ids_of_groups_and_disciplines

"""
class Teacher(Person):
   def __init__(self, name: str, tabel_number: str, groups_and_disciplines: list):
        super().__init__(name, tabel_number, groups_and_disciplines)
        self.status = STATUS_TEACHER


class Student(Person):
   def __init__(self, name: str, tabel_number: str, groups_and_disciplines: list):
        super().__init__(name, tabel_number, groups_and_disciplines)
        self.status = STATUS_STUDENT
"""
