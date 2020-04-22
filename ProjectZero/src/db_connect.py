import mysql.connector

class mySql():
	def __init__(self,User,Passwd,Database):

			self.host="localhost"
			self.user=str(User)
			self.passwd=str(Passwd)
			self.database=str(Database)
			self.dbconnect()
		
	def dbconnect(self):
			self.db = mysql.connector.connect(
			host="localhost",
			user=self.user,
			passwd=self.passwd,
			database=self.database	)
			self.dbcursor = self.db.cursor()		

	def tableCreate(self, tablename, rows, values=None):
		sql = "create table "
		sql = sql + str(tablename)
		"""definitino of rows"""
		sql = sql + "(id int auto_increment primary key,"
		if type(rows) == str:
			sql = sql + str(rows)+","
		else:
			x=0
			for item in rows:
				if values == None:
					sql = sql + str(item)+","
				else:
					sql = sql + str(item) + " "+ str(values[x])+","
					x +=1
		try:
			sql = sql + 'create_at timestamp default current_timestamp)'
			self.dbcursor.execute(sql)
			return True

		except mysql.connector.errors.ProgrammingError as error:
			#Table allready exist
			if error.sqlstate == "42S01":
				return error.sqlstate
			else:
				return error.msg

	def tableDelete(self,tableName):
		try:
			sql="DROP TABLE "+ tableName
			self.dbcursor.execute(sql)
			return True
		except mysql.connector.errors.ProgrammingError as error:
			#table does not exist
			if error.sqlstate == "42S02":
				return error.sqlstate
			else:
				return error.msg
	#attributes are a 2 dimension Array [["row01",value]]
	def recordCreate(self, table, attributes):
		sql= "insert into " + table+" ("
		sqlTail = ") values ("
		values = []
		for item in attributes:
			sql = sql + str(item[0])+","
			values.append(item[1])
			sqlTail = sqlTail + "%s,"
		sql = sql[0:-1]
		sqlTail = sqlTail[0:-1] +")"
		values = (values)
		sql= sql + sqlTail
		try:
			self.dbcursor.execute(sql, values)
			self.db.commit()
			return True
		except mysql.connector.errors.ProgrammingError as error:
			print(error)
			return False

	def executeSql(self, sql):
		try:
			self.dbcursor.execute(sql)
			return True
		except mysql.connector.errors.ProgrammingError as error:
			return False
		
	def recordDelete(self,table,rowname,value):
		sql = 'delete from '+table+' where '+rowname+'="'+value+'"'
		try:
			self.dbcursor.execute(sql)
			self.db.commit()
			return True
		except mysql.connector.errors.ProgrammingError as error:
			return False

	# selectAttribute= rowto select  condition=row to select
	def recordSelect(self, table, selectColume, condition, value,maxResult):
		sql = 'select '+selectColume+' from '+table+' where '+condition+'="'+value+'"'
		try:
			self.dbcursor.execute(sql)
			result = self.dbcursor.fetchone()
			return self.returnSpecificCountOfResult(result,maxResult)
		except mysql.connector.errors.ProgrammingError as error:
			result = None
			return result

	def returnSpecificCountOfResult(self,result, maxResult):
		i=0
		value = []
		if maxResult == 0:
			return None

		while i != maxResult:
			value.append(result[i])
			i += 1
			if i>10:
				break
		return value
		
	def recordDoesExists(self, table,attribute, value):
		sql = 'select * from '+table+' where '+attribute+'="'+value+'"'
		try:
			self.dbcursor.execute(sql)
			result = self.dbcursor.fetchall()
			if result:
				return True
			else:
				return False
		except mysql.connector.errors.ProgrammingError as error:

			return False
			
#sql = mySql("dbuser","34df!5awe","belegeablegen")
#rows=["name varchar(250)","match01 varchar(250)","match02 varchar(250),match03 varchar(250)","match04 varchar(250)"]
#rows=["data_path varchar (250)","archive_path varchar (250)","steuern_path varchar (250)"]
#table="config"
#sql.createTable(table,rows)
# ~ attributes =  [["latitude","47.22133"],["longitude", "8.222311"],["homebase", False]]
# ~ value = sql.createRecord("waypoints", attributes)
# ~ value = sql.selectRecord("waypoints", "homebase=true")

# ~ attributes = "wp_number"
# ~ value = sql.deleteRecord("waypoints", attributes)

# ~ print (value)

