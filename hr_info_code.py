        
         ######                               ####        
       ###    ###                               ##        @                      
     ###        ###    #######   ##      ##     ##      ####   
     ###        ###   ##         ##      ##     ##        ##        
     ###        ###   ##         ##      ##     ##        ##         
       ###    ###     ##         ##      ##     ##        ##        
         ######        #######    ########    ######    ######


#Oculi
#philip youssef
#2020   

import sqlite3 as sq
from PyQt5 import QtCore, QtGui
from functools import partial
import main_win_code as m_w_c
import datetime

def edit_info(self,main_win):

    a=sq.connect('Data_Bases/hr_company_data.db')

    
    
    print(type(self.time_from.time().hour()),type(self.time_from.time().minute()))
    data=(datetime.datetime.timestamp(datetime.datetime( 2000,1,1,self.time_from.time().hour(),self.time_from.time().minute())),
        datetime.datetime.timestamp(datetime.datetime(2000,1,1, self.time_to.time().hour(),self.time_to.time().minute())))

    try:
        a.execute('delete from hr_info')
        
    except:
        a.execute('create table hr_info ("from","to","photo")')

    a.execute('insert into hr_info ("from","to") values (?,?)',data)
    a.commit()
    main_win.edit_hr_i.destroy() 


def start(self,main_win):
    a=sq.connect('Data_Bases/hr_company_data.db')
    try:
        data=a.execute('select * from hr_info').fetchall()[0]
        
    except:
        try:
            data=('946720800.0','946720800.0','icons/profile.png')
            a.execute('create table hr_info ("from","to",photo)')
            
        except :
            pass
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(data[2]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.hr_photo.setIcon(icon)
    self.time_from.setTime(datetime.datetime.fromtimestamp(float(data[0])).time())
    self.time_to.setTime(datetime.datetime.fromtimestamp(float(data[1])).time())

    a=partial(edit_info,self,main_win)
    self.ok.clicked.connect(a)

