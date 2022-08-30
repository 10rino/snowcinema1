from flask import Flask
from flask import request
from flask import Response
import requests
 
TOKEN = "5666296465:AAFCC5I8QN6pWhad0ZoprGFjFyIVG1CbfWM"
app = Flask(__name__)
 
def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = parse_message(msg)
        if txt == "/ozviat":
            tel_send_message(chat_id,"https://t.me/+fbO6I1VKJzZmNjE0")
        elif txt == "/darkhast" :
            tel_send_message(chat_id,'اسم و فیلم سریال درخواستی خود را ارسال کنید')
       
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(debug=True)
