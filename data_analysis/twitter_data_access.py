import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = '2NbcgFV9O0xet7R0xFbhOeT3S'
consumer_secret = '6BFL9WLHibbMiXrblnKcoV3J0b0tly47m66PNpCNOd1SbpH2yr'
access_token = '5736532-eAGwOSUyIPAOQSUvTQbarw4GurSaAtD1SiTzPa8hBA'
access_token_secret = '7Rm3wQVe9HpRRuggLtLdkg6NdwZJH9qPAGJQYazrBDFJw'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')

    def on_error(self, status_code):
        print ("Error Code: {}".format(status_code))
        return True

    def on_timeout(self):
        print('Timed out')
        return True

def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)

if __name__ == '__main__':
    #print_to_terminal()
    pull_down_tweets(auth.username)