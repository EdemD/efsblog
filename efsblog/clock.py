from apscheduler.schedulers.blocking import BlockingScheduler
import sqlite3

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
   print('This job is run every three minutes.')
   
   # connect withe the myTable database 
   connection = sqlite3.connect("myTable.db") 

   # cursor object 
   crsr = connection.cursor() 

   # execute the command to fetch all the data from the table emp 
   crsr.execute("SELECT * FROM Customer")  

   # store all the fetched data in the ans variable 
   ans= crsr.fetchall()  

   # loop to print all the data 
   for i in ans: 
       print(i) 

sched.start()
