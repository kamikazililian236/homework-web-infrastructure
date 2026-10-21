import requests

SUBREDDIT = "python"
HEADERS = {"User-Agent": "python:class-assignment:v1.0 (by /u/lilian)"}
BASE = f"https://www.reddit.com/r/{SUBREDDIT}"


# A small helper so we don't repeat ourselves
def get_json(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Error:", response.status_code, "for", url)
        return None
    return response.json()


# 1. About: name, subscribers, description
about = get_json(f"{BASE}/about.json")
if about:
    info = about["data"]
    print("Subreddit name:", info["display_name"])
    print("Number of subs:", info["subscribers"])
    print("Description:", info["public_description"])

# 2. The 10 newest posts
new = get_json(f"{BASE}/new.json?limit=10")
if new:
    print("\n10 newest posts:")
    count = 1
    for post in new["data"]["children"]:
        print(count, "-", post["data"]["title"])
        count = count + 1

# 3. Rules
rules = get_json(f"{BASE}/about/rules.json")
if rules:
    print("\nRules:")
    count = 1
    for rule in rules["rules"]:
        print(count, "-", rule["short_name"])
        count = count + 1