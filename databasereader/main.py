from base import *


class DataBaseReader:
    def __init__(self):
        pass

    # Препод создает новую лабу
    def new_lab(self, name, list_of_gds_with_settings, content):
        labs.append([labs[-1][0] + 1, name, content])
        for i in list_of_gds_with_settings:
            self.add_gd_to_lab(labs[-1][0], i)

    # Препод добавляет ГП к лабе
    def add_gd_to_lab(self, lab_id, gd_status_deadline):
        lab_gd.append([lab_id] + gd_status_deadline)

    # Возвращает все лабосдачи по выбранной лабе (строки полностью)
    def teacher_to_del_labs(self, lab_id):
        ret = []
        for i in lab_del_lab:
            if i[1] == lab_id:
                for j in del_labs:
                    if j[0] == i[0]:
                        ret.append(j)
        return ret

    # Возвращает список лаб, созданных данным преподом (полностью строки)
    def teacher_to_labs(self, teacher_id):
        gds = set(self.teacher_to_gds(teacher_id))
        l = set()
        for i in lab_gd:
            if i[1] in gds:
                l.add(i[0])
        ret = []
        for i in labs:
            if i[0] == i:
                ret.append(i)
        return ret

    # Возвращает строку лабы по ее id
    def what_is_lab(self, lab_id):  # yep it's a reference
        for i in labs:
            if i[0] == lab_id:
                return i

    # Оценивание лабосдачи
    def set_mark(self, del_lab_id, mark, comm):
        for i in del_labs:
            if i[0] == del_lab_id:
                i[3] = mark
                i[4] = comm
                break

    # Возвращает список групп, в которых состоит студент
    def get_all_student_groups(self, student_id):
        ret = []
        for i in students_in_groups:
            if i[1] == student_id:
                ret.append(i[0])
        return ret

    # Возвращает список id лаб, назначенных данной группе (не ГД)
    def student_to_labs(self, group_id):
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
    def add_del_lab(self, student_id, lab_id, content, date):
        del_labs.append([del_labs[-1][0] + 1, student_id, content, -1, '', date])
        lab_del_lab.append([del_labs[-1][0], lab_id])

    # Строчка лабосдачи по id
    def del_lab(self, del_id):
        for i in del_labs:
            if i[0] == del_id:
                return i

    # Возвращает список id ГД препода
    def teacher_to_gds(self, teacher_id):
        ret = []
        for i in teacher_gd:
            if i[0] == teacher_id:
                ret.append(i[1])
        return ret

    # Удаление лабы
    def delete_lab(self, lab_id):
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
