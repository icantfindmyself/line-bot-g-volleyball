from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate
def buttons_message_taxi():
    message = TemplateSendMessage(
        alt_text='3',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/yfgUVrj.jpg",
            title="你選擇了黑車當交通工具",
            text="黑車司機都覺得自己是賽車手，一路飆到時速150，我命大，平安到達隊聚餐廳開始點餐。想吃哪一種方案呢？",
            actions=[
                MessageTemplateAction(
                    label="418小資方案",
                    text="418的方案就夠吃了吧"
                ),
                MessageTemplateAction(
                    label="628豪華方案",
                    text="628方案的牛舌看起來超好吃，我們吃628好不好"
                )
            ]
        )
    )
    return message