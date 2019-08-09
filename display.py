import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from pynput.keyboard import Key, Controller
import time
import random
from image_proc import *
import mss
import mss.tools

# 843 383 - 981 497
swiper = Controller()


class mymainwindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
            )
        self.setGeometry(QtGui.QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignRight,
            QtCore.QSize(480, 280),
            QtGui.qApp.desktop().availableGeometry()))
        ## add widgets here
        button = QPushButton('Start', self)
        button.move(20,80)

        textbox = QLineEdit(self)
        textbox.setText("Swiping")
        textbox.move(20, 20)
        textbox.resize(180,40)

        pic_dif = QLineEdit(self)
        pic_dif.setText("Avgs")
        pic_dif.move(240, 20)
        pic_dif.resize(180,40)

        pic1 = QtGui.QLabel(self)
        pic1.move(20, 120)
        pic1.resize(138,114)

        pic2 = QtGui.QLabel(self)
        pic2.move(158, 120)
        pic2.resize(138,114)

        def get_pics(state):
            with mss.mss() as sct:
                # The screen part to capture
                monitor = {"top": 450, "left": 750, "width": 160, "height": 135}
                output = "screenshots/user_{}.png".format(state)

                # Grab the data
                sct_img = sct.grab(monitor)

                # Save to the picture file
                mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
                #print(output)

        def on_click(self):
            textbox.setText("Button clicked.")
            #get_pics("start")
            #pic1.setPixmap(QtGui.QPixmap("screenshots/user_start.png"))
            #pic1.setPixmap(QtGui.QPixmap("sct-{top}x{left}_{width}x{height}.png".format(**monitor)))
            #pic1.show()
            #swiper.press(Key.space)
            #swiper.release(Key.space)
            time.sleep(0.2)
            #show_curpic(self)
            swiping()
        button.clicked.connect(on_click)
        def show_curpic(self):
            get_pics("now")
            pic2.setPixmap(QtGui.QPixmap("screenshots/user_now.png"))
            pic2.show()
        def swiping():
            time.sleep(1)
            while True:
                count = 0
                time.sleep((random.randint(1,10)/10)+1)
                get_pics("start")
                pic1.setPixmap(QtGui.QPixmap("screenshots/user_start.png"))
                pic1.show()
                print(return_avgs())
                pic_dif.setText(str(return_avgs()))
                while return_avgs() >2 or return_avgs() <-2 and count <8:
                    print(return_avgs())
                    swiper.press(Key.space)
                    swiper.release(Key.space)
                    time.sleep(0.3)
                    show_curpic(self)
                    count = count+1
                    print(return_avgs())
                    pic_dif.setText(str(return_avgs()))
                swiper.press(Key.right)
                time.sleep(0.1)
                swiper.release(Key.right)


    def mousePressEvent(self, event):
        QtGui.qApp.quit()





app = QtGui.QApplication(sys.argv)
mywindow = mymainwindow()
mywindow.show()
app.exec_()
