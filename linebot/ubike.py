from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate
def buttons_message_ubike():
    message = TemplateSendMessage(
        alt_text='2',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/TNFujDQ.jpg",
            title="你選擇了UBike當交通工具",
            text="糟糕！騎腳踏車到餐廳時已經遲到半個小時了，完蛋了，學姊要罰我酒了...",
            actions=[
                MessageTemplateAction(
                    label="喝",
                    text="學姐這杯也太多了吧，沒事，我喝、我喝..."
                ),
                MessageTemplateAction(
                    label="抵死不喝",
                    text="學姊你是不是醉了"
                )
            ]
        )
    )
    return message