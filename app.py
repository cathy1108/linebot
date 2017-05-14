# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('z+UnBJjmTu5BUzS4/vqJGvy3Q50OyoC/amuvZ4TtgTPJhI/TTX+ltwADrq52FU1apf/QfpMx48Tg2fqn583l7qxUBGZ6u6vnc1KmOvqD/AeisXXtF5/FDW52RkvtK0vIA8Ac11xSEiO0yQNK+IE08gdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('6b2c400a14237466a31d32667ea10829') #Your Channel Secret

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

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=os.environ['PORT'])