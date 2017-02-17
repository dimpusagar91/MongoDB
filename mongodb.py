import pymongo

class mdb:

	def create_mdb(self): #creation of Database
		connection = pymongo.MongoClient()
		mydatabase1=input("Enter the Database name: ")
		db = connection[mydatabase1]
		cursor = db.move.insert({"Data":""})

	def insert_mdb(self): #insertion of document into Collection
		connection = pymongo.MongoClient()
		mydatabase1=input("Enter the Database name: ")
		db = connection[mydatabase1]
		col=input("Enter the Collection name: ")
		collection = db[col]
		flag = True
		while flag:

			ans = input("Do you want to insert document[Y/N]: ")
	
			if( ans == "Y" or ans == "y"):
				title1=str(input("Enter the title: ")) 
				description1=str(input("Enter the description: "))
				by1=str(input("Enter the by: "))
				url1=str(input("Enter the url: "))
				tags1=str(input("Enter the tags: "))
				likes1=int(input("Enter the likes: "))
				dbcol = {'title':title1,'description':description1,'by':by1,'url':url1,'tags':tags1,'likes':likes1}
				db[col].insert(dbcol)
				flag = True

			elif( ans == "N" or ans == "n"):
				flag = False
		
			else:
				print("Invalid Entry..!!")

	def update_mdb(self):#updation of document into Collection
		connection = pymongo.MongoClient()
		mydatabase1=input("Enter the Database name: ")
		db = connection[mydatabase1]
		col=input("Enter the Collection name: ")
		collection = db[col]		
		flag = True
		while flag:
			ans = input("Do you want to update document[Y/N]: ")
			if( ans == "Y" or ans == "y"):
				key1=input("Enter the key for the identification of Document: ")
				value1=input("Enter the value for the entered key for identification of the document: ")
				title1=str(input("Enter the title: ")) 
				description1=str(input("Enter the description: "))
				by1=str(input("Enter the by: "))
				url1=str(input("Enter the url: "))
				tags1=str(input("Enter the tags: "))
				likes1=int(input("Enter the likes: "))
				dbcol = {'title':title1,'description':description1,'by':by1,'url':url1,'tags':tags1,'likes':likes1}
				db[col].update({key1:value1},dbcol)
				flag = True

			elif( ans == "N" or ans == "n"):
				flag = False

			else:
				print("Invalid Entry..!!")

	def read_mdb(self):#reading the Collection
		connection = pymongo.MongoClient()
		mydatabase1=input("Enter the Database name: ")
		db = connection[mydatabase1]
		col=input("Enter the Collection name: ")
		collection = db[col]
		cursor = db[col].find()
		for i in cursor:
			print(i)

	def delete_mdb(self):#deleting the document from the Collection
		connection = pymongo.MongoClient()
		mydatabase1=input("Enter the Database name: ")
		db = connection[mydatabase1]
		col=input("Enter the Collection name: ")
		collection = db[col]
		key1=input("Enter the key: ")
		value1=input("Enter the value: ")
		result = db[col].remove({key1:value1})
c=mdb()
while True:
	print("Enter 1 for Creation of Database\nEnter 2 for Insertion of Documents\nEnter 3 for Updation of document\nEnter 4 for Deletion of document\nEnter 5 for Exit")
	a = int(input("Enter the desired option: "))
	if(a==1):
		flag = True
		while flag:
			ans = input("Do you want to CREATE database[Y/N]: ")
			if(ans == 'Y' or ans == 'y'):
				c.create_mdb()
				flag = True
			elif(ans == 'N' or ans == 'n'):
				flag = False
			else:
				print("Invalid Input..!!!")
	elif(a==2):	
		flag = True
		while flag:
			ans = input("Do you want to INSERT documents into collection[Y/N]: ")
			if(ans == 'Y' or ans == 'y'):
				c.insert_mdb()
				c.read_mdb()
				flag = True
			elif(ans == 'N' or ans == 'n'):
				flag = False
			else:
				print("Invalid Input..!!!")
	elif(a==3):
		flag = True
		while flag:
			ans = input("Do you want to UPDATE any documents from a collection[Y/N]: ")
			if(ans == 'Y' or ans == 'y'):
				c.update_mdb()
				c.read_mdb()
				flag = True
			elif(ans == 'N' or ans == 'n'):
				flag = False
			else:
				print("Invalid Input..!!!")
	elif(a==4):
		flag = True
		while flag:
			ans = input("Do you want to Delete document in the collection[Y/N]: ")
			if(ans == 'Y' or ans == 'y'):
				c.delete_mdb()
				c.read_mdb()
				flag = True
			elif(ans == 'N' or ans == 'n'):
				flag = False
			else:
				print("Invalid Input..!!!")
	elif(a==5):
		break
	
	else:
		print("Invalid Entry..!!!")

