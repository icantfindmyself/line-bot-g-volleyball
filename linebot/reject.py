from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def buttons_message_reject():
    message = TemplateSendMessage(
        alt_text='6',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/lo4J1t3.jpg",
            title="你選擇了抵死不喝",
            text="學姊們自己越喝越嗨，眼看要失控了...",
            actions=[
                MessageTemplateAction(
                    label="續攤",
                    text="學姊們都要畢業了，今天晚上好好玩吧"
                ),
                MessageTemplateAction(
                    label="架著學姊離開餐廳",
                    text="學姊你可以自己站嗎，我撐不住你的體重"
                )
            ]
        )
    )
    return message