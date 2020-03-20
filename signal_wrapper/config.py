SERVER_ADRESS="+447535690702"

test=False


if test:
    READ_COMMAND='start echo "{}"'
    SEND_COMMAND='start echo "{} {} {}"'
    
else:
    READ_COMMAND="signal-cli -u {} receive"
    SEND_COMMAND="signal-cli -u {} send -m '{}' {}"