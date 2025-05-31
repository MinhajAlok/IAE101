# mytwitterbot.py
# IAE 101, Fall 2024
# Project 04 - Building a Twitterbot
# Name: Minhaj Alok
# netid: malok
# Student ID: 114868408

import sys
import time, random
import simple_twit

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# API Key, also known as Consumer Key
API_KEY = "73bhKtdDcWRplCnM0FRD7TYif"

# API Key Secret, also known as Consumer Secret
API_KEY_SECRET = "vUMYiTh7rBy1JS4vWOuXD1WxWrsaYiL3fJOBN58XzvC7rhFOe4"

# Project 04 Exercises
    
# Exercise 1 - Get and print 3 tweets from your home timeline
# For each tweet, print:
#   the tweet ID,
#   the author ID, 
#   the tweet creation date, and
#   the tweet text
def exercise1(client):
    print("<--------------Excersise 1--------------->")
    num = 3 # Number of tweets to get
    response = simple_twit.get_home_timeline(client, num)
    for i in range(num):
        print("Tweet #", i+1)
        print("Tweet ID:", response.data[i].id)
        print("Author ID:", response.data[i].author_id)
        print("Creation Date:", response.data[i].created_at)
        print("Text:", response.data[i].text)
        print()

# Exercise 2 - Get and print 3 tweets from another user
# For each tweet, print:
#   the tweet ID,
#   the author ID,
#   the tweet creation date, and
#   the tweet text
def exercise2(client):
    print("<--------------Excersise 2--------------->")
    username = "elonmusk"
    num = 3
    response = simple_twit.get_users_tweets(client, username, 5)
    for i in range(num):
        print("Tweet #", i+1)
        print("Tweet ID:", response.data[i].id)
        print("Author ID:", response.data[i].author_id)
        print("Creation Date:", response.data[i].created_at)
        print("Text:", response.data[i].text)
        print()

# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(client):
    print("<--------------Excersise 3--------------->")
    tweet = "testing"
    response = simple_twit.send_tweet(client, tweet)
    print("Tweet posted successfully.")



# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(client):
    print("<--------------Excersise 4--------------->")
    tweet = "testing media"
    media = "phreddit.png"
    response = simple_twit.send_media_tweet(client, tweet, media)
    print("Media Tweet posted successfully.")

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
def twitterbot(client):
    print("<--------------Twitter Bot--------------->")
    user = "IAE101_ckane"
    response = simple_twit.get_users_tweets(client, user, 5)
    tweets = response.data
    tweet = tweets[0].text
    print(tweet)
    response = simple_twit.send_tweet(client, tweet[::-1])
    print("Reversed tweet posted successfully.")




if __name__ == "__main__":
    # This call to simple_twit.create_client will create the Tweepy Client 
    # object that Tweepy needs in order to make authenticated requests to 
    # Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "client" holding this Tweepy Client object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    print()
    
    try:
        client = simple_twit.create_client(API_KEY, API_KEY_SECRET)
    except Exception as e:
        print("ERROR:", e)
    
    print(client)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
    exercise1(client)
    exercise2(client)
    exercise3(client)
    exercise4(client)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(client)
