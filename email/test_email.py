#!/usr/local/bin/python3.7

import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login('username@gmail.com', 'password')

message = 'Test Message'

s.sendmail('steve.lowrance@gmail.com', 
			['steve.lowrance@gmail.com', 'lowrance@pdx.edu'], message)
			
s.quit()
