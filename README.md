# Pixelfed Profile Image Downloader

Download all images from a pixelfed profile.

## Setup


Install `git` and `virtualenv`

```
sudo apt-get install git virtualenv
```

Clone the repository.

```
git clone git@github.com:AmmanVMS/pixelfed-account-image-download.git
```

Setup the repository Python environment

```
virtualenv -p python3 ENV
source ENV/bin/activate
pip install -r requirements.txt
```

Edit the parameters in `schedule.sh`

Schedule the update:

```
crontab -e
```

Add this for updating each minute:

```
* * * * * /home/pi/pixelfed-account-image-download/schedule.sh
```

## Access Token

![image](https://user-images.githubusercontent.com/564768/214557602-504e0afa-a8d0-4cb2-9d05-56296012145c.png)

You will to retrieve an API token and put it into `secret.txt` from
[pix.toot.wales/settings/applications](https://pix.toot.wales/settings/applications) or
any other server as such.

## Usage

```
python3 download.py /path/to/images/folder https://pixelfed.server username@instance secret.txt 2000-01-01
```

