import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton,QGridLayout,QLineEdit
class  MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,150)
        self.box = QLineEdit()
        self.box.setReadOnly(True)
        self.box.setAlignment(Qt.AlignRight) 
        self.num1 = QPushButton("1")
        self.num2 = QPushButton("2")
        self.num3 = QPushButton("3")
        self.num4 = QPushButton("4")
        self.num5 = QPushButton("5")
        self.num6 = QPushButton("6")
        self.num7 = QPushButton("7")
        self.num8 = QPushButton("8")
        self.num9 = QPushButton("9")
        self.num0 = QPushButton("0")
        self.plus = QPushButton("+")
        self.sub = QPushButton("-")
        self.mult = QPushButton("x")
        self.div = QPushButton("÷")
        self.AC = QPushButton("AC")
        self.equal = QPushButton("=")

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.box,0,0,1,4)
        grid_layout.addWidget(self.num1,1,0)
        grid_layout.addWidget(self.num2,1,1)
        grid_layout.addWidget(self.num3,1,2)
        grid_layout.addWidget(self.plus,1,3)
        grid_layout.addWidget(self.num4,2,0)
        grid_layout.addWidget(self.num5,2,1)
        grid_layout.addWidget(self.num6,2,2)
        grid_layout.addWidget(self.sub,2,3)
        grid_layout.addWidget(self.num7,3,0)
        grid_layout.addWidget(self.num8,3,1)
        grid_layout.addWidget(self.num9,3,2)
        grid_layout.addWidget(self.mult,3,3)
        grid_layout.addWidget(self.AC,4,0)
        grid_layout.addWidget(self.num0,4,1)
        grid_layout.addWidget(self.equal,4,2)
        grid_layout.addWidget(self.div,4,3)
        self.setLayout(grid_layout)

        self.num1.clicked.connect(self.action1)
        self.num2.clicked.connect(self.action2)
        self.num3.clicked.connect(self.action3)
        self.num4.clicked.connect(self.action4)
        self.num5.clicked.connect(self.action5)
        self.num6.clicked.connect(self.action6)
        self.num7.clicked.connect(self.action7)
        self.num8.clicked.connect(self.action8)
        self.num9.clicked.connect(self.action9)
        self.num0.clicked.connect(self.action0)
        self.plus.clicked.connect(self.action11)
        self.sub.clicked.connect(self.action12)
        self.mult.clicked.connect(self.action13)
        self.AC.clicked.connect(self.action14)
        self.div.clicked.connect(self.action15)
        self.equal.clicked.connect(self.action16)

    def action1(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "1")  
    def action2(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "2") 
    def action3(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "3") 
    def action4(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "4") 
    def action5(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "5") 
    def action6(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "6") 
    def action7(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "7") 
    def action8(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "8") 
    def action9(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "9") 
    def action0(self):
        current_text = self.box.text()      
        self.box.setText(current_text + "0") 
    def action11(self):
        global operator
        global plus_text
        operator = "+"
        current_text = self.box.text()  
        plus_text = current_text
        plus_text = int(plus_text)
        self.box.clear()
    def action12(self):
        global operator
        global sub_text
        operator = "-"
        current_text = self.box.text()  
        sub_text = current_text
        sub_text = int(sub_text)
        self.box.clear()
    def action13(self):
        global operator
        global mult_text
        operator = "x"
        current_text = self.box.text()  
        mult_text = current_text
        mult_text = int(mult_text)
        self.box.clear()
    def action14(self):
        self.box.clear()
    def action15(self):
        global operator
        global div_text
        operator = "/"
        current_text = self.box.text()  
        div_text = current_text
        div_text = int(div_text)
        self.box.clear()
    def action16(self):
        if operator == "+":
            current_text = self.box.text() 
            current_text = int(current_text)
            sum =  plus_text + current_text
            sum = str(sum)
            self.box.setText(sum)
        if operator == "-":
            current_text = self.box.text() 
            current_text = int(current_text)
            diff =  sub_text - current_text
            diff = str(diff)
            self.box.setText(diff) 
        if operator == "x":
            current_text = self.box.text() 
            current_text = int(current_text)
            prod =  mult_text * current_text
            prod = str(prod)
            self.box.setText(prod)
        if operator == "/":
            current_text = self.box.text() 
            current_text = int(current_text)
            try:
                quot =  div_text / current_text
                quot = str(quot)
                self.box.setText(quot)
            except  ZeroDivisionError:
                print("You cannot divide by zero")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()