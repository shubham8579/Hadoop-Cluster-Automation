import subprocess

subprocess.getoutput("echo '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>dfs.data.dir</name>\n<value>/slavemydata</value>\n</property>\n\n</configuration>' > /etc/hadoop/hdfs-site.xml")

subprocess.getoutput("mkdir /slavemydata")

subprocess.getoutput("echo '<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n<property>\n<name>fs.default.name</name>\n<value>hdfs://192.168.43.149:9001</value>\n</property>\n\n</configuration>' > /etc/hadoop/core-site.xml")

subprocess.getoutput("firewall-cmd --add-port=0-65535/udp --permanent")

subprocess.getoutput("firewall-cmd --add-port=0-65535/tcp --permanent")

subprocess.getoutput("hadoop-daemon.sh start datanode")
