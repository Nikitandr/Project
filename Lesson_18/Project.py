import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from for_project import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.line1_place1.clicked.connect(self.line1place1)
        self.line1_place1.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place1 = True

        self.line1_place2.clicked.connect(self.line1place2)
        self.line1_place2.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place2 = True

        self.line1_place3.clicked.connect(self.line1place3)
        self.line1_place3.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place3 = True

        self.line1_place4.clicked.connect(self.line1place4)
        self.line1_place4.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place4 = True

        self.line1_place5.clicked.connect(self.line1place5)
        self.line1_place5.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place5 = True

        self.line1_place6.clicked.connect(self.line1place6)
        self.line1_place6.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place6 = True

        self.line1_place7.clicked.connect(self.line1place7)
        self.line1_place7.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place7 = True

        self.line1_place8.clicked.connect(self.line1place8)
        self.line1_place8.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place8 = True

        self.line1_place9.clicked.connect(self.line1place9)
        self.line1_place9.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place9 = True

        self.line1_place10.clicked.connect(self.line1place10)
        self.line1_place10.setStyleSheet("background-color: #DCDCDC")
        self.flag_line1_place10 = True

        self.line2_place1.clicked.connect(self.line2place1)
        self.line2_place1.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place1 = True

        self.line2_place2.clicked.connect(self.line2place2)
        self.line2_place2.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place2 = True

        self.line2_place3.clicked.connect(self.line2place3)
        self.line2_place3.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place3 = True

        self.line2_place4.clicked.connect(self.line2place4)
        self.line2_place4.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place4 = True

        self.line2_place5.clicked.connect(self.line2place5)
        self.line2_place5.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place5 = True

        self.line2_place6.clicked.connect(self.line2place6)
        self.line2_place6.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place6 = True

        self.line2_place7.clicked.connect(self.line2place7)
        self.line2_place7.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place7 = True

        self.line2_place8.clicked.connect(self.line2place8)
        self.line2_place8.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place8 = True

        self.line2_place9.clicked.connect(self.line2place9)
        self.line2_place9.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place9 = True

        self.line2_place10.clicked.connect(self.line2place10)
        self.line2_place10.setStyleSheet("background-color: #DCDCDC")
        self.flag_line2_place10 = True

        self.line3_place1.clicked.connect(self.line3place1)
        self.line3_place1.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place1 = True

        self.line3_place2.clicked.connect(self.line3place2)
        self.line3_place2.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place2 = True

        self.line3_place3.clicked.connect(self.line3place3)
        self.line3_place3.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place3 = True

        self.line3_place4.clicked.connect(self.line3place4)
        self.line3_place4.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place4 = True

        self.line3_place5.clicked.connect(self.line3place5)
        self.line3_place5.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place5 = True

        self.line3_place6.clicked.connect(self.line3place6)
        self.line3_place6.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place6 = True

        self.line3_place7.clicked.connect(self.line3place7)
        self.line3_place7.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place7 = True

        self.line3_place8.clicked.connect(self.line3place8)
        self.line3_place8.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place8 = True

        self.line3_place9.clicked.connect(self.line3place9)
        self.line3_place9.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place9 = True

        self.line3_place10.clicked.connect(self.line3place10)
        self.line3_place10.setStyleSheet("background-color: #DCDCDC")
        self.flag_line3_place10 = True

        self.line4_place1.clicked.connect(self.line4place1)
        self.line4_place1.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place1 = True

        self.line4_place2.clicked.connect(self.line4place2)
        self.line4_place2.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place2 = True

        self.line4_place3.clicked.connect(self.line4place3)
        self.line4_place3.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place3 = True

        self.line4_place4.clicked.connect(self.line4place4)
        self.line4_place4.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place4 = True

        self.line4_place5.clicked.connect(self.line4place5)
        self.line4_place5.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place5 = True

        self.line4_place6.clicked.connect(self.line4place6)
        self.line4_place6.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place6 = True

        self.line4_place7.clicked.connect(self.line4place7)
        self.line4_place7.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place7 = True

        self.line4_place8.clicked.connect(self.line4place8)
        self.line4_place8.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place8 = True

        self.line4_place9.clicked.connect(self.line4place9)
        self.line4_place9.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place9 = True

        self.line4_place10.clicked.connect(self.line4place10)
        self.line4_place10.setStyleSheet("background-color: #DCDCDC")
        self.flag_line4_place10 = True

        self.line5_place1.clicked.connect(self.line5place1)
        self.line5_place1.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place1 = True

        self.line5_place2.clicked.connect(self.line5place2)
        self.line5_place2.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place2 = True

        self.line5_place3.clicked.connect(self.line5place3)
        self.line5_place3.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place3 = True

        self.line5_place4.clicked.connect(self.line5place4)
        self.line5_place4.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place4 = True

        self.line5_place5.clicked.connect(self.line5place5)
        self.line5_place5.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place5 = True

        self.line5_place6.clicked.connect(self.line5place6)
        self.line5_place6.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place6 = True

        self.line5_place7.clicked.connect(self.line5place7)
        self.line5_place7.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place7 = True

        self.line5_place8.clicked.connect(self.line5place8)
        self.line5_place8.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place8 = True

        self.line5_place9.clicked.connect(self.line5place9)
        self.line5_place9.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place9 = True

        self.line5_place10.clicked.connect(self.line5place10)
        self.line5_place10.setStyleSheet("background-color: #DCDCDC")
        self.flag_line5_place10 = True

        self.buy.clicked.connect(self.bought)
        self.buy.setStyleSheet("background-color: #DCDCDC")

        self.ticket = 0
        self.total = 0

    def line1place1(self):
        if self.flag_line1_place1:
            self.line1_place1.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place1 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place1.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place1 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place2(self):
        if self.flag_line1_place2:
            self.line1_place2.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place2 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place2.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place2 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place3(self):
        if self.flag_line1_place3:
            self.line1_place3.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place3 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place3.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place3 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place4(self):
        if self.flag_line1_place4:
            self.line1_place4.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place4 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place4.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place4 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place5(self):
        if self.flag_line1_place5:
            self.line1_place5.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place5 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place5.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place5 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place6(self):
        if self.flag_line1_place6:
            self.line1_place6.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place6 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place6.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place6 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place7(self):
        if self.flag_line1_place7:
            self.line1_place7.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place7 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place7.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place7 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place8(self):
        if self.flag_line1_place8:
            self.line1_place8.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place8 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place8.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place8 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place9(self):
        if self.flag_line1_place9:
            self.line1_place9.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place9 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place9.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place9 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line1place10(self):
        if self.flag_line1_place10:
            self.line1_place10.setStyleSheet("background-color: #FF0000")
            self.flag_line1_place10 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line1_place10.setStyleSheet("background-color: #DCDCDC")
            self.flag_line1_place10 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place1(self):
        if self.flag_line2_place1:
            self.line2_place1.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place1 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place1.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place1 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place2(self):
        if self.flag_line2_place2:
            self.line2_place2.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place2 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place2.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place2 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place3(self):
        if self.flag_line2_place3:
            self.line2_place3.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place3 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place3.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place3 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place4(self):
        if self.flag_line2_place4:
            self.line2_place4.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place4 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place4.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place4 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place5(self):
        if self.flag_line2_place5:
            self.line2_place5.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place5 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place5.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place5 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place6(self):
        if self.flag_line2_place6:
            self.line2_place6.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place6 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place6.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place6 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place7(self):
        if self.flag_line2_place7:
            self.line2_place7.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place7 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place7.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place7 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place8(self):
        if self.flag_line2_place8:
            self.line2_place8.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place8 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place8.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place8 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place9(self):
        if self.flag_line2_place9:
            self.line2_place9.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place9 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place9.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place9 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line2place10(self):
        if self.flag_line2_place10:
            self.line2_place10.setStyleSheet("background-color: #FF0000")
            self.flag_line2_place10 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line2_place10.setStyleSheet("background-color: #DCDCDC")
            self.flag_line2_place10 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place1(self):
        if self.flag_line3_place1:
            self.line3_place1.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place1 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place1.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place1 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place2(self):
        if self.flag_line3_place2:
            self.line3_place2.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place2 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place2.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place2 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place3(self):
        if self.flag_line3_place3:
            self.line3_place3.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place3 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place3.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place3 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place4(self):
        if self.flag_line3_place4:
            self.line3_place4.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place4 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place4.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place4 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place5(self):
        if self.flag_line3_place5:
            self.line3_place5.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place5 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place5.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place5 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place6(self):
        if self.flag_line3_place6:
            self.line3_place6.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place6 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place6.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place6 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place7(self):
        if self.flag_line3_place7:
            self.line3_place7.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place7 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place7.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place7 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place8(self):
        if self.flag_line3_place8:
            self.line3_place8.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place8 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place8.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place8 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place9(self):
        if self.flag_line3_place9:
            self.line3_place9.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place9 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place9.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place9 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line3place10(self):
        if self.flag_line3_place10:
            self.line3_place10.setStyleSheet("background-color: #FF0000")
            self.flag_line3_place10 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line3_place10.setStyleSheet("background-color: #DCDCDC")
            self.flag_line3_place10 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place1(self):
        if self.flag_line4_place1:
            self.line4_place1.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place1 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place1.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place1 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place2(self):
        if self.flag_line4_place2:
            self.line4_place2.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place2 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place2.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place2 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place3(self):
        if self.flag_line4_place3:
            self.line4_place3.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place3 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place3.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place3 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place4(self):
        if self.flag_line4_place4:
            self.line4_place4.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place4 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place4.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place4 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place5(self):
        if self.flag_line4_place5:
            self.line4_place5.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place5 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place5.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place5 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place6(self):
        if self.flag_line4_place6:
            self.line4_place6.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place6 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place6.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place6 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place7(self):
        if self.flag_line4_place7:
            self.line4_place7.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place7 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place7.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place7 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place8(self):
        if self.flag_line4_place8:
            self.line4_place8.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place8 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place8.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place8 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place9(self):
        if self.flag_line4_place9:
            self.line4_place9.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place9 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place9.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place9 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line4place10(self):
        if self.flag_line4_place10:
            self.line4_place10.setStyleSheet("background-color: #FF0000")
            self.flag_line4_place10 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line4_place10.setStyleSheet("background-color: #DCDCDC")
            self.flag_line4_place10 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place1(self):
        if self.flag_line5_place1:
            self.line5_place1.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place1 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place1.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place1 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place2(self):
        if self.flag_line5_place2:
            self.line5_place2.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place2 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place2.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place2 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place3(self):
        if self.flag_line5_place3:
            self.line5_place3.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place3 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place3.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place3 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place4(self):
        if self.flag_line5_place4:
            self.line5_place4.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place4 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place4.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place4 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place5(self):
        if self.flag_line5_place5:
            self.line5_place5.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place5 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place5.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place5 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place6(self):
        if self.flag_line5_place6:
            self.line5_place6.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place6 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place6.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place6 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place7(self):
        if self.flag_line5_place7:
            self.line5_place7.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place7 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place7.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place7 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place8(self):
        if self.flag_line5_place8:
            self.line5_place8.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place8 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place8.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place8 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place9(self):
        if self.flag_line5_place9:
            self.line5_place9.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place9 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place9.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place9 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def line5place10(self):
        if self.flag_line5_place10:
            self.line5_place10.setStyleSheet("background-color: #FF0000")
            self.flag_line5_place10 = False
            self.ticket += 1
            self.total += 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))
        else:
            self.line5_place10.setStyleSheet("background-color: #DCDCDC")
            self.flag_line5_place10 = True
            self.ticket -= 1
            self.total -= 350
            self.tickets.setText('Билетов: {}'.format(self.ticket))
            self.totals.setText('Итого: {}'.format(self.total))

    def bought(self):
        if not self.flag_line1_place1:
            self.line1_place1.setEnabled(False)

        if not self.flag_line1_place2:
            self.line1_place2.setEnabled(False)

        if not self.flag_line1_place3:
            self.line1_place3.setEnabled(False)

        if not self.flag_line1_place4:
            self.line1_place4.setEnabled(False)

        if not self.flag_line1_place5:
            self.line1_place5.setEnabled(False)

        if not self.flag_line1_place6:
            self.line1_place6.setEnabled(False)

        if not self.flag_line1_place7:
            self.line1_place7.setEnabled(False)

        if not self.flag_line1_place8:
            self.line1_place8.setEnabled(False)

        if not self.flag_line1_place9:
            self.line1_place9.setEnabled(False)

        if not self.flag_line1_place10:
            self.line1_place10.setEnabled(False)

        if not self.flag_line2_place1:
            self.line2_place1.setEnabled(False)

        if not self.flag_line2_place2:
            self.line2_place2.setEnabled(False)

        if not self.flag_line2_place3:
            self.line2_place3.setEnabled(False)

        if not self.flag_line2_place4:
            self.line2_place4.setEnabled(False)

        if not self.flag_line2_place5:
            self.line2_place5.setEnabled(False)

        if not self.flag_line2_place6:
            self.line2_place6.setEnabled(False)

        if not self.flag_line2_place7:
            self.line2_place7.setEnabled(False)

        if not self.flag_line2_place8:
            self.line2_place8.setEnabled(False)

        if not self.flag_line2_place9:
            self.line2_place9.setEnabled(False)

        if not self.flag_line2_place10:
            self.line2_place10.setEnabled(False)

        if not self.flag_line3_place1:
            self.line3_place1.setEnabled(False)

        if not self.flag_line3_place2:
            self.line3_place2.setEnabled(False)

        if not self.flag_line3_place3:
            self.line3_place3.setEnabled(False)

        if not self.flag_line3_place4:
            self.line3_place4.setEnabled(False)

        if not self.flag_line3_place5:
            self.line3_place5.setEnabled(False)

        if not self.flag_line3_place6:
            self.line3_place6.setEnabled(False)

        if not self.flag_line3_place7:
            self.line3_place7.setEnabled(False)

        if not self.flag_line3_place8:
            self.line3_place8.setEnabled(False)

        if not self.flag_line3_place9:
            self.line3_place9.setEnabled(False)

        if not self.flag_line3_place10:
            self.line3_place10.setEnabled(False)

        if not self.flag_line4_place1:
            self.line4_place1.setEnabled(False)

        if not self.flag_line4_place2:
            self.line4_place2.setEnabled(False)

        if not self.flag_line4_place3:
            self.line4_place3.setEnabled(False)

        if not self.flag_line4_place4:
            self.line4_place4.setEnabled(False)

        if not self.flag_line4_place5:
            self.line4_place5.setEnabled(False)

        if not self.flag_line4_place6:
            self.line4_place6.setEnabled(False)

        if not self.flag_line4_place7:
            self.line4_place7.setEnabled(False)

        if not self.flag_line4_place8:
            self.line4_place8.setEnabled(False)

        if not self.flag_line4_place9:
            self.line4_place9.setEnabled(False)

        if not self.flag_line4_place10:
            self.line4_place10.setEnabled(False)

        if not self.flag_line5_place1:
            self.line5_place1.setEnabled(False)

        if not self.flag_line5_place2:
            self.line5_place2.setEnabled(False)

        if not self.flag_line5_place3:
            self.line5_place3.setEnabled(False)

        if not self.flag_line5_place4:
            self.line5_place4.setEnabled(False)

        if not self.flag_line5_place5:
            self.line5_place5.setEnabled(False)

        if not self.flag_line5_place6:
            self.line5_place6.setEnabled(False)

        if not self.flag_line5_place7:
            self.line5_place7.setEnabled(False)

        if not self.flag_line5_place8:
            self.line5_place8.setEnabled(False)

        if not self.flag_line5_place9:
            self.line5_place9.setEnabled(False)

        if not self.flag_line5_place10:
            self.line5_place10.setEnabled(False)

        self.ticket = 0
        self.total = 0
        self.tickets.setText('Билетов:')
        self.totals.setText('Итого:')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
