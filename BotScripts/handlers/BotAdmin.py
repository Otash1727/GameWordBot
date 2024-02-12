from BotScripts.create_bot import bot,dp 
from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message,BotCommand,BotCommandScopeChat,InlineKeyboardButton,CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import BaseFilter
from wordgame.models import GamersList,MatchList,ChempionsList
from BotScripts.functions import BotFuctions

import csv




import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
    


router=Router()
chat_id=None






@router.message(Command('start'))
async def runbot(message:Message):
    await bot.send_message(chat_id=message.from_user.id,text='Hello send /help command to know what you can do with me')
    await bot.send_message(chat_id=message.from_user.id,text='The game is played only with an opponent and in a group.')
    await bot.set_my_commands([BotCommand(command='start',description='Run the bot'),BotCommand(command='help',description='If you want to know more about our bot, this command will help you')],BotCommandScopeChat(chat_id=message.from_user.id))
    with open('englishDictionary.csv',mode='r') as csvfile:
        spamreader=csv.reader(csvfile)
        for row in spamreader:
            print(row)
@router.message(Command('help'))
async def help(message:Message):
    await bot.send_message(chat_id=message.from_user.id,text='This is a word chain game for English learners!')
    await bot.send_message(chat_id=message.from_user.id,text='The game is played only with an opponent and in a group.')
    await bot.send_message(chat_id=message.from_user.id,text="If you want to use the bot,add the bot to your group and give admin and send /new_match")
    await bot.set_my_commands([BotCommand(command='new_macht1',description='Create a new match',)],BotCommandScopeChat(chat_id=message.from_user.id),request_timeout=2)


@router.message(Command('new_match'))
async def fff(message:Message):
    chat_id=message.chat.id
    check_status= await bot.get_chat_member(chat_id=chat_id,user_id=bot.id)
    join_kb=InlineKeyboardBuilder()
    join_kb.row(InlineKeyboardButton(text='Join',callback_data='join'))
    print(check_status.status)  
    if check_status.status=='administrator':
        await bot.send_message(chat_id=chat_id,text="Great, get ready and click on start button below",reply_markup=join_kb.as_markup())        
    else:
        await bot.send_message(chat_id=chat_id,text='You can play only with an opponent(s) and in a group.')
        await bot.send_message(chat_id=chat_id,text="You can play only with an opponent(or more) and in a group.")
    
@router.callback_query(F.data=='join')
async def join_game(callback:CallbackQuery):  
    chat_id=callback.message.chat.id
    chat_info= await bot.get_chat(chat_id=chat_id)
    data=BotFuctions.game_boolen()
    print(data)
  #  print(chat_info)
    data_id=BotFuctions.get_ID(chat_id=chat_id,chat_name=chat_info.title)
    print(data_id[1])
    if data_id[1]==True:
        players=BotFuctions.connect_gamers(user_id=callback.from_user.id,user_name=callback.from_user.full_name,match_ID=data_id[0])
        show=BotFuctions.show_players(match_id=data_id[0])
        
        await callback.message.answer(text=f"Match_ID: {data_id[0]}\nPlayers:\n{[i.user_name  for i in show]}")
    


    #try:
    #    if last_match.finished ==False:
    #      
    #            data=BotFuctions.check_users(callback=callback.message.from_user.id) 
    #            print(data)     
    #            await callback.answer('You are practicipating in the game',show_alert=True)
    #    elif last_match.finished==True:
    #        await callback.answer('You are already practicipating in the game!\n Please wait for others to join',show_alert=True)
    #        fsm_save=MatchList(channel_name=channel_info.title,channel_ID=channel_info.id)
    #        fsm_save2=GamersList(user_id=callback.from_user.id,user_name=callback.from_user.full_name,match_ID=last_match.match_ID+1)
    #        fsm_save.save()
    #        fsm_save2.save()
    #except AttributeError:
    #    pass
        
   
@router.message()
async def empty_handler(message:Message):
    chat_id=message.chat.id
    print(chat_id)
    await bot.set_my_commands([BotCommand(command='new_match',description='Star new match')],BotCommandScopeChat(chat_id=chat_id))
    
    

    



