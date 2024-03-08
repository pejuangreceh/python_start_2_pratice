from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

import json


app = QApplication([])

'''Application interface'''
#application window parameters
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(900, 600)

#kiri
field_text = QTextEdit('')

# kanan 
list_notes = QListWidget()
list_notes_label = QLabel('List of notes')
button_note_create = QPushButton('Create Note')
button_note_del = QPushButton('Delete Note')
save_note = QPushButton('Save Note')

list_tags = QListWidget()
list_tags_label = QLabel('List of tags')
button_tags_create = QPushButton('Create the Tags')
button_tags_del = QPushButton('Delete the Tags')
save_tags = QPushButton('Simpan')

search_tag = QLineEdit('Enter tag...')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

# kiri
col_1.addWidget(field_text)

# kanan
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(save_note)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
row_5 = QHBoxLayout()
row_5.addWidget(search_tag)
col_2.addLayout(row_5)
row_3 = QHBoxLayout()
row_3.addWidget(button_tags_create)
row_3.addWidget(button_tags_del)
col_2.addLayout(row_3)
row_4 = QHBoxLayout()
row_4.addWidget(save_tags)
col_2.addLayout(row_4)



layout_notes.addLayout(col_1,stretch = 2)
layout_notes.addLayout(col_2,stretch = 1)
notes_win.setLayout(layout_notes)


#run the application
notes_win.show()
app.exec_()
