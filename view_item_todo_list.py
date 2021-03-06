# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
import view_item_todo_list_code as func


class Ui_view_item_todo_list(object):
    def setupUi(self, view_item_todo_list,main_win,id2):
        view_item_todo_list.setObjectName("view_item_todo_list")
        view_item_todo_list.resize(505, 448)
        view_item_todo_list.setMinimumSize(QtCore.QSize(505, 448))
        view_item_todo_list.setMaximumSize(QtCore.QSize(505, 448))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/hr logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        view_item_todo_list.setWindowIcon(icon)
        view_item_todo_list.setStyleSheet("background-color: rgb(21, 29, 47);")
        self.centralwidget = QtWidgets.QWidget(view_item_todo_list)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.frame.setFont(font)
        self.frame.setStyleSheet("#frame{\n"
"background-color: rgb(31, 41, 64);\n"
" border-radius: 5px;\n"
"color:rgb(255,255,255);\n"
"    \n"
"}\n"
"QLabel,QCheckBox{\n"
"\n"
"color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"\n"
"#edit{\n"
"border: 2px solid rgb(198, 116, 69);\n"
"color: rgb(220, 220, 220);\n"
"}\n"
"#delete_item{\n"
"border: 2px solid rgb(218, 0, 3);\n"
"color: rgb(220, 220, 220);\n"
"}\n"
"#add_new_item{\n"
"border: 2px solid rgb(45, 208, 0);\n"
"color: rgb(220, 220, 220);\n"
"}\n"
"#edit:pressed , #delete_item:pressed , #add_new_item:pressed{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(21, 29, 47);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLabel,QCheckBox{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));\n"
"}\n"
"\n"
"\n"
"QLineEdit , QPushButton , QToolButton , QListWidget , QListWidget::item , QPushButton , QDateEdit,QTimeEdit\n"
",QTextEdit\n"
"{\n"
"padding-left:6px;\n"
"padding-right:6px;\n"
"color:rgb(255,255,255);\n"
"border: 1px solid rgb(48, 64, 99);;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListWidget{\n"
"background-color: rgb(23, 31, 49);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton , QToolButton,QLineEdit,QDateEdit,QTimeEdit{\n"
"\n"
"border-radius: 10px;}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::sub-page:vertical ,QScrollBar::add-page:vertical{\n"
"background:rgb(24, 32, 49);}\n"
"\n"
"\n"
"QToolButton:pressed,QPushButton:pressed,QListWidget:item {\n"
"padding:1px;\n"
"background-color: rgb(20, 27, 45);}\n"
"\n"
"\n"
"QListWidget {\n"
"padding-top:8px;\n"
"\n"
"}\n"
" QPushButton , QToolButton{\n"
"\n"
"padding:0px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical,QListWidget:item:hover{\n"
"border-radius: 4px;\n"
"border: 2px solid rgb(164, 190, 217);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));\n"
"}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));\n"
"\n"
"border: 2px solid rgb(17, 0, 255);\n"
"color:rgb(10, 57, 170);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QToolTip{\n"
"color:rgb(210,210,210);\n"
"background-color:rgb(42, 58, 94);\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(0, 112, 187);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.time_from = QtWidgets.QTimeEdit(self.frame)
        self.time_from.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.time_from.setFont(font)
        self.time_from.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.time_from.setObjectName("time_from")
        self.gridLayout_2.addWidget(self.time_from, 2, 1, 1, 1)
        self.everyday = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.everyday.setFont(font)
        self.everyday.setObjectName("everyday")
        self.gridLayout_2.addWidget(self.everyday, 1, 5, 1, 1)
        self.done = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.done.setFont(font)
        self.done.setObjectName("done")
        self.gridLayout_2.addWidget(self.done, 0, 5, 1, 1)
        self.delete_item = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_item.sizePolicy().hasHeightForWidth())
        self.delete_item.setSizePolicy(sizePolicy)
        self.delete_item.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.delete_item.setFont(font)
        self.delete_item.setObjectName("delete_item")
        self.gridLayout_2.addWidget(self.delete_item, 1, 6, 1, 1)
        self.auto_del = QtWidgets.QCheckBox(self.frame)
        self.auto_del.setObjectName("auto_del")
        self.gridLayout_2.addWidget(self.auto_del, 2, 5, 1, 1)
        self.edit = QtWidgets.QPushButton(self.frame)
        self.edit.setMinimumSize(QtCore.QSize(74, 24))
        self.edit.setObjectName("edit")
        self.gridLayout_2.addWidget(self.edit, 2, 6, 1, 1)
        self.add_new_item = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_item.sizePolicy().hasHeightForWidth())
        self.add_new_item.setSizePolicy(sizePolicy)
        self.add_new_item.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.add_new_item.setFont(font)
        self.add_new_item.setObjectName("add_new_item")
        self.gridLayout_2.addWidget(self.add_new_item, 0, 6, 1, 1)
        self.discription = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.discription.setFont(font)
        self.discription.setObjectName("discription")
        self.gridLayout_2.addWidget(self.discription, 3, 0, 1, 7)
        self.date = QtWidgets.QDateEdit(self.frame)
        self.date.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.date.setFont(font)
        self.date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.date.setObjectName("date")
        self.gridLayout_2.addWidget(self.date, 1, 1, 1, 4)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.total_time = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.total_time.setFont(font)
        self.total_time.setText("")
        self.total_time.setObjectName("total_time")
        self.gridLayout_2.addWidget(self.total_time, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 2, 1, 1)
        self.time_to = QtWidgets.QTimeEdit(self.frame)
        self.time_to.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.time_to.setFont(font)
        self.time_to.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.time_to.setObjectName("time_to")
        self.gridLayout_2.addWidget(self.time_to, 2, 3, 1, 1)
        self.title = QtWidgets.QLineEdit(self.frame)
        self.title.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 1, 1, 4)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        view_item_todo_list.setCentralWidget(self.centralwidget)

        self.retranslateUi(view_item_todo_list)
        QtCore.QMetaObject.connectSlotsByName(view_item_todo_list)
        view_item_todo_list.setTabOrder(self.title, self.date)
        view_item_todo_list.setTabOrder(self.date, self.time_to)
        view_item_todo_list.setTabOrder(self.time_to, self.time_from)
        view_item_todo_list.setTabOrder(self.time_from, self.auto_del)
        view_item_todo_list.setTabOrder(self.auto_del, self.everyday)
        view_item_todo_list.setTabOrder(self.everyday, self.done)
        view_item_todo_list.setTabOrder(self.done, self.discription)
        view_item_todo_list.setTabOrder(self.discription, self.add_new_item)
        view_item_todo_list.setTabOrder(self.add_new_item, self.delete_item)
        view_item_todo_list.setTabOrder(self.delete_item, self.edit)

        func.start(self,main_win,id2)

    def retranslateUi(self, view_item_todo_list):
        _translate = QtCore.QCoreApplication.translate
        view_item_todo_list.setWindowTitle(_translate("view_item_todo_list", "view item"))
        self.label_5.setText(_translate("view_item_todo_list", "<html><head/><body><p align=\"right\">Date :</p></body></html>"))
        self.label_2.setText(_translate("view_item_todo_list", "<html><head/><body><p align=\"right\">from :</p></body></html>"))
        self.everyday.setText(_translate("view_item_todo_list", "Every Day"))
        self.done.setText(_translate("view_item_todo_list", "Done"))
        self.delete_item.setText(_translate("view_item_todo_list", "Delete"))
        self.auto_del.setText(_translate("view_item_todo_list", "Auto Delete"))
        self.edit.setText(_translate("view_item_todo_list", "Edit"))
        self.add_new_item.setText(_translate("view_item_todo_list", "Add"))
        self.discription.setPlaceholderText(_translate("view_item_todo_list", "Discription"))
        self.label.setText(_translate("view_item_todo_list", "<html><head/><body><p align=\"right\">Title :</p></body></html>"))
        self.label_3.setText(_translate("view_item_todo_list", "<html><head/><body><p align=\"right\">to :</p></body></html>"))
        self.title.setPlaceholderText(_translate("view_item_todo_list", "Title"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view_item_todo_list = QtWidgets.QMainWindow()
    ui = Ui_view_item_todo_list()
    ui.setupUi(view_item_todo_list)
    view_item_todo_list.show()
    sys.exit(app.exec_())
