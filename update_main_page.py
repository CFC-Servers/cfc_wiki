import requests
from bs4 import BeautifulSoup

wiki_home = 'cfc_wiki.wiki/Home.md'

header = '# Welcome to the CFC Wiki!\n\n'

projects_header = '## Projects\n'

github_base = 'https://github.com'

request = requests.get("https://github.com/CFC-Servers")
if request.status_code != 200:
    print("Failed to reach CFC-Servers github page!")
    exit()

soup = BeautifulSoup(request.text)

repos = []

for item in soup.find_all('a', {'itemprop': 'name codeRepository'}):
    repo_name = item.text.strip()
    if repo_name == 'cfc_wiki' or not repo_name.startswith('cfc_'):
        continue

    link = '{}{}'.format(github_base, item['href'] + '/wiki')

    repoStr = '[{}]({})'.format(repo_name, link)

    print("Appending {}...".format(repo_name))

    repos.append('* ' + repoStr + '\n')

repos.sort()

outfile = open(wiki_home, 'w')
outfile.write(header)
outfile.write(projects_header)
for repo in repos:
    outfile.write(repo)

outfile.close()
