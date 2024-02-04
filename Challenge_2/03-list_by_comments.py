import requests

def fetch_top_stories_by_comments(limit=30):
    # Fetch top story IDs from the Hacker News API
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    story_ids = response.json()

    top_stories = []
    for story_id in story_ids[:limit]:
        # Fetch each story's details
        story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty')
        story = story_response.json()
        top_stories.append({
            'title': story.get('title'),
            'comments': story.get('descendants', 0)  # 'descendants' represents the number of comments
        })

    # Sort all stories based on the number of comments
    top_stories.sort(key=lambda x: x['comments'], reverse=True)

    return top_stories[:20]  # Return the top 20 stories by comments

# Print the top 20 stories sorted by comments out of the top 30
for index, story in enumerate(fetch_top_stories_by_comments(), start=1):
    print(f"{index}: {story['title']} (Comments: {story['comments']})")
