# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
from bs4 import BeautifulSoup
import time


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    jsonFile = 'movies.json'
    # htmlFile = '1.html'
    # f = open(htmlFile)
    # htmlText = f.read()

    BASE_URL = 'https://www.imdb.com/search/title/?year=2021&title_type=feature&'  # must use https

    for i in range(6):

        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        # soup = BeautifulSoup(htmlText, 'html.parser')

        parent = soup.find('div', class_="lister-list")
        print(parent)
        rows = parent.find_all('div', recursive=False)
        for row in rows:
            # Info in header
            header = row.find('h3', class_="lister-item-header")
            num = header.find('span', class_='lister-item-index unbold text-primary')
            name = header.find('a')

            # Info in text-muted
            try:
                runtime = row.find('span', class_='runtime')
                runtime = runtime.text
                genreInfo = row.find('span', class_='genre')
                genreInfo = genreInfo.text
                genreInfo = genreInfo.strip()
                genreInfo = genreInfo.strip('\n')
                genreInfo = genreInfo.split()
            except:
                runtime = 'No runtime so far'
                genreInfo = 'No runtime so far'

            try:
                certificate = row.find('span', class_='certificate')
                certificate = certificate.text
            except:
                certificate = 'No certificate so far'

            # Info in rating
            try:
                # ratingBar = row.find('div', class_="inline-block ratings-imdb-rating")
                ratingBar = row.find('strong')
                rating = float(ratingBar.text)

                # rating = ratingBar['data-value']
            except:
                rating = "No rating so far"

            # Info in votes
            try:
                votesTag = row.find('p', class_='sort-num_votes-visible')
                votes = votesTag.find_all('span')
                count = 1
                for vote in votes:
                    if count == 2:
                        vote = int(vote['data-value'])
                        print(vote)
                        break
                    count += 1
            except:
                vote = 'No votes so far'

            # Info in Director and Star
            starClass = row.find('p', class_="")
            starTags = starClass.find_all('a', recursive=False)
            director = []
            star = []
            count = 1
            for a in starTags:
                if count == 1:
                    director.append(a.text)
                else:
                    star.append(a.text)
                count += 1

            movieInfo = {
                'number': num.text,
                'name': name.text,
                'runtime': runtime,
                'genre': genreInfo,
                'certificate': certificate,
                'rating': rating,
                'votes': vote,
                'director': director,
                'star': star
            }
            # print(movieInfo)
            with open(jsonFile, 'a') as file:
                json.dump(movieInfo, file, indent=2)
                file.write(',\n')

        linkTag = soup.find('div', class_="desc")
        link = linkTag.find('a', class_="lister-page-next next-page")
        href = link['href']
        BASE_URL = 'https://www.imdb.com' + href
        time.sleep(16)



