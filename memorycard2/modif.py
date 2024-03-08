from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)


app = QApplication([])


btn_OK = QPushButton('Answer') 
lb_Question = QLabel('The most difficult question in the world!') 

RadioGroupBox = QGroupBox("Answer options")
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)

# create the result
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('are you correct or not?') 
lb_Correct = QLabel('the answer will be here!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox) 
# hide the result
# AnsGroupBox.hide()



layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # this button should be big
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spacing the content
AnsGroupBox.hide()

# ----------------------------------------------------------
# The widgets and mockups have been created. Next, the functions: 
# ----------------------------------------------------------

def show_result():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    btn_OK.setText("Next Question")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Answer")

def test():
    if btn_OK.text() == "Answer":
        print("Pindah ke Aswer")
        show_result()
    else:
        print("Pindah ke QUestion")
        show_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(test) # check that the answer panel appears when the button is pressed
window.show()
app.exec()
