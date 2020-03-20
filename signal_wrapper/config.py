test = True

if test:
    READ_COMMAND = 'start echo "read for address: {}"'
    SEND_COMMAND = 'start echo Sender: {}  Message: {} Receiver: {}'

else:
    READ_COMMAND = "signal-cli -u {} receive"
    SEND_COMMAND = "signal-cli -u {} send -m '{}' {}"
