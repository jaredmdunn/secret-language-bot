import tweepy
import logging

from config import create_api

logger = logging.getLogger()


def main():
    api = create_api()
    print("run main")


if __name__ == "__main__":
    main()
