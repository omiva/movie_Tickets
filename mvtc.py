from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sys
import datetime

global a  # screen no.
global ticket  # no. of tickets
global x  # time
global cityName  # city name
global movieName  # movie name
global tName  # theater name
global scno  # screen no.


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400, 400, 500, 500)
    win.setWindowTitle("MOVIE BOOKING APP")
    win.setStyleSheet("background: #161219;")
    win.show()
    sys.exit(app.exec_())


window()


def display():
    print('the ticket is successfully booked ')
    print('details')
    print('city name: ', cityName)
    print('theater name: ', tName)
    print('movie name: ', movieName)
    print('movie screen: ', a)
    print('number of tickets: ', ticket)
    print('time :', x)
    return 0


def theater():
    global ticket, scno, a
    print("which screen do you want to watch movie: ")
    scr = {1: 'SCREEN 1', 2: 'SCREEN 2', 3: 'SCREEN 3', 4: 'back to movie selection'}
    con = input('do you wish to view the available screens screening the movie?(yes/no): ')
    if con == 'yes':
        for sno, scr_no in scr.items():
            print("{}:{}".format(sno, scr_no))
    else:
        return 0

    a = int(input("choose your screen: "))
    if a == 1:
        print('-' * 8 + scr[a] + '-' * 8)
        a = scr[a]
    elif a == 2:
        print('-' * 8 + scr[a] + '-' * 8)
        a = scr[a]
    elif a == 3:
        print('-' * 8 + scr[a] + '-' * 8)
        a = scr[a]
    elif a == 4:
        inox()
        return 0
    print(a)
    seats = [50, 45, 41]
    for scno in seats:
        if a == 'SCREEN 1':
            scno = seats[0]
        elif a == 'SCREEN 2':
            scno = seats[1]
        elif a == 'SCREEN 3':
            scno = seats[1]
    print(scno)
    ticket = int(input("Enter the number of tickets you want to purchase: "))
    if ticket > scno:
        print("SORRY! IT'S HOUSEFULL\nBut you can try looking for a different screen\n")
        theater()
    else:
        scno -= ticket
        timing(a)
        return ticket


def timing(a):
    global x
    print("THE AVAILABLE SLOTS FOR THE NEXT 5 DAYS ARE:\n")
    curr_date = datetime.date.today()
    for i in range(1, 6):
        curr_date += datetime.timedelta(days=1)
        dates = {i: curr_date}
        for sno, mov_date in dates.items():
            print("{}:{}".format(sno, mov_date))
        # ADD CONDITIONAL STATEMENTS AND SEPARATE DATE INPUT AND TIME INPUT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
    time1 = {1: "10.00-1.00", 2: "1.10-4.10", 3: "4.20-7.20", 4: "7.30-10.30"}
    time2 = {1: "10.15-1.15", 2: "1.25-4.25", 3: "4.35-7.35", 4: "7.45-10.45"}
    time3 = {1: "10.30-1.30", 2: "1.40-4.40", 3: "4.50-7.50", 4: "8.00-10.45"}
    t = int(input("select the day: "))
    if a == 'SCREEN 1':
        print(time1)
        input("choose your time:")
        x = time1[t]
        print("successful!, enjoy movie at " + x)

    elif a == 'SCREEN 2':
        print(time2)
        input("choose your time:")
        x = time2[t]
        print("successful!, enjoy movie at " + x)

    elif a == 'SCREEN 3':
        print(time2)
        input("choose your time:")
        x = time3[t]
        print("successful!, enjoy movie at " + x)
    display()

def movie(theater):
    if theater == 1:
        inox()
    elif theater == 2:
        inox()  # need update
    elif theater == 3:
        inox()  # need update
    elif theater == 4:
        city()

    else:

        print("wrong choice")


def inox():
    global movieName
    mvs = {1: 'No time to die', 2: 'Venom', 3: 'Far from home', 4: 'back to theaters'}
    con = input('do you wish to view available shows in Inox?(yes/no): ')
    if con == 'yes':
        for sno, mov_name in mvs.items():
            print("{}:{}".format(sno, mov_name))

    mn = int(input("choose your movie:"))
    if mn == 1:
        print('-' * 8 + mvs[mn] + '-' * 8)
        movieName = mvs[mn]
    elif mn == 2:
        print('-' * 8 + mvs[mn] + '-' * 8)
        movieName = mvs[mn]
    elif mn == 3:
        print('-' * 8 + mvs[mn] + '-' * 8)
        movieName = mvs[mn]
    elif mn == 4:
        bglr_thtr()
        return 0
    theater()


def bglr_thtr():  # ask for theater name. used dictionary so that more theaters can be added with conviniance
    global tName
    tr = {1: 'Inox', 2: 'Cinepolis', 3: 'PVR', 4: 'back to cities'}
    con = input('do you wish to view available theaters in?(yes/no): ')
    if con == 'yes':
        for sno, tr_name in tr.items():
            print("{}:{}".format(sno, tr_name))
    a = int(input("choose your theater: "))
    if a == 1:
        print('-' * 8 + tr[a] + '-' * 8)
        tName = tr[a]

    elif a == 2:
        print('-' * 8 + tr[a] + '-' * 8)
        tName = tr[a]

    elif a == 3:
        print('-' * 8 + tr[a] + '-' * 8)
        tName = tr[a]

    elif a == 4:
        movie(a)
    else:
        print("wrong choice\n")
    movie(a)
    return a


def theater_name(loc):
    global tName
    if loc == 1:
        bglr_thtr()
    elif loc >= 2:
        print('NOT AVAILABLE\n\n')
        city()


def city():  # ask for city, used dictionary because more cities can be added easily
    global cityName
    print("----------------HEY WELCOME TO MOVIE TICKET BOOKING!----------------")
    cn = {1: 'Bangalore', 2: 'Mysore', 3: 'Chennai'}
    con = input('do you wish to view the cities with available theaters? (yes/no): ')
    if con == 'yes':
        # print('\n1.' + cn[1] + '\n2.' + cn[2] + '\n3.' + cn[3])
        for sno, place in cn.items():
            print("{}:{}".format(sno, place))
    else:
        return 0
    loc = int(input("choose your city: "))
    if loc == 1:

        print('-' * 8 + cn[loc] + '-' * 8)
        cityName = cn[loc]

    elif loc == 2:
        print('-' * 8 + cn[loc] + '-' * 8)  # unused
        cityName = cn[loc]

    elif loc == 3:
        print('-' * 8 + cn[loc] + '-' * 8)  # unused
        cityName = cn[loc]

    else:
        print("wrong choice")
    theater_name(loc)

city()
