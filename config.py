import tweepy
import os
import logging

from dotenv import load_dotenv

logger = logging.getLogger()


def create_api():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    API_SECRET_KEY = os.getenv("API_SECRET_KEY")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API")
        raise e

    return api
