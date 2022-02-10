from apscheduler.schedulers.blocking import BlockingScheduler

import luigi_etl  as myetl

#import folder.file as myModule
# k = myModule.Klasa()

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')
    myetl.externalCallTask()
    print('End of job ....')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()