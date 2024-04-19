from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Dialogue for opening files (and folders)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)

app = QApplication([])
win = QWidget()
win.resize(700, 500) 
win.setWindowTitle('Easy Editor')
btn_dir = QPushButton("Folder")



row = QHBoxLayout() 
col1 = QVBoxLayout()  
col2 = QVBoxLayout()  
col1.addWidget(btn_dir)

row.addLayout(col1,20)
row.addLayout(col2,80)
win.setLayout(row)
win.show()
app.exec()