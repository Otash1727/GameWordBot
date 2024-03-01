from BotScripts.create_bot import bot,dp 
from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message,BotCommand,BotCommandScopeChat,InlineKeyboardButton,CallbackQuery
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import BaseFilter
from wordgame.models import GamersList,MatchList,ChempionsList
from BotScripts.functions import BotFuctions

import csv,json,re
csv.field_size_limit(1000000)






import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
    


router=Router()
chat_id=None

#message_id
#in_turn




# keyboards
join=(InlineKeyboardButton(text='join',callback_data='join'))
start=(InlineKeyboardButton(text='start',callback_data='start'))
end=(InlineKeyboardButton(text='end',callback_data='end'))

join_kb=InlineKeyboardBuilder()
join_kb.row(join)

start_kb=InlineKeyboardBuilder()
start_kb.row(start)

end_kb=InlineKeyboardBuilder()
end_kb.row(end)

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
                print('ishlamiyman')
                pass
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
                players_count=BotFuctions.check_players_count()
                if players_count+1<6:
                    connect_user=BotFuctions.connect_user(user_id=callback.from_user.id,user_name=callback.from_user.full_name)
                    print('sen oyinga qo\'shilding')
                    count_update=BotFuctions.count_update()
                    get_msg=BotFuctions.get_msg()
                    show_match=BotFuctions.show_match()
                    if get_msg!=None:
                        print('deleted message')
                        await bot.delete_message(chat_id=chat_id,message_id=get_msg)
                        await callback.answer(text='You joined the game',show_alert=True)
                        M_id=await callback.message.answer(text=f"Match ID - {show_match.match_ID} \n Number of players - {show_match.players_count} \n Players \n _____",reply_markup=mix_kb.as_markup())              
                        BotFuctions.msg_id(send_id=M_id.message_id)
                    else:
                        await callback.answer(text='You joined the game',show_alert=True)
                        M_id=await callback.message.answer(text=f"Match ID - {show_match.match_ID} \n Number of players - {show_match.players_count} \n Players \n _____",reply_markup=mix_kb.as_markup())              
                        BotFuctions.msg_id(send_id=M_id.message_id)
                else:
                    change_game_status=BotFuctions.change_game_status()
                    create_game=BotFuctions.create_game(chat_id=chat_id,chat_name=chat_info.title,user_id=callback.from_user.id,user_name=callback.from_user.full_name)
                   
            else:
                create_game=BotFuctions.create_game(chat_id=chat_id,chat_name=chat_info.title,user_id=callback.from_user.id,user_name=callback.from_user.full_name)
                print('oyin tashkil qilindi')
                await callback.answer(text='You are create new game. Please wait for other to join!',show_alert=True)
        else:
            await callback.answer(text='🫵 have an unfinished game\n Please finished the game 😡',show_alert=True)
    else:
        create_game=BotFuctions.create_game(chat_id=chat_id,chat_name=chat_info.title,user_id=callback.from_user.id,user_name=callback.from_user.full_name)
        print('oyin tashkil qilindi')
        await callback.answer(text='You are create new game. Please wait for other to join!',show_alert=True)

@router.callback_query(F.data=='start')
async def  match_start(callback:CallbackQuery):
    chat_id=callback.message.chat.id
    get_msg=BotFuctions.get_msg()
    show_match=BotFuctions.show_match()
    await bot.edit_message_text(chat_id=chat_id,message_id=get_msg,text=f"<b>Match ID</b> - <i>{show_match.match_ID}</i> \n <b>Number of players</b> - <i>{show_match.players_count}</i> \n <b>Players</b> \n<b>dsdsd</b>\n<b>✅✅ The game started✅✅</b>",parse_mode=ParseMode.HTML)
    first_queue=BotFuctions.first_queue()
    info_user=await bot.get_chat(chat_id=first_queue[0])
    if info_user.username==None:
        await bot.send_message(chat_id=chat_id,text=f'<b>{first_queue[1]}</b> must write an English word',parse_mode=ParseMode.HTML)
    else:
        await bot.send_message(chat_id=chat_id,text=f'<b>{first_queue[1]}</b> must write an English word\n@{info_user.username}',parse_mode=ParseMode.HTML)
    BotFuctions.start()

@router.callback_query(F.data=='end')
async def end_game(callback:CallbackQuery):
    pass

@router.message()
async def empty_handler(message:Message):
    chat_id=message.chat.id
    check_status=await bot.get_chat_member(chat_id=chat_id,user_id=bot.id)
    if check_status.status=='administrator':
        print('inside chat')
        current_game=BotFuctions.current_game(user_id=message.from_user.id)
        if len(current_game)!=0:
            print('inside game')
            current_id=BotFuctions.current_id(user_id=message.from_user.id)
            if current_id[0]==current_id[1] and current_id[2]!=0:
                next_level=False
                Dictionary=open('englishDictionary.csv',mode='r') 
                csvfile=csv.reader(Dictionary)
                for i in csvfile:
                    if str(message.text).capitalize() in i and len(message.text)>1:
                        current_queue=BotFuctions.current_queue(match_id=current_id[3])
                        show_player=BotFuctions.show_player(match_id=current_id[3])
                        if current_queue==show_player.count():
                            BotFuctions.update_queue(match_id=current_id[3])
                        else:    
                            BotFuctions.count_queue(match_id=current_id[3])
                        BotFuctions.last_word_save(match_id=current_id[3],last_letter=str(message.text[-1]),text=json.dumps(message.text))
                        next_level=True
                        print(1727)
                        break
                    else:
                        pass
                if next_level==True:
                    print('Togri javob')

                else:
                    print('xato qilding')
            else:
                if current_id[2]==0:
                    print('you lose')
                else:
                    print('seni navbating emas')
                    next_queue=BotFuctions.next_queue(match_id=current_id[3])
                    info_user= await bot.get_chat(chat_id=next_queue.user_id)
                    if info_user.username!=None:
                        await bot.send_message(chat_id=chat_id,text=f"<b>Sorry</b> - <i>{message.from_user.full_name}</i>\n<b>It's not 🫵 turn</b>\n<b>Please wait❗️</b>\n<b>It's 🫵 turn</b> - <i>{current_id[1]}</i>\n<b>Now it is</b> <i>{next_queue.user_name}'s</i> <b>turn</b>\n@{info_user.username}",parse_mode=ParseMode.HTML)
                    else:
                        await bot.send_message(chat_id=chat_id,text=f"<b>Sorry</b> - <i>{message.from_user.full_name}</i>\n<b>It's not 🫵 turn</b>\n<b>Please wait❗️</b>\n<b>It's 🫵 turn</b> - <i>{current_id[1]}</i>\n<b>Now it is</b> <i>{next_queue.user_name}'s</i> <b>turn</b>",parse_mode=ParseMode.HTML)


        else:
            pass
        

    else:
        print('oddiy rejim')