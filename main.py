import requests
from bs4 import BeautifulSoup

language = 'python' # 'all' for all languages
searchPhrase = "Fortnite Bot"

def grabUrls():
    urls = []
    for i in range(1, 10):
        url = f'github.com/search?p={i}&q={searchPhrase}&type=Repositories&ref=advsearch&l={language}&o=desc&s=stars'
        urls.append(url)
    return urls

def scrape(url):
    r = requests.get(f'https://{url}')
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def getRepos(soup):
    repos = soup.find_all('div', {'class': 'f4 text-normal'})
    return repos

def getStars(soup):
    stars = soup.find_all('a', {'class': 'Link--muted'})
    return stars

def getLang(soup):
    lang = soup.find_all('span', {'itemprop': 'programmingLanguage'})
    return lang

def main():
    urls = grabUrls()
    for url in urls:
        soup = scrape(url)
        repos = getRepos(soup)
        stars = getStars(soup)
        lang = getLang(soup)
        for i in range(len(repos)):
            print("Found a repo with " + stars[i].text.strip() + " stars")
            print("Repo: " + repos[i].text.strip())
            print("Language: " + lang[i].text.strip())
            print("")
            with open('repos.txt', 'a') as f:
                format = f"{'https://github.com/' + repos[i].text.strip() }"
                f.write(format + '\n')

if __name__ == '__main__':
    main()
