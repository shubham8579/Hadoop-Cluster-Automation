import subprocess

subprocess.getoutput('''echo "<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>dfs.name.dir</name>\n<value>/mydata</value>\n</property>\n\n</configuration>" > /etc/hadoop/hdfs-site.xml''')

subprocess.getoutput("mkdir /mydata")

subprocess.getoutput('''echo "<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://192.168.43.149:9001</value>\n</property>\n\n</configuration>" > /etc/hadoop/core-site.xml''')
#print("1")
subprocess.getoutput("firewall-cmd --add-port=0-65535/udp --permanent")
#print("2")
subprocess.getoutput("firewall-cmd --add-port=0-65535/tcp --permanent")
#print("3")
subprocess.getoutput("hadoop namenode -format -force")
#subprocess.getoutput("hadoop namenode -format | echo "\ny" )
#print("4") 
subprocess.getoutput("hadoop-daemon.sh start namenode")
#print("ujjawal")
