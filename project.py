import tweepy
from time import sleep   #allowed 2400 per day. Intervals of 50 tweets every 30 mins

# Consumer keys and access tokens, used for OAuth
c_key = '0J8a5eA78o5XSHQaA0CcNKIQ7' #consumer key
c_secret = 'ab7KuPzY3QuIV0dRuufHznLpFXZCunUwoSlIQjoYyBH31peuBH' #consumer secret
a_token = '49130071-1kRvEgnRscgug8Y7IymiiTfcpsgnMQWux01croAS6'  #access token
a_token_secret = 'LW4dS5sMv5uzCe3fJC86dXuQE9npmQT08CPgZe8QwUEyr' #access token secret

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(c_key, c_secret) #Authorize to know which account you want to access.
auth.set_access_token(a_token, a_token_secret) #
auth.secure = True

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#print(str(api.get_user(screen_name = '@PyTweetAnalysis')))
file = open("tweetfile.txt", 'w', encoding='utf8')
tweets = api.user_timeline(screen_name="realdonaldtrump", count=3000, include_rts = False)
i = 1
for tweet in tweets:

    stri = str(tweet.text)
    file.write(str(i) + ")  ")
    file.write(stri)
    file.write('\n'+'\n')
    i = i + 1

    '''print(tweet.text)




