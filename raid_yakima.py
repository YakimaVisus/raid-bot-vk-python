# -*- coding: utf-8 -*-
from re import I
import vk_api
import json
import random
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor



vk = vk_api.VkApi(token='ТОКЕН') #токен группы
vk._auth_token()
vk.get_api()
def get_random_id():
    return random.randint(0, 100000000)

group_id = 'АЙДИ' #id группы

longpoll = VkBotLongPoll(vk, group_id)
bot_help = '''
Приветствую тебя username
 Перед тобой рейд бот для ВКонтакте от Yakima Visus
 Давай начнем с настройки данного бота)
 в "attachment": 'wall-айдигруппы_пост' загружаем свой пост со спамом ну я отсавлю свой возможно его удалят кароч ты понял
 в sleep = random.uniform(ВРЕМЯ, ВРЕМЯ) лучше не трогать ибо говно вк ввел флуд контроль, но вы можете поиграться
 токен думаю вы ввели как и айди группы
 Версия API: - должна быть самая новая 
 Далее просто инвайтим группу в беседу и наслождаемся

 Гитхаб кстати чекни: https://github.com/YakimaVisus
'''
print(bot_help)
for event in longpoll.listen():
   if event.type == VkBotEventType.MESSAGE_NEW:
            #не важно зачем ето написана я просто дурачек
            d1 = event.object.message
            s1 = json.dumps(d1)
            d2 = json.loads(s1)

            json_object = d2
            message = json_object['text']

            message = message.split(" ")
            msg_text = event.object.message['text']
            str1 = message[0].split("|")[0]


            str1 = str1.replace("[club", "")
            if group_id == str1:
                message.pop(0)

            message = ' '.join(message).lower()

            id = json_object['peer_id']
            try:
                dey = event.message.action['type']
            except:
                dey = ''
            
            print(message)
            if dey == 'chat_invite_user':
                while True:
                    sleep = random.uniform(2.199, 3.399)
                    keyboard = VkKeyboard()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)

                    keyboard.add_line()#Обозначает добавление новой строки
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

                    keyboard.add_line()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

                    keyboard.add_line()#Обозначает добавление новой строки
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("Yakima Visus https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)

                    keyboard.add_line()
                    keyboard.add_button("НАС ЕБЁТ vto.pe", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
                    keyboard.add_button("YAKIMA vto.pe", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("VISUS https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)

                    keyboard.add_line()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)

                    keyboard.add_line()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("получить ст https://vto.pe yakima_visus", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.get_keyboard()
                    vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message": f"Хелоу Воралд вас ебет Yakima Visus @all", "attachment": 'wall-186110456_27',"keyboard": keyboard.get_keyboard()})
                    time.sleep(sleep)

