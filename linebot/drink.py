from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate
def buttons_message_drink():
    message = TemplateSendMessage(
        alt_text='5',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/xVcfu0S.jpg",
            title="你選擇了喝",
            text="學姊們在身旁叫囂著和倒數十秒，眼看就要喝不完了...",
            actions=[
                MessageTemplateAction(
                    label="看結局",
                    text="我都忘了到底發生了什麼事"
                )
            ]
        )
    )
    return message