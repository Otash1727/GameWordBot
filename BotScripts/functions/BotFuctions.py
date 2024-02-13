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
        if last_progress.progress=='active'     :
            if last_progress.start_game==False:
                start_or_not=True
                return start_or_not
            else:
                
                return start_or_not 
        else:
            if last_progress.start_game==False:
                return start_or_not      
            else:
                start_or_not=True
                return start_or_not 
    except AttributeError:
        return start_or_not     

 
def check_creator(user_id,user_name):
    exists=False
    try:
        data=MatchList.objects.last()
        check_user=GamersList.objects.filter(match_ID=data.match_ID)
        if user_id in [i.user_id for i in check_user ]:
            exists=True
            return  exists
        else:
            fsm=(GamersList(user_id=user_id,user_name=user_name,match_ID=data.match_ID))
            fsm.save()
            return exists
    except (ObjectDoesNotExist,AttributeError):
        return exists,print(404)
        
def check_creator1(user_id,user_name):
    pass

def create_game(chat_id,chat_name,user_id,user_name):
    data=MatchList(channel_name=chat_name,channel_ID=chat_id,players_count=+1)
    data.save()
    copy_data=MatchList.objects.last()
    copy_data.progress='active'
    copy_data.save()
    creator=GamersList(user_id=user_id,user_name=user_name,match_ID=copy_data.match_ID)
    creator.save()
    
    


    
        

        

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

def match_info():
    last_match=MatchList.objects.last()
    return last_match

def show_players(match_id):
    data=GamersList.objects.filter(match_ID=match_id)   
    return data

def start_game():
        last_match=MatchList.objects.last()
        last_match.start_game=True
        last_match.save()
        return print(last_match.start_game)

def start_write():
    last_match=MatchList.objects.last()
    return last_match.start_game
    
def finished():
    last_match=MatchList.objects.last()
    return last_match.finished




