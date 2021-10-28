base_labs = [
    ['lab1', 'name1', 'subj1', ['m3100', 'm3101'], 'blabla.txt'],
    ['lab1', 'name1', 'subj2', ['m3101'], 'bla.txt'],
    ['lll', 'name3', 'subj4', ['b25'], 'nice_try.txt']
]

base_students = [
    ['m3100', 's1', 's2', 's3'],
    ['m3101', 's4', 's5', 's6'],
    ['m3102', 's7'],
    ['m3105', 's8'],
    ['b25', 's1', 's5', 's6']
]

base_groups = [
    ['m3100', 'subj1', 'name1'],
    ['m3100', 'subj3', 'name2'],
    ['m3101', 'subj1', 'name1'],
    ['m3102', 'subj2', 'name1'],
    ['m3105', 'subj3', 'name2'],
    ['b25', 'subj4', 'name3']
]


class Teacher:
    def __init__(self, name):
        global base_groups
        self.name = name
        self.subjects = {}
        for i in base_groups:
            if i[2] == name:
                if i[1] in self.subjects:
                    self.subjects[i[1]].append(i[0])
                else:
                    self.subjects[i[1]] = [i[0]]

    def make_new_lab(self):
        global base_labs
        print("Choose the subject:")
        for i in self.subjects:
            print("\t" + i)
        subj = input()
        print("Choose the groups:")
        for i in self.subjects[subj]:
            print("\t" + i)
        groups = []
        gr = input()
        while True:
            if gr == '-1':
                if len(groups):
                    break
            groups.append(gr)
            gr = input()
        print("Name of the file:")
        lab_text = input()
        while True:
            print("Name of lab:")
            flag = True
            lab_name = input()
            lab_mass = [lab_name, self.name, subj, groups]
            for i in base_labs:
                if i[:-1] == lab_mass:
                    flag = False
            if flag:
                break
        base_labs.append(lab_mass + [lab_text])


class Student:
    def __init__(self, name):
        global base_students
        self.name = name
        self.groups = []
        for i in base_students:
            if name in i:
                self.groups.append((i[0]))

    def see_labs(self):
        global base_labs
        print("Choose group:")
        for i in self.groups:
            print('\t' + i)
        group = input()
        print("Choose subject:")
        for i in base_groups:
            if i[0] == group:
                print('\t' + i[1])
        subject = input()
        print("Labs:")
        for i in base_labs:
            if (i[2] == subject) and (group in i[3]):
                print("\tLab '{}' by {}, subject {}: {}".format(i[0], i[1], subject, i[4]))


hi = Student('s1')
hi.see_labs()
bye = Teacher('name1')
bye.make_new_lab()
hi.see_labs()
