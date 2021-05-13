import tweepy
import os

from dotenv import load_dotenv


def create_api():
    print("creating api")
    print("loading dotenv")
    load_dotenv()
    print("after load")
    API_KEY = os.getenv("API_KEY")
    API_SECRET_KEY = os.getenv("API_SECRET_KEY")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
    print("api key: ", API_KEY)

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        raise e

    return api
