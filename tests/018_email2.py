import smtplib
import datetime
from email.mime.text import MIMEText
from getpass import getpass

file_name = "R:/_docs/zzzprivate/tmp_mail.txt"
src_email = "i@xxx.com"


def get_pwd():
	#pwd = ""
	pwd = getpass()
	return pwd


def send_message(dest_mail, msg_text, subject):
	msg = MIMEText(msg_text)

	pwd = get_pwd()

	msg['Subject'] = subject
	msg['From'] = src_email
	msg['To'] = dest_mail
	
	_send_message_norm(msg, pwd)


def _send_message_tls(msg, pwd):
	s = smtplib.SMTP('smtp.gmail.com', 587)

	try:
		#s.set_debuglevel(1)
		s.ehlo()
		s.starttls()
		s.login(src_email, pwd)
		s.sendmail(src_email, dest_mail, msg.as_string())
		print("message succesfully sent - tls")
		s.quit()
	finally:
		s.close()


def _send_message_norm(msg, pwd):
	s = smtplib.SMTP('smtp.beget.ru')
	s.login(src_email, pwd)

	try:
		s.sendmail(src_email, dest_mail, msg.as_string())
		print("message succesfully sent")
	finally:
		s.close()


emails = ["i@xxx.com"]

#date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
subject = ""
msg_text = ""

with open (file_name, "r", encoding = "cp1251") as f:
	for line in f:
		line = line.rstrip()

		jj = line.find('Subject=')
		if jj != -1:
			subject = line[8:]
		else:
		    msg_text = msg_text + line + "\n"


#print("Subject = " + subject)
#print(";---Text = \n" + msg_text)


for dest_mail in emails:
	send_message(dest_mail, msg_text, subject)
