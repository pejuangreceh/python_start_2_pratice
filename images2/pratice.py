from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt5.QtCore import Qt
app = QApplication([])
main_win = QWidget()
main_win.resize(700, 400)
main_win.setWindowTitle('Easy Editor')

folderButton = QPushButton('Folder')
listImage = QListWidget()
imageLabel = QLabel('Image')

left = QPushButton('Left')
right = QPushButton('Right')
mirror = QPushButton('Mirror')
sharpness = QPushButton('Sharpness')
bw = QPushButton('B & W')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

rowButton = QHBoxLayout()

col1.addWidget(folderButton)
col1.addWidget(listImage)

col2.addWidget(imageLabel)

rowButton.addWidget(left)
rowButton.addWidget(right)
rowButton.addWidget(mirror)
rowButton.addWidget(sharpness)
rowButton.addWidget(bw)

col2.addLayout(rowButton)

row.addLayout(col1,20)
row.addLayout(col2,80)

main_win.setLayout(row)
main_win.show()
app.exec_()