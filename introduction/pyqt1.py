from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Winner Identifier')
button = QPushButton('Generate')
text = QLabel('Click to find out the winner')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, stretch=1, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button,stretch=1, alignment = Qt.AlignCenter)
main_win.setLayout(line)

main_win.show()
app.exec_()
