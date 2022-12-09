from urllib.request import urlopen, urlretrieve
from json import load
import os
from subprocess import run

try:
	with urlopen("https://api.github.com/users/revanced/repos") as contents:
		json = load(contents)
except Exception as e:
	print(e.reason)

for repo in json:
	filename = f"{repo['name']}.zip"
	valid_repos = [
		"revanced-cli",
		"revanced-patcher",
		"revanced-patches",
		"revanced-integrations",
		"revanced-manager"
	]

	if repo["name"] not in valid_repos:
		continue

	if(os.path.exists(filename)):
		os.remove(filename)
		print(f"Deleted {filename}")

	urlretrieve(f"{repo['html_url']}/archive/{repo['default_branch']}.zip", filename)
	print(f"Downloaded {repo['full_name']}")
