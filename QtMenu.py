import sys
from PyQt4 import QtGui, QtCore
import os
import DB_manager

mainPath = ('main240.png')
homePath = ('home.png')
exitPath = ('exit.png')
fillPath = ('prescription32.png')
logoPath = ('coordinates.png')
tagPath = ('name.png')
tag2Path = ('tag2.png')
cancelPath = ('cancel.png')
resetPath = ('reset.png')
savePath = ('save.png')
printPath = ('print.png')
stockPath = ('stock.png')
alterPath = ('medicine.png')
nextPath = ('next.png')
beforePath = ('before.png')
afterPath = ('after.png')
saveAfter = ('saveafter.png')
nextAfter = ('nextafter.png')
resetAfter = ('resetafter.png')

sheetFields = {'Item':[], 'Code':[], 'Item Type':[], 'Quantity':[], 'Batch no.':[], 'Expiry':[], 'Price':[], 'Discount %':[], 'VAT %':[], 'Amount':[]}
sheetHeaders = ['Item',  'Quantity', 'Code', 'Item Type', 'Batch no.', 'Expiry', 'Price', 'Discount %', 'VAT %', 'Amount']

dbu = DB_manager.DatabaseUtility('MedDB', 'DemoDB')
dbu.AddEntryToTable('M1', 1, 'MED', 11, '2018-06-20', 20, 18, 1, 1)
dbu.AddEntryToTable('M2', 2, 'MED', 12, '2018-06-21', 25, 18, 2, 2)
dbu.AddEntryToTable('M3', 3, 'SYP', 13, '2018-06-22', 30, 18, 3, 3)
dbu.AddEntryToTable('M4', 4, 'SYP', 14, '2018-06-23', 40, 18, 4, 4)
dbu.AddEntryToTable('M5', 5, 'FMCG', 15, '2018-06-24', 50, 18, 5, 5)

gpname = "Default"
gdname = "Default"
ganame = "Default"
gpaddr = "Default"
gpcont = "Default"
gtamt = 100
gtdisc = 20
gttax = 18

class MainLogo(QtGui.QLabel):
	def __init__(self, parent = None):
		super(MainLogo, self).__init__(parent)
		self.setMouseTracking(1)
		self.pixmap = QtGui.QPixmap(beforePath)
		self.pixmap2 = QtGui.QPixmap(afterPath)
		self.setPixmap(self.pixmap)
		self.installEventFilter(self)

	def eventFilter(self, object, event):
		if event.type() == QtCore.QEvent.MouseMove:
			self.setPixmap(self.pixmap2)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		elif event.type() == QtCore.QEvent.Leave:
			self.setPixmap(self.pixmap)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

class ResetLogo(QtGui.QLabel):
	def __init__(self, parent = None):
		super(ResetLogo, self).__init__(parent)
		self.setMouseTracking(1)
		self.pixmap = QtGui.QPixmap(resetPath)
		self.pixmap2 = QtGui.QPixmap(resetAfter)
		self.setPixmap(self.pixmap)
		self.installEventFilter(self)

	def eventFilter(self, object, event):
		if event.type() == QtCore.QEvent.MouseMove:
			self.setPixmap(self.pixmap2)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		elif event.type() == QtCore.QEvent.Leave:
			self.setPixmap(self.pixmap)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

class SaveLogo(QtGui.QLabel):
	def __init__(self, parent = None):
		super(SaveLogo, self).__init__(parent)
		self.setMouseTracking(1)
		self.pixmap = QtGui.QPixmap(savePath)
		self.pixmap2 = QtGui.QPixmap(saveAfter)
		self.setPixmap(self.pixmap)
		self.installEventFilter(self)

	def eventFilter(self, object, event):
		if event.type() == QtCore.QEvent.MouseMove:
			self.setPixmap(self.pixmap2)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		elif event.type() == QtCore.QEvent.Leave:
			self.setPixmap(self.pixmap)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))	

class NextLogo(QtGui.QLabel):
	def __init__(self, parent = None):
		super(NextLogo, self).__init__(parent)
		self.setMouseTracking(1)
		self.pixmap = QtGui.QPixmap(nextPath)
		self.pixmap2 = QtGui.QPixmap(nextAfter)
		self.setPixmap(self.pixmap)
		self.installEventFilter(self)

	def eventFilter(self, object, event):
		if event.type() == QtCore.QEvent.MouseMove:
			self.setPixmap(self.pixmap2)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		elif event.type() == QtCore.QEvent.Leave:
			self.setPixmap(self.pixmap)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))								


class Home(QtGui.QWidget):
	def __init__(self, parent = None):
		super(Home,self).__init__(parent)
		self.setStyleSheet("background-color: white;")
		
		alias = QtGui.QWidget(self)

		self.l = QtGui.QLabel()
		self.logo = MainLogo(self.l) 
			
		tag = QtGui.QLabel()
		pixmap2 = QtGui.QPixmap(tagPath)
		tag.setPixmap(pixmap2)
			
		tag2 = QtGui.QLabel()
		pixmap3 = QtGui.QPixmap(tag2Path)
		tag2.setPixmap(pixmap3)

		ministock = QtGui.QLabel()
		pixmap4 = QtGui.QPixmap(stockPath)
		ministock.setPixmap(pixmap4)
			
		self.searchInventory = QtGui.QLineEdit(self)
		self.searchInventory.setPlaceholderText('Search Inventory...')
		#self.searchInventory.setFocus()
		#self.searchInventory.show()
		self.goSearch = QtGui.QPushButton('Go', self)

		vbox = QtGui.QVBoxLayout()
		self.setLayout(vbox)

			
		hbox1 = QtGui.QHBoxLayout()
		element1 = QtGui.QWidget(self)
		element1.setLayout(hbox1)
		hbox1.addSpacing(455)
		#hbox1.addWidget(self.logo)
			
		hbox2 = QtGui.QHBoxLayout()
		element2 = QtGui.QWidget(self)
		element2.setLayout(hbox2)
		hbox2.addSpacing(870)
		hbox2.addWidget(tag)
			
		hbox3 = QtGui.QHBoxLayout()
		element3 = QtGui.QWidget(self)
		element3.setLayout(hbox3)
		hbox3.addSpacing(795)
		hbox3.addWidget(tag2)

		hbox4 = QtGui.QHBoxLayout()
		element4 = QtGui.QWidget(self)
		element4.setLayout(hbox4)
		hbox4.addSpacing(800)
		hbox4.addWidget(ministock)
		hbox4.addWidget(self.searchInventory)
		hbox4.addWidget(self.goSearch)
			
		vbox.addWidget(element4)	
		vbox.addSpacing(250)
		vbox.addWidget(element1)
		vbox.addSpacing(100)
		vbox.addWidget(element2)

			#self.setCentralWidget(alias)
		self.menu = QtGui.QMenuBar(self)
		self.toolbar = QtGui.QToolBar(self)

		exitAction = QtGui.QAction(QtGui.QIcon(exitPath), '&Exit', self)
		exitAction.setShortcut('Ctrl+D')
		exitAction.setStatusTip('Exit AxesPro')
		exitAction.triggered.connect(QtGui.qApp.quit)

		self.fillAction = QtGui.QAction(QtGui.QIcon(fillPath), '&New', self)
		self.fillAction.setShortcut('Ctrl+N')
		self.fillAction.setStatusTip('New Prescription')

		self.checkAction = QtGui.QAction(QtGui.QIcon(stockPath), '&Stock', self)
		self.checkAction.setShortcut('Ctrl+F')
		self.checkAction.setStatusTip('Check Inventory')


			#self.statusBar()
		self.toolbar.addAction(self.fillAction)
		self.toolbar.addAction(self.checkAction)
		self.toolbar.addAction(exitAction)

		fileMenu = self.menu.addMenu('&File')
		fileMenu.addAction(exitAction)
			
		self.setGeometry(50, 50, 600, 400)
		self.setWindowTitle('AxesPro')
		self.setFocus()
		self.show()

	def mouseMoveEvent(event):
		print "on Hover"

class Prescription(QtGui.QWidget):
	def __init__(self, parent = None):
		super(Prescription,self).__init__(parent)
		self.setStyleSheet("background-color: white;")
	
		alias = QtGui.QWidget(self)
		self.count = -1
		self.totamt = 0
		self.tottax = 0
		self.totdisc = 0
		vbox = QtGui.QVBoxLayout()
		self.setLayout(vbox)
 
		self.patientPrompt = QtGui.QLabel('Patient Name:')
		self.patientID = QtGui.QLineEdit()
		self.patientID.setFixedWidth(200)

		self.contactPrompt = QtGui.QLabel('Patient Contact:')
		self.patientContact = QtGui.QLineEdit()

		self.addrPrompt = QtGui.QLabel('Patient Address:')
		self.patientAddress = QtGui.QLineEdit()

		self.itemPrompt = QtGui.QLabel('Enter Item Name/ID')
		self.itemID = QtGui.QLineEdit()

		self.qtyPrompt = QtGui.QLabel('Enter Quantity')
		self.Qty = QtGui.QLineEdit()

		self.expFlag = QtGui.QLabel('Expiry Date')
		self.Exp = QtGui.QLineEdit()

		self.dosagePrompt = QtGui.QLabel('Dosage Instructions')
		self.Dosage = QtGui.QLineEdit()

		self.discPrompt = QtGui.QLabel('Discount %')
		self.Discount = QtGui.QLineEdit()

		self.time_label = QtGui.QLabel('Time:', self)
		self.time_label.setText(QtCore.QDateTime.currentDateTime().toString()) 

		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.updateTime)
		self.timer.start(1000)

		self.empPrompt = QtGui.QLabel('Attendant Name:')
		self.empID = QtGui.QLineEdit()
		#self.empID.setFixedWidth(200)

		self.docPrompt = QtGui.QLabel('Doctor Name:')
		self.docID = QtGui.QLineEdit()
		#self.docID.setFixedWidth(200)

		self.adder = QtGui.QPushButton('Add', self)
		self.adder.clicked.connect(self.addMed)

		self.cancelOrder = QtGui.QLabel(self)
		self.pixmap = QtGui.QPixmap(cancelPath)
		self.cancelOrder.setPixmap(self.pixmap)

		self.l1 = QtGui.QLabel()
		self.resetOrder = ResetLogo(self.l1)

		self.l2 = QtGui.QLabel()
		self.saveOrder = SaveLogo(self.l2)

		self.l3 = QtGui.QLabel()
		self.proceed = QtGui.QPushButton('Next', self)


		self.table = QtGui.QTableWidget(self)
		self.table.setRowCount(15)
		self.table.setColumnCount(10)
		headers = []
		for key, value in sheetFields.items():
			headers.append(key)
			for m, item in enumerate(sheetFields[key]):
				newitem = QtGui.QTableWidgetItem(item)
				self.table.setItem(m, n, newitem)
		self.table.setHorizontalHeaderLabels(sheetHeaders)		
		self.table.setColumnWidth(0, 200)
		self.table.setColumnWidth(5, 150)
		self.table.setColumnWidth(9, 100)
		self.table.setColumnWidth(2, 150)
		self.table.setColumnWidth(4, 105)
		self.table.setItem(14, 8, QtGui.QTableWidgetItem("Total Amount "))
		
		hbox1 = QtGui.QHBoxLayout()
		element1 = QtGui.QWidget(self)
		element1.setLayout(hbox1)
		#hbox1.addSpacing(40)
		hbox1.addWidget(self.table)
		
		hbox2 = QtGui.QHBoxLayout()
		element2 = QtGui.QWidget(self)
		element2.setLayout(hbox2)
		hbox2.addSpacing(1000)
		hbox2.addWidget(self.time_label)

		hbox3 = QtGui.QHBoxLayout()
		element3 = QtGui.QWidget(self)
		element3.setLayout(hbox3)
		hbox3.addWidget(self.empPrompt)
		#hbox3.addSpacing(5)
		hbox3.addWidget(self.empID)
		#hbox3.addSpacing(50)
		hbox3.addWidget(self.docPrompt)
		#hbox3.addSpacing(5)
		hbox3.addWidget(self.docID)

		hbox4 = QtGui.QHBoxLayout()
		element4 = QtGui.QWidget(self)
		element4.setLayout(hbox4)
		hbox4.addSpacing(900)
		hbox4.addWidget(self.resetOrder)
		hbox4.addWidget(self.saveOrder)
		hbox4.addWidget(self.proceed)

		hbox5 = QtGui.QHBoxLayout()
		element5 = QtGui.QWidget(self)
		element5.setLayout(hbox5)
		hbox5.addSpacing(35)
		hbox5.addWidget(self.itemPrompt)
		hbox5.addWidget(self.qtyPrompt)
		hbox5.addWidget(self.expFlag)
		hbox5.addWidget(self.dosagePrompt)
		hbox5.addWidget(self.discPrompt)

		hbox6 = QtGui.QHBoxLayout()
		element6 = QtGui.QWidget(self)
		element6.setLayout(hbox6)
		#hbox6.addSpacing(100)
		hbox6.addWidget(self.itemID)
		hbox6.addWidget(self.Qty)
		hbox6.addWidget(self.Exp)
		hbox6.addWidget(self.Dosage)
		hbox6.addWidget(self.Discount)
		hbox6.addWidget(self.adder)

		grid1 = QtGui.QGridLayout()
		element7 = QtGui.QWidget(self)
		element7.setLayout(grid1)
		grid1.addWidget(self.patientPrompt, 1, 0)
		grid1.addWidget(self.patientID, 1, 1)
		grid1.addWidget(self.addrPrompt, 1, 2)
		grid1.addWidget(self.patientAddress, 1, 3, 2, 1)
		grid1.addWidget(self.contactPrompt)
		grid1.addWidget(self.patientContact)


		vbox.addSpacing(20)
		vbox.addWidget(element2)
		#vbox.addSpacing(5)
		vbox.addWidget(element3)
		vbox.addWidget(element7)
		vbox.addWidget(element5)
		vbox.addWidget(element6)
		vbox.addWidget(element1)
		vbox.addWidget(element4)

		#self.setCentralWidget(alias)
		self.menu = QtGui.QMenuBar(self)
		self.toolbar = QtGui.QToolBar(self)



		self.homeAction = QtGui.QAction(QtGui.QIcon(homePath), '&Home', self)
		self.homeAction.setShortcut('Esc')
		self.homeAction.setStatusTip('Return Home')

		#self.statusBar()

		self.toolbar.addAction(self.homeAction)
		#self.toolbar.addAction(exitAction)

		fileMenu = self.menu.addMenu('&File')
		#fileMenu.addAction(exitAction)
			
		self.setGeometry(50, 50, 600, 400)
		self.setWindowTitle('AxesPro')
		self.show()


	def updateTime(self):
		current = QtCore.QDateTime.currentDateTime().toString()
		self.time_label.setText(current)

	def addMed(self):
		global gpname
		gpname = str(self.patientID.text())
		#print(str(self.patientID.text()))
		#print(gpname)
		global ganame 
		ganame = str(self.empID.text())
		global gdname
		gdname = str(self.docID.text())
		global gpaddr
		gpaddr = str(self.patientAddress.text())
		global gpcont
		gpcont = str(self.patientContact.text())
		self.count += 1
		med = str(self.itemID.text())
		cmd = "SELECT * FROM DemoDB WHERE Item_Name = '" + med + "'"
		res1 = dbu.RunCommand(cmd)
		res = res1[0]
		#print res
		tname = res[0]
		tcode = res[1]
		ttype = res[2]
		tbno = res[3]
		texp = res[4]
		tprice = int(res[5])
		tvat = res[6]
		x = res[7]
		y = res[8]
		tqty = int(self.Qty.text())
		tdisc = str(self.Discount.text())
		tdos = str(self.Dosage.text())
		tamt = tqty*tprice
		#self.table.setItem()
		fin = []
		fin.append(tname)
		fin.append(tqty)
		fin.append(tcode)
		fin.append(ttype)
		fin.append(tbno)
		fin.append(texp)
		fin.append(tprice)
		fin.append(tdisc)
		fin.append(tvat)
		fin.append(tamt)
		#print tamt
		self.totamt += tamt
		for i in xrange(0,10):
			self.table.setItem(self.count, i, QtGui.QTableWidgetItem(str(fin[i])))
		self.table.setItem(14, 9, QtGui.QTableWidgetItem(str(self.totamt)))	
		global gtamt
		gtamt = str(self.totamt)
		global gtdisc
		gtdisc = str(self.totdisc)
		global gttax
		gttax = str(self.tottax)

class Inventory(QtGui.QWidget):
	def __init__(self, parent = None):
		super(Inventory, self).__init__(parent)
		self.setGeometry(100,100,600,400)
		self.setStyleSheet("background-color: white;")

		vbox = QtGui.QVBoxLayout()
		self.setLayout(vbox)

		self.prompt = QtGui.QLabel('Enter Item Name:')
		self.input = QtGui.QLineEdit()

		self.search = QtGui.QPushButton('Go', self)
		self.search.clicked.connect(self.findStock)

		self.out1 = QtGui.QLabel('Stock in Inventory:')
		self.stock = QtGui.QLineEdit()

		self.out2 = QtGui.QLabel('Expiry Date:')
		self.expiry = QtGui.QLineEdit()

		self.out3 = QtGui.QLabel('Next Refill On:')
		self.refill = QtGui.QLineEdit()

		hbox1 = QtGui.QHBoxLayout()
		element1 = QtGui.QWidget(self)
		element1.setLayout(hbox1)
		hbox1.addWidget(self.prompt)
		hbox1.addSpacing(5)
		hbox1.addWidget(self.input)
		hbox1.addSpacing(5)
		hbox1.addWidget(self.search)
		hbox1.addSpacing(500)
		
		hbox2 = QtGui.QHBoxLayout()
		element2 = QtGui.QWidget(self)
		element2.setLayout(hbox2)
		hbox2.addWidget(self.out1)
		hbox1.addSpacing(5)
		hbox2.addWidget(self.stock)
		hbox2.addSpacing(700)

		hbox3 = QtGui.QHBoxLayout()
		element3 = QtGui.QWidget(self)
		element3.setLayout(hbox3)
		hbox3.addWidget(self.out2)
		hbox3.addSpacing(5)
		hbox3.addWidget(self.expiry)
		hbox3.addSpacing(700)

		hbox4 = QtGui.QHBoxLayout()
		element4 = QtGui.QWidget(self)
		element4.setLayout(hbox4)
		hbox4.addWidget(self.out3)
		hbox4.addSpacing(5)
		hbox4.addWidget(self.refill)
		hbox4.addSpacing(700)

		vbox.addSpacing(100)
		vbox.addWidget(element1)
		vbox.addSpacing(100)
		vbox.addWidget(element2)
		vbox.addSpacing(5)
		vbox.addWidget(element3)
		vbox.addSpacing(5)
		vbox.addWidget(element4)
		vbox.addSpacing(400)
		
		self.menu = QtGui.QMenuBar(self)
		self.toolbar = QtGui.QToolBar(self)

		self.homeAction = QtGui.QAction(QtGui.QIcon(homePath), '&Home', self)
		self.homeAction.setShortcut('Esc')
		self.homeAction.setStatusTip('Return Home')

		#self.statusBar()

		self.toolbar.addAction(self.homeAction)
		#self.toolbar.addAction(exitAction)

		fileMenu = self.menu.addMenu('&File')
		#fileMenu.addAction(exitAction)
			
		self.setGeometry(50, 50, 600, 400)
		self.setWindowTitle('Stock')
		self.show()

	def findStock(self):
		self.stock.setText("None")
		self.expiry.setText("Today")
		self.refill.setText("Tomorrow")	

class confirmPrescription(QtGui.QWidget):
	def __init__(self, parent = None):
		super(confirmPrescription, self).__init__(parent)
		self.setGeometry(50, 50, 600, 400)
		self.setStyleSheet("background-color: white;")

		vbox = QtGui.QVBoxLayout()
		self.setLayout(vbox)

		self.pName = QtGui.QLabel("Patient Name: ")
		self.confPName = QtGui.QLabel()
		self.aName = QtGui.QLabel("Attendant Name: ")
		self.confAName = QtGui.QLabel()
		self.dName = QtGui.QLabel("Doctor Name: ")
		self.confDName = QtGui.QLabel()
		self.pAddr = QtGui.QLabel("Patient Address: ")
		self.confPAddr = QtGui.QLabel()
		self.pContact = QtGui.QLabel("Patient Contact: ")
		self.confPCnct = QtGui.QLabel()
		self.Amt = QtGui.QLabel("Total Amount: ")
		self.confAmt = QtGui.QLabel()
		self.Disc = QtGui.QLabel("Total Discount: ")
		self.confDisc = QtGui.QLabel()
		self.Tax = QtGui.QLabel("Tax %: ")
		self.confTax = QtGui.QLabel()
		self.amtPay = QtGui.QLabel("Net Amount Payable: ")
		self.confAmtPay = QtGui.QLabel()
		self.payMode = QtGui.QLabel("Payment Mode")

		self.cash = QtGui.QRadioButton("Cash")
		self.debit = QtGui.QRadioButton("Debit Card")
		self.credit = QtGui.QRadioButton("Credit Card")

		self.printPres = QtGui.QLabel()
		pixmap = QtGui.QPixmap(printPath)
		self.printPres.setPixmap(pixmap)

		hbox1 = QtGui.QHBoxLayout()
		element1 = QtGui.QWidget(self)
		element1.setLayout(hbox1)
		hbox1.addWidget(self.pName)
		hbox1.addWidget(self.confPName)
		hbox1.addSpacing(300)
		hbox1.addWidget(self.aName)
		hbox1.addWidget(self.confAName)

		hbox2 = QtGui.QHBoxLayout()
		element2 = QtGui.QWidget(self)
		element2.setLayout(hbox2)
		hbox2.addWidget(self.pAddr)
		hbox2.addWidget(self.confPAddr)
		hbox2.addSpacing(300)
		hbox2.addWidget(self.dName)
		hbox2.addWidget(self.confDName)

		hbox3 = QtGui.QHBoxLayout()
		element3 = QtGui.QWidget(self)
		element3.setLayout(hbox3)
		hbox3.addWidget(self.pContact)
		hbox3.addWidget(self.confPCnct)

		hbox4 = QtGui.QHBoxLayout()
		element4 = QtGui.QWidget(self)
		element4.setLayout(hbox4)
		hbox4.addWidget(self.Amt)
		hbox4.addWidget(self.confAmt)

		hbox5 = QtGui.QHBoxLayout()
		element5 = QtGui.QWidget(self)
		element5.setLayout(hbox5)
		hbox5.addWidget(self.Disc)
		hbox5.addWidget(self.confDisc)
		
		hbox6 = QtGui.QHBoxLayout()
		element6 = QtGui.QWidget(self)
		element6.setLayout(hbox6)
		hbox6.addWidget(self.Tax)
		hbox6.addWidget(self.confTax)
		
		hbox7 = QtGui.QHBoxLayout()
		element7 = QtGui.QWidget(self)
		element7.setLayout(hbox7)
		hbox7.addWidget(self.amtPay)
		hbox7.addWidget(self.confAmtPay)
		
		hbox8 = QtGui.QHBoxLayout()
		element8 = QtGui.QWidget(self)
		element8.setLayout(hbox8)
		hbox8.addWidget(self.payMode)

		hbox9 = QtGui.QHBoxLayout()
		element9 = QtGui.QWidget(self)
		element9.setLayout(hbox9)
		hbox9.addWidget(self.cash)
		hbox9.addSpacing(50)
		hbox9.addWidget(self.debit)
		hbox9.addSpacing(50)
		hbox9.addWidget(self.credit)

		hbox10 = QtGui.QHBoxLayout()
		element10 = QtGui.QWidget(self)
		element10.setLayout(hbox10)
		hbox10.addSpacing(950)
		hbox10.addWidget(self.printPres)

		vbox.addWidget(element1)
		vbox.addWidget(element2)
		vbox.addWidget(element3)
		vbox.addWidget(element4)
		vbox.addWidget(element5)
		vbox.addWidget(element6)
		vbox.addWidget(element7)
		vbox.addWidget(element8)
		vbox.addWidget(element9)
		vbox.addWidget(element10)
		self.setWindowTitle('Confirm')
		self.show()		
		
		


class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setGeometry(50, 50, 600, 400)
		self.setStyleSheet("background-color: white;")
		self.startHome()

	def startHome(self):
		self.Home = Home(self)
		self.setWindowTitle('AxesPro')
		self.setCentralWidget(self.Home)
		self.Home.fillAction.triggered.connect(self.startNewOrder)
		self.Home.logo.mousePressEvent = self.startNewOrder
		self.Home.goSearch.clicked.connect(self.checkInventory)
		self.Home.checkAction.triggered.connect(self.checkInventory)
		self.setStyleSheet("background-color: white;")
		self.show()

	def startNewOrder(self, event):
		QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.window = Prescription(self)
		self.setWindowTitle('Fill New Prescription')
		self.setCentralWidget(self.window)
		self.window.homeAction.triggered.connect(self.startHome)
		self.window.proceed.clicked.connect(self.confPres)
		self.setStyleSheet("background-color: white;")
		self.show()	

	def checkInventory(self):
		self.window = Inventory(self)
		self.setWindowTitle('Check Inventory')
		self.setCentralWidget(self.window)
		self.window.homeAction.triggered.connect(self.startHome)
		self.setStyleSheet("background-color: white;")
		self.show()			

	def confPres(self):
		QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.window = confirmPrescription(self)
		self.setWindowTitle('Confirm Prescription')
		self.setCentralWidget(self.window)
		self.setStyleSheet("background-color: white;")
		self.window.confPName.setText(str(gpname))
		#print(gpname)
		self.window.confAName.setText((str(ganame)))
		self.window.confDName.setText((str(gdname)))
		self.window.confPAddr.setText((str(gpaddr)))
		self.window.confPCnct.setText((str(gpcont)))
		self.window.confAmt.setText((str(gtamt)))
		self.window.confDisc.setText((str(gtdisc)))
		self.window.confTax.setText((str(gttax)))
		apay = int(gtamt) - int(gtdisc) + int(gttax)
		self.window.confAmtPay.setText(str(apay))
		self.show()


def main():
	app = QtGui.QApplication(sys.argv)
	demo = MainWindow()
	sys.exit(app.exec_())

if __name__ == main():
	main()
