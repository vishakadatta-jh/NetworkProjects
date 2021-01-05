import os.path
import sys

def ip_file_valid():
    "Function to check the file with IP address is valid or not"
    ip_file_path = input("Provide the correct file path for the IP adress file : ") #accepting the file path
    
    #checking if the path is valid
    if os.path.isfile(ip_file_path) == True:
        print("The file exists ...")
    else :
        print("File doesn't exist! Provide correct path! ")
        sys.exit()
    
    ip_file = open(ip_file_path,'r') #opening file
    
    ip_file.seek(0)#starting from  the beginning of the file
    
    ip_file_content = ip_file.readlines() #extracting the content of the file
    
    ip_file.close() #file close
    
    return ip_file_content