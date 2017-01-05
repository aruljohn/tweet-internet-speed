import subprocess
import tweepy
import requests

#
# Python script to tweet your Internet speed
# Arul John { http://aruljohn.com }
#

def main():
  # Find IP address and remove the last 2 octets
  ip = None
  r = requests.get('https://api.aruljohn.com/ip')
  if r.status_code == requests.codes.ok:
    ip = r.text
    if ip != None:
      ip =  '.'.join(ip.split('.')[:2]) + '.xx.xx'

  # Get the Internet speed by calling speedtest-cli
  speed = subprocess.check_output(["python", "/usr/local/bin/speedtest.py", "--simple"])
  speed = "My #InternetSpeed :\n" + speed
  if ip != None:
    speed += "IP address: " + ip

  # Twitter consumer key, secret, access token and secret
  consumer_key = ''
  consumer_secret = ''
  access_token = ''
  access_token_secret = ''
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)

  # Set status on Twitter
  status = api.update_status(status=speed)

  # Display information for logging
  print speed

if __name__ == "__main__":
  main()
