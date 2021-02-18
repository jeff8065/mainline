#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uiautomator2 as u2
import os,time
d = u2.connect()
#d(resourceId="com.google.android.gms:id/sud_layout_content").click()
d.WAIT_FOR_DEVICE_TIMEOUT = 70
d.implicitly_wait(10.0)
#-----------------------Wifi----------------------#
def wifisetup():
	os.system("adb  shell am start  -n com.android.settings/.wifi.WifiDialogActivity")

	d.send_keys("CTS_GSI_5G", clear=True)
	d(resourceId="com.android.settings:id/security").click()
	time.sleep(2)
	d(resourceId="android:id/text1", text="WPA/WPA2-Personal").click()
	d(resourceId="com.android.settings:id/password").click()
	d.send_keys("01111111", clear=True)
	d(resourceId="android:id/button1").click()
	os.system("adb  shell svc wifi disable")
	time.sleep(1.5)	
	os.system("adb shell svc wifi enable")
	time.sleep(10)	

#---------------------Addaccount--------------------#
def Addaccount2():
	os.system("adb shell am start -n com.android.settings/.accounts.AddAccountSettings")
	d(resourceId="android:id/title", text="Google").click()
	time.sleep (5)


	check=d(text="Sign in").exists(timeout=30)
	if str(check) == "True":#檢查text是否存在
		print("pass")
		d(resourceId="identifierId").click()
		d.send_keys("mainlinebeta98", clear=True)

		d(text="Next").click()
		time.sleep(5)
		d.send_keys("qwerty@#", clear=True)
		nextbutton1=d(text="Next").exists(timeout=6)
		nextbutton2=d(resourceId="passwordNext").exists(timeout=5)
		time.sleep(3)
		if str(d(text="Next").exists(timeout=6)) == "True":
			print("Next")
			nextbutton_name=d(text="Next").click()
		elif str(d(resourceId="passwordNext").exists(timeout=5)) == "True" :
			print("passwordNext") 
			d(resourceId="passwordNext").click()
		time.sleep(3)

		if str(d(resourceId="signinconsentNext").exists(timeout=6)) == "True":
			d(resourceId="signinconsentNext").click()
		time.sleep(3)
		if str(d(text="More").exists(timeout=6)) == "True":
			d(text="More").click()
			time.sleep(2)
		d(text="Accept").click()
	else:
		print("fail")
		print(check)

def Addaccount():
	sum = 0   # 累加變數
	i = 1   # 索引變數
	while i <= 3:
		os.system("adb  shell input keyevent 03")
		os.system("adb shell am start -n com.android.settings/.accounts.AddAccountSettings")
		d(resourceId="android:id/title", text="Google").click()
		time.sleep (5)

		if str(d(text="Sign in").exists(timeout=10)) == "True":#檢查text是否存在
			#print("pass")
			d(resourceId="identifierId").click()
			d.send_keys("mainline_test@pegatroncorp.com", clear=True)
			time.sleep(2)
			d(text="Next").click()
			time.sleep(5)
			d.send_keys("pega#1234", clear=True)
			if str(d(text="Next").exists(timeout=6)) == "True":
				d(text="Next").click()
			elif str(d(resourceId="passwordNext").exists(timeout=5)) == "True" :
				d(resourceId="passwordNext").click()

			if str(d(resourceId="signinconsentNext").exists(timeout=6)) == "True":
				d(resourceId="signinconsentNext").click()
			
			if str(d(text="More").exists(timeout=6)) == "True":
				d(text="More").click()
				time.sleep(2)
			if str(d(text="Accept").exists(timeout=6)) == "True":
				d(text="Accept").click()
			break
		else:
			
			#print(check)
			sum += i
			print("reconnect wifi "+str(i)+"/3")
			i += 1 # 改變索引變數的值

			wifisetup()
	if sum == 3 :
		print("Something wrong")

#-----------------update module----------------------------
def update():
	sum = 0   # 累加變數
	i = 1   # 索引變數
	while i <= 3:
		os.system("adb shell am force-stop com.android.vending") # force stop play store
		time.sleep(6)
		os.system("adb shell am start -a android.settings.MODULE_UPDATE_SETTINGS")


		if str(d(text="Download & install").exists(timeout=10)) == "True":
			d(resourceId="com.android.vending:id/0_resource_name_obfuscated", text="Download & install").click()
			break
		else:
			sum +=i
			print("Restart")
			i +=1
	if sum == 3 :
		print("Something wrong")		

	#	d(resourceId="com.android.vending:id/0_resource_name_obfuscated", text="Restart now").click()
	#	time.sleep(10)
	#	os.system("adb shell am start -a android.settings.MODULE_UPDATE_SETTINGS")
	#	if str(d(text="Download & install").exists(timeout=6)) == "True":
	#		d(resourceId="com.android.vending:id/0_resource_name_obfuscated", text="Download & install").click()
#wifisetup()
#update()
#os.system("adb shell am start -a android.settings.MODULE_UPDATE_SETTINGS")





wifisetup()
Addaccount()
update()