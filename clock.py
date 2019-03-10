from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=120)
def timed_job():
   print('This job is run every three minutes.')

sched.start()
