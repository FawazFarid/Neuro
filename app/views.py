# -*- coding: utf-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup


class Lyricsviews(object):
    def __init__(self):
        self.headers = {
            'Authorization': 'Bearer I01LPneQJjxNd9qsMdOukM2Z64MzuUekMRnuxubPGWvpL90WncPVl0uOYMBpXDny'
        }

    def find(self, search_criteria):
        # replace whitespaces with utf-8 v
        query = urllib.quote(str(search_criteria))
        search_url = 'http://api.genius.com/search?q=' + query
        r = requests.get(search_url, headers=self.headers)

        data = r.json()

        print len(data['response']['hits'])

    def view(self, song_id):
        # check if there is local copy in database

        song_url = 'http://api.genius.com/songs/' + str(song_id)

        r = requests.get(song_url, headers=self.headers)

        data = r.json()

        lyrics_url = data['response']['song']['url']
        response = requests.get(lyrics_url)

        soup = BeautifulSoup(response.text, "html.parser")
        lyrics = soup.find("lyrics", class_="lyrics").text.encode('utf-8')
        print lyrics


song = Lyricsviews()
song.view(378195)
