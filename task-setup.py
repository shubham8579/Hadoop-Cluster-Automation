import subprocess

subprocess.getoutput('''echo "<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>mapred.job.tracker</name>\n<value>192.168.43.149:9002</value>\n</property>\n\n</configuration>" > /etc/hadoop/mapred-site.xml''')


subprocess.getoutput("firewall-cmd --add-port=0-65535/udp --permanent")

subprocess.getoutput("firewall-cmd --add-port=0-65535/tcp --permanent")

subprocess.getoutput("hadoop-daemon.sh start tasktracker")
