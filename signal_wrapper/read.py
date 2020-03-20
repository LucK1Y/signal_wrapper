from .config import SERVER_ADRESS,READ_COMMAND
from .models import Message

import subprocess,json

def read():
    """Reads all new messages and parses them
    
    Returns:
        List[Messages] -- List of Messages
    """
    print(READ_COMMAND.format(SERVER_ADRESS))
    process=subprocess.run(READ_COMMAND.format(SERVER_ADRESS),capture_output=True,shell=True)

    #  stdout=PIPE and/or stderr=PIPE
    if process.stderr:
        print(f"[-] ERROR in checking {READ_COMMAND.format(SERVER_ADRESS)}")
        return

    string=process.stdout.decode()
    
    msgs=[]

    for line in string.split("\n"):
        msgs.append(Message.parse(line))

    return msgs

def myconverter(o):
    type(o)
    if isinstance(o,list):
        return o
    print(o.__dict__)
    return o.__dict__

def read_Raw():
    out=[]

    for msg in read():
        if isinstance(msg,Message):
            out.append(msg.__dict__)

    return out