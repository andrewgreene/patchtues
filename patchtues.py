import urllib
import os.path
import tweepy

def get_api(tweetconfig):
    auth = tweepy.OAuthHandler(tweetconfig['consumer_key'], tweetconfig['consumer_secret'])
    auth.set_access_token(tweetconfig['access_token'], tweetconfig['access_token_secret'])
    return tweepy.API(auth)

tweetconfig = {
        "consumer_key": "N/A",
        "consumer_secret": "N/A",
        "access_token": "N/A",
        "access_token_secret": "N/A"
        }

mbsasave = os.path.exists('patchtues.txt')

if mbsasave == False:
    file = open('patchtues.txt', 'w')
    file.close()

mbsacab = urllib.urlopen("http://go.microsoft.com/fwlink/?linkid=74689")
newfilesize =  mbsacab.info()['Content-Length']

existingfilesize = open('patchtues.txt', 'r').read()

if existingfilesize != 0 and newfilesize != existingfilesize:
    writenewsize = open('patchtues.txt', 'w')
    writenewsize.write("%s" % newfilesize)
    writenewsize.close()
    api = get_api(tweetconfig)
    tweet = "The WSUS MBSA Scanner CAB file has been updated. The new size is %s bytes. #microsoft #patchtuesday" % newfilesize
    status = api.update_status(status=tweet)
