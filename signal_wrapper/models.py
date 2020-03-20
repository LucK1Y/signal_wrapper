from .config import SERVER_ADRESS

class   Message(object):


    def __init__(self,content:str,receiver:str,sender:str):
        """Create Message
        
        Arguments:
            content {str} -- Content of message
            receiver {str} -- receiver adress
            sender {str} -- sender adress
        """

        self.content=content
        self.receiver=receiver
        self.sender=sender

    @classmethod
    def fromServer(cls,content:str,receiver:str):
        """Create Message which is from the server
        
        Arguments:
            content {str} -- Content of message
            receiver {str} -- receiver adress
        
        Returns:
            Message -- Message Object
        """
        return cls(content,receiver,SERVER_ADRESS)

    @classmethod
    def toServer(cls,content:str,sender:str):
        """Create Message which is to the server
        
        Arguments:
            content {str} -- Content of message
            sender {str} -- receiver adress
        
        Returns:
            Message -- Message Object
        """
        return cls(content,SERVER_ADRESS,sender)

    @classmethod
    def parse(cls,line:str):
        print(f"received {line}")

        # raise NotImplementedError("Not implemented yet")

        return cls("test","12","aw")