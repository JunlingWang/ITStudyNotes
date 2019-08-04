## [AWS](https://aws.amazon.com/)  
# Online resources  
## Videos
[Amazon Web Services - EC2 Server Setup - Connect with Webstorm](https://www.youtube.com/watch?v=HfnIL5lM8WY)  
[How to MANUALLY Migrate Your Wordpress Site](https://www.youtube.com/watch?v=wROa37k_RQA)  
[Migrate any website to Amazon AWS EC2 in 5 Easy Steps](https://www.youtube.com/watch?v=6eH_XNMUsFQ)  
[How to migrate a local WordPress MySQL database to RDS](https://www.youtube.com/watch?v=gwO76ar56Kg)  
[How To Make Your Own Web Hosting Cpanel in AWS Step by Step | WHM installation](https://www.youtube.com/watch?v=Kmfy6yzDTu0)  
[How to Install Cpanel/whm on AWS Amazon EC2](https://www.youtube.com/watch?v=qPFcsY6I6vQ)  
## Text Tutorial
[Launch and connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance)  
[Connect with PuTTY and WinSCP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)  
[Tutorial: Install a LAMP Web Server with the Amazon Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html)  
[How to Migrate WordPress from AWS EC2 to cPanel-based Shared Hosting](http://www.thegurleyman.com/how-to-migrate-wordpress-from-aws-ec2-to-cpanel-based-shared-hosting/)  
[Migrate Self-Hosted Wordpress to EC2](https://forums.aws.amazon.com/thread.jspa?threadID=120283)  
[Migrate Data From One WordPress Instance to Another](https://docs.bitnami.com/aws/how-to/migrate-wordpress/)  
[How to Setup WHM & cPanel on AWS Instances](https://tecadmin.net/setup-whm-cpanel-on-aws/)  
[cPanel-Launch an AWS AMI Instance](https://documentation.cpanel.net/display/CKB/Launch+an+AWS+AMI+Instance#LaunchanAWSAMIInstance-LoginviaSSH.)  
[How to Setup cPanel on AWS](https://hostadvice.com/how-to/how-to-setup-cpanel-on-aws/)  
# Notes
## Usernames
A plain EC2 instance's username is "ec2-user".  
If you use the "cPanel&WHM for Linux" pre-installed instance from the market place, the username is "centos".  
## Setup elastic IP
> 1. Go to the instance page and shoose the instance and click "Elastic IPs" from the left column.  
> 2. Hit "Allocate New Address" button.  
> 3. Click "Allocate".  
> 4. Close.  
> 5. Actions -> Associate.  
> 6. Select instance and private IP, no need to allow reassociate if you don't move it to a new server.  
> 7. Click "Associate" -> Close.  

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
## cPanel
### Installation
#### "cPanel&WHM for Linux" pre-installed instance
> 1. Search it from the market place.  
> 2. Install it as normal.  
> 3. The username is "centos".  
> 4. Connect to the instance through SSH using this username.  
> --------Login to WHM--------
> 5. Use the "sudo su root" and then "passwd" commands to change to a new password.  
> 6. https://publicIP:2087  (If it warns that the link is unsecure, ignor it.)  go to the login page.  
> 7. Login using the username "root" and the new password.  
> --------Login to cPanel--------
> 8. Click "Create a new account" to creat a new cPanel account.  
> 9. Input email, domain name (DNS), usrname, password, etc. You might need a **elastic IP** to make sure the domain name works all the time.
> 10. Go to cPanel.  https://publicIP:2083  
### Login
WHM:  
https://publicIP:2087  (If it warns that the link is unsecure, ignor it.)  
cPanel:  
https://publicIP:2083  (If it warns that the link is unsecure, ignor it.)  
