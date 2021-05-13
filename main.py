import tweepy
import time

from config import create_api
from secret_languages import translate_text, LANGUAGES


def check_mentions(api, since_id):
    print("check mentions")
    user = api.me()

    new_since_id = since_id
    mentions = api.mentions_timeline(since_id=since_id, tweet_mode="extended")

    for tweet in mentions:
        new_since_id = max(tweet.id, new_since_id)

        replies = tweepy.Cursor(
            api.search,
            q=f"to:{tweet.user.screen_name} from:{user.screen_name}",
            result_type="recent",
            timeout=999999,
        ).items(1000)

        for reply in replies:
            if (
                hasattr(reply, "in_reply_to_status_id")
                and reply.in_reply_to_status_id == tweet.id
            ):
                return new_since_id

        print(f"{tweet.user.name} says {tweet.full_text}")

        if not tweet.favorited:
            tweet.favorite()

        language = "piglatin"
        for hashtag in tweet.entities["hashtags"]:
            if hashtag in LANGUAGES:
                language = hashtag
                break

        response = translate_text(tweet.full_text, language=language)

        if f"#{language}" not in response:
            response += f" #{language}"

        response = response.replace(
            f"@{user.screen_name}", f"@{tweet.user.screen_name}"
        )

        api.update_status(
            status=response,
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True,
        )
    if not len(mentions):
        print("no mentions :-(")

    return new_since_id


def main():
    api = create_api()
    user = api.me()

    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        time.sleep(5)


if __name__ == "__main__":
    main()
