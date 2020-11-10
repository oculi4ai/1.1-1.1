
from PyQt5 import QtCore, QtGui, QtWidgets
import company_info_code as func

class Ui_company_info_edit_win(object):
    def setupUi(self, company_info_edit_win,main_win):
        company_info_edit_win.setObjectName("company_info_edit_win")
        company_info_edit_win.resize(614, 245)
        company_info_edit_win.setMinimumSize(QtCore.QSize(614, 245))
        company_info_edit_win.setMaximumSize(QtCore.QSize(614, 245))
        company_info_edit_win.setStyleSheet("\n"
"background-color: rgb(21, 29, 47);")
        self.centralwidget = QtWidgets.QWidget(company_info_edit_win)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(592, 223))
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
        self.edit_section = QtWidgets.QPushButton(self.frame)
        self.edit_section.setMinimumSize(QtCore.QSize(0, 24))
        self.edit_section.setObjectName("edit_section")
        self.gridLayout_2.addWidget(self.edit_section, 3, 3, 1, 1)
        self.company_name = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_name.sizePolicy().hasHeightForWidth())
        self.company_name.setSizePolicy(sizePolicy)
        self.company_name.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.company_name.setFont(font)
        self.company_name.setText("")
        self.company_name.setClearButtonEnabled(True)
        self.company_name.setObjectName("company_name")
        self.gridLayout_2.addWidget(self.company_name, 0, 2, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 1, 1, 1)
        self.company_logo_but = QtWidgets.QPushButton(self.frame)
        self.company_logo_but.setEnabled(True)
        self.company_logo_but.setMinimumSize(QtCore.QSize(201, 201))
        self.company_logo_but.setMaximumSize(QtCore.QSize(201, 201))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.company_logo_but.setFont(font)
        self.company_logo_but.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/hr logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.company_logo_but.setIcon(icon)
        self.company_logo_but.setIconSize(QtCore.QSize(226, 166))
        self.company_logo_but.setCheckable(False)
        self.company_logo_but.setObjectName("company_logo_but")
        self.gridLayout_2.addWidget(self.company_logo_but, 0, 0, 4, 1)
        self.company_tele = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_tele.sizePolicy().hasHeightForWidth())
        self.company_tele.setSizePolicy(sizePolicy)
        self.company_tele.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.company_tele.setFont(font)
        self.company_tele.setText("")
        self.company_tele.setClearButtonEnabled(True)
        self.company_tele.setObjectName("company_tele")
        self.gridLayout_2.addWidget(self.company_tele, 2, 2, 1, 2)
        self.company_email = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_email.sizePolicy().hasHeightForWidth())
        self.company_email.setSizePolicy(sizePolicy)
        self.company_email.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.company_email.setFont(font)
        self.company_email.setText("")
        self.company_email.setClearButtonEnabled(True)
        self.company_email.setObjectName("company_email")
        self.gridLayout_2.addWidget(self.company_email, 1, 2, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 2, 1, 1, 1)
        self.section_count = QtWidgets.QSpinBox(self.frame)
        self.section_count.setMinimumSize(QtCore.QSize(0, 24))
        self.section_count.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.section_count.setObjectName("section_count")
        self.gridLayout_2.addWidget(self.section_count, 3, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 3, 1, 1, 1)
        self.ok = QtWidgets.QPushButton(self.frame)
        self.ok.setMinimumSize(QtCore.QSize(0, 24))
        self.ok.setObjectName("ok")
        self.gridLayout_2.addWidget(self.ok, 4, 3, 1, 1)
        self.cancel = QtWidgets.QPushButton(self.frame)
        self.cancel.setMinimumSize(QtCore.QSize(0, 24))
        self.cancel.setObjectName("cancel")
        self.gridLayout_2.addWidget(self.cancel, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        company_info_edit_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(company_info_edit_win)
        QtCore.QMetaObject.connectSlotsByName(company_info_edit_win)


        #####

        func.start(self,main_win)
        #####
    def retranslateUi(self, company_info_edit_win):
        _translate = QtCore.QCoreApplication.translate
        company_info_edit_win.setWindowTitle(_translate("company_info_edit_win", "MainWindow"))
        self.edit_section.setText(_translate("company_info_edit_win", "Edit"))
        self.company_name.setPlaceholderText(_translate("company_info_edit_win", "Oculus"))
        self.label_18.setText(_translate("company_info_edit_win", "<html><head/><body><p align=\"right\">Company email :</p></body></html>"))
        self.label_17.setText(_translate("company_info_edit_win", "<html><head/><body><p align=\"right\">Company name :</p></body></html>"))
        self.company_logo_but.setToolTip(_translate("company_info_edit_win", "<html><head/><body><p>Click to change company info</p></body></html>"))
        self.company_tele.setPlaceholderText(_translate("company_info_edit_win", "1234567890"))
        self.company_email.setPlaceholderText(_translate("company_info_edit_win", "oculus036@gmail.com"))
        self.label_20.setText(_translate("company_info_edit_win", "<html><head/><body><p align=\"right\">Telephone number :</p></body></html>"))
        self.label_19.setText(_translate("company_info_edit_win", "<html><head/><body><p align=\"right\">Section count :</p></body></html>"))
        self.ok.setText(_translate("company_info_edit_win", "Ok"))
        self.cancel.setText(_translate("company_info_edit_win", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    company_info_edit_win = QtWidgets.QMainWindow()
    ui = Ui_company_info_edit_win()
    ui.setupUi(company_info_edit_win)
    company_info_edit_win.show()
    sys.exit(app.exec_())
