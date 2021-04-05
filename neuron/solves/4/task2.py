""" Task2
Create classes for Student, BudgetStudent, ContractStudent, Group, Discipline, Tutor
"""


class Student:
    firstName = ''
    middleName = ''
    lastName = ''
    birthYear = 0
    startyear = 0

    def __init__(self, firstName, middleName, lastName, birthYear, startYear):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.birthYear = birthYear
        self.startYear = startYear


class BudgetStudent(Student):
    grant = 0

    def __init__(self, firstName, middleName, lastName, birthYear, startYear, grant):
        super().__init__(firstName, middleName, lastName, birthYear, startYear)
        self.grant = grant


class ContractStudent(Student):
    monthly_payment = 0

    def __init__(self, firstName, middleName, lastName, birthYear, startYear, monthly_payment):
        super().__init__(firstName, middleName, lastName, birthYear, startYear)
        self.monthly_payment = monthly_payment


class Group:
    group_number = ''
    students = []

    def __init__(self, group_number, students):
        self.group_number = group_number
        self.students = students


class Discipline:
    name = ''
    credit_amount = 0
    semester = 1

    def __init__(self, name, credit_amount, semester):
        self.credit_amount = credit_amount
        self.name = name
        self.semester = semester


class Tutor:
    firstName = ''
    middleName = ''
    lastName = ''
    birthYear = 0
    yearsWorking = 0
    disciplines = []

    def __init__(self, firstName, middleName, lastName, birthYear, yearsWorking, disciplines):
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
