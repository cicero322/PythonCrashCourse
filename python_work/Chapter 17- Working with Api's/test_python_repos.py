# Make an API call and check the response.
import requests

#17.3

url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}

def test_status_code():
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    assert r.status_code == 200
