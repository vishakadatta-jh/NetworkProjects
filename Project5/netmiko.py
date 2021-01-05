import difflib
import datetime
import smtplib
from email.mime.multipart import MIMRMultipart
from email.mime.text import MIMEText
from netmiko import ConnectHandler

#Device IP
ip = '10.10.10.10'

#type of device
device_type = 'arista_eos'

#User credentials
username = 'admin'
password = 'python'

#the command to run
command = 'show running'

#Connectin to thw switch using SSH
session = ConnectHandler(device_type=device_type,ip=ip,username=username,password=password,global_delay_factor =3)

#enable mode
enable = session.enable()

#Send commands written previously
output = session.send_command(command)


#Defining one day old files (yesterday) the file name is ip_date and here date is yesterdays
device_old_cfg = 'cfgfiles/' +ip+'_'+(datetime.date.today() - datetime.timedelta(days=1)).isoformat() #iso format is YYYY-MM-DD 

#writing output of the command in today's file 

with open('cfgfiles/'+ip+'_'+datetime.date.today().isoformat(),'w') as device_new_cfg:
    device_new_cfg.write(output +'\n')
    
#now finding the differencebetween yesterday  and today's files in HTML (so that it is easy for sending in mail)
with open(device_old_cfg,'r') as old_file , open('cfgfiles/'+ip+'_'+datetime.date.today().isoformat(),'r') as new_file:
    difference = difflib.HtmlDiff().make_file(fromlines = old_file.readlines(),tolines = new_file.readlines(),fromdesc ='Yesterday',todesc='Today')



#Sending Email
fromaddr = 'vishakahebbar@gmail.com'
toaddr = 'vhshetty1996@gmail.com'

#MIME google it !
msg = MIMRMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Daily report of SWITCHES'
msg.attach(MIMEText(difference,'html'))

#Using Gmail's SMTP SERVER on port 587
server = smtplib.SMTP('smtp.gmail.com',587)

#SMTP connectio is in TLS mode for encryption
server.starttls()

#logging in ti gmail and sending
server.login('vishakahebbar@gmail','anuammaA1972#')
server.sendmail(fromaddr,toaddr,msg.as_string())
server.quit()