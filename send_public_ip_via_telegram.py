from requests import post, get
from time import sleep


apiToken = 'token'
apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'


time_in_second = 1000


def send_to_telegram(message, chatID, apiURL):

    try:
        return post(apiURL, json={'chat_id': chatID, 'text': message}).text
    except Exception as e:
        return e


def get_ip():
    try:
        return get('https://api.ipify.org').text
    except Exception as e:
        return e


while True:
    send_to_telegram(get_ip(), chatID, apiURL)
    sleep(time_in_second)
