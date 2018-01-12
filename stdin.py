import datetime
import sys

now = datetime.datetime.now()
day = now.day

if day == 15:
    sys.exit()


import sys
while True:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    print 'line is ' + line