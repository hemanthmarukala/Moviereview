#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:45:02 2017

@author: hemanthrahulmarukala
"""
import webbrowser
"""
-Movie class to assign the instance variables for the objects that will be included in the entertainment_center.py
-show_trailer function to how the youtube video of the movie trailer. 
"""
class Movie():
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = movie_poster
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        