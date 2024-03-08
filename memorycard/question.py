from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)


app = QApplication([])
window = QWidget()

window.setWindowTitle('Memo Card')


'''Interface for the Memory Card Application'''
btn_OK = QPushButton('Answer') # answer button
lb_Question = QLabel('What year was Moscow founded?') # question text


RadioGroupBox = QGroupBox("Answer options") # group on the screen for radio buttons with answers
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')
# rbtn_5 = QRadioButton('2000')


layout_ans1 = QHBoxLayout() #dasar
layout_ans2 = QVBoxLayout() # the vertical ones will be inside the horizontal ones
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)
# layout_ans3.addWidget(rbtn_5)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # columns are in the same line

RadioGroupBox.setLayout(layout_ans1) # “panel” with answer options is ready 


layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test results
layout_line3 = QHBoxLayout() # “Answer” button


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=1) # the button should be large
layout_line3.addStretch(1)


# Now let’s put the lines we’ve created one under one another:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between the content

def test():
    print("this is test")

btn_OK.clicked.connect(test) # check that the answer panel appears when the button is pressed

window.setLayout(layout_card)
window.show()
app.exec()
