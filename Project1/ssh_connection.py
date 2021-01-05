import paramiko
import os.path
import time
import sys
import re


# In[5]:


#Asking user to provide the USERNAME/PASSWORD FILE
user_file = input("\n Provide the correct file path containing the USERNAME/PASSWORD :  ") #accepting the file path    #checking if the path is valid
    
if os.path.isfile(user_file) == True:
    print("\n *USERNAME/PASSWORD FILE EXISTS")
else :
    print("\n *File '{}' doesn't exist! Provide the correct path! ".format(user_file))
    sys.exit()

#Asking user the command file
command_file = input("\n *Provide the correct file path containing the command : ") #accepting the file path
    
    #checking if the path is valid
if os.path.isfile(command_file) == True:
    print("\n *COMMAND FILE EXISTS")
else :
    print("File {} doesn't exist! Provide the correct path! ".format(command_file))
    sys.exit()

#Open the SSH connection for the arista switches
def ssh_connection(ip):
    global user_file
    global command_file
    
    try:
        the_user_file = open(user_file,'r')
    
        the_user_file.seek(0)
    
        Username = the_user_file.readlines()[0].split(',')[0].rstrip("\n") #username extracted from the file
    
        the_user_file.seek(0)
    
        Password = the_user_file.readlines()[0].split(',')[1].rstrip("\n") #password extracted from the file
        
        #Starting the SSH session
        session = paramiko.SSHClient()
        
        #Handling unknown session keys in testing environment 
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        #Connecting to the session in remote and starting it 
        session.connect(ip.strip("\n"),username = Username,password = Password)
        
        #Starting the session
        start_session = session.invoke_shell()
        
        #Sending commands and disabling pagination
        start_session.send("enable\n")
        start_session.send("terminal length 0\n")
        time.sleep(0)
        
        #Commands for Config mode
        start_session.send("\n")
        start_session.send("configure terminal\n")
        time.sleep(1)
        
        #Opening the Command file by user
        the_cmd_file = open(command_file,'r')
    
        the_cmd_file.seek(0)
        
        #Executing each line in the command file
        for line in the_cmd_file.readlines():
            start_session.send(line + '\n')
            time.sleep(2)
        
        #Close all the files
        the_user_file.close()
        the_cmd_file.close()
        
        #Receving the outputs
        
        output = start_session.recv(65535)
        
        #Checking for errors
        if re.search(b"% Invalid input" ,output):
            print("One or more Syntax errors were found on {}".format(ip))
        else:
            print("All good for {}".format(ip))
        
        #Printing the received Outputs
        ips = (re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",str(output)))
        print(ips)
        #Close all session
        session.close()
        
    except paramiko.AuthenticationException:
        print("Invalid username or password \n Please check and enter again")
        print("\Program closed ......bye")        