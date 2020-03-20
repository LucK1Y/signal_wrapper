import subprocess,threading

from .models import Message
from .config import SEND_COMMAND

def send(msg:Message):
    subprocess.run(SEND_COMMAND.format(msg.sender,msg.content,msg.receiver),shell=True)

def send_Thread(msg:Message):
    x=threading.Thread(target=send,args=(msg,),daemon=True)

    x.start()