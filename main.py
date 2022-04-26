import os, time, requests, json
from apscheduler.schedulers.blocking import BlockingScheduler
  
def get_all_monitors():
    monitorsResponse = requests.get(os.environ.get('API-URL') + 'monitor')
    monitors = json.loads(monitorsResponse.text)
    return monitors

def execute_monitors():
    monitors = get_all_monitors()
    for monitor in monitors:
        executeResponse = requests.post(os.environ.get('API-URL') + 'executor/execute/' + monitor["_id"])
        print(executeResponse)

print("scheduler is up!")
scheduler = BlockingScheduler()
scheduler.add_job(execute_monitors, 'interval', hours=1)
scheduler.start()



  
