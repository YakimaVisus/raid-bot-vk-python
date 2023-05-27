import vk_api
import json
import random
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard

vk = vk_api.VkApi(token="Сюда вставляете токен")
vk._auth_token()
vk.get_api()

group_id = "сюда вставить ID вашей группы с ботом (только цифры)"
wallID = "Сюда вставить айди поста, с группы а не паблика"

def get_random_id():
    return random.randint(0, 100000000)


longpoll = VkBotLongPoll(vk, group_id)
print("""
Улучшенный RAID-бот от Данила Пистолетова
Оригинал: github.com/YakimaVisus/raid-bot-vk-python
Данил: github.com/DanilPistoletov
""")
def main():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW or event.from_chat:
            d1 = event.object.message
            s1 = json.dumps(d1)
            d2 = json.loads(s1)
            json_object = d2
            message = json_object["text"]
            message = message.split(" ")
            msg_text = event.object.message["text"]
            str1 = message[0].split("|")[0]
            str1 = str1.replace("[club", "")
            if group_id == str1:
                message.pop(0)

            message = " ".join(message).lower()

            id = json_object["peer_id"]
            try:
                dey = event.message.action["type"]
            except:
                dey = ""

            print(message)
            if dey == "chat_invite_user" or 1:
                print("Начинаю рейд беседы. ID: ", id)
                while 1:
                    sleep = random.uniform(0.555, 1.333)
                    keyboard = VkKeyboard()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.PRIMARY)

                    keyboard.add_line()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)

                    keyboard.add_line()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

                    keyboard.add_line()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("Макима Асус https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("вотофак vto.pe", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)

                    keyboard.add_line()
                    keyboard.add_button("НАС АБИЖАИТ vto.pe", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
                    keyboard.add_button("YAKIMA vto.pe", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("VISUS https://vto.pe vto.pe", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)

                    keyboard.add_line()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.PRIMARY)

                    keyboard.add_line()
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)
                    keyboard.add_button("получить стикеры https://vto.pe vto.pe",
                                        color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
                    keyboard.add_button("получить ст https://vto.pe yakima_visus",
                                        color=vk_api.keyboard.VkKeyboardColor.POSITIVE)
                    keyboard.get_keyboard()
                    vk.method("messages.send", {"peer_id": id, "random_id": get_random_id(),
                                                "message": f"дратути это добрый чат ботик @all",
                                                "attachment": wallID, "keyboard": keyboard.get_keyboard()})
                    time.sleep(sleep)

if __name__ == "__main__":
    main()