from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

import os

line_bot_api = LineBotApi(os.environ.get('IlabAccessToken'))

def lambda_handler(event, context):
    print(event["to"])
    
    try:
        line_bot_api.push_message(event["to"],TextSendMessage(event["messages"]["text"]))
    except LineBotApiError as e:
        print("エラーだよ")
        # error handle