#This code is a Python script that fetches the top stories from the Hacker News website using their API and then prints out the titles of those stories

#Imports the requests library, enabling HTTP requests to be made in the script.
import requests


#Defining a function with an optional parameter limit set to 20 by default. This function will fetch the top stories from Hacker News.
def fetch_top_stories(limit=20):
    # Fetch top story IDs from the Hacker News API
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    story_ids = response.json()                 #Parses JSON Content, Converting story ID's to python list       
    

    #Initializes an empty list top_stories, which will later contain the titles of the top stories.
    top_stories = []
    for story_id in story_ids[:limit]:

        # Fetch each story's details
        story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty')
        story = story_response.json()           #Parses the JSON content of the story's details 'response', converting it into a Python dictionary.
        top_stories.append(story.get('title'))  #append the extracted title from Story dictionary.

    return top_stories

# Print the top 20 stories
for index, story in enumerate(fetch_top_stories(), start=1):
    print(f"{index}: {story}")