import sys
import subprocess

def ip_reach(list):
    for i in list:
        i = i.rstrip('\n')
        
        #variable to store the output of call process and also second argument is to supress the unneccasry err messages
        #/n is number of times we are pinging and it is 2
        ping_reply = subprocess.call('ping %s /n 2' %(i) ,stdout = subprocess.DEVNULL ,stderr = subprocess.DEVNULL)
        
        #if ping'ed' the call will return '0' so..
        if ping_reply == 0:
            print("IP {} IS REACHABLE".format(i))
            continue
        else:
            print("IP {} IS NOT REACHABLE".format(i))
            sys.exit()
