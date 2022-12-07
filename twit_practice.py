import time
import tweepy

access_token="1589823832117940225-kH4TfiSzwPenEfK6T6Pe3N0ilpj2OH"
access_token_secret="Swvy5If0ZmRRGF4mC5h8HbWNwTgjq33acZEtDXwkFgZp0"
API_key="Df5mq3K87RHbYYWNY6Fph5zwL"
API_secret_key="PQTkA3rE4ZAjHu2N8J2hKzUunaJABMTpkYnjFNE7N5E5cID01K"

auth = tweepy.OAuthHandler(API_key,API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.get_user(userid='apoorv__tyagi')
