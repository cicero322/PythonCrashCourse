from operator import itemgetter

import requests

import plotly.express as px


# Make an API call and check the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []

try:
    for submission_id in submission_ids[:30]:
        # Make a new API call for each submission.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        response_dict = r.json()
        
        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'] if 'descendants' in response_dict else 0,
        }
        submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

except KeyError as e:
    print(f"KeyError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Prepare data for visualization
submission_links = [f"<a href='{submission['hn_link']}'>{submission['title']}</a>" for submission in submission_dicts[:30]]
comments = sorted([submission['comments']  for submission in submission_dicts], reverse=True)


# Make visualization
labels = {
    'x':  "",
    'y': 'Number of Comments',
}
fig = px.bar(x=submission_links, y=comments,labels=labels )
fig.update_layout(title="Most-Discussed Articles on Hacker News")
fig.show()