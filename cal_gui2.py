from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import math as mt
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ahmed`s Calculator :)")
        self.setGeometry(140,150,450,450)
        #flags=QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
        #self.setWindowFlags(flags)
        self.calc()
        self.showNormal()

    def action_close(self):
        self.window.destroy
    def action_equal(self):
        a=self.label.text()
        try:
            ans=eval(a)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong Input")
    def action_plus(self):
        text=self.label.text()
        self.label.setText(text + " + ")
    def action_minus(self):
        text=self.label.text()
        self.label.setText(text + " - ")
    def action_div(self):
        text=self.label.text()
        self.label.setText(text + " / ")
    def action_mul(self):
        text=self.label.text()
        self.label.setText(text + " * ")
    def action_point(self):
        text=self.label.text()
        self.label.setText(text + ".")
    def action0(self):
        text=self.label.text()
        self.label.setText(text + "0") 
    def action1(self):
        text=self.label.text()
        self.label.setText(text + "1")
    def action2(self):
        text=self.label.text()
        self.label.setText(text + "2")
    def action3(self):
        text=self.label.text()
        self.label.setText(text + "3")
    def action4(self):
        text=self.label.text()
        self.label.setText(text + "4")
    def action5(self):
        text=self.label.text()
        self.label.setText(text + "5")
    def action6(self):
        text=self.label.text()
        self.label.setText(text + "6")
    def action7(self):
        text=self.label.text()
        self.label.setText(text + "7")  
    def action8(self):
        text=self.label.text()
        self.label.setText(text + "8")
    def action9(self):
        text=self.label.text()
        self.label.setText(text + "9")
    def action_clear(self):
        self.label.setText("")
    def action_del(self):
        text=self.label.text()
        self.label.setText(text[:len(text)-1])
    def action_fac(self):
        text=self.label.text()
        try:
            a=int(text)
            ans=mt.factorial(a)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong Input")
    
    def calc(self):
        grid = QGridLayout()
        self.label=QLabel(self)
        #lb1=QLabel()
        self.label.setStyleSheet("QLabel""{""border : 5px solid black;""background : white;""}")
       # self.label.setAlignment(Qt.AlignRight)
        
        self.label.setFont(QFont('Arial', 22))
        
        self.setLayout(grid)
        grid.addWidget(self.label,0,0,1,4)
        names=["Clear","Del","OFF","x!", 
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+"]
        buttons=[]
        positions=[(i, j) for i in range(1,6) for j in range(4)]
   
        for position,name in zip(positions,names):
            if name=="":
                continue
            button=QPushButton(name,self)
            button.setMinimumHeight(60)
            grid.addWidget(button,*position)
            buttons.append(button)
        buttons[0].clicked.connect(self.action_clear)
        buttons[1].clicked.connect(self.action_del)
        buttons[2].clicked.connect(self.action_close)
        buttons[3].clicked.connect(self.action_fac)
        buttons[4].clicked.connect(self.action7)
        buttons[5].clicked.connect(self.action8)
        buttons[6].clicked.connect(self.action9)
        buttons[7].clicked.connect(self.action_div)
        buttons[8].clicked.connect(self.action4)
        buttons[9].clicked.connect(self.action5)
        buttons[10].clicked.connect(self.action6)
        buttons[11].clicked.connect(self.action_mul)
        buttons[12].clicked.connect(self.action1)
        buttons[13].clicked.connect(self.action2)
        buttons[14].clicked.connect(self.action3)
        buttons[15].clicked.connect(self.action_minus)
        buttons[16].clicked.connect(self.action0)
        buttons[17].clicked.connect(self.action_point)
        buttons[18].clicked.connect(self.action_equal)
        buttons[19].clicked.connect(self.action_plus)
            



App=QApplication(sys.argv)
window=Calculator()
sys.exit(App.exec())
  
        