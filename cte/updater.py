from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from cte import funcoes

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(funcoes.updatesp, 'interval', seconds=10)
    scheduler.start()
