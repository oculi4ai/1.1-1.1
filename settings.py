# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import settings_code as func

class Ui_settings(object):
    def setupUi(self, settings,main_win):
        settings.setObjectName("settings")
        settings.resize(878, 447)
        settings.setMinimumSize(QtCore.QSize(878, 447))
        settings.setMaximumSize(QtCore.QSize(878, 447))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/hr logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settings.setWindowIcon(icon)
        settings.setStyleSheet("background-color: rgb(21, 29, 47);")
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("\n"
"QTabWidget::pane {\n"
"    border-top: 0px solid #C2C7CB;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; \n"
"}\n"
"QTabBar::tab {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"    border: 0px solid rgb(0, 0, 0);\n"
"    min-width: 53ex;\n"
"    padding: 09px;\n"
"    color:rgb(255,255,255)\n"
"}\n"
"#frame_54,QProgressBar,QLineEdit{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));\n"
"\n"
"    border-bottom: 4px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 112, 187, 0), stop:0.263682 rgba(0, 112, 187, 255), stop:0.517413 rgba(0, 112, 187, 255), stop:0.766169 rgba(0, 112, 187, 255), stop:1 rgba(0, 112, 187, 0));\n"
"}\n"
"\n"
" \n"
"QTabBar::tab:selected {\n"
"    border-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 112, 187, 0), stop:0.189055 rgba(17, 0, 255, 255), stop:0.517413 rgba(17, 0, 255, 255), stop:0.81592 rgba(17, 0, 255, 255), stop:1 rgba(0, 112, 187, 0));\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-bottom: 4px; \n"
"}\n"
"QTabBar::tab:selected {\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"#frame{\n"
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
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setMinimumSize(QtCore.QSize(116, 0))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(47, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 4, 1, 1, 1)
        self.values_list = QtWidgets.QListWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.values_list.setFont(font)
        self.values_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.values_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.values_list.setObjectName("values_list")
        self.gridLayout_3.addWidget(self.values_list, 4, 2, 1, 3)
        self.delete_value = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_value.sizePolicy().hasHeightForWidth())
        self.delete_value.setSizePolicy(sizePolicy)
        self.delete_value.setMinimumSize(QtCore.QSize(81, 24))
        self.delete_value.setMaximumSize(QtCore.QSize(81, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.delete_value.setFont(font)
        self.delete_value.setObjectName("delete_value")
        self.gridLayout_3.addWidget(self.delete_value, 2, 4, 1, 1)
        self.add_value = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_value.sizePolicy().hasHeightForWidth())
        self.add_value.setSizePolicy(sizePolicy)
        self.add_value.setMinimumSize(QtCore.QSize(81, 24))
        self.add_value.setMaximumSize(QtCore.QSize(81, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.add_value.setFont(font)
        self.add_value.setObjectName("add_value")
        self.gridLayout_3.addWidget(self.add_value, 2, 2, 1, 1)
        self.variables = QtWidgets.QListWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.variables.setFont(font)
        self.variables.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.variables.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.variables.setObjectName("variables")
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variables.addItem(item)
        self.gridLayout_3.addWidget(self.variables, 1, 0, 4, 1)
        self.edit_value = QtWidgets.QPushButton(self.frame)
        self.edit_value.setMinimumSize(QtCore.QSize(80, 24))
        self.edit_value.setMaximumSize(QtCore.QSize(80, 24))
        self.edit_value.setObjectName("edit_value")
        self.gridLayout_3.addWidget(self.edit_value, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 2, 1, 3)
        self.variables_list = QtWidgets.QLabel(self.frame)
        self.variables_list.setObjectName("variables_list")
        self.gridLayout_3.addWidget(self.variables_list, 0, 0, 1, 1)
        self.value_text = QtWidgets.QLineEdit(self.frame)
        self.value_text.setObjectName("value_text")
        self.gridLayout_3.addWidget(self.value_text, 0, 3, 1, 2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settings)

        func.start(self,main_win)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "settings"))
        self.delete_value.setText(_translate("settings", "Delete"))
        self.add_value.setText(_translate("settings", "Add"))
        __sortingEnabled = self.variables.isSortingEnabled()
        self.variables.setSortingEnabled(False)
        item = self.variables.item(0)
        item.setText(_translate("settings", "Gender"))
        item = self.variables.item(1)
        item.setText(_translate("settings", "Nationality"))
        item = self.variables.item(2)
        item.setText(_translate("settings", "Blood Group"))
        item = self.variables.item(3)
        item.setText(_translate("settings", "Section"))
        item = self.variables.item(4)
        item.setText(_translate("settings", "Position"))
        item = self.variables.item(5)
        item.setText(_translate("settings", "Marital Status"))
        item = self.variables.item(6)
        item.setText(_translate("settings", "Work Time"))
        item = self.variables.item(7)
        item.setText(_translate("settings", "Military Service"))
        item = self.variables.item(8)
        item.setText(_translate("settings", "Driving"))
        self.variables.setSortingEnabled(__sortingEnabled)
        self.edit_value.setText(_translate("settings", "Edit"))
        self.label_2.setText(_translate("settings", "<html><head/><body><p align=\"center\">Vlues</p></body></html>"))
        self.variables_list.setText(_translate("settings", "<html><head/><body><p align=\"center\">Variables</p></body></html>"))
        self.label.setText(_translate("settings", "<html><head/><body><p align=\"right\">Value text :</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("settings", "Constant values"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("settings", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings = QtWidgets.QMainWindow()
    ui = Ui_settings()
    ui.setupUi(settings)
    settings.show()
    sys.exit(app.exec_())
