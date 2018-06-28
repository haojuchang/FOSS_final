# encoding: utf-8

import sys
sys.path.append("./assest")
import youtube
from linebot.models import *
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

line_bot_api = LineBotApi('RIMmaonvD7Bi/W4guIsCuwrLAXFqtHgYFWmF+/c8mIgnF7FzZsScZLVF223lEJH2jdbpyM/+NXn0oJSbWpZGrIDEwfu/qv6GTd/GCs0yFGhPIuEtIMkgQczguukg60DnOyv9xLF1NIvjxDlqwyMwbQdB04t89/1O/w1cDnyilFU=')  # Your Channel Access Token
handler = WebhookHandler('2b7ac49c414175ad1fc3c72595f5731f')  # Your Channel Secret


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
def handle_message(event):
    text = event.message.text  # message from user

    if text == "搜歌模式":
        text = "此模式可以推薦你想要的歌手的歌曲"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text))
        return 0
    if text == "心情模式":
        text = "我們會根據你的心情指數來推薦歌曲"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text))
        return 0
    if text == "關於我們":
        text = "吳泰德\n羅皓煒\n張皓儒\n劉泳儀\n白恬安"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text))
        return 0

    if text.find('Y<<') != -1:
        song = youtube.youtube()
        song_data = song.search(text)
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(
                text=song_data[0][0],
                actions=[URITemplateAction(label='Watch it !!', uri=song_data[1][0])]
            ),
            CarouselColumn(
                text=song_data[0][1],
                actions=[URITemplateAction(label='Watch it !!', uri=song_data[1][1])]
            ),
            CarouselColumn(
                text=song_data[0][2],
                actions=[URITemplateAction(label='Watch it !!', uri=song_data[1][2])]
            ),
            CarouselColumn(
                text=song_data[0][3],
                actions=[URITemplateAction(label='Watch it !!', uri=song_data[1][3])]
            ),
            CarouselColumn(
                text=song_data[0][4],
                actions=[URITemplateAction(label='Watch it !!', uri=song_data[1][4])]
            ),
        ])
        template_message = TemplateSendMessage(alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return 0

    buttons_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ButtonsTemplate(
            title='請選擇以下服務',
            text='點選顯示介紹',
            thumbnail_image_url='https://storage.googleapis.com/biggg/f48c6734853348ff9f9f473f6d640ef1.gif',
            actions=[
                MessageTemplateAction(
                    label='搜歌模式',
                    text='搜歌模式'
                ),
                MessageTemplateAction(
                    label='心情模式',
                    text='心情模式'
                ),
                MessageTemplateAction(
                    label='關於我們',
                    text='關於我們'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
