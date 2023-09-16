import pyfiglet
import sys
import socket
from datetime import datetime


Ascii_banner = pyfiglet.figlet_format("P0RT-SCANNER")
print(Ascii_banner)

if len(sys.argv) == 2:
    target = (socket.gethostbyname(sys.argv[1]))
else:
    print("Your Argument is invalid!!!")


print("-" * 50)
print("Scanning-Target: " + target)
print("Scanning Started at:" + str(datetime.now()))
print("-" * 50)
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result == 0:
            print("P0rt {} is open".format(port))
        s.close()


except KeyboardInterrupt:
    print("\n Programming exited!!!")
    sys.exit()

except socket.gaierror:
    print("\n Hostname Could Not be Resolved !!!!!")
    sys.exit()

except socket.error:
    print("\n Server is currently not Responding !!!!!")
    sys.exit()
