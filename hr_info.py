        
         ######        #######   ##      ##   ##       ##      ##      ####### 
       ###    ###     ##         ##      ##   ##       ##      ##     ##       
     ###        ###   ##         ##      ##   ##       ##      ##     ##       
     ###        ###   ##         ##      ##   ##       ##      ##      #######       
     ###        ###   ##         ##      ##   ##       ##      ##            ##        
       ###    ###     ##         ##      ##   ##       ##      ##            ##       
         ######        #######    ########    #######   ########       ####### 


#Oculus
#philip youssef
#2020   



from PyQt5 import QtCore, QtGui, QtWidgets
import hr_info_code as func

class Ui_hr_info_edit_win(object):
    def setupUi(self, hr_info_edit_win,main_win):
        hr_info_edit_win.setObjectName("hr_info_edit_win")
        hr_info_edit_win.resize(480, 245)
        hr_info_edit_win.setMinimumSize(QtCore.QSize(480, 245))
        hr_info_edit_win.setMaximumSize(QtCore.QSize(480, 245))
        hr_info_edit_win.setStyleSheet("\n"
"background-color: rgb(21, 29, 47);")
        self.centralwidget = QtWidgets.QWidget(hr_info_edit_win)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"    background:rgb(31, 41, 64);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;}\n"
"\n"
"\n"
"QLabel,QCheckBox{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPushButton,QDateEdit,QTimeEdit,QListWidget,QSpinBox,QComboBox{\n"
"background-color: rgb(48, 64, 99);\n"
" border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
" padding: 0 8px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(21, 29, 45);\n"
"}\n"
"\n"
"QScrollBar{\n"
"width: 10px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-page:vertical ,QScrollBar::add-page:vertical{\n"
"background:rgb(24, 32, 49);}\n"
"\n"
"\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background-color:rgb(75, 134, 199);}\n"
"\n"
"\n"
"QComboBox:editable {\n"
"    background:qlineargradient(spread:pad, x1:0.478, y1:0, x2:0.494, y2:1, stop:0 rgba(73, 75, 135, 255), stop:1 rgba(33, 37, 70, 255));\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"background-color: rgb(10, 57, 170);\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    padding: 0 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hr_photo = QtWidgets.QPushButton(self.frame)
        self.hr_photo.setMinimumSize(QtCore.QSize(200, 200))
        self.hr_photo.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.hr_photo.setFont(font)
        self.hr_photo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hr_photo.setIcon(icon)
        self.hr_photo.setIconSize(QtCore.QSize(168, 152))
        self.hr_photo.setDefault(False)
        self.hr_photo.setFlat(True)
        self.hr_photo.setObjectName("hr_photo")
        self.gridLayout_2.addWidget(self.hr_photo, 0, 0, 4, 1)
        self.label_20 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 1, 1, 1)
        self.time_from = QtWidgets.QTimeEdit(self.frame)
        self.time_from.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.time_from.setObjectName("time_from")
        self.gridLayout_2.addWidget(self.time_from, 1, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 2, 1, 1, 1)
        self.time_to = QtWidgets.QTimeEdit(self.frame)
        self.time_to.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.time_to.setObjectName("time_to")
        self.gridLayout_2.addWidget(self.time_to, 2, 2, 1, 1)
        self.cancel = QtWidgets.QPushButton(self.frame)
        self.cancel.setMinimumSize(QtCore.QSize(0, 24))
        self.cancel.setObjectName("cancel")
        self.gridLayout_2.addWidget(self.cancel, 3, 1, 1, 1)
        self.ok = QtWidgets.QPushButton(self.frame)
        self.ok.setMinimumSize(QtCore.QSize(0, 24))
        self.ok.setObjectName("ok")
        self.gridLayout_2.addWidget(self.ok, 3, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        hr_info_edit_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(hr_info_edit_win)
        QtCore.QMetaObject.connectSlotsByName(hr_info_edit_win)

        #####

        func.start(self,main_win)
        #####

    def retranslateUi(self, hr_info_edit_win):
        _translate = QtCore.QCoreApplication.translate
        hr_info_edit_win.setWindowTitle(_translate("hr_info_edit_win", "HR info edit"))
        self.label_20.setText(_translate("hr_info_edit_win", "<html><head/><body><p align=\"right\">From:</p></body></html>"))
        self.label_21.setText(_translate("hr_info_edit_win", "<html><head/><body><p align=\"right\">To:</p></body></html>"))
        self.cancel.setText(_translate("hr_info_edit_win", "Cancel"))
        self.ok.setText(_translate("hr_info_edit_win", "Ok"))
        self.label_19.setText(_translate("hr_info_edit_win", "<html><head/><body><p align=\"center\">W O R K _  T I M E</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hr_info_edit_win = QtWidgets.QMainWindow()
    ui = Ui_hr_info_edit_win()
    ui.setupUi(hr_info_edit_win)
    hr_info_edit_win.show()
    sys.exit(app.exec_())
