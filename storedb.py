import sqlite3

import os

conf_dir = os.path.expanduser("~/PycharmProjects/Jarvis")
db_dir=os.path.join(conf_dir,"databases")
db_file=os.path.join(db_dir,"jarvis.db")

class db:
	con = sqlite3.connect(db_file,check_same_thread=False)
	with con:
		cur = con.cursor()
	cur.execute("create table if not exists commands(name text,action text);")
	
	def get_action(self,name):
		action=self.cur.execute("select action from commands where name=?",(name,))
		action=self.cur.fetchone()
		return action


	def update_action(self,name,action):
		self.cur.execute("update commands set action=? where name=?",(action,name))
		self.con.commit()

	def new_action(self,name,action):
		self.cur.execute("insert into commands(name,action) values(?,?);",(name,action))
		self.con.commit()
	
	def query(self,query):
		self.cur.execute(query)

	def delete_action(self,name):
		self.cur.execute("delete from commands where name = ?;",(name,))
		self.con.commit()

	def get_all(self):
		act_dict={}
		actions=self.cur.execute('select * from commands')
		actions=self.cur.fetchall()
		for l in actions:
			act_dict[l[0]]=l[1]
		return act_dict

class pushdb():
	con = sqlite3.connect(db_file,check_same_thread=False)
	with con:
		cur = con.cursor()
	cur.execute("create table if not exists pushbullet(api_key text);")
	

	def query(self,query):
		self.cur.execute(query)	

	def add_key(self,key):
		query="insert or ignore into pushbullet(api_key) values('{0}');".format(key)
		self.query(query)
		self.con.commit()
		
class sysdb():
	con = sqlite3.connect(db_file,check_same_thread=False)
	with con:
		cur = con.cursor()
	cur.execute("create table if not exists system(name text,action text);")

	def query(self,query):
		self.cur.execute(query)	

	def get_action(self,name):
		action=self.cur.execute("select action from system where name=?",(name,))
		action=self.cur.fetchone()
		return action
	def get_all(self):
		act_dict={}
		actions=self.cur.execute('select * from system')
		actions=self.cur.fetchall()
		for l in actions:
			act_dict[l[0]]=l[1]
		return act_dict