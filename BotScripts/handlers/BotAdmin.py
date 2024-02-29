from BotScripts.create_bot import bot,dp 
from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message,BotCommand,BotCommandScopeChat,InlineKeyboardButton,CallbackQuery
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import BaseFilter
from wordgame.models import GamersList,MatchList,ChempionsList
from BotScripts.functions import BotFuctions

import csv
csv.field_size_limit(1000000)






import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
    


router=Router()
chat_id=None

#message_id
message_id1=[]
#in_turn




# keyboards
join=(InlineKeyboardButton(text='join',callback_data='join'))
start=(InlineKeyboardButton(text='start',callback_data='start'))
end=(InlineKeyboardButton(text='end',callback_data='end'))

join_kb=InlineKeyboardBuilder()
join_kb.row(join)

mix_kb=InlineKeyboardBuilder()
mix_kb.row(join).row(start)

mix_kb2=InlineKeyboardBuilder()
mix_kb2.row(start).row(end)

End=InlineKeyboardBuilder()
End.row(end)






@router.message(Command('start'))
async def runbot(message:Message):
    await bot.send_message(chat_id=message.from_user.id,text='Hello send /help command to know what you can do with me')
    await bot.send_message(chat_id=message.from_user.id,text='The game is played only with an opponent and in a group.')
    await bot.set_my_commands([BotCommand(command='start',description='Run the bot'),BotCommand(command='help',description='If you want to know more about our bot, this command will help you')],BotCommandScopeChat(chat_id=message.from_user.id))
    BotFuctions.off()
            

    

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
    
    if check_status.status=='administrator':
        exists_game=BotFuctions.exists_game()
        #ff=BotFuctions.get_user(user_id=message.from_user.id)
        print(exists_game)#ff)
        if exists_game==True:
            exists_user=BotFuctions.exists_user(user_id=message.from_user.id)
            if exists_user=='active':
                await bot.send_message(chat_id=chat_id,text='ishlamiyman')
            else:
                print(exists_user,'gege')
                await bot.send_message(chat_id=chat_id,text="Great, get ready and click on start button below",reply_markup=join_kb.as_markup())
        else:
            print('bu yerdaman')  
            await bot.send_message(chat_id=chat_id,text="Great, get ready and click on start button below",reply_markup=join_kb.as_markup())

    else:
        await bot.send_message(chat_id=chat_id,text='You can play only with an opponent(s) and in a group.')
        await bot.send_message(chat_id=chat_id,text="You can play only with an opponent(or more) and in a group.")
    
    
@router.callback_query(F.data=='join')
async def  created_game(callback:CallbackQuery):
    chat_id=callback.message.chat.id
    chat_info=await bot.get_chat(chat_id=chat_id)
    exists_game=BotFuctions.exists_game()

    print(exists_game,'bu user')
    if exists_game==True:
        exists_user=BotFuctions.exists_user(user_id=callback.from_user.id)
        print(exists_user,'ff')
        if exists_user=='no active':
            start_match=BotFuctions.start_match()
            if start_match==False:
                connect_user=BotFuctions.connect_user(user_id=callback.from_user.id,user_name=callback.from_user.full_name)
                print('sen oyinga qo\'shilding')
            else:
                create_game=BotFuctions.create_game(chat_id=chat_id,chat_name=chat_info.title,user_id=callback.from_user.id,user_name=callback.from_user.full_name)
                print('oyin tashkil qilindi')
        else:
            await bot.send_message(chat_id=chat_id,text='Senda yakunlanamgan o\'yin bor ')
    else:
        create_game=BotFuctions.create_game(chat_id=chat_id,chat_name=chat_info.title,user_id=callback.from_user.id,user_name=callback.from_user.full_name)
        print('oyin tashkil qilindi')