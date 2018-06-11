import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##===============================================

class DatabaseUtility: 
	def __init__(self, database, tableName):
		self.db = database
		self.tableName = tableName
		self.cnx = mysql.connector.connect(user = 'root',
									password = 'AviPiyaSanskar004',
									host = '127.0.0.1')
		self.cursor = self.cnx.cursor()

		self.ConnectToDatabase()
		self.CreateTable()
		
	def ConnectToDatabase(self):
		try:
			self.cnx.database = self.db
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				self.CreateDatabase()
				self.cnx.database = self.db
			else:
				print(err.msg)

	def CreateDatabase(self):
		try:
			self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" %self.db)
		except mysql.connector.Error as err:
			print("Failed creating database: {}".format(err))

	def CreateTable(self):
		cmd = (" CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
			" `Item_Name` char(50) NOT NULL,"
			" `Item_Code` int(10) NOT NULL,"
			" `Item_Type` char(10) NOT NULL,"
			" `Batch_No.` int(10) NOT NULL,"
			" `Expiry` date NOT NULL,"
			" `Price` int(10) NOT NULL,"
			" `VAT` int(10) NOT NULL,"
			" `x_pos` int(5) NOT NULL,"
			" `y_pos` int(5) NOT NULL,"
			" PRIMARY KEY (`Item_Name`, `Item_Code`)"
			") ENGINE=InnoDB;")
		self.RunCommand(cmd)

	def GetTable(self):
		self.CreateTable()
		return self.RunCommand("SELECT * FROM %s;" % self.tableName)

	def GetColumns(self):
		return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName)

	def RunCommand(self, cmd):
		print ("RUNNING COMMAND: " + cmd)
		try:
			self.cursor.execute(cmd)
		except mysql.connector.Error as err:
			print ('ERROR MESSAGE: ' + str(err.msg))
			print ('WITH ' + cmd)
		try:
			msg = self.cursor.fetchall()
		except:
			msg = self.cursor.fetchone()
		return msg

	def AddEntryToTable(self, Iname, ICode, IType, Bno, Exp, Price, vat, x, y):
		
		cmd = " INSERT INTO " + self.tableName + " (`Item_Name`, `Item_Code`, `Item_Type`, `Batch_No.`, `Expiry`, `Price`, `VAT`, `x_pos`, `y_pos`)"
		cmd += " VALUES ('%s', %d, '%s', %d, '%s', %d, %d, %d, %d )" % (Iname, ICode, IType, Bno, Exp, Price, vat, x, y)
		self.RunCommand(cmd)

	def __del__(self):
		self.cnx.commit()
		self.cursor.close()
		self.cnx.close()

##===============================================
##===============================================


if __name__ == '__main__':
	db = 'myFirstDB'
	tableName = 'test8'

	dbu = DatabaseUtility(db, tableName)

	#dbu.AddEntryToTable('M1', 123, 'MED', 789, '2018-06-10', 25, 18, 2, 2)
	#print (dbu.GetColumns())
	#print(dbu.GetTable())
