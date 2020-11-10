
import sqlite3 as sq
from functools import partial
from PyQt5 import QtWidgets
import main_win_code as func

def start(self,main_win):

	f1=partial(view_values,self)
	self.variables.clicked.connect(f1)
    

	f1=partial(select_value,self)
	self.values_list.clicked.connect(f1)

	f2=partial(add_value,self,main_win)
	self.add_value.clicked.connect(f2)

	f3=partial(edit_value,self,main_win)
	self.edit_value.clicked.connect(f3)

	f4=partial(delete_value,self,main_win)
	self.delete_value.clicked.connect(f4)





#####################################################################################################################
################################################ constant values ####################################################
#####################################################################################################################



def view_values(self):
	self.values_list.clear()

	a=sq.connect('Data_Bases/constant_values.db')

	variable=self.variables.currentItem().text().replace(" ","_")
	try:
		values=a.execute('select * from {}'.format(variable)).fetchall()
		print(values)
		for value in values:
			item = QtWidgets.QListWidgetItem()
			item.setText(value[0])
			self.values_list.addItem(item)
	except:
		a.execute('create table {} (value)'.format(variable))

	a.close()

def add_value(self,main_win):
	a=sq.connect('Data_Bases/constant_values.db')
	try:
		variable=self.variables.currentItem().text().replace(" ","_")
		
		a.execute('insert into {} (value) values ("{}")'.format(variable,self.value_text.text()))
		a.commit()
		self.value_text.clear()
		view_values(self)
		a.close()
		refresh_constant(self,main_win)
	except:
		pass
	

def select_value(self):
	value=self.values_list.currentItem().text()
	self.value_text.setText(value)

def edit_value(self,main_win):
	a=sq.connect('Data_Bases/constant_values.db')
	try:
		variable=self.variables.currentItem().text().replace(" ","_")

		a.execute('update {} set value="{}" where value="{}"'.format(variable,self.value_text.text(),self.values_list.currentItem().text()))
		a.commit()
		a.close()

		view_values(self)
		self.value_text.clear()
		refresh_constant(self,main_win)
	except:
		pass

def delete_value(self,main_win):
		a=sq.connect('Data_Bases/constant_values.db')
	#try:
		variable=self.variables.currentItem().text().replace(" ","_")
		value=self.values_list.currentItem().text()
		a.execute('delete from {} where value="{}"'.format(variable,value))
		a.commit()
		a.close()

		view_values(self)
		self.value_text.clear()
		refresh_constant(self,main_win)
	#except:
		pass


def refresh_constant(self,main_win):
	combo_boxs=[main_win.worker_gender_2,main_win.nationality,main_win.worker_blood,main_win.worker_section,main_win.worker_position,main_win.marital_status,main_win.worker_work_time,main_win.military_service,main_win.worker_driving]

	print((main_win,self.variables.currentItem().text().replace(" ","_"),combo_boxs[self.variables.currentIndex().row()]))
	func.set_constant_values(main_win,(self.variables.currentItem().text().replace(" ","_"),),(combo_boxs[self.variables.currentIndex().row()],))

#####################################################################################################################
################################################ ############### ####################################################
#####################################################################################################################
