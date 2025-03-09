import requests
import plotly.express as px

#17.2

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict['items']
repo_names,repo_links, stars = [], [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    repo_link = f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>"
    repo_links.append(repo_link)

# Make visualization.
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x= repo_links, y= stars, labels=labels)
fig.update_layout(title="Most-Starred JavaScript Projects on GitHub")
fig.update_xaxes(tickangle=45)
fig.update_yaxes(title="Stars")
fig.show()