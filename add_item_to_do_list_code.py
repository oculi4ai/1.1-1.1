        
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
import datetime
import main_win_code as func
from PyQt5.QtWidgets import QMessageBox,QWidget


def add(self,add_todo,main_win):
  
  title=str(self.title.text())
  if len(title)==0:
   
   print("error (no title)")
  else:
   a=sq.connect('Data_Bases/hr_company_data.db')
   ids=a.execute('select id from todo_list').fetchall()
   if len(ids)==0:
   	Id='0'
   else:
   	Id=str(int(ids[-1][0])+1)


   from_time=(datetime.datetime(2000,1,1,self.from_time.time().hour(),self.from_time.time().minute()))

   from_time=str(datetime.datetime.timestamp(datetime.datetime(2000,1,1,self.from_time.time().hour(),self.from_time.time().minute())))
   

   to_time=(datetime.datetime(2000,1,1,self.to_time.time().hour(),self.to_time.time().minute()))

   to_time=str(datetime.datetime.timestamp((datetime.datetime(2000,1,1,self.to_time.time().hour(),self.to_time.time().minute()))))
   
   if self.evrey_day.isChecked():
   	date=str(int(self.evrey_day.isChecked()))
   else:
   	date=str(datetime.datetime.timestamp(datetime.datetime(self.date.date().year(),self.date.date().month(),self.date.date().day())))
   

   

   
   discription=str(self.discription.toPlainText())

   
   try:
    #a.execute('insert into todo_list ("title","from","to","done","discription","date","auto_del","id") values ("'+title+'","'+from_time+'","'+to_time+'",0,"'+discription+'","'+date+'",'+str(self.auto_del.isChecked())+','+Id+')')
    a.execute('insert into todo_list ("title","from","to","done","discription","date","auto_del") values (?,?,?,?,?,?,?)',(title,from_time,to_time,'0',discription,date,str(int(self.auto_del.isChecked()))))
   except:
    a.execute('create table todo_list ("title","from","to","done","discription","date",id integer primary key autoincrement)')
    a.execute('insert into todo_list ("title","from","to","done","discription","date","auto_del") values (?,?,?,?,?,?,?)',(title,from_time,to_time,'0',discription,date,str(int(self.auto_del.isChecked()))))
   a.commit()
   a.close()
   add_todo.destroy()
   func.todo_list_f(main_win)
   try :
    main_win.view_todo.destroy() 
    func.open_view_to_do_list(main_win,-1)
   except :
    pass  

   
   print(self.from_time.time())
   print(self.to_time.time())



def culc_time(self):
 


 h_from=self.from_time.time().hour()
 min_from=self.from_time.time().minute()
 h_to=self.to_time.time().hour()
 min_to=self.to_time.time().minute()

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

