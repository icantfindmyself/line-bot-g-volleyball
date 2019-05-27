from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate

def buttons_message():

    message = TemplateSendMessage(

        alt_text='吃隊聚囉～',

        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/fWfnwXP.jpg",
            title="女子排球隊員吃期末隊聚",
            text="選擇一種交通工具讓自己平安到達隊聚地點吧。",
            actions=[
                MessageTemplateAction(
                    label="UBike",
                    text="我要騎UBike"
                ),

                MessageTemplateAction(
                    label="黑車",
                    text="我要搭黑車去"
                ),

                MessageTemplateAction(
                    label="機車",
                    text="我騎機車去"
                )

            ]

        )

    )

    return message

