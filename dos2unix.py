import sys
filename = sys.argv[2]
operation = sys.argv[1]

if operation == 'dos2unix':
    text = open(filename, 'rb').read().replace('\r\n', '\n')
    open(filename, 'wb').write(text)
elif operation == 'unix2dos':
    text = open(filename, 'rb').read().replace('\n', '\r\n')
    open(filename, 'wb').write(text)
else:
    sys.exit('Possible args can be dos2unix or unix2dos')

