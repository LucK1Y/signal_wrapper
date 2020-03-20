# signal_wrapper
Python Wrapper for Signal wrapper

# not ready yet

# Requirements
Signal-cli: https://github.com/AsamK/signal-cli

# Usage
Read and send messages:

````python
from pysi_wrapper import Message

m=Message(sender="SENDER",receiver="RECEIVER",content="MESSAGE BODY")
````

### Read Messages
````python
from pysi_wrapper import PySiWrapper

x=PySiWrapper(serveraddress="server adress")
x.read() # returns list of messages

x.read(json_format=True) # returns list of dicts
````

### Write Message
````python
from pysi_wrapper import PySiWrapper,Message

x=PySiWrapper(serveraddress="server adress")
thread=x.send_message(message_body="MESSAGE",receiveraddress="ADRESS")

# or with Message
m=Message(sender="SENDER",receiver="RECEIVER",content="MESSAGE BODY")
thread=x.send(m)

# check if send is done:
while thread.is_alive():
    pass

````