## [AWS](https://aws.amazon.com/)  
# Online resources  
## Videos
[Amazon Web Services - EC2 Server Setup - Connect with Webstorm](https://www.youtube.com/watch?v=HfnIL5lM8WY)  
[How to MANUALLY Migrate Your Wordpress Site](https://www.youtube.com/watch?v=wROa37k_RQA)  
[Migrate any website to Amazon AWS EC2 in 5 Easy Steps](https://www.youtube.com/watch?v=6eH_XNMUsFQ)  
[How to migrate a local WordPress MySQL database to RDS](https://www.youtube.com/watch?v=gwO76ar56Kg)  
## Text Tutorial
[Launch and connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance)  
[Connect with PuTTY and WinSCP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)  
[Tutorial: Install a LAMP Web Server with the Amazon Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html)  
[How to Migrate WordPress from AWS EC2 to cPanel-based Shared Hosting](http://www.thegurleyman.com/how-to-migrate-wordpress-from-aws-ec2-to-cpanel-based-shared-hosting/)  
[Migrate Self-Hosted Wordpress to EC2](https://forums.aws.amazon.com/thread.jspa?threadID=120283)  
[Migrate Data From One WordPress Instance to Another](https://docs.bitnami.com/aws/how-to/migrate-wordpress/)  
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
## Wordpress  
### Installation
Click “Launch new instance”, then search "Wordpress", find the result in Market Place, then install it as normal.  
Go to instance page, right click instance, Choose Instance Settings/Get system log, and find the username and password.  
Login to Wordpress.
### Migration
> 1 Go to Wordpress dashboard/tools/export to download a XML file.  
> 2 Go to the new Wordpress dashboard/tools/import to upload the XML, and all the pages and posts and database is moved to the new site.

