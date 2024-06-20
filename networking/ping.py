
#pip install aio_ping
#from ping3 import ping, verbose_ping
# from aio_ping import ping
# ping('google.com', timeout=3000, count=3, delay=0.5)
#ping('google.com')  # Returns delay in seconds.
#---------------------------------
#pip install wheel
#pip install icmplib
#https://pypi.org/project/icmplib/
#https://python-forum.io/thread-36547.html
from icmplib import ping, multiping, traceroute, resolve
print(ping('google.com', count=4))



#---------------------------------
# Option 2
#---------------------------------

