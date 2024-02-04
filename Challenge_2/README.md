Programmatically list out the top 20 articles from the Hacker News homepage (https://news.ycombinator.com).
----------------------------------------------------------------------------------------------------------------------------------
Using the Hacker news API Documentation: https://github.com/HackerNews/API

# Code explaination:

import requests: 
    Imports the requests library, enabling HTTP requests to be made in the script.

# #Please note: Multiple functions has been created to list based on Story ID, Time, Comments. ##
## List by Story ID##
def fetch_top_stories(limit=20)::
     Defines a function fetch_top_stories with an optional parameter limit set to 20 by default. This function will fetch the top stories from Hacker News.

## List by time##
def fetch_top_stories_by_time(limit=30):


## List by comments##
def fetch_top_stories_by_comments(limit=30):
 

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'): 
    Makes an HTTP GET request to the Hacker News API endpoint that lists the top story IDs. The response is stored in the variable response.

story_ids = response.json():
     Parses the JSON content from the response, converting it into a Python list of story IDs, and stores this list in story_ids.

top_stories = []: 
    Initializes an empty list top_stories, which will later contain the titles of the top stories.

for story_id in story_ids[:limit]:: 
    Begins a loop over the first limit number of story IDs in story_ids.

story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty'): 
    For each story_id, makes an HTTP GET request to fetch the story's details from the API.

story = story_response.json(): 
    Parses the JSON content of the story's details response, converting it into a Python dictionary.

top_stories.append(story.get('title')): 
    Extracts the title from the story dictionary using .get('title') (which safely returns None if title is not a key in the dictionary) and appends it to the top_stories list.

for index, story in enumerate(fetch_top_stories(), start=1):: 
    After defining and calling fetch_top_stories(), this line iterates over each title in the returned list of top stories. enumerate is used to get both the index (starting from 1) and the story title for printing.

print(f"{index}: {story}"): 
    Prints each story's index and title, formatting them in a readable format.