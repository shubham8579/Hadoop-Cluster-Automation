import os
import subprocess
import cv2
import getpass

os.system("echo 'hello    welcome to   tools    menu      enter your password' | festival --tts")

os.system('tput setaf 1')
print("\t\t\t Welcome to Tool Menu")
print("\t\t\t =====================")
os.system('tput setaf 6')

mypasswd = "redhat"
passwd = getpass.getpass("\nEnter your password : \n")

if passwd == mypasswd:

	os.system("echo 'hello user       enter your choice' | festival --tts")
	print("\nWhere do you wish to execute th tool local or remote : ")
	system = input()
	print("\nSystem is : {}".format(system))

	while True:
		if system == "local":
			os.system("clear")
			os.system("echo 'select one of the following options' | festival --tts")
			print ("""
		
			press 1 to setup pre-requsite to set-up hadoop cluster(JAVA AND HADOOP)
			press 2 to setup master node
			press 3 to setup slave node
			press 4 to setup client
			press 0 to exit
			""")
			print("\nEnter your choice : ",end='')
			ch=input()
			print("\nThe entered choice is {}".format(ch))


			if int(ch) == 1:
				subprocess.getoutput("python36 /root/Desktop/minor2/hadoop-setup.py")
				input("Press Enter to Continue .....")

			if int(ch) == 2:
				subprocess.getoutput("python36 /root/Desktop/minor2/master-setup.py")
				input("Press Enter to Continue .....")

			if int(ch) == 3:
				subprocess.getoutput("python36 /root/Desktop/minor2/slave-setup.py")
				input("Press Enter to Continue .....")


			if int(ch) == 4:
				subprocess.getoutput("python36 /root/Desktop/minor2/client-setup.py")
				input("Press Enter to Continue .....")


			if int(ch) == 0:
				print("\nThank You")
				os.system('tput setaf 0')
				exit()



		elif system == "remote":
			os.system("clear")
			os.system("echo 'select one of the following options' | festival --tts")
			print ("""

			press 1 to setup pre-requsite to set-up hadoop cluster(JAVA AND HADOOP)
			press 2 to setup master node
			press 3 to setup slave node
			press 4 to setup client
			press 0 to exit
			""")
			print("\nEnter your choice : ",end='')
			ch=input()
			print("\nThe entered choice is {}".format(ch))


				
			if int(ch) == 1:
				
				ip = input("Enter the IP to access : ")
				cd0 = "ssh {} mkdir /root/Desktop/test1".format(ip)
				cd1 = "scp /root/Desktop/minor2/hadoop-1.2.1-1.x86_64.rpm  {}:/root/Desktop/test1/hadoop-1.2.1-1.x86_64.rpm".format(ip)
				cd2 = "scp /root/Desktop/jdk-8u171-linux-x64.rpm  {}:/root/Desktop/test1/jdk-8u171-linux-x64.rpm".format(ip)
				cd3 = "scp /root/Desktop/minor2/hadoop-setup.py  {}:/root/Desktop/test1/hadoop-setup.py".format(ip)
				cd4 = "ssh {} python36 /root/Desktop/test1/hadoop-setup.py".format(ip)

				
				subprocess.getoutput(cd0)
				subprocess.getoutput(cd1)
				subprocess.getoutput(cd2)
				subprocess.getoutput(cd3)
				subprocess.getoutput(cd4)
				input("Press Enter to Continue .....")


			

			if int(ch) == 2:

				ip = input("Enter the IP to access : ")

				cd1 = "scp /root/Desktop/minor2/master-setup.py  {}:/root/Desktop/test1/master-setup.py".format(ip)
				cd2 = "ssh {} python36 /root/Desktop/test1/master-setup.py".format(ip)

				subprocess.getoutput(cd1)
				subprocess.getoutput(cd2)
				input("Press Enter to Continue .....")

			if int(ch) == 3:

				ip = input("Enter the IP to access : ")

				cd1 = "scp /root/Desktop/minor2/slave-setup.py  {}:/root/Desktop/test1/slave-setup.py".format(ip)
				cd2 = "ssh {} python36 /root/Desktop/test1/slave-setup.py".format(ip)

				subprocess.getoutput(cd1)
				subprocess.getoutput(cd2)
				input("Press Enter to Continue .....")


			if int(ch) == 4:

				ip = input("Enter the IP to access : ")

				cd1 = "scp /root/Desktop/minor2/client-setup.py  {}:/root/Desktop/test1/client-setup.py".format(ip)
				cd2 = "ssh {} python36 /root/Desktop/test1/client-setup.py".format(ip)

				subprocess.getoutput(cd1)
				subprocess.getoutput(cd2)
				input("Press Enter to Continue .....")




			if int(ch) == 0:
				print("\nThank You")
				os.system('tput setaf 0')
				exit()



else:
	print("Login Error!!")


os.system('tput setaf 0')
