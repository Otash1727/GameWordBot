from django.core.exceptions import ObjectDoesNotExist
from BotScripts.create_bot import bot
from wordgame.models import MatchList,GamersList,ChempionsList,EnglishDictionary
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


def exists_game():
    exists=False
    try:
        data=MatchList.objects.all()
        for i in data:
            pass
        if i !=None:
            exists=True
            return exists
    except (UnboundLocalError,ObjectDoesNotExist):
        return exists

def exists_user(user_id):
    exists='no active'
    try:
        data=GamersList.objects.get(user_id=user_id,progress='active')
        exists='active' 
        return exists
    except (AttributeError,ObjectDoesNotExist,UnboundLocalError):
        return exists
    
def connect_user1(user_id):
    connect=False
    try:
        data=GamersList.objects.get(user_id=user_id,progress='active')
        data2=MatchList.objects.get(match_ID=data.match_ID,finished=False)
        if data2!=None:
            connect
    except:
        pass
    


def get_user(user_id):
    data=GamersList.objects.get(user_id=user_id)
    return data.progress

def start_match():
    data=MatchList.objects.last()
    return data.start_game
    
def create_game(chat_id,chat_name,user_id,user_name):
    data=MatchList(channel_name=chat_name,channel_ID=chat_id)
    data.save()
    copy_data=MatchList.objects.last()
    copy_data.progress='active'
    copy_data.save()
    creator=GamersList(user_id=user_id,user_name=user_name,match_ID=data.match_ID,progress='active')
    creator.save()

def connect_user(user_id,user_name):
    data=MatchList.objects.get(start_game=False)
    data2=GamersList.objects.last()
    fsm=GamersList(user_id=user_id,user_name=user_name,match_ID=data.match_ID,queue=data2.queue+1)
    fsm.save()

def check_creator(user_id):
    pass

    








def off():
    oddd=GamersList.objects.all()
    oddd.delete()
    dd=MatchList.objects.all()
    dd.delete()

