from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

card_width, card_height = 600, 500
menu_card = QWidget()
menu_card.resize(card_width, card_height)
menu_card.move(0,0)
menu_card.setWindowTitle("Memory card")

line = QVBoxLayout()

text_stat = QLabel(f"Статистика")
text_ask = QLabel("Кількість відповідей:")
text_right = QLabel("Вірних відповідей:")
text_Percent = QLabel("Успішність:")
back = QPushButton("Назад")

line.addWidget(text_stat)
line.addWidget(text_ask)
line.addWidget(text_right)
line.addWidget(text_Percent)
line.addWidget(back)

menu_card.setLayout(line)
menu_card.hide()
