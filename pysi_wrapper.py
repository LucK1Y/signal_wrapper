from .signal_wrapper.models import Message
from .signal_wrapper import read
from .signal_wrapper.send import send_Thread

from threading import Thread
from typing import Union, Iterable


class PySiWrapper(object):
    def __init__(self, serveraddress: str):
        self.address = serveraddress
        self.task = None

    def send(self, msg: Message) -> Union[Thread, None]:
        if self.task:
            if self.task.is_alive():
                print("[-] already sending one message, ABORTING")
                return None

        self.task = send_Thread(msg)
        return self.task

    def send_message(self, receiveraddress: str, message_body: str) -> Thread:
        x = Message(content=message_body, sender=self.address, receiver=receiveraddress)

        return self.send(x)

    def read(self, json_format: bool = False) -> Union[Iterable[Message], Iterable[dict]]:
        if json_format:
            return read.read_Raw(self.address)
        else:
            return read.read(self.address)
