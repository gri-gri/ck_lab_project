from base import *


class DataBaseReader:
    def __init__(self):
        pass

    # Препод создает новую лабу
    @classmethod
    def teacher_creates_new_lab(cls, name, list_of_gds_with_settings, content):
        labs.append([labs[-1][0] + 1, name, content])
        for i in list_of_gds_with_settings:
            cls.teacher_adds_gd_to_the_lab(labs[-1][0], i)

    # Препод добавляет ГП к лабе
    @staticmethod
    def teacher_adds_gd_to_the_lab(lab_id, gd_status_deadline):
        lab_gd.append([lab_id] + gd_status_deadline)

    # Возвращает все лабосдачи по выбранной лабе (только id)
    @staticmethod
    def get_deliv_labs_for_the_lab(lab_id):
        ret = []
        for i in lab_del_lab:
            if i[1] == lab_id:
                ret.append(i[0])
        return ret

    # Возвращает список лаб, созданных данным преподом (полностью строки)
    @classmethod
    def get_labs_of_the_teacher(cls, teacher_id):
        gds = set(cls.get_gps_of_the_teacher(teacher_id))
        teacher_labs = set()
        for i in lab_gd:
            if i[1] in gds:
                teacher_labs.add(i[0])
        ret = []
        for i in labs:
            if i[0] in teacher_labs:
                ret.append(i)
        return ret

    # Возвращает строку лабы и информацию по ГД, которым она назначена, по ее id
    @staticmethod
    def what_is_lab(lab_id):  # yep it's a reference
        ret = []
        for i in labs:
            if i[0] == lab_id:
                ret.append(i)
                break
        ret.append([])
        for i in lab_gd:
            if i[0] == lab_id:
                ret[-1].append(i)
        return ret

    # Оценивание лабосдачи
    @staticmethod
    def teacher_sets_mark(deliv_lab_id, mark, comm):
        for i in del_labs:
            if i[0] == deliv_lab_id:
                i[3] = mark
                i[4] = comm
                break

    # Возвращает список групп, в которых состоит студент
    @staticmethod
    def get_groups_of_the_student(student_id):
        ret = []
        for i in students_in_groups:
            if i[1] == student_id:
                ret.append(i[0])
        return ret

    # Возвращает список id лаб, назначенных данной группе (не ГД)
    @staticmethod
    def get_labs_for_the_group(group_id):
        gds = set()
        ret = []
        for i in group_disc:
            if i[1] == group_id:
                gds.add(i[0])
        for i in lab_gd:
            if i[1] in gds:
                ret.append(i[0])
        return ret

    # Новая лабосдача
    @staticmethod
    def add_deliv_lab(student_id, lab_id, content, date):
        del_labs.append([del_labs[-1][0] + 1, student_id, content, '', '', date])  # 1-ая пустая строка - дефолт оценки
        lab_del_lab.append([del_labs[-1][0], lab_id])

    # Строчка лабосдачи по id
    @staticmethod
    def deliv_lab_information(deliv_id):
        for i in del_labs:
            if i[0] == deliv_id:
                return i

    # Возвращает список id ГД препода
    @staticmethod
    def get_gps_of_the_teacher(teacher_id):
        ret = []
        for i in teacher_gd:
            if i[0] == teacher_id:
                ret.append(i[1])
        return ret

    # Удаление лабы
    @staticmethod
    def delete_lab(lab_id):
        for i in range(len(labs)):
            if labs[i][0] == lab_id:
                del labs[i]
                break
        for i in range(len(lab_gd) - 1, -1, -1):
            if lab_gd[i][0] == lab_id:
                del lab_gd[i]
        delete_del = []
        for i in range(len(lab_del_lab) - 1, -1, -1):
            if lab_del_lab[i][1] == lab_id:
                delete_del.append(lab_del_lab[i][0])
                del lab_del_lab[i]
        for i in range(len(del_labs) - 1, -1, -1):
            if del_labs[i][0] in delete_del:
                del del_labs[i]

    # Возвращает список строк всех лабосдач студента
    @staticmethod
    def get_all_deliv_labs_of_the_student(student_id):
        ret = []
        for i in del_labs:
            if i[1] == student_id:
                ret.append(i)
        return ret
