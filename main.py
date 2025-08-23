from PyQt5.QtWidgets import QApplication
from random import choice, shuffle 
from time import sleep


app = QApplication([])
from main_window import *

class Question():
    def __init__(self, question, answer, wrong_answer1,wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer 
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True 
        self.count_ask = 0
        self.count_right = 0

    def got_right(self):
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_ask += 1

q1 = Question("Яблуко", "apple", "application", "pinapple", "apply")
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

app.exec_()
