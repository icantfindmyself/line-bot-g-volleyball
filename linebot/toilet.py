from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def buttons_message_toilet():
    message = TemplateSendMessage(
        alt_text='9',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/xVcfu0S.jpg",
            title="你選擇了勉強吃",
            text="勉強吃對身體真是一大挑戰，我的肚子現在...",
            actions=[
                MessageTemplateAction(
                    label="看結局",
                    text="現在..."
                )
            ]
        )
    )
    return message