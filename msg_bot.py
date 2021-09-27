import requests
import json

name = input("enter you name: ")
print('\n')


while(1):

    msg = input(name+' : ')
    if msg == 'exit':
    	break

    resp=requests.get('https://api.simsimi.net/v1/?text={}&lang=en&cf=true'.format(msg))
    resp=resp.text
    temp=json.loads(resp)
    reply=temp['messages'][0]['response']
    print("bot: ",reply)

