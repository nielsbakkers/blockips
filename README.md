# BlockIps ![Release](https://badgen.net/github/release/nielsbakkers/blockips) ![Contributors](https://badgen.net/github/contributors/nielsbakkers/blockips)

> This is a script that blocks ip-addresses when they make a request with a bad search such as wp-admin.php or bingbot. The script also checks if they visit the website more then ten times within that day. The script is made with Python.

## Casus
 
I started this project because I wanted to learn more about Python scripting and the use of reading and changing files. I also wanted to make a script that blocks people that are scraping the website for bad use.

## Libraries

This project uses two Python libraries that are standardly installed:
* [subprocess](https://docs.python.org/3/library/subprocess.html)
* [datetime](https://docs.python.org/3/library/datetime.html)

## Usage

In order to use the blockips script you need to follow the next steps.

### 1. git clone

The first step is to clone the git repository where the script is located. Run the following command: `git clone https://github.com/nielsbakkers/blockips.git`.

### 2. move the script

The second step is to move the Python script to the home directory. Use the following command: `mv blockips.py /home/{username}`.

### 3. make conf file

The next step is to make a config file where the blocked ip addresses will be listed. Use the following command to make the file at the desired location:
`mkdir /etc/nginx/blockips.conf`.

### 4. include the config file

Next include the config file we just made into the nginx configuration. Edit the file located at `/etc/nginx/nginx.conf`.

Place the following line of code somewhere in the nginx configuration file: `include blockips.conf`.

### 5. restart nginx

After changing the nginx config it is recommended to restart the nginx service so the blockips file will be included.

Command: `service nginx restart`

### 6. automatically run the script

The final step is to run the script that bans ip addresses automaticcaly. We will use Crontab to run the script every 2 minutes.

Open the Crontab editor by executing `crontab -e`. Insert `*/2 * * * * /home/{username}/blockips.py 2>&1` at the end of the file and save.

<strong>NOTE:</strong> Don't forget to change the {username} tag with your own username!

## Tested on Python versions

Python 2.7.17
Python 3.6.9

## Contact

Created by [@nbakkers](https://nbakkers.nl) - Feel free to contact me!


