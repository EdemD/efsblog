from apscheduler.schedulers.blocking import BlockingScheduler
import psycopg2

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():

	print('This job is run every three minutes.')
	
	try:
		connection = psycopg2.connect(user="lcpswybvhdtxgt",
									  password="eb128c6e75b41212a5709223ffa9ec58f975939f2267bf262e07e93729e222f3",
									  host="ec2-54-83-203-198.compute-1.amazonaws.com",
									  port="5432",
									  database="d5k81ffjrgb3gr",
									  sslmode="require")
		cursor = connection.cursor()
		# Print PostgreSQL Connection properties
		print(connection.get_dsn_parameters(), "\n")
		# Print PostgreSQL version
		cursor.execute("SELECT version();")
		record = cursor.fetchone()
		print("You are connected to - ", record, "\n")
		
		cursor.execute("SELECT * from Customer;")
		record = cursor.fetchone()
		print("Here are our customers - ", record, "\n")
		
		cursor.close()
		connection.close()
		# print("PostgreSQL connection is closed")
	except (Exception, psycopg2.Error) as error:
		print("Error while connecting to PostgreSQL", error)
	finally:
		# closing database connection.
		# if (connection):
		# cursor.close()
		# connection.close()
		print("PostgreSQL connection is closed")

		# store all the fetched data in the ans variable

		# ans= cursor.fetchall()

		# loop to print all the data
		# for i in ans:
		#    print(i)

sched.start()
