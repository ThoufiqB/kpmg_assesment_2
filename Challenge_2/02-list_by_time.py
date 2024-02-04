import requests

def fetch_top_stories_by_time(limit=30):
    # Fetch top story IDs from the Hacker News API sorted by time
    response = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty&orderBy="$key"&limitToFirst=30')
    story_ids = response.json()

    top_stories = []
    for story_id in story_ids[:limit]:
        # Fetch each story's details
        story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty')
        story = story_response.json()
        top_stories.append({
            'title': story.get('title'),
            'time': story.get('time')
        })

    # Sort all stories based on time
    top_stories.sort(key=lambda x: x['time'])

    return top_stories[:20]  # Return the top 20 stories by time

# Print the top 20 stories sorted by time out of the top 30
for index, story in enumerate(fetch_top_stories_by_time(), start=1):
    print(f"{index}: {story['title']} (Time: {story['time']})")
