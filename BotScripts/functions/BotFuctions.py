from django.core.exceptions import ObjectDoesNotExist
from BotScripts.create_bot import bot
from wordgame.models import MatchList,GamersList,ChempionsList
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()



def game_boolen():
    start_or_not=False
    try:
        last_progress=MatchList.objects.last()
        print(last_progress.progress)
        if last_progress.progress=='active':
            start_or_not=True
            return start_or_not
        else:
            return start_or_not
    except AttributeError:
        return start_or_not

def get_ID(chat_id,chat_name):
    exists=False
    try:
        last_match=MatchList.objects.last()
        exists=True
        return last_match.match_ID, exists
    except (ObjectDoesNotExist,AttributeError):
        fsm=(MatchList(channel_name=chat_name,channel_ID=chat_id))
        fsm.save()
        

def chat_info(chat_id,user_id):
    data= bot.get_chat_member(chat_id=chat_id,user_id=user_id)
    return data.id, data.title 


def connect_gamers(user_id,user_name,match_ID):
    try:
        data1=GamersList.objects.get(user_id=user_id,match_ID=match_ID)
        return data1
    except ObjectDoesNotExist:
        fsm=(GamersList(user_id=user_id,user_name=user_name,match_ID=match_ID))
        fsm.save()

def show_players(match_id):
    data=GamersList.objects.filter(match_ID=match_id)   
    return data


