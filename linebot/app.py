from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#呼叫的檔案
from message import *
from ubike import *
from taxi import *
from scooter import *
from drink import *
from reject import *
from cheap import *
from moneybye import *
from toilet import *
from stomach import *


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('SaVdy0FMkNMgbyeEI+F691CZE/WAt2JwTFB/yBiX81+JOEVEppmazLvAvub241x/oEQtTJEu26tR0kpLBeb2uBYdbZ1oNj0+m+Dks9bfp3moBaDSSpp9U9xwWdgiDsUncVtqzUxcojorei0OtTe3kAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('954d19b8d7c291d6551ca65405d7698b')
user_id = "U7c0f7e501a868aa4462eb301b7135102"
image_url1 = "https://i.imgur.com/0JgKXPV.jpg"
image_url2 = "https://i.imgur.com/6PhU8kS.jpg"

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

try:
    line_bot_api.push_message(user_id, TextSendMessage(text='女排在校內系際盃贏得了冠軍，得到了二連霸的稱號！期末隊聚兼慶功宴就選擇燒烤吧！但吃隊聚如上球場比賽，每一顆飛過來的球都驚險萬分，幫助自己度過和享受隊聚吧！輸入「我要吃隊聚」開始！'))
except LineBotApiError as e:
    raise e

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = event.message.text

    if '我要吃隊聚' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)

    elif '我要騎UBike' in msg:
        message = buttons_message_ubike()
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '學姐這杯也太多了吧，沒事，我喝、我喝...' in msg:
        message = buttons_message_drink()
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '我都忘了到底發生了什麼事' in msg:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='因為喝太急結果啤酒從鼻孔噴出來，被嗆的無話可說，最後再混酒比賽中喝到不省人事，醒來後發現自己在宿舍房間地板上，旁邊都是嘔吐物。'),ImageSendMessage(original_content_url=image_url1, preview_image_url=image_url1),TextSendMessage(text='輸入「我要吃隊聚」可以重新再吃一次隊聚！')])

    elif '學姊你是不是醉了' in msg:
        message = buttons_message_reject()
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '學姊們都要畢業了，今天晚上好好玩吧' in msg:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='去KTV續攤，繼續點了贈送一箱啤酒的方案，結果學姊們都在搶包廂內的垃圾桶吐，學妹們忙著收拾學姊們的東西，地上濕濕滑滑的，分不清楚是被弄倒的啤酒還是嘔吐物。'),ImageSendMessage(original_content_url=image_url1, preview_image_url=image_url1),TextSendMessage(text='輸入「我要吃隊聚」可以重新再吃一次隊聚！')])
    
    elif '學姊你可以自己站嗎，我撐不住你的體重' in msg:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='貼心把學姊送回了她的住處，看著學姊發酒瘋，躺在地上轉圈圈，只能希望學姊隔天頭不要太痛了。'),ImageSendMessage(original_content_url=image_url2, preview_image_url=image_url2),TextSendMessage(text='輸入「我要吃隊聚」可以重新再吃一次隊聚！')])
    
    elif '我要搭黑車去' in msg:
        message = buttons_message_taxi()
        line_bot_api.reply_message(event.reply_token, message)

    elif '418的方案就夠吃了吧' in msg:
        message = buttons_message_418()
        line_bot_api.reply_message(event.reply_token, message)

    elif '今天真的太幸福了~' in msg:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='吃到飽的冰淇淋區竟然有起司草莓的口味！這個口味可遇不可求啊！之前找了很多家店都找不到呢！吃飽飽跟大家拍了大合照。'),ImageSendMessage(original_content_url=image_url2, preview_image_url=image_url2),TextSendMessage(text='輸入「我要吃隊聚」可以重新再吃一次隊聚！')])

    elif '628方案的牛舌看起來超好吃，我們吃628好不好' in msg:
        message = buttons_message_628()
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '我怎麼這麼衰...' in msg:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='今天明明原本是順遂的啊，難道是運氣用光了嗎？明天路過土地公去拜拜好了。'),ImageSendMessage(original_content_url=image_url1, preview_image_url=image_url1),TextSendMessage(text='輸入「我要吃隊聚」可以重新再吃一次隊聚！')])
    
    elif '學姊，什麼？你說要我幫你搬家嗎？！' in msg: 
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='跟學姊借了錢，沒想到去還學姊錢時，學姊正好在搬家，於是就順勢幫學姊搬了個家。從沒有電梯的三樓搬到一樓真的苦不堪言，但有幫到救命恩人就滿足了。'),ImageSendMessage(original_content_url=image_url2, preview_image_url=image_url2),TextSendMessage(text='輸入「我要吃隊聚」可以重新再吃一次隊聚！')])
    
    elif '我騎機車去' in msg:
        message = buttons_message_scooter()
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '來都來了，不吃也太虧了吧' in msg:
        message = buttons_message_toilet()
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '現在...' in msg:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='因為餐廳在快要結束營業時會關閉廁所做清潔工作，用餐到餐廳快關閉的我只好抱著肚子衝刺百米到附近的百貨公司上廁所。連大合照都沒有拍到，只能靠學妹把我修圖修上去。'),ImageSendMessage(original_content_url=image_url1, preview_image_url=image_url1),TextSendMessage(text='輸入「我要吃隊聚」可以重新再吃一次隊聚！')])

    elif '抱歉，我的胃真的很不舒服，我先去看一下醫生QQ' in msg:
        message = buttons_message_stomach()
        line_bot_api.reply_message(event.reply_token, message)

    elif '因為這樣沒有吃到隊聚真的很令人難過...' in msg:
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='打了點滴後的我感覺好多了，在醫院待了一晚。沒想到學姐和學妹隔天竟然來來探病，女排真是個溫暖的地方。<3'),ImageSendMessage(original_content_url=image_url2, preview_image_url=image_url2),TextSendMessage(text='輸入「我要吃隊聚」可以重新再吃一次隊聚！')])

    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='走錯路了？再這樣下去會吃不到隊聚的！輸入「我要吃隊聚」回到正確的路上吧。'))


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
