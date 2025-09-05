from PyQt5.QtWidgets import QApplication, QMessageBox
from random import choice, shuffle 
from time import sleep

app = QApplication([])
from main_window import *

count_ask = 0
count_right = 0

class Question():
    def __init__(self, question, answer, wrong_answer1,wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer 
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True 

    def got_right(self):
        global count_ask, count_right
        count_ask += 1
        count_right += 1

    def got_wrong(self):
        global count_ask
        count_ask += 1

q1 = Question("Яблуко", "apple", "application", "pinapple", "apply")
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')





radio_buttons = [answer_1,answer_2,answer_3,answer_4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_Question.setText(cur_q.question)
    Correct.setText(cur_q.answer)
    shuffle(radio_buttons)
    
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == Correct.text():
                cur_q.got_right()
                Result.setText('Вірно!')
                answer.setChecked(False)
                break
    else:
        Result.setText('Не вірно!')
        cur_q.got_wrong()
    RadioGroup.setExclusive(True)

def rest():
    win_card.hide()
    time = box_Minutes.value() * 60
    sleep(time)
    win_card.show()

btn_sleep.clicked.connect(rest)

def click_ok():
    if btn_OK.text() == 'Відповісти':
        check()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    else:
        new_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()

        btn_OK.setText('Відповісти')

btn_OK.clicked.connect(click_ok)

def menu_generation():
    if count_ask == 0:
        c = 0
    else:
        c = (count_right / count_ask) * 100
    
    print(f"Разів відповіли: {count_ask}\n"
          f"Вірних відповідей: {count_right}\n"
          f"Успішність: {round(c, 2)}%"
          )
    

menu.clicked.connect(menu_generation)


app.exec_()
