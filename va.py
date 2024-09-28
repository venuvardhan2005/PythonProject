import mysql.connector

mydb=mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "user"
)
mycursor=mydb.cursor()

class TravelAdvisories:
      def __init__(self, advisory_id, title, description, date_issued):
        self.advisory_id = advisory_id
        self.title = title
        self.description = description
        self.date_issued = date_issued

      def __str__(self):
        return f"Advisory({self.advisory_id}, {self.title}, {self.description}, {self.date_issued})"
      
class Country:
     def __init__(self, country_id, name, region, population):
        self.country_id = country_id
        self.name = name
        self.region = region
        self.population = population
        self.travel_advisories = []

     def __repr__(self):
        return f"Country({self.country_id}, {self.name}, {self.region}, {self.population})"


class ForeignAffairsPortal:
    def createdb():     
        try:
            mycursor.execute("CREATE DATABASE MYDB")
        except Exception:
            print('Already created db')
    
    def useDB():
        try:
            mycursor.execute('USE MYDB')
        except Exception:
            print('already used db')
    
    def createProgram():
        try:
            mycursor.execute('create table MyTable (country varchar(100),level varchar(20))')
        except Exception:
            print('already created table')

    def insertProgram():
        try:
            mycursor.execute("INSERT INTO MyTable(country,level) values('RUSSIA','created1 ')")
            mydb.commit()
            print('inserted Successfully  !')
        except Exception:
            print('Already inserted Data into Table')

    def updateProgram():
        try:
            mycursor.execute("UPDATE MYTABLE Set level='not-created' where country='RUSSIA'")
            mydb.commit()
            print('Updated Successfully !')
        except Exception:
            print('Already nstertd Data into Table')

    def deleteProgram():
        try:
            mycursor.execute("delete from MyTable where country='USA' ")
            mydb.commit()
            print('Deleted Successfully')
        except Exception:
            print('Issue While Deleting')
            


        
tm=ForeignAffairsPortal
tm.createdb()
tm.useDB()
tm.createProgram()
tm.insertProgram()
tm.updateProgram()
