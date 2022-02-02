import requests
import json
from bs4 import BeautifulSoup


def scrape_jokes():
    res = dict()
    res['with_author'], res['without_author'] = list(), list()
    url = "https://inews.co.uk/light-relief/jokes/funny-jokes-110-funniest-best-one-liners-192413"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    cont = soup.find("div", {"class": "article-content"})

    p_tags = cont.findAll('p')[1:]
    p_list = [p.get_text().replace('“', '').replace('”', '').replace("'", "") for p in p_tags]
    for idx, p in enumerate(p_list):
        try:
            quote, author = p.rsplit('–', 1)
            res['with_author'].append(quote.strip() + '\n— ' + author.strip())
            if idx == 53:  # hard-coded for this specific page
                p_list = p_list[54:]
                break
        except Exception:
          pass

    for idx, p in enumerate(p_list):
        if p == ' ' or p == "" or p[0].isdigit() or p.startswith('More') or p.startswith('Read'):
            continue
        res['without_author'].append(p.strip())
        if p.startswith('My girlfriend '):  # hard-coded for this specific page
            break
    with open('jokes.json', 'w') as outfile:
        json.dump(res, outfile)


if __name__ == '__main__':
    scrape_jokes()