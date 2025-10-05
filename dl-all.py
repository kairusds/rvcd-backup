from urllib.request import urlopen, urlretrieve
from json import load
import os
from datetime import datetime, timezone

try:
	with urlopen("https://api.github.com/orgs/revanced/repos") as contents:
		json = load(contents)
except Exception as e:
	print(e.reason)

for repo in json:
	updated_at = datetime.fromisoformat(repo["updated_at"].replace('Z', '+00:00')).strftime("%Y%m%d_%H%M%S_UTC")
	filename = f"{repo['name']}_{updated_at}.zip"
	valid_repos = [
		"revanced-cli",
		"revanced-patches",
		"revanced-manager"
	]

	if repo["name"] not in valid_repos:
		continue

	if(os.path.exists(filename)):
		os.remove(filename)
		print(f"Deleted {filename}")

	urlretrieve(f"{repo['html_url']}/archive/{repo['default_branch']}.zip", filename)
	print(f"Downloaded {repo['full_name']}")
