# coding: utf-8
#
import uiautomator2 as u2
import os,time
d = u2.connect()
#d(resourceId="com.google.android.gms:id/sud_layout_content").click()

#-----------------------Wifi----------------------#
os.system("adb  shell am start  -n com.android.settings/.wifi.WifiDialogActivity")

d.send_keys("CTS_GSI_5G", clear=True)
d(resourceId="com.android.settings:id/security").click()
d(resourceId="android:id/text1", text="WPA/WPA2-Personal").click()
d(resourceId="com.android.settings:id/password").click()
d.send_keys("01111111", clear=True)
d(resourceId="android:id/button1").click()


#---------------------update--------------------#
def update():
	os.system("adb shell am start -n com.android.settings/.accounts.AddAccountSettings")
	d(resourceId="android:id/title", text="Google").click()
	time.sleep (5)


	check=d(text="Sign in").exists(timeout=30)
	if str(check) == "True":#檢查text是否存在
		print("pass")
		d(resourceId="identifierId").click()
		d.send_keys("testpega5888", clear=True)

		d(text="Next").click()
		time.sleep(5)
		d.send_keys("588888888", clear=True)
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
		d(text="Accept").click()
	else:
		print("fail")
		print(check)


	os.system("adb shell am force-stop com.android.vending") # force stop play store
	time.sleep(6)
	os.system("adb shell am start -a android.settings.MODULE_UPDATE_SETTINGS")

	d(resourceId="com.android.vending:id/0_resource_name_obfuscated", text="Download & install").click()
	d(resourceId="com.android.vending:id/0_resource_name_obfuscated", text="Restart now").click()

update()