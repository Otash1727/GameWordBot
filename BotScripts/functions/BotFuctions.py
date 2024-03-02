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
    fsm=GamersList(user_id=user_id,user_name=user_name,match_ID=data.match_ID,queue=data2.queue+1,progress='active')
    fsm.save()
    data.players_count+=1
    data.save()

def check_players_count():
    data=MatchList.objects.get(start_game=False)
    return data.players_count

def change_game_status():
    data=MatchList.objects.last()
    data.start_game=True
    data.save()
    data2=GamersList.objects.filter(match_ID=data.match_ID)
    for i in data2:
        i.start_game=True
        i.save()
        return i.user_id


def show_match():
    data=MatchList.objects.get(start_game=False)
    return data

def show_user():
    data=MatchList.objects.get(start_game=False)
    data2=GamersList.objects.filter(match_ID=data.match_ID)
    return data2
# compare player count

def count_update():
    data=MatchList.objects.get(start_game=False)
    return data.players_count
    

# function gameinfo_msg_id from Matchlist
def gameinfo_msg_bool():
    data=MatchList.objects.get(start_game=False)
    if data.players_count<=2:
        return True
    else:
        return False

def gameinfo_msg():
    data=MatchList.objects.get(start_game=False)
    return data.gameinfo_msg_id


def gameinfo_msg_id():
    data=MatchList.objects.get(start_game=False)
    return data.gameinfo_msg_id

# function send_msg_id from matchlist
def send_msg():
    data=MatchList.objects.get(start_game=False)
    data2=GamersList.objects.filter(match_ID=data.match_ID,send_msg=False)  
    return data2

def send_msg_booln():
    data=MatchList.objects.get(start_game=False)
    data2=GamersList.objects.filter(match_ID=data.match_ID)
    for i in data2:
        i.send_msg=True
        i.save()

def msg_id(send_id):
    data=MatchList.objects.get(start_game=False)
    data.send_msg_id=send_id
    data.save()

def get_msg():
    data=MatchList.objects.get(start_game=False)
    return data.send_msg_id

def get_user():
    data=GamersList.objects.get(progress='active')
    data2=GamersList.objects.filter(match_ID=data.match_ID)
    return data2

# start function
def start():
    data=MatchList.objects.get(start_game=False)
    data2=GamersList.objects.filter(match_ID=data.match_ID)
    for i in data2:
        i.start_game=True
        i.save()
        data.start_game=True
        data.save()

def first_queue():
    data=MatchList.objects.get(start_game=False)
    queue=GamersList.objects.filter(match_ID=data.match_ID,queue=1)
    for i in queue:
        return i.user_id,i.user_name

# game functions
    
def current_game(user_id):
    data=GamersList.objects.filter(progress='active',user_id=user_id)
    return data

def current_id(user_id):
    data=GamersList.objects.filter(progress='active',user_id=user_id)
    for i in data:
        pass
    data2=MatchList.objects.get(match_ID=i.match_ID)
    return data2.queue,i.queue,i.chance,i.match_ID

def count_queue(match_id):
    last_match=MatchList.objects.filter(match_ID=match_id)
    for i in last_match:
        i.queue+=1
        i.save()

def current_queue(match_id):
    data=MatchList.objects.get(match_ID=match_id)
    return data.queue

def show_player(match_id):
    data=GamersList.objects.filter(match_ID=match_id)
    return data

def update_queue(match_id):
    data=MatchList.objects.get(match_ID=match_id)
    data.queue=1
    data.save()

def next_queue(match_id):
    data=MatchList.objects.get(match_ID=match_id)
    data2=GamersList.objects.get(queue=data.queue)
    return data2

def last_word_save(match_id,last_letter,text):
    data=MatchList.objects.get(match_ID=match_id)
    data.last_latter=last_letter
    data.save()
    if data.founded_word!=None:
        data.founded_word=data.founded_word+text
        data.save()
    else:
        data.founded_word=text
        data.save()

def update_chance(user_id):
    data=GamersList.objects.filter(user_id=user_id,progress='active')
    for i in data:
        return i.chance
    

def chance_count(match_id,user_id):
    data=GamersList.objects.filter(user_id=user_id,match_ID=match_id)
    for i in data:
        i.chance-=1
        i.save()
    if i.chance==0:
        i.progress='no active'
        i.save()
        i.finished=True
        i.save() 
    




def off():
    oddd=GamersList.objects.all()
    oddd.delete()
    dd=MatchList.objects.all()
    dd.delete()

