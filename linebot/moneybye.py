from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def buttons_message_628():
    message = TemplateSendMessage(
        alt_text='8',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/79x2WXd.jpg",
            title="你選擇了628豪華方案",
            text="牛舌超好吃！诶？！我的錢包呢，沒錢付該怎麼辦？",
            actions=[
                MessageTemplateAction(
                    label="留下來洗碗",
                    text="我怎麼這麼衰..."
                ),
                MessageTemplateAction(
                    label="跟學姊借錢",
                    text="學姊，什麼？你說要我幫你搬家嗎？！"
                )
            ]
        )
    )
    return message