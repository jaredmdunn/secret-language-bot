import tweepy
import logging
import time

from config import create_api

logger = logging.getLogger()


def check_mentions(api, since_id):
    print("check mentions")
    new_since_id = since_id

    mentions = api.mentions_timeline(since_id=since_id)

    for tweet in mentions:
        new_since_id = max(tweet.id, new_since_id)
        print(f"{tweet.user.name} says {tweet.text}")

    if not len(mentions):
        print("no mentions :-(")

    return new_since_id


def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(5)


if __name__ == "__main__":
    main()
