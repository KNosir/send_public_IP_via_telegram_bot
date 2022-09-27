from requests import post
from socket import gethostname, gethostbyname
from requests import get
from time import sleep

ip = get('https://api.ipify.org').text

time_in_second = 1000


host_name = gethostname()
IP_adderss = gethostbyname(host_name)

def send_to_telegram(message):

    apiToken = 'token'
    chatID = 'Number'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response_Sadam = post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
    print(type(response_Nosir.text))
while True:
    send_to_telegram(ip)
    sleep(time_in_second)