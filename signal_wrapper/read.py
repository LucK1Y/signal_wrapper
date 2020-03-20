from .config import READ_COMMAND
from .models import Message

import subprocess, json


def read(serveraddress: str):
    """Reads all new messages and parses them
    
    Returns:
        List[Messages] -- List of Messages
    """
    print(READ_COMMAND.format(serveraddress))
    process = subprocess.run(READ_COMMAND.format(serveraddress), capture_output=True, shell=True)

    #  stdout=PIPE and/or stderr=PIPE
    if process.stderr:
        print(f"[-] ERROR in checking {READ_COMMAND.format(serveraddress)}")
        return

    string = process.stdout.decode()

    msgs = []

    for line in string.split("\n"):
        msgs.append(Message.parse(line))

    return msgs


# def myconverter(o):
#     type(o)
#     if isinstance(o, list):
#         return o
#     print(o.__dict__)
#     return o.__dict__


def read_Raw(serveraddress: str):
    out = []

    for msg in read(serveraddress):
        if isinstance(msg, Message):
            out.append(msg.__dict__)

    return out
