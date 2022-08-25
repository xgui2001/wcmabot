import time
import tweepy
import helper

wcma_url = 'https://artmuseum.williams.edu/collection/'
wcma_hashtag = '#WilliamsCollegeMuseumOfArt'


# get api credentials from twitterkeys
def get_api():
    all_keys = open('twitterkeys', 'r').read().splitlines()
    api_key = all_keys[0]
    api_key_secret = all_keys[1]
    bearer_token = all_keys[2]
    access_token = all_keys[3]
    access_token_secret = all_keys[4]

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit=True)


# create a tweet that has an image
def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)
    return 0


# verify api authentication and tweet out object every 10 minutes
if __name__ == "__main__":
    api = get_api()
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    while True:
        tweet(api, helper.generate_object() +
              ' ' + wcma_hashtag + ' ' + wcma_url)
        time.sleep(600)
