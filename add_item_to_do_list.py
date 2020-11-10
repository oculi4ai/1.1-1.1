        
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
import add_item_to_do_list_code as func
import main_win_code as func_2
from functools import partial
from datetime import date
import datetime

class Ui_add_todo(object):
    def setupUi(self, add_todo ,main_win):
        add_todo.setObjectName("add_todo")
        add_todo.resize(713, 430)
        add_todo.setMinimumSize(QtCore.QSize(713, 430))
        add_todo.setMaximumSize(QtCore.QSize(713, 430))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/hr logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_todo.setWindowIcon(icon)
        add_todo.setStyleSheet("background-color: rgb(21, 29, 47);")
        self.centralwidget = QtWidgets.QWidget(add_todo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.frame.setFont(font)
        self.frame.setStyleSheet("""#frame{
background-color: rgb(31, 41, 64);
 border-radius: 5px;
color:rgb(255,255,255);
    
}
QLabel,QCheckBox{

color: rgb(220, 220, 220);
}


#edit{
border: 2px solid rgb(198, 116, 69);
color: rgb(220, 220, 220);
}
#delete_item{
border: 2px solid rgb(218, 0, 3);
color: rgb(220, 220, 220);
}
#add_new_item{
border: 2px solid rgb(45, 208, 0);
color: rgb(220, 220, 220);
}
#edit:pressed , #delete_item:pressed , #add_new_item:pressed{
color: rgb(255, 255, 255);
    background-color: rgb(21, 29, 47);
}










QLabel,QCheckBox{
background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));
}


QLineEdit , QPushButton , QToolButton , QListWidget , QListWidget::item , QPushButton , QDateEdit,QTimeEdit
,QTextEdit
{
padding-left:6px;
padding-right:6px;
color:rgb(255,255,255);
border: 1px solid rgb(48, 64, 99);;
background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));
border-radius: 4px;

}


QListWidget{
background-color: rgb(23, 31, 49);

}


QPushButton , QToolButton,QLineEdit,QDateEdit,QTimeEdit{

border-radius: 10px;}




QScrollBar::sub-page:vertical ,QScrollBar::add-page:vertical{
background:rgb(24, 32, 49);}


QToolButton:pressed,QPushButton:pressed,QListWidget:item {
padding:1px;
background-color: rgb(20, 27, 45);}


QListWidget {
padding-top:8px;

}
 QPushButton , QToolButton{

padding:0px;
}


QScrollBar::handle:vertical,QListWidget:item:hover{
border-radius: 4px;
border: 2px solid rgb(164, 190, 217);
background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));
}


QListWidget::item:selected {
background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.243781 rgba(62, 62, 62, 0));

border: 2px solid rgb(17, 0, 255);
color:rgb(10, 57, 170);
}






QToolTip{
color:rgb(210,210,210);
background-color:rgb(42, 58, 94);
border-radius: 7px;
border: 2px solid rgb(0, 112, 187);
}
""")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cancel_bui = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_bui.sizePolicy().hasHeightForWidth())
        self.cancel_bui.setSizePolicy(sizePolicy)
        self.cancel_bui.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.cancel_bui.setFont(font)
        self.cancel_bui.setStyleSheet("background-color: rgb(48, 64, 99);\n"
"")
        self.cancel_bui.setObjectName("cancel_bui")
        self.gridLayout_2.addWidget(self.cancel_bui, 1, 5, 1, 1)
        self.add_bui = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_bui.sizePolicy().hasHeightForWidth())
        self.add_bui.setSizePolicy(sizePolicy)
        self.add_bui.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.add_bui.setFont(font)
        self.add_bui.setStyleSheet("")
        self.add_bui.setShortcut("")
        self.add_bui.setObjectName("add_bui")
        self.gridLayout_2.addWidget(self.add_bui, 0, 5, 1, 1)
        self.discription = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.discription.setFont(font)
        self.discription.setObjectName("discription")
        self.gridLayout_2.addWidget(self.discription, 3, 0, 1, 6)
        self.auto_del = QtWidgets.QCheckBox(self.frame)
        self.auto_del.setChecked(True)
        self.gridLayout_2.addWidget(self.auto_del, 2, 5, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.date = QtWidgets.QDateEdit(self.frame)
        self.date.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.date.setFont(font)
        self.date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.date.setObjectName("date")
        self.gridLayout_3.addWidget(self.date, 0, 3, 1, 1)
        self.evrey_day = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.evrey_day.setFont(font)
        self.evrey_day.setObjectName("evrey_day")
        self.gridLayout_3.addWidget(self.evrey_day, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.title = QtWidgets.QLineEdit(self.frame)
        self.title.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout_3.addWidget(self.title, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)
        self.total_time = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.total_time.setFont(font)
        self.total_time.setObjectName("total_time")
        self.gridLayout_3.addWidget(self.total_time, 1, 4, 1, 1)
        self.to_time = QtWidgets.QTimeEdit(self.frame)
        self.to_time.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.to_time.setFont(font)
        self.to_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.to_time.setObjectName("to_time")
        self.gridLayout_3.addWidget(self.to_time, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 2, 1, 1)
        self.from_time = QtWidgets.QTimeEdit(self.frame)
        self.from_time.setMinimumSize(QtCore.QSize(74, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.from_time.setFont(font)
        self.from_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.from_time.setObjectName("from_time")
        self.gridLayout_3.addWidget(self.from_time, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 3)
        self.gridLayout_3.setColumnStretch(4, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 3, 5)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 2)
        self.gridLayout_2.setColumnStretch(4, 2)
        self.gridLayout_2.setColumnStretch(5, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        add_todo.setCentralWidget(self.centralwidget)

        self.retranslateUi(add_todo)
        QtCore.QMetaObject.connectSlotsByName(add_todo)
        add_todo.setTabOrder(self.title, self.date)
        add_todo.setTabOrder(self.date, self.evrey_day)
        add_todo.setTabOrder(self.evrey_day, self.from_time)
        add_todo.setTabOrder(self.from_time, self.to_time)
        add_todo.setTabOrder(self.to_time, self.discription)
        add_todo.setTabOrder(self.discription, self.add_bui)
        add_todo.setTabOrder(self.add_bui, self.cancel_bui)
        add_todo.setTabOrder(self.cancel_bui, self.auto_del)


        ###
        add = partial(func.add, self,add_todo,main_win)
        self.add_bui.clicked.connect(add)
        culc_time = partial(func.culc_time , self)
        self.to_time.timeChanged.connect(culc_time)
        self.from_time.timeChanged.connect(culc_time)
        self.r_1=0
        self.date.setDate(date.today())
        def d(): 
            add_todo.destroy()
        self.cancel_bui.clicked.connect(d)

        def f():
            if self.evrey_day.isChecked():
                self.date.setStyleSheet('color:rgb(200,200,200);')
                self.date.setEnabled(0)
                
            else:
                self.date.setStyleSheet('color:rgb(255,255,255);')
                self.date.setEnabled(1)
        
        self.evrey_day.stateChanged.connect(f)

        self.from_time.setTime(datetime.time(1,0))
        ###
    def retranslateUi(self, add_todo):
        _translate = QtCore.QCoreApplication.translate
        add_todo.setWindowTitle(_translate("add_todo", "Add Item"))
        self.cancel_bui.setText(_translate("add_todo", "Cancel"))
        self.cancel_bui.setShortcut(_translate("add_todo", "Esc"))
        self.add_bui.setText(_translate("add_todo", "Add"))
        self.discription.setPlaceholderText(_translate("add_todo", "Discription"))
        self.auto_del.setToolTip(_translate("add_todo", "auto delete item from when done in the next day"))
        self.auto_del.setText(_translate("add_todo", "auto delete"))
        self.evrey_day.setText(_translate("add_todo", "Every Day"))
        self.label.setText(_translate("add_todo", "<html><head/><body><p align=\"right\">Title :</p></body></html>"))
        self.title.setPlaceholderText(_translate("add_todo", "Title"))
        self.label_5.setText(_translate("add_todo", "<html><head/><body><p align=\"right\">Date :</p></body></html>"))
        self.total_time.setText(_translate("add_todo", "X h"))
        self.label_3.setText(_translate("add_todo", "<html><head/><body><p align=\"right\">to :</p></body></html>"))
        self.label_2.setText(_translate("add_todo", "<html><head/><body><p align=\"right\">from :</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_todo = QtWidgets.QMainWindow()
    ui = Ui_add_todo()
    ui.setupUi(add_todo)
    add_todo.show()
    sys.exit(app.exec_())
