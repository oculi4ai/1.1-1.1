        
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



import sqlite3 as sq
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import datetime
import main_win_code as m_w_c




def edit_data(self,main_win):
    try:

        Id=str(self.todo_items.currentItem().data(3))
        a=sq.connect('Data_Bases/hr_company_data.db')

        a.execute('update todo_list set   title=? where id=?',(self.title.text(),Id))
        a.execute('update todo_list set  "from"=? where id=?',(datetime.datetime.timestamp(datetime.datetime(2000,1,1,self.time_from.time().hour(),self.time_from.time().minute())) ,Id))
        a.execute('update todo_list set  "to"=? where id=?',(datetime.datetime.timestamp(datetime.datetime(2000,1,1,self.time_to.time().hour(),self.time_to.time().minute())),Id))
        a.execute('update todo_list set  discription=? where id=?',(self.discription.toPlainText(),Id))
        

        dat=str(a.execute('select date from todo_list where id=?',(Id,)).fetchall()[0][0]).split(',')
        dn=str(a.execute('select done from todo_list where id=?',(Id,)).fetchall()[0][0])

        if self.everyday.isChecked()  :
            if len(dat)==1:
                dat=str(int(self.everyday.isChecked()))
                if dn=='1':
                    dat+=(','+str(datetime.datetime.timestamp(datetime.datetime.today())))
                a.execute('update todo_list set  date=? where id=?',(dat,Id))


        else:    
            a.execute('update todo_list set  date=? where id=?',(datetime.datetime.timestamp(datetime.datetime(self.date.date().year(),self.date.date().month(),self.date.date().day())),Id))
        
        a.execute('update todo_list set  auto_del=? where id=?',(int(self.auto_del.isChecked()),Id))

        a.commit()
        a.close()
        
        
        m_w_c.todo_list_f(main_win)
        m_w_c.open_view_to_do_list(main_win)
    except:
        pass

def done_ch(self,main_win):
    try:
        Id=str(self.todo_items.currentItem().data(3))
        a=sq.connect('Data_Bases/hr_company_data.db')
        
        
        a.execute('update todo_list set done=? where id=?' ,(str(int(self.done.isChecked())),  str(Id)))
        a.commit()
        ev=a.execute('select date from todo_list where id=?',(str(Id),)).fetchall()[0][0]
        print('ev:',ev)
        if 3>int(float(str(ev).split(',')[0]))>0  and self.done.isChecked():
            
            a.execute('update todo_list set date=? where id=?',('1,'+str(datetime.datetime.timestamp(datetime.datetime.today())),str(Id)))    
            print('every day done',('1,'+str(datetime.datetime.timestamp(datetime.datetime.today()))))

        a.commit()
        a.close()
        m_w_c.todo_list_f(main_win)
        m_w_c.open_view_to_do_list(main_win)
    except:
        pass

def everyday_ch(self):
    if self.everyday.isChecked():
        self.date.setStyleSheet('color:rgb(200,200,200);')
        self.date.setEnabled(0)
                
    else:
        self.date.setStyleSheet('color:rgb(255,255,255);')
        self.date.setEnabled(1)

def get_i_info(self,main_win):
    

    Id=str(self.todo_items.currentItem().data(3))
    
    a=sq.connect('Data_Bases/hr_company_data.db')
    
    item=a.execute('select "from","to",done,discription,date,auto_del,title from todo_list where id="'+Id+'"').fetchall()[0]
    
    a.close()
    
    self.time_from.setTime(datetime.datetime.fromtimestamp(float(item[0])).time())
    self.time_to.setTime(datetime.datetime.fromtimestamp(float(item[1])).time())
    self.done.setChecked(int(item[2]))
    self.discription.setText(item[3])
    
    if float(str(item[4]).split(',')[0])<3:
        
        self.date.setEnabled(0)
        self.date.setStyleSheet('color:rgb(200,200,200);')
        self.everyday.setChecked(1)
    else:
        
        self.date.setEnabled(1)
        self.date.setStyleSheet('color:rgb(255,255,255);')
        self.everyday.setChecked(0)
        self.date.setDate(datetime.datetime.fromtimestamp(float(item[4])).date())
    self.auto_del.setChecked(int(item[5]))
    self.title.setText(str(item[6]))
    culc_time(self)
    
def todo_item(self,main_win):
    self.todo_items.clear()
    a=sq.connect('Data_Bases/hr_company_data.db')
    items=a.execute('select "title","from","to","done","discription","date","auto_del","id" from todo_list').fetchall()

    for i in items:
        item = QtWidgets.QListWidgetItem()
        item.setData(3,i[7])
        if str(i[5]).split(',')[0]=='1':
            item.setText((i[0]+"        (Every day)"))    
        else:
            item.setText((i[0]+"        ("+str(datetime.datetime.fromtimestamp(float(i[5])).date())+')'))

        self.todo_items.addItem(item)
    
    a.close()

    don=partial(done_ch,self,main_win)
    self.done.clicked.connect(don)

def delete_item_f(self,main_win):
    try:
        a=sq.connect('Data_Bases/hr_company_data.db')
        print(self.todo_items.currentItem().data(3))
        Id=str(self.todo_items.currentItem().data(3))
        print(Id)
        a.execute('delete from todo_list where id=?',(Id,))
        a.commit()
        m_w_c.todo_list_f(main_win)
        m_w_c.open_view_to_do_list(main_win)
    except:
        pass

def culc_time(self):
 


    h_from=self.time_from.time().hour()
    min_from=self.time_from.time().minute()
    h_to=self.time_to.time().hour()
    min_to=self.time_to.time().minute()

    min_t=min_to - min_from
    h_t=h_to - h_from
     

    if min_t<0:
        h_t-=1
        min_t=60+min_t
    total_time=''
    if h_t>0:
        total_time+=str(h_t)+'h '

    if min_t>0:
        total_time+=str(min_t)+'min'

    total_time="""<html><head/><body><p><span style=" color:#6a6a6a;">"""+total_time+"""</span></p></body></html>"""
    self.total_time.setText(total_time)

def start(self,main_win):
    a=partial(get_i_info,self,main_win)
    self.todo_items.clicked.connect(a)
    #try:
    todo_item(self,main_win)


    b=partial(edit_data,self,main_win)    
    self.edit.clicked.connect(b)


    c=partial(everyday_ch,self)    
    self.everyday.clicked.connect(c)

    d=partial(m_w_c.open_add_to_do_list,main_win)
    self.add_new_item.clicked.connect(d)


    e=partial(delete_item_f,self,main_win)
    self.delete_item.clicked.connect(e)

    culc_tim = partial(culc_time , self)
    self.time_to.timeChanged.connect(culc_tim)
    self.time_from.timeChanged.connect(culc_tim)
    culc_time(self)



        

