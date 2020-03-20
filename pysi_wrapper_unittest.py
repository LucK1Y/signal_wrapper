import unittest, sys
from pysi_wrapper import PySiWrapper

from threading import Thread


class PySiTestCas(unittest.TestCase):
    address = "adress"
    x = PySiWrapper(address)

    def test_a_check_init(self):
        self.assertEqual(self.x.address, self.address)

    def test_b_send(self):
        thread = self.x.send_message(message_body="message", receiveraddress="receiver")
        self.assertIsInstance(thread, Thread)

        while thread.is_alive():
            sys.stdout.write(".")

    def test_c_read(self):
        pass


if __name__ == '__main__':
    unittest.main()
