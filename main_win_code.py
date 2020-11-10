        
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
import concurrent.futures
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
from add_item_to_do_list import Ui_add_todo
from view_todo_list import Ui_view_todo_list
from view_item_todo_list import Ui_view_item_todo_list
from company_info import Ui_company_info_edit_win
from hr_info import Ui_hr_info_edit_win
from settings import Ui_settings
from functools import partial
from qr_scanner import scan
from playsound import playsound





def start(self):

	self.icon_done = QtGui.QIcon()
	self.icon_done.addPixmap(QtGui.QPixmap('icons/Done.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                                                                                                                
	self.icon_undone = QtGui.QIcon()
	self.icon_undone.addPixmap(QtGui.QPixmap('icons/Undone.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.icon_inprogress = QtGui.QIcon()
	self.icon_inprogress.addPixmap(QtGui.QPixmap('icons/In_progress.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                
	self.icon_wait = QtGui.QIcon()
	self.icon_wait.addPixmap(QtGui.QPixmap('icons/Wait.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.done_sound=partial(playsound,"sound_effects/done.mp3")

	######### start functions ############

	self.now_date.setDate(datetime.date.today())
	todo_list_f(self)
	set_company_info(self)
	work_time_f(self)


	tables=["Gender","Nationality","Blood_Group","Section","Position","Marital_Status","Work_Time","Military_Service","Driving"]
	combo_boxs=[self.worker_gender_2,self.nationality,self.worker_blood,self.worker_section,self.worker_position,self.marital_status,self.worker_work_time,self.military_service,self.worker_driving]

	set_constant_values(self,tables,combo_boxs)

	######### connecting functions ############

	f1= partial(open_add_to_do_list, self)
	self.add_to_todo_list.clicked.connect(f1)
	
	f2= partial(open_view_to_do_list, self)
	self.view_todo_list.clicked.connect(f2)


	f3=partial(open_view_item_to_do_list,self)
	self.todo_list.clicked.connect(f3)


	f4=partial(scanning,self)
	self.bar_code.clicked.connect(f4)

	f5=partial(todo_list_f,self) # refresh todo_list
	self.refresh_todo_list.clicked.connect(f5)

	
	f6=partial(open_edit_company_info,self)
	self.company_logo_but.clicked.connect(f6)

	f7=partial(open_edit_hr_info,self)
	self.hr_photo.clicked.connect(f7)
	
	f8=partial(self.tabWidget.setCurrentIndex,4)
	self.presentation_but.clicked.connect(f8)


	f9=partial(add_new_em,self)
	self.add_new_button.clicked.connect(f9)

	f10=partial(open_settings,self)
	self.settings.clicked.connect(f10)



##########################################################################################################################
##################################################################################### set info functions #################
##########################################################################################################################



def set_constant_values(self,tables,combo_boxs):

	print("refresh")	

	for i in range(len(tables)):
		a=sq.connect('Data_Bases/constant_values.db')
		print('select * from "{}"'.format(tables[i]))
		data=a.execute('select * from "{}"'.format(tables[i])).fetchall()

		combo_boxs[i].clear()
		combo_boxs[i].addItem("")
		for bit in data:
			combo_boxs[i].addItem(bit[0])




def set_company_info(self):

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
	self.label.setPixmap(QtGui.QPixmap(data[3]))

	self.company_name_label.setText(( """<html><head/><body><p align="center">{}</p>
										<p align="center"><span style=" font-size:10pt; color:#c8c8c8;">{}</span></p>
										<p align="center"><span style=" font-size:10pt; color:#c8c8c8;">{}</span></p></body></html>""").format(data[0],data[1],data[2]))

def work_time_f(self):


	a=sq.connect('Data_Bases/hr_company_data.db')
	data=a.execute('select "from","to" from hr_info ').fetchall()[0]

	time_from= datetime.datetime.fromtimestamp(data[0])
	time_to=datetime.datetime.fromtimestamp(data[1])


	time_s=((time_to-time_from).total_seconds())
	

	t_time=''
	time_h=0
	time_m=0
	print('seconds :',time_s)
	while int(time_s)>=3600:
		time_s-=3600
		time_h+=1

	while int(time_s)>=60:
		time_s-=60
		time_m+=1

	time_s=(time_h*3600)+(time_m*60)

	if time_h>0:
		t_time=(str(time_h)+'h ')

	if time_m>0:
		t_time+=(str(time_m)+'min')
		
	#if time_from.time()>datetime.datetime.today().time():
	
	#	time.sleep((time_from.time() - datetime.datetime.today().time()).time().seconds())
	#else:

	
	bar_v=100

	def auto_work_time(bar_v=bar_v):
		while bar_v>=0:

			time.sleep(time_s/100)
			bar_v-=1
			print(bar_v)
			self.work_time_bar.setProperty("value", bar_v)

	#self.run_work_time=threading.Thread(target=auto_work_time)

	
	#self.run_work_time.start()

def gg():
	def auto_work_time():
		
		point_done=0
		current_point=-1

		time_point=time_s/20
		if time_from.time()>datetime.datetime.now().time(): #waiting for start work time
			self.work_time_label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">work time<br/></span>{}</p></body></html>".format(t_time+' (early for work)'))
			self.frame_3.setEnabled(0)
			time.sleep((time_from-datetime.datetime.now()).seconds)
			self.frame_3.setEnabled(1)

		elif time_from.time()<datetime.datetime.now().time()<time_from.time() :# in work time
			point_done=((datetime.datetime.now()-time_from).seconds)/time_point

			for i in range(int(point_done)):
				dots[i].setChecked(0)
			 
			current_point=i
		self.work_time_label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">work time<br/></span>{}</p></body></html>".format(t_time))
		if datetime.datetime.now().time()<time_from.time() :
			for i in range(20-int(point_done)):
				time.sleep(time_point)
				current_point+=1
				dots[current_point].setChecked(0)

		else:

			for i in range(20):
				dots[i].setChecked(0)
		self.work_time_label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">work time<br/></span>{}</p></body></html>".format(t_time+' (out of work time)'))

	self.run_work_time=threading.Thread(target=auto_work_time)

	self.run_work_time.start()

##########################################################################################################################
##################################################################################### employers functions ################
##########################################################################################################################

def add_new_em(self):
	a=sq.connect('Data_Bases/employers_data.db')
	a.execute(('''insert into em_info_1 (
			id,
			name1,
			name2,
			name3,
			gender,
			nationality,
			blood_group,
			address,
			situation,
			starting_date,
			section,
			position,
			marital_status,
			work_time,
			military_service,
			in_num,
			driving,
			email,
			telephone_num,
			mobile_num,
			smoker,
			detained)

			values

			("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")''').format(
			self.worker_id_2.text(),
			self.worker_name_1.text(),
			self.worker_name_2.text(),
			self.worker_name_3.text(),

			self.worker_gender_2.text(),
			self.nationality.text(),
			self.worker_blood.text(),

			self.worker_address.text(),
			self.worker_situation.text(),
			datetime.datetime.timestamp(datetime.datetime(self.worker_start_date.date().year(),self.worker_start_date.date().month(),self.worker_start_date.date().day())),


			self.worker_section.text(),
			self.worker_position.text(),
			self.marital_status.text(),
			self.worker_work_time.text(),
			self.military_service.text(),
			
			self.worker_ins.text(),

			self.worker_driving.text(),

			self.worker_email_2.text(),
			self.worker_tele.text(),
			self.worker_mobile.text(),

			self.detained_input.isChecked(),
			self.smoke_input.isChecked()


			))


def get_data(self):
	a=sq.connect('Data_Bases/employers_data.db')
	try:
		data_1=a.execute('''select 
			id,
			name1,
			name2,
			name3,
			gender,
			nationality,
			blood_group,
			address,
			situation,
			starting_date,
			section,
			position,
			marital_status,
			work_time,
			military_service,
			in_num,
			driving,
			email,
			phone_num,
			mobile_num,
			smoker,
			detained,
			profile_photo
			 
			from em_info_1
			 ''').fetchall()
		print(data_1)
	except :
		print(2)
		a.execute('''create table em_info_1 (
			id,
			name1,
			name2,
			name3,
			gender,
			nationality,
			blood_group,
			address,
			situation,
			starting_date,
			sction,
			position,
			marital_status,
			work_time,
			military_service,
			in_num,
			driving,
			email,
			phone_num,
			mobile_num,
			smoker,
			detained,
			profile_photo
			)''')


def scanning(self):
	id2=scan(self)

	




##########################################################################################################################
##################################################################################### todo list functions ################
##########################################################################################################################


def todo_list_f(self):
	




	self.todo_list.clear()
	a=sq.connect('Data_Bases/hr_company_data.db')
	
	try:
		todo_data=a.execute("select * from todo_list").fetchall()
	except:
		a.execute('create table todo_list ("title","from","to","done","discription","date","auto_del",id integer primary key autoincrement)')
		todo_data=a.execute("select * from todo_list").fetchall()
		
	#####
	done_items=[]
	wait_items=[]
	inprogress_items=[]
	undone_items=[]
	#####		


	times_stop=[]
	n=0
	for i in todo_data:	#('title', 'from', 'to', 'done', 'discription','date','auto_del','id')

		
		da=float(str(i[5]).split(',')[0])
		try:
			da_2=float(str(i[5]).split(',')[1])
		except :
			da_2=0.0



		if int(da)==1 and datetime.datetime.fromtimestamp(da_2).date()<datetime.date.today() and i[3]=='1':#every day daone last days
				a.execute('update todo_list set date=? where id=?',(1,i[7]))
				a.execute('update todo_list set done=? where id=?',('0',i[7]))
				a.commit()
				todo_list_f(self)
				print('one every day')

		else:
			if 3<da and datetime.datetime.fromtimestamp(da).date()<datetime.datetime.today().date() and int(i[6])>0 and int(i[3])==1:
				
				a.execute('delete from todo_list where id=?',(str(i[7]),))
				a.commit()


			elif ((datetime.datetime.fromtimestamp(float(da)).date()==datetime.date.today())

				or 
				((datetime.datetime.fromtimestamp(float(da)).date()<datetime.date.today() and i[3]==0))
				or 
				(int(da)==1)):																	   # condition 1 to view all item have today date
																								   # condition 2 to view all item from past that haven't done yet
																								   # condition 3 to view item that selected everyday


				item = QtWidgets.QListWidgetItem()#create new item
			
			  



				now=datetime.datetime.now().time()
				don=''
				don2=''


				
				from_time=datetime.datetime.fromtimestamp(float(i[1]))

				to_time=datetime.datetime.fromtimestamp(float(i[2]))


				if float(da)==1.0:
					dat='every day'
				else:
					dat=str(datetime.datetime.fromtimestamp(da).date()).replace('-',' \ ')



				item.setData(5,don2)
				item.setData(4,i[0])
				item.setData(6,i[7])

				item.setToolTip(


				"""<html><head/><body><p align="center"><span style=" font-weight:600; text-decoration: underline; color:##c8c8c8;">
				{}</span></p><p align="center"><span style=" color:##c8c8c8;">
				from {} to {}</span></p><p align="center"><span style=" color:#c8c8c8;">
				{} \n {}</span></p><p align="center"><span style=" font-weight:600; text-decoration: underline; color:##000000;">Discroption</span></p><p align="center"><span style=" color:#c8c8c8;">
				{}</span></p><p align="center"><br/></p></body></html>""".format(str(i[0]),str(':'.join(from_time.time().isoformat().split(':')[0:2])),str(':'.join(to_time.time().isoformat().split(':')[0:2])),str(to_time-from_time),don,str(i[4])))

				

				item.setText(str(i[0]))
				from_time=datetime.datetime.fromtimestamp(float(i[1])).time()

				to_time=datetime.datetime.fromtimestamp(float(i[2])).time()			

				if i[3].split(',')[0]=='1':#done today
					
					icon = self.icon_done
					item.setIcon(icon)
					don="""<span style=" font-weight:600; color:#217246;">Done </span>"""
					don2='Done'
					item.setIcon(icon)
					done_items.append(item)

				elif ((datetime.datetime.fromtimestamp(da).date()<datetime.date.today()) or
						(to_time<datetime.datetime.now().time())) and i[3]=='0' :#condition 1 item from last days not done yet
																										  
					
					icon = self.icon_undone
					item.setIcon(icon)
					don="""<span style=" font-weight:600; color:#fe1111;">Undone</span>"""
					don2='Undone'
					item.setIcon(icon)
					undone_items+=[item]


				elif ((datetime.datetime.fromtimestamp(da).date()==datetime.date.today() or float(da)==1.0) and from_time<=now<=to_time): # in progress
					icon = self.icon_inprogress
					
					don="""<span style=" font-weight:600; color:#fdc300;">In progress</span>"""
					don2='In progress'
					times_stop.append((datetime.datetime.fromtimestamp(float(i[2]))))
					item.setIcon(icon)
					inprogress_items.append(item)

				else :#wait
					icon = self.icon_wait


					don="""<span style=" font-weight:600; color:#fdc300;">wait</span>"""
					don2='wait'

					times_stop.append(datetime.datetime.fromtimestamp(float(i[1])))
					times_stop.append(datetime.datetime.fromtimestamp(float(i[2])))
					item.setIcon(icon)
					wait_items.append(item)


				#self.todo_list.addItem(item)      #add it to list
				n+=1

		

		
		for items in (undone_items,inprogress_items,wait_items,done_items):
			for item in items:
				self.todo_list.addItem(item)

		def auto_refresh(self=self):

			if len(times_stop)>0:
				times_stop.sort()
				time_stop=(times_stop[0]-datetime.datetime.now()).seconds

				while time_stop>86400:
					time_stop-=86400

				time.sleep(time_stop+1)

				todo_list_f(self)
		try:
			run_auto_refresh._stop()
		except :
			pass

		def fff():
			print ('threading...')

		with concurrent.futures.ThreadPoolExecutor() as executer:

			executer.submit(fff)


		#run_auto_refresh=threading.Thread(target=auto_refresh)
		
			
		#run_auto_refresh.start()
		
def open_add_to_do_list(self):
    try:
    	self.add_todo_list.destroy() 
    except :
    	pass
    self.add_todo_list = QtWidgets.QMainWindow()
    self.ui = Ui_add_todo()
    self.ui.setupUi(self.add_todo_list,self)
    self.add_todo_list.show()

def open_view_to_do_list(self):
	
	try:
		self.view_todo.destroy() 
	except :
		pass
	self.view_todo = QtWidgets.QMainWindow()
	self.ui = Ui_view_todo_list()
	self.ui.setupUi(self.view_todo,self)
	self.view_todo.show()
	
def open_view_item_to_do_list(self):
	
	try:
		self.view_item_todo.destroy() 
	except :
		pass
	self.view_item_todo = QtWidgets.QMainWindow()
	self.ui = Ui_view_item_todo_list()
	self.ui.setupUi(self.view_item_todo,self,self.todo_list.currentItem().data(6))
	self.view_item_todo.show()
	

##########################################################################################################################
##################################################################################### edit info functions ################
##########################################################################################################################

def open_edit_company_info(self):
    try:
    	self.edit_c_i.destroy() 
    except :
    	pass
    self.edit_c_i = QtWidgets.QMainWindow()
    self.ui = Ui_company_info_edit_win()
    self.ui.setupUi(self.edit_c_i , self)
    self.edit_c_i.show()

def open_edit_hr_info(self):

	

	try:
		self.edit_hr_i.destroy() 
	except :
		pass
	self.edit_hr_i = QtWidgets.QMainWindow()
	self.ui = Ui_hr_info_edit_win()
	self.ui.setupUi(self.edit_hr_i , self)
	self.edit_hr_i.show()



###############################################################--------------###########################################################
############################################################### open windows ###########################################################
###############################################################--------------###########################################################

def open_settings(self):

	try:
		self.settings.destroy() 
	except :
		pass
	self.settings = QtWidgets.QMainWindow()
	self.ui = Ui_settings()
	self.ui.setupUi(self.settings , self)
	self.settings.show()
