import smtplib
from email.mime.text import MIMEText

msg = MIMEText(msg_text)

msg['Subject'] = "text"
msg['To'] = "dest@gmail.com"

s = smtplib.SMTP('smtp.gmail.com')
s.login("from@gmail.com", "password")

try:
	s.sendmail("from@gmail.com", "dest@gmail.com", msg.as_string())
finally:
	s.close()
