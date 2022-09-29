from requests import post, get
from time import sleep



time_in_second = 1000

def send_to_telegram(message):

    apiToken = 'token'
    chatID = 'Number'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
    print(type(response.text))
while True:
    ip = get('https://api.ipify.org').text
    send_to_telegram(ip)
    sleep(time_in_second)