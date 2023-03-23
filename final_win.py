from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QVBoxLayout, 
        QLabel)

from instr_py import *
from asecond_win import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


    def get_index(self, index, text_index):
        self.final_txt_index = index
        self.final_workheart = text_index

    def initUI(self):
        self.index = QLabel(self.final_txt_index)
        self.workheart = QLabel(self.final_workheart)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index, alignment = Qt.AlignCenter) 
        self.layout_line.addWidget(self.workheart, alignment = Qt.AlignCenter)          
        self.setLayout(self.layout_line)

if __name__ == "__main__":
    print('final')
    app = QApplication([])
    fw = FinalWin()
    app.exec_()