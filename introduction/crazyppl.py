from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
 
app = QApplication([])
 
# main window:
my_win = QWidget()
my_win.setWindowTitle('Winner Identifier')
my_win.move(100, 100)
my_win.resize(400, 200)


#window widgets: button and label
button = QPushButton('Generate')
text = QLabel('Click to find out the winner')
winner = QLabel('?')


#widget layout
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)
 
#function that generates and displays a number
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Winner:')
 
#button click processing
button.clicked.connect(show_winner)


my_win.show()
app.exec_()
