class Message(object):

    def __init__(self, content: str, receiver: str, sender: str):
        """Create Message
        
        Arguments:
            content {str} -- Content of message
            receiver {str} -- receiver adress
            sender {str} -- sender adress
        """

        self.content = content
        self.receiver = receiver
        self.sender = sender

    @classmethod
    def parse(cls, line: str):
        print(f"received {line}")

        # raise NotImplementedError("Not implemented yet")

        return cls("test", "12", "aw")
