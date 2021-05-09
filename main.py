import tweepy
import time

from config import create_api


def check_mentions(api, since_id):
    print("check mentions")
    new_since_id = since_id

    mentions = api.mentions_timeline(since_id=since_id)

    for tweet in mentions:
        new_since_id = max(tweet.id, new_since_id)
        print(f"{tweet.user.name} says {tweet.text}")

        if not tweet.user.following:
            tweet.user.follow()

        api.update_status(
            status=f"Thanks for reaching out. We are not functional yet.",
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True,
        )
    if not len(mentions):
        print("no mentions :-(")

    return new_since_id


def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        time.sleep(5)


if __name__ == "__main__":
    main()
