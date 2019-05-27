from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate
def buttons_message_stomach():
    message = TemplateSendMessage(
        alt_text='10',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/xVcfu0S.jpg",
            title="你選擇了先去看醫生",
            text="醫生說只是吃到不乾淨的食物而已，住院打點滴一天就可以了。",
            actions=[
                MessageTemplateAction(
                    label="看結局",
                    text="因為這樣沒有吃到隊聚真的很令人難過..."
                )
            ]
        )
    )
    return message