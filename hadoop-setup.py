import subprocess

print("Installing ORACLE JAVA.....")
subprocess.getoutput("rpm -ivh /home/test1/jdk-8u171-linux-x64.rpm")
print("Installation complete.....")

print("Defining path for JAVA")
subprocess.getoutput("echo 'export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/' >> /root/.bashrc")
subprocess.getoutput("echo 'export PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH' >> /root/.bashrc")
print("JAVA path defined.")

print("Installing HADOOP ARCHITECTURE.....")
subprocess.getoutput("rpm -ivh /home/test1/hadoop-1.2.1-1.x86_64.rpm --force")
print("Installation complete.....")


