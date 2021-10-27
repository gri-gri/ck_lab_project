from classes import *


STATUS_STUDENT = "student"
STATUS_TEACHER = "teacher"


class Database:
    def __init__(self):
        self.accounts_base = \
        """gri-gri;1234;1;student;Григорий Симонов;336970;1,2\nteacher;123456;2;teacher;Какой-то учитель;333333;2"""
        self.groups_and_disciplines_base = ""
        self.labs_base = ""
        self.lab_deliveries_base = ""

    def log_in(self, key_login, key_password):
        for line in self.accounts_base.split("\n"):
            login, password, id_, status, name, tabel_number, ids_of_groups_and_disciplines = line.split(";")
            if key_login == login and key_password == password:
                return Person(int(id_), status, name, tabel_number, list(map(int, ids_of_groups_and_disciplines.split(","))))
        raise KeyError(f"There is no account with login '{key_login}' and password '{key_password}'")
    
    def get_groups_and_disciplines(self):
        result = []
        for line in self.groups_and_disciplines_base.split("\n"):
            id_, group, discipline, ids_of_labs = line.split(";")
            result.append(GroupAndDiscipline(int(id_), group, discipline, list(map(int, ids_of_labs.split(",")))))
        return result
    
    def get_labs(self):
        result = []
        for line in self.labs_base.split("\n"):
            id_, name, ids_of_lab_deliveries = line.split(";")
            result.append(Lab(int(id_), name, list(map(int, ids_of_lab_deliveries.split(",")))))
        return result

    def get_lab_deliveries(self):
        result = []
        for line in self.lab_deliveries_base.split("\n"):
            id_, student_id, content, mark = line.split(";")
            result.append(LabDelivery(int(id_), int(student_id), content, mark))
        return result 


class Main:
    def __init__(self):
        self.database = Database()
        #self.groups_and_disciplines = self.database.get_groups_and_disciplines()
        #self.labs = self.database.get_labs()
        #self.lab_deliveries = self.database.get_lab_deliveries()
        self.main_loop()
    
    def main_loop(self):
        print("Программа запущена!")
        print("Нажмите Enter, чтобы выйти, или одну из следующих команд: login, unlogin")
        current_user = None
        while True:
            inp = input()
            if inp == "":
                print("Goodbye")
                break
            elif inp == "login":
                cur = input("Введите логин и пароль через пробел:\n")
                login, password = cur.split()
                current_user = self.log_in(login, password)
                print("Здравствуй, {}".format(current_user.name))
            elif inp == "unlogin":
                print("До свидания, {}".format(current_user.name))
                current_user = None
            else:
                print("Нажмите Enter, чтобы выйти, или одну из следующих команд: login, unlogin")

    def log_in(self, login, password):
        return self.database.log_in(login, password)
    
    

if __name__ == "__main__":
    main = Main()