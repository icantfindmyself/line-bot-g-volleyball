from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate
def buttons_message_418():
    message = TemplateSendMessage(
        alt_text='7',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/xVcfu0S.jpg",
            title="你選擇了418小資方案",
            text="才418竟然可以吃到多達三十幾種菜，看來下星期要多練幾個小時瘦回來。",
            actions=[
                MessageTemplateAction(
                    label="看結局",
                    text="今天真的太幸福了~"
                )
            ]
        )
    )
    return message