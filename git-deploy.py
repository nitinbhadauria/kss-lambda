import paramiko
import os
import json
def handler_name(event, context):
        msg = event['Records'][0]['Sns']['Message']
        print msg
        read = json.loads(msg)
        branch = read['ref']
	kss_env = os.environ['ENV']
	print kss_env
	output = "Its not deploy branch"
	if branch == "refs/heads/"+kss_env:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect('ec2-34-229-42-135.compute-1.amazonaws.com', username='ubuntu', password='123456')
		stdin, stdout, stderr = ssh.exec_command("cd /usr/share/nginx/html/kss-lambda; git pull origin "+kss_env)
		output = stdout.readlines()
        return output
