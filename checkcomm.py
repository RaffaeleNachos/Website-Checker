import requests
import time
import smtplib
import urllib.request


while True:
    
	opener = urllib.request.FancyURLopener({})
	url = "https://www.google.com"
	f = opener.open(url)
	content = f.read()
	#uncomment the following line if you want the HTML code to be printed
	#print(content) 
	if str(content).find("Keyword or string") != -1: #if the keyword isn't found the code go to the else and send the email
		time.sleep(60) #or it waits 60 seconds and download the HTML code again
		continue
	
	else:
		msg = 'Check the Website, now!'
		fromaddr = 'your_email_add'
		toaddrs  = ['fist_email_add','second_email_add', 'n_email_add']
		#uncomment the line that corresponds to your email domain

		#Hotmail, Live, Outlook
		#server = smtplib.SMTP('smtp.live.com', 25)

		#Yahoo		
		#server = smtplib.SMTP('smtp.mail.yahoo.it', 25)		
		
		#Gmail
		#server = smtplib.SMTP('smtp.gmail.com', 587)
		
		server.starttls()
		server.login("YOUR_EMAIL_ADDRESS", "YOUR_PASSWORD")
		print('From: ' + fromaddr)
		print('To: ' + str(toaddrs))
		print('Message: ' + msg)
		server.sendmail(fromaddr, toaddrs, msg)
		server.quit()

		break
