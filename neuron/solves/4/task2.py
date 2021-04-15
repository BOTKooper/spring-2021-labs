
""" Task2
Create classes for Student, BudgetStudent, ContractStudent, Group, Discipline, Tutor
"""


class Student:
    id = 0
    firstName = ''
    middleName = ''
    lastName = ''
    birthYear = 0
    startyear = 0

    def __init__(self, id, firstName, middleName, lastName, birthYear, startYear):
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.birthYear = birthYear
        self.startYear = startYear

    def __str__(self):
        id_str = "id: " + str(self.id) + "\n"
        firstName_str = "First name: " + str(self.firstName) + "\n"
        middleName_str = "Middle name: " + str(self.middleName) + "\n"
        lastName_str = "last name: " + str(self.lastName) + "\n"
        birthYear_str = "Year of birth: " + str(self.birthYear) + "\n"
        startyear_str = "Started studying: " + str(self.startyear) + "\n"
        return id_str + firstName_str + middleName_str + lastName_str + birthYear_str + startyear_str



class BudgetStudent(Student):
    grant = 0.0

    def __init__(self, id, firstName, middleName, lastName, birthYear, startYear, grant):
        super().__init__(id, firstName, middleName, lastName, birthYear, startYear)
        self.grant = grant

    def __str__(self):
        s = super().__str__()
        return s + 'Grant: ' + str(self.grant) + "\n"


class ContractStudent(Student):
    monthly_payment = 0.0

    def __init__(self, id, firstName, middleName, lastName, birthYear, startYear, monthly_payment):
        super().__init__(id, firstName, middleName, lastName, birthYear, startYear)
        self.monthly_payment = monthly_payment

    def __str__(self):
        s = super().__str__()
        return s + 'Monthly payment: ' + str(self.monthly_payment) + "\n"


class Group:
    id = 0
    group_number = ''
    students = []

    def __init__(self, id, group_number, students):
        self.id = id
        self.group_number = group_number
        self.students = students

    def addStudent(self, student):
        self.students.append(student)

    def deleteStudent(self, id):
        tmp_sts = []
        for st in self.students:
            if st.id != id:
                tmp_sts.append(Student)
        self.students = tmp_sts

    def __str__(self):
        id_str = "id: " + str(self.id) + "\n"
        st_ids = ''
        for st in self.students:
            st_ids += str(st.id) + ", "
        student_ids = "Student IDs: " + st_ids



class Discipline:
    id = 0
    name = ''
    credit_amount = 0
    semester = 1

    def __init__(self, id, name, credit_amount, semester):
        self.id = id
        self.credit_amount = credit_amount
        self.name = name
        self.semester = semester


class Tutor:
    id = 0
    firstName = ''
    middleName = ''
    lastName = ''
    birthYear = 0
    yearsWorking = 0
    disciplines = []

    def __init__(self, id, firstName, middleName, lastName, birthYear, yearsWorking, disciplines):
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.birthYear = birthYear
        self.yearsWorking = yearsWorking
        self.disciplines = disciplines

    def TotalSubject(self):
        disciplines_count = len(self.disciplines)
        total_credits = 0
        for discipline in self.disciplines:
            total_credits += discipline.credit_amount
        return disciplines_count, total_credits

    def PrintTotalSubject(self):
        disciplines_count, total_credits = self.TotalSubject()
        print('Total disciplines: ' + str(disciplines_count))
        print('Total credits: ' + str(total_credits))

    def addDiscipline(self, discipline):
        self.disciplines.append(discipline)


class CommandPalette:
    TICKET_DB = []
    TUTOR_DB = []
    DISCIPLINE_DB = []
    GROUP_DB = []
    STUDENT_DB = []

    def __init__(self):
        print('Command Palette created')

    def get_entity_by_id(self, id, db):
        if id > len(db):
            return
        return db[id - 1]

    def createBudgetStudent(self, firstName, middleName, lastName, birthYear, startYear, grant):
        student = BudgetStudent(len(self.STUDENT_DB), firstName, middleName, lastName, birthYear, startYear, grant)
        self.STUDENT_DB.append(student)
        return student

    def createContractStudent(self, firstName, middleName, lastName, birthYear, startYear, monthly_payment):
        student = ContractStudent(len(self.STUDENT_DB), firstName, middleName, lastName, birthYear, startYear, monthly_payment)
        self.STUDENT_DB.append(student)
        return student

    def createDiscipline(self, name, credit_amount, semester):
        discipline = Discipline(len(self.DISCIPLINE_DB), name, credit_amount, semester)
        self.DISCIPLINE_DB.append(discipline)
        return discipline

    def createGroup(self, name, student_ids):
        group = Group(len(self.DISCIPLINE_DB), name, [])
        self.DISCIPLINE_DB.append(group)

        for id in student_ids:
            group.addStudent(self.get_entity_by_id(id, self.STUDENT_DB))

        return group

    def createTutor(self, firstName, middleName, lastName, birthYear, yearsWorking, discipline_ids):
        tutor = Tutor(len(self.TUTOR_DB), firstName, middleName, lastName, birthYear, yearsWorking, [])
        self.TUTOR_DB.append(tutor)

        for id in discipline_ids:
            tutor.addDiscipline(self.get_entity_by_id(id, self.DISCIPLINE_DB))

        return tutor


    def print_entity(self, id, db):
        entity = self.get_entity_by_id(id, db)
        if entity:
            print('----')
            print(entity)
            print('----')
        else:
            print('Not found')
        return

    def print_all_entities(self, db):
        for ent in db:
            self.print_entity(ent.id, db)


    def executeCommand(self, cmd):
        if cmd == 1:
            firstName = input('First name: ')
            middleName = input('Middle name: ')
            lastName = input('Last name: ')
            birthYear = int(input('Birth year: '))
            startYear = int(input('Study start year: '))
            typeofStudent = input('Pass type of student ((c)ontract/(b)udget): ').lower()

            if typeofStudent == 'c':
                monthly = float(input('Monthly payment: '))
                self.createContractStudent(firstName, middleName, lastName, birthYear, startYear, monthly)
            elif typeofStudent == 'b':
                monthly = float(input('Monthly grant: '))
                self.createBudgetStudent(firstName, middleName, lastName, birthYear, startYear, monthly)
            else:
                print('Invalid type of student')
        elif cmd == 2:
            name = input('Group name: ')
            student_ids = list(map(int, input("Type student ids in the single line (e.g. 1 5 ... 43 22): ").split()))
            self.createGroup(name, student_ids)
        elif cmd == 3:
            name = input('Discipline name: ')
            credit_amount = int(input('Credit amount: '))
            semester = int(input('Semester: '))
            self.createDiscipline(name, credit_amount, semester)
        elif cmd == 4:
            firstName = input('First name: ')
            middleName = input('Middle name: ')
            lastName = input('Last name: ')
            birthYear = int(input('Birth year: '))
            yearsWorking = int(input('Years working: '))
            disciplines_ids = list(map(int, input("Type disciplines ids in the single line (e.g. 1 5 ... 43 22): ").split()))
            self.createBudgetStudent(firstName, middleName, lastName, birthYear, yearsWorking, disciplines_ids)
        elif cmd == 5:
            self.print_all_entities(self.STUDENT_DB)
        elif cmd == 6:
            self.print_all_entities(self.GROUP_DB)
        elif cmd == 7:
            self.print_all_entities(self.DISCIPLINE_DB)
        elif cmd == 8:
            self.print_all_entities(self.TUTOR_DB)
        elif cmd == 9:
            id = int(input('Enter id: '))
            self.print_entity(id, self.STUDENT_DB)
        elif cmd == 10:
            id = int(input('Enter id: '))
            self.print_entity(id, self.GROUP_DB)
        elif cmd == 11:
            id = int(input('Enter id: '))
            self.print_entity(id, self.DISCIPLINE_DB)
        elif cmd == 12:
            id = int(input('Enter id: '))
            self.pprint_entity(id, self.TUTOR_DB)
        elif cmd == 0:
            self.show_help()
        else:
            print('Invalid command')


    def show_help(self):
        print('0 - this help')
        print('1 - Create Student')
        print('2 - Create Group')
        print('3 - Create Discipline')
        print('4 - Create Tutor')
        print('5 - Print all Students')
        print('6 - Print all Groups')
        print('7 - Print all Disciplines')
        print('8 - Print all Tutors')
        print('9 - Print Student by id')
        print('10 - Print Group by id')
        print('11 - Print Discipline by id')
        print('12 - Print Tutor by id')



PALETTE = CommandPalette()

while True:
    cmd = int(input('Print cmd number (0 for help): '))
    PALETTE.executeCommand(cmd)
