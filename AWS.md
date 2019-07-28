## [AWS](https://aws.amazon.com/)  
# Online resources  
## Videos
[Amazon Web Services - EC2 Server Setup - Connect with Webstorm](https://www.youtube.com/watch?v=HfnIL5lM8WY)  
## Text Tutorial
[Launch and connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance)  
[Connect with PuTTY and WinSCP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)  
[Tutorial: Install a LAMP Web Server with the Amazon Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html)
# Notes
## How to open a terminal after connecting to an instance
Webstorm: Tools -> Start SSH session
## 'No such file' in var
$ sudo usermod -a -G apache ec2-user  
$ exit  
and re-connect  
Then stop and start instance (reboot sometimes doesn't work)
## Permission denied while uploading files to server
$ sudo chown -R ec2-user:apache /var/www  
$ sudo chmod 2775 /var/www  
$ find /var/www -type d -exec sudo chmod 2775 {} \;  
$ find /var/www -type f -exec sudo chmod 0664 {} \;  
## Instal Wordpress  
Download wordpress package from [wordpress.org](https://wordpress.org/), and then upload it to the server's var/www/html folder.  

