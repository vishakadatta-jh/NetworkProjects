import sys
import time

#importing all the functions
from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_thread import create_thread

#importing all the IP address from ip text file
ip_list = ip_file_valid()

#validate the ips in the given file
try:
    ip_addr_valid(ip_list)
    
except KeyboardInterrupt:
    print("\n Program aborted !! by the user !! \n")
    sys.exit()

#validate the reachibility of the ip address
try:
    ip_reach(ip_list)
    
except KeyboardInterrupt:
    print("\n Program aborted !! by the user !! \n")
    sys.exit()

#start the application for one or more application
while True:
    create_thread(ip_list,ssh_connection)
    time.sleep(5)
    