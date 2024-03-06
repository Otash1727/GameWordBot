from django.db import models
from django import forms
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import Now



class MatchList(models.Model):
    channel_name=models.CharField(max_length=200)   
    channel_ID=models.IntegerField()  
    match_ID=models.AutoField(primary_key=True)
    players_count=models.IntegerField(null=True,blank=True,default=1)
    word_count=models.IntegerField(null=True,blank=True)
    queue=models.PositiveIntegerField(default=1)
    last_latter=models.CharField(null=True,blank=True,max_length=2)
    founded_word=models.CharField(null=True,blank=True,max_length=10000)
    start_game=models.BooleanField(default=False)
    finished=models.BooleanField(default=False)
    progress=models.CharField(max_length=20,default='no active')
    gameinfo_msg_id=models.CharField(max_length=300,null=True,blank=True)
    send_msg_id=models.PositiveIntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,db_index=True)
    DisplyFields=['match_ID','channel_name','channel_ID','start_game','finished']
    SearchFilds=['channel_ID','channel_name','match_ID','players_count','word_count']
    FiltersFields=['channel_name']
        
        
class EnglishDictionary(models.Model):    
    dictionary=models.CharField(max_length=300)
    DisplayField=['dictionary']
        

        
    

class GamersList(models.Model):
    match_ID=models.IntegerField(null=True,blank=True)
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=200)
    found_word_count=models.IntegerField(null=True,blank=True)
    chance=models.IntegerField(default=3)
    queue=models.PositiveIntegerField(default=1)  
    start_game=models.BooleanField(default=False)
    finished=models.BooleanField(default=False)
    progress=models.CharField(default='no active', max_length=15,null=True,blank=True)
    send_msg=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,db_index=True)
    Match_List=models.ForeignKey(to=MatchList,on_delete=models.CASCADE,null=True,blank=True)  
    DisplayFields=['match_ID','user_name','progress','finished']
    SearchFields=['match_ID','user_id','user_name','found_word_count']
    FiltersFields=['found_word_count']
    def clone_matchID(cloned):
        first_ID=MatchList.objects.last()
        print(1)
        

class ChempionsList(models.Model):
    match_ID=models.IntegerField(null=True,blank=True)
    channel_name=models.CharField(max_length=200)
    channel_ID=models.IntegerField()
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=100)
    results=models.IntegerField()
    MatchList=models.ForeignKey(to=MatchList,on_delete=models.CASCADE,null=True,blank=True)  
    DisplayFields=['match_ID','user_name']
    SearchFields=['match_ID','channel_ID','channel_name','user_id','user_name','results']
    FiltersFields=['channel_name']
    








