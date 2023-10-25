import socket
import time
import smtplib
import subprocess
time.sleep(150)
def get_ip():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254',1))
        IP=s.getsockname()[0]
    except Exception:
            IP='127.0.0.1'
    finally:
            s.close()
    return IP
s=smtplib.SMTP("smtp.gmail.com",587)
#print("START")
s.starttls()
s.login("ipaddresssend2003@gmail.com","wirf hciq ppsx ifgi")
ip=get_ip()
s.sendmail("ipaddresssend2003@gmail.com","pmsathak@gmail.com",ip)
s.quit()

#print("ENd")
