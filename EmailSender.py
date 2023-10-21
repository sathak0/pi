
import smtplib
import subprocess
# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
# Authentication
s.login("ipaddresssend2003@gmail.com","wirf hciq ppsx ifgi")
# message to be sent
cmd = "hostname -i | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True )
#message="https://"+str(IP,'utf-8')
#print(message)
# sending the mail

s.sendmail("ipaddresssend2003@gmail.com", "pmsathak@gmail.com")
# terminating the session
s.quit()
