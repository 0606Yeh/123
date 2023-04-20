#複製訊息
from flask_ngrok import run_with_ngrok   # colab 使用，本機環境請刪除
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
import json

app = Flask(__name__)
access_token = 'yQsu2Fkm4b2BcKWdk4YblQfPt+vxae7H4NdcXcVU3mpLbHAcn5P+tPUir8Evi5TlhUTkSgUnCe04uza7+Es0kYjZMoxefvvSN/zt9cIPsB2J1ihNmViwe5tEnjQ1Qeo263KgDAVF9w85CypS2e0jvQdB04t89/1O/w1cDnyilFU=' 
channel_secret = 'a8299a71b2f1cfd2eab5350c88820fb6' 

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        
        tk = json_data['events'][0]['replyToken']         
        msg = json_data['events'][0]['message']['text'] 
        if msg == '建立分帳活動':
            message = TemplateSendMessage(
                alt_text='確認建立活動',
                template=ConfirmTemplate(   #各種樣板可上網查
                    text="是否建立活動?",
                    actions=[   #各種Action
                        MessageAction(
                            label='否',   #按鈕文字
                            text='不新增活動'
                        ),
                        URIAction(
                            label='是',
                            uri=''
                        )
                    ]
                )
            )
            line_bot_api.reply_message(tk, message)
    except:
        print('error')
    return 'OK'


if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()