
from asyncio.windows_events import NULL
from email import message
import json, requests
from pyparsing import null_debug_action 
import time
import xlrd
import os
from fun import*
url = requests.get("https://kaikai5.herokuapp.com/getjson")
text =  url.text 

data = json.loads(text)
mes_message=data['message']
mes_time=data['time']

control_val = 0

cost_time = NULL
cost = NULL

while(True):
    url = requests.get("https://kaikai5.herokuapp.com/getjson")
    text =  url.text
    data = json.loads(text)
    if(mes_time!=data['time']):
        mes_time=data['time']
        mes_message=data['message']
        print("----------------------------------------------------------------")
        print("time : " + mes_time + "\na one message:" + mes_message)
        if(control_val!=0):
            if(cost_time==NULL):
                cost_time = mes_message
                print("cost_time already")
            else:
                cost = mes_message
                excel(control_val,cost_time,cost)
                print("successful")
                cost_time = NULL
                cost = NULL

        elif(mes_message=='伙食'):
            control_val = 1
        elif(mes_message=='零食'):
            control_val = 2
        elif(mes_message=='飲料'):
            control_val = 2
        elif(mes_message=='其他花費'):
            control_val = 3
    time.sleep(1)
