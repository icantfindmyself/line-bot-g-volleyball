from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#TemplateSendMessage - ButtonsTemplate
def buttons_message_scooter():
    message = TemplateSendMessage(
        alt_text='4',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/Iu7CCnX.jpg",
            title="你選擇了機車當交通工具",
            text="機車果然在X壢地區最方便了，一下就到餐廳了。等等，中午吃的鵝肉飯在胃裡翻滾，都到這裡了，該怎麼辦？",
            actions=[
                MessageTemplateAction(
                    label="硬著頭皮進去吃",
                    text="來都來了，不吃也太虧了吧"
                ),
                MessageTemplateAction(
                    label="不行了，先去看醫生吧",
                    text="抱歉，我的胃真的很不舒服，我先去看一下醫生QQ"
                )
            ]
        )
    )
    return message