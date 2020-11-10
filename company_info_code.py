import sqlite3 as sq
from PyQt5 import QtCore, QtGui
from functools import partial
import main_win_code as m_w_c

def edit_main_info(self,main_win):

    a=sq.connect('Data_Bases/hr_company_data.db')

    
    

    data=(self.company_name.text(),self.company_email.text(),self.company_tele.text(),'icons/oculus [Recovered]2.png')

    try:
        a.execute('delete from company_info')
        
    except:
        a.execute('create table company_info (name,email,phone,logo)')

    a.execute('insert into company_info (name,email,phone,logo) values (?,?,?,?)',data)
    a.commit()
    print(data)
    m_w_c.set_company_info(main_win)
    main_win.edit_c_i.destroy() 



def start(self,main_win):
    a=sq.connect('Data_Bases/hr_company_data.db')
    try:
        data=a.execute('select * from company_info').fetchall()[0]
        
    except:
        try:
            data=('oculus','oculus036@gmail.com','0994705538','icons/hr logo.png')
            a.execute('create table company_info (name,email,phone,logo)')
            
        except :
            pass
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(data[3]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.company_logo_but.setIcon(icon)
    self.company_name.setText(data[0])
    self.company_email.setText(data[1])
    self.company_tele.setText(data[2])


    a=partial(edit_main_info,self,main_win)
    self.ok.clicked.connect(a)
