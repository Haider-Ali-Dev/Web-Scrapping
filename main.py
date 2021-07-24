from bs4 import BeautifulSoup # We are gonna use BeautifulSoup for Webscrapping.
import requests # We are gonna use requests to use access HTML data.
import pprint # Optional. Im using it cuz it prints in better way.


res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

news_title = soup.select('.storylink')
votes = soup.select('.score')

em = []

for index, item in enumerate(news_title):
    try:
        href = item.get('href')
        vote = int(votes[index].getText().replace(' points', ''))

        if vote:
            my_news = {
                'title' : item.getText(),
                'link' : href,
                'votes' : vote
            }
            em.append(my_news)
        else:
            continue
    except IndexError:
        continue
        

    

pprint.pprint(em)