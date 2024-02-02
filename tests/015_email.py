import smtplib
import datetime
from email.mime.text import MIMEText
from getpass import getpass


def send_test_message(dest_mail, msg_text, pwd):
	msg = MIMEText(msg_text)

	src_email = "i@xxx.com"

	msg['Subject'] = msg_text
	msg['From'] = src_email
	msg['To'] = dest_mail

	s = smtplib.SMTP('smtp.beget.ru')

	s.login(src_email, pwd)

	try:
		s.sendmail(src_email, dest_mail, msg.as_string())
		print("message succesfully sent")
	finally:
		s.close()


emails = ["i@xxx.com", "zzz4rec@xxx.com", "services@xxx.com", "den@xxx.ru"]

date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
msg_text = "test " + date
pwd = getpass()

for dest_mail in emails:
	send_test_message(dest_mail, msg_text, pwd)
