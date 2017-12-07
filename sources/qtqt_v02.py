
# coding: utf-8

# In[1]:


import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
# pyqt5를 지원하는 matplotlib 모듈 호출
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import pandas as pd
from pandas import Series, DataFrame


# In[2]:


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("Usn Chart Viewer v0.1")
        self.setWindowIcon(QIcon('icon.png'))

        self.lineEdit = QLineEdit()
        self.pushButton = QPushButton("차트그리기")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        
        # FigureCanvas 객체를 생성한다.
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addStretch(1) # 크기 조절이 가능한 공백을 추가

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        print(self.lineEdit.text())
        df = pd.read_sql('select * from usnnode', con = conn)
        ax = self.fig.add_subplot(111)
        ax.plot(df.index, df['temp'],label='temp')
        ax.plot(df.index, df['humi'],label='humi')
        ax.legend(loc='upper right')
        ax.grid()
        
        self.canvas.draw()


# In[3]:


conn = pymysql.connect(host='localhost', user='root', password='1234', db='usn', charset='utf8')


# In[ ]:


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

