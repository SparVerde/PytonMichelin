import time
import random

#second from 1 Jan 1907
print(time.time())
#stop for 7 seconds
#time.sleep(7)

#Stop for 1-5 sec.
wait_for_sec = random.randint(1,5)
print('Wait for', wait_for_sec)
time.sleep(wait_for_sec)

print(time.time())
