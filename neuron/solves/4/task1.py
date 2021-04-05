import datetime

N = 13.0

""" Task 1
Create program that could sell tickets for masaster-classes
- each ticket has unique # and price
- there're 4 types of tickets: ordinary, preorder (>=90 days until), late (7-0 days until), student

Prices:
- preorder discount 30%
- student discount 50%
- late 20% on top

You can search by ticker number
YOu can get ticket price
You can view ticket
"""


class Ticket:
    id = 0
    price = 0.0
    sell_date = datetime.date.today()
    is_student = False
    event_date = datetime.date.today()

    """
    0=ordinary
    1=student
    2=preorder
    3=late
    """
    ticket_type = 0

    def __init__(self, id, is_student, sell_date, event_date):
        self.id = id
        self.is_student = is_student
        self.sell_date = sell_date
        self.event_date = event_date
        self.calculate_price()

    def __str__(self):
        types = {
            0: 'Ordinary',
            1: 'Student',
            2: 'Preorder',
            3: 'Late'
        }
        id_str = "id: " + str(self.id) + "\n"
        price_str = "Price: " + str(self.price) + "\n"
        sell_date_str = "Sell Date: " + str(self.sell_date) + "\n"
        types_str = "Ticket Type: " + \
            types.get(self.ticket_type, 'Unknown') + "\n"
        return id_str + price_str + sell_date_str + types_str

    def calculate_price(self):
        if self.is_student == True:
            self.price = N * 0.5
            self.ticket_type = 1
            return
        delta = (self.event_date - self.sell_date).days
        if delta > 90:
            self.price = N * 0.7
            self.ticket_type = 2
            return
        if delta <= 7:
            self.price = N * 1.2
            self.ticket_type = 3
            return
        self.price = N
        self.ticket_type = 0
        return self.price


class CommandOPalette:
    TICKET_DB = []

    def __init__(self):
        print('Command Palette created')

    def createTicket(self, event_date):
        sell_date = getDatetimeFromInput('sell date')
        is_student_ans = input('Is student? (y/N): ')

        is_student = False
        if is_student_ans.lower() == 'y':
            is_student = True

        ticket = Ticket(len(self.TICKET_DB), is_student, sell_date, event_date)
        self.TICKET_DB.append(ticket)
        return ticket

    def get_all_tickets(self):
        return self.TICKET_DB

    def print_all_tickets(self):
        for t in self.TICKET_DB:
            print(t)
        return

    def get_ticket_by_id(self, id):
        if id > len(self.TICKET_DB):
            return
        return self.TICKET_DB[id - 1]

    def print_ticket(self, id):
        ticket = self.get_ticket_by_id(id)
        if ticket:
            print('----')
            print(ticket)
            print('----')
        else:
            print('Not found')
        return

    def executeCommand(self, cmd, event_date):
        if cmd == 1:
            self.print_all_tickets()
        elif cmd == 2:
            id = int(input('Enter ticket id: '))
            self.print_ticket(id)
        elif cmd == 3:
            self.createTicket(event_date)
        elif cmd == 0:
            self.show_help()
        else:
            print('Invalid command')

    def show_help(self):
        print('0 - this help')
        print('1 - Prints all tickets')
        print('2 - Prints particulat ticket')
        print('3 - Create new ticket')


def getDatetimeFromInput(date_of_what):
    date_entry = input('Enter date of the ' +
                       date_of_what + ' in YYYY/MM/DD format: ')
    year, month, day = map(int, date_entry.split('/'))
    date = datetime.date(year, month, day)
    return date


PALETTE = CommandOPalette()
EVENT_DATE = getDatetimeFromInput('event')

while True:
    cmd = int(input('Print cmd number (0 for help): '))
    PALETTE.executeCommand(cmd, EVENT_DATE)
