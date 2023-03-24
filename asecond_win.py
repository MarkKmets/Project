from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit, )

import time
import final_win
import instr_py
from instr_py import txt_index
from instr_py import txt_workheart

class Testwin(QWidget):
    def __init__(self):
        self.aghx = 15
        super().__init__()
        self.timer1()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

        
    def timer1(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer_label = QLabel(self)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 64px;")
        self.time_remaining = 15
        self.timer.timeout.connect(self.update_time)
        self.update_time()
        # Create a QTimer to update the time remaining every second
        
        # Update the timer_label with the initial time remaining
    def start_timer(self):
        self.timer.start(1000)
        self.update_time()
    def set_appear(self):
        self.setWindowTitle(instr_py.txt_title)
        self.resize(instr_py.win_width, instr_py.win_height)
        self.move(instr_py.win_x, instr_py.win_y)
    def connects(self):
        self.btn_last.clicked.connect(self.next_click)
    def next_click(self):
        global txt_index
        global txt_workheart
        self.text_age = self.age_line.text()
        self.text_age = int(self.text_age)
        self.pulse_text = int(self.pulse_1.text())
        self.text_1 = int(self.test_3_l.text())
        self.last = int(self.last_line.text())
        self.pcd1 =  self.pulse_text + self.text_1 + self.last
        self.pcd2 = 4 * self.pcd1 - 200
        self.pcd = self.pcd2 / 10
        if self.text_age >= 15 and self.text_age <= 18:
            if self.pcd >= 15:
                txt_workheart = 'Працездатність серця: Погана'
            elif self.pcd >= 11 and self.pcd < 15:
                txt_workheart = 'Працездатність серця: Слабо'   
            elif self.pcd >= 6 and self.pcd <= 10:
                txt_workheart = 'Працездатність серця: Задовільно' 
            elif self.pcd >= 0.5 and self.pcd <= 5:
                txt_workheart = 'Працездатність серця: Добре'
            else:
                txt_workheart = 'Працездатність серця: Відмінно'
        elif self.text_age >=13 and self.text_age <= 14:
            if self.pcd >= 16.5:
                txt_workheart = 'Працездатність серця: Погана'
            elif self.pcd >= 12.5 and self.pcd < 16.5:
                txt_workheart = 'Працездатність серця: Слабо'   
            elif self.pcd >= 7.5 and self.pcd <= 11.4:
                txt_workheart = 'Працездатність серця: Задовільно' 
            elif self.pcd >= 2 and self.pcd <= 6.5:
                txt_workheart = 'Працездатність серця: Добре'
            else:
                txt_workheart = 'Працездатність серця: Відмінно'
        elif self.text_age >=11 and self.text_age <= 12:
            if self.pcd >= 18:
                txt_workheart = 'Працездатність серця: Погана'
            elif self.pcd >= 14 and self.pcd < 18:
                txt_workheart = 'Працездатнысть серця: Слабо'
            elif self.pcd >= 9 and self.pcd <= 13:
                txt_workheart = 'Працездатність серця: Задовільно' 
            elif self.pcd >= 6 and self.pcd <= 9:
                txt_workheart = 'Працездатність серця: Добре'
            else:
                txt_workheart = 'Працездатність серця: Відмінно'
        elif self.text_age >=9 and self.text_age <= 10:
            if self.pcd >= 19.5:
                txt_workheart = 'Працездатність серця: Погана'
            elif self.pcd >= 15.5 and self.pcd < 19.5:
                txt_workheart = 'Працездатність серця: Слабо'   
            elif self.pcd >= 10.5 and self.pcd <= 14.5:
                txt_workheart = 'Працездатність серця: Задовільно' 
            elif self.pcd >= 5 and self.pcd <= 9.5:
                txt_workheart = 'Працездатність серця: Добре'
            else:
                txt_workheart = 'Працездатність серця: Відмінно' 

        

        txt_index = "Індекс Руф'є: " + str(self.pcd)   
        if self.pcd == 6.9:
            self.pcd == 'ඞ'
        final_win.FinalWin.get_index(final_win.FinalWin,txt_index, txt_workheart)
        self.hide()
        self.fw = final_win.FinalWin()
    def initUI(self):
        # напрямки
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        # кнопки для r_line
        self.PIB = QLabel(instr_py.txt_name)
        self.pib_line = QLineEdit(instr_py.txt_hintname)
        self.label_age = QLabel(instr_py.txt_age)
        self.age_line = QLineEdit(instr_py.txt_hintage)
        self.test_1 = QLabel(instr_py.txt_test1)
        self.start_test = QPushButton(instr_py.txt_starttest1, self)
        self.pulse_1 = QLineEdit(instr_py.txt_hinttest1)
        self.test_2_l = QLabel(instr_py.txt_test2)
        self.pulse_2 = QPushButton(instr_py.txt_starttest2, self)
        self.test_3 = QLabel(instr_py.txt_test3)
        self.last_test = QPushButton(instr_py.txt_starttest3, self)
        self.test_3_l = QLineEdit(instr_py.txt_hinttest2)
        self.last_line = QLineEdit(instr_py.txt_hinttest3)
        self.btn_last = QPushButton(instr_py.txt_sendresults)
        self.btn_last.setGeometry(int(instr_py.win_width / 2), instr_py.win_height - 20, self.btn_last.width(), self.btn_last.height())

        # connects
        # довжина кнопок
        btn_width = int(instr_py.win_width / 6)
        line_edit_width = int(instr_py.win_width / 6)
        self.start_test.setFixedWidth(btn_width)
        self.pulse_1.setFixedWidth(btn_width)
        self.pulse_2.setFixedWidth(btn_width)
        self.last_test.setFixedWidth(btn_width)
        self.btn_last.setFixedWidth(btn_width)
        self.pib_line.setFixedWidth(line_edit_width)
        self.age_line.setFixedWidth(line_edit_width)
        self.test_3_l.setFixedWidth(line_edit_width)
        self.last_line.setFixedWidth(line_edit_width)
        # кнопка для l_line
        self.l_line.addWidget(self.timer_label)
        # додаємо віджети
        self.r_line.addWidget(self.PIB)
        self.r_line.addWidget(self.pib_line)
        self.r_line.addWidget(self.label_age)
        self.r_line.addWidget(self.age_line)
        self.r_line.addWidget(self.test_1)
        self.r_line.addWidget(self.start_test)
        self.r_line.addWidget(self.pulse_1)
        self.r_line.addWidget(self.test_2_l)
        self.r_line.addWidget(self.pulse_2)
        self.r_line.addWidget(self.test_3)
        self.r_line.addWidget(self.last_test)
        self.r_line.addWidget(self.test_3_l)
        self.r_line.addWidget(self.last_line)
        self.r_line.addWidget(self.btn_last)
        # додмаємо лінії
        self.h_line.addLayout(self.r_line)
        self.h_line.addLayout(self.l_line)
        self.setLayout(self.h_line)
        self.start_test.clicked.connect(self.start_timer)
    def update_time(self):
        if self.aghx > 0:
            self.timer_label.setText("00:00:" + str(int(self.aghx)))
            self.aghx -= 0.5
        else:
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication([])
    tw = Testwin()
    app.exec_()



