import tweepy
import unicodecsv
from unidecode import unidecode
import config

# Authentication and connection to Twitter API.
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key, config.access_secret)
api = tweepy.API(auth)

# Load profiles from config
profiles = config.profiles

with open('tweets.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    # Write header row.
    writer.writerow(["profile_name",
                    "profile_username",
                    "profile_followers_count",
                    "profile_listed_count",
                    "profile_following",
                    "profile_favorites",
                    "profile_verified",
                    "profile_default_profile",
                    "profile_location",
                    "profile_time_zone",
                    "profile_statuses_count",
                    "profile_description",
                    "profile_geo_enabled",
                    "profile_contributors_enabled",
                    "tweet_year",
                    "tweet_month",
                    "tweet_day",
                    "tweet_hour",
                    "tweet_link",
                    "tweet_text",
                    "tweet_lat",
                    "tweet_long",
                    "tweet_source",
                    "tweet_in_reply_to_screen_name",
                    "tweet_direct_reply",
                    "tweet_retweet_status",
                    "tweet_retweet_count",
                    "tweet_favorite_count",
                    "tweet_hashtags",
                    "tweet_hashtags_count",
                    "tweet_urls",
                    "tweet_urls_count",
                    "tweet_user_mentions",
                    "tweet_user_mentions_count",
                    "tweet_media_type",
                    "tweet_contributors"
                    ])

    for user in profiles:
        user_obj = api.get_user(user)

        # Gather info specific to the current user.
        user_info = [user_obj.name,
                     user_obj.screen_name,
                     user_obj.followers_count,
                     user_obj.listed_count,
                     user_obj.friends_count,
                     user_obj.favourites_count,
                     user_obj.verified,
                     user_obj.default_profile,
                     user_obj.location,
                     user_obj.time_zone,
                     user_obj.statuses_count,
                     user_obj.description,
                     user_obj.geo_enabled,
                     user_obj.contributors_enabled]

        # Get 2000 most recent tweets for the current user.
        for index, tweet in enumerate(tweepy.Cursor(api.user_timeline, screen_name = user).items(2000)):
            print("Getting tweet {} of 2000........ {}% complete".format(index, round(index/2000 * 100, 1)))
            # Latitude and longitude stored as array of floats within a dictionary.
            lat = tweet.coordinates['coordinates'][1] if tweet.coordinates != None else None
            long = tweet.coordinates['coordinates'][0] if tweet.coordinates != None else None
            # If tweet is not in reply to a screen name, it is not a direct reply.
            direct_reply = True if tweet.in_reply_to_screen_name != "" else False
            # Retweets start with "RT ..."
            retweet_status = True if tweet.text[0:3] == "RT " else False
            tweet_link = "https://twitter.com/user/status/" + tweet.id_str
            # Get info specific to the current tweet of the current user.
            tweet_info = [tweet.created_at.year,
                          tweet.created_at.month,
                          tweet.created_at.day,
                          tweet.created_at.hour,
                          tweet_link,
                          unidecode(tweet.text),
                          lat,
                          long,
                          tweet.source,
                          tweet.in_reply_to_screen_name,
                          direct_reply,
                          retweet_status,
                          tweet.retweet_count,
                          tweet.favorite_count
                          ]

            # Below entities are stored as variable-length dictionaries, if present.
            hashtags = []
            hashtags_data = tweet.entities.get('hashtags', None)
            if(hashtags_data != None):
                for i in range(len(hashtags_data)):
                    hashtags.append(unidecode(hashtags_data[i]['text']))

            urls = []
            urls_data = tweet.entities.get('urls', None)
            if(urls_data != None):
                for i in range(len(urls_data)):
                    urls.append(unidecode(urls_data[i]['url']))

            user_mentions = []
            user_mentions_data = tweet.entities.get('user_mentions', None)
            if(user_mentions_data != None):
                for i in range(len(user_mentions_data)):
                    user_mentions.append(unidecode(user_mentions_data[i]['screen_name']))

            media = []
            media_data = tweet.entities.get('media', None)
            if(media_data != None):
                for i in range(len(media_data)):
                    media.append(unidecode(media_data[i]['type']))

            contributors = []
            if(tweet.contributors != None):
                for contributor in tweet.contributors:
                    contributors.append(unidecode(contributor['screen_name']))

            more_tweet_info = [', '.join(hashtags),
                               len(hashtags),
                               ', '.join(urls),
                               len(urls),
                               ', '.join(user_mentions),
                               len(user_mentions),
                               ', '.join(media),
                               ', '.join(contributors)]

            # Write data to CSV.
            writer.writerow(user_info + tweet_info + more_tweet_info)

        # Show progress.
        print("###############################################")
        print("Wrote tweets by {} to CSV file.".format(user))
        print("###############################################")