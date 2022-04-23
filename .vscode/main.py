import os
import sched
import time

# instance is created
scheduler = sched.scheduler(time.time, time.sleep)
  
def get_all_monitors:
    pass

def execute_monitor:
    pass
  
# first event with delay of
# 1 second
e1 = scheduler.enter(1, 1, 
                     print_event, ('1 st', ))
  
# second event with delay of
# 2 seconds
e1 = scheduler.enter(60, 1, 
                     print_event, (' 2nd', ))
  
# executing the events
scheduler.run()


#print(os.environ.get('API-URL'))



  
