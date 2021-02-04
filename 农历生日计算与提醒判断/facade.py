from 邮件发送 import message as emailSend
from main import *
def update(message, flag=False):
    if flag:
        print(message)
        emailSend.sendMessage(receiver=reciver,title=message)
    else:
        print(message)
