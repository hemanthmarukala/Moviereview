#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:38:38 2017
@author: hemanthrahulmarukala
"""
import media
import fresh_tomatoes
toy_story = media.Movie(
"Toy Story",
"Toys",
"https://tinyurl.com/ybwq7sfo",  # NOQA
"https://www.youtube.com/watch?v=KYz2wyBy3kc&t=34s"
)
avatar = media.Movie(
"Avatar",
"S",
"https://tinyurl.com/y8x4tzd7",  # NOQA
"https://www.youtube.com/watch?v=5PSNL1qE6VY"
)
bahubali = media.Movie(
"Bahubali",
"prince story",
"https://tinyurl.com/ycjetn3b",  # NOQA
"https://www.youtube.com/watch?v=G62HrubdD6o&t=2s"
)
bahubali_2 = media.Movie(
"Bahubali2",
"flashback story of the king",
"https://tinyurl.com/ycar6arj",  # NOQA
"https://www.youtube.com/watch?v=G62HrubdD6o&t=2s"
)
dirty_grandpa = media.Movie(
"Dirty Grandpa",
"Roadtrip",
"https://tinyurl.com/yc9or6lc",  # NOQA
"https://www.youtube.com/watch?v=aZSzMIFZT7Q"
)
wizard_of_lies = media.Movie(
"Wizard of lies",
"A chronicle of Bernie.",
"https://tinyurl.com/ycsgouej",  # NOQA
"https://www.youtube.com/watch?v=05HK-z6HoHM&t=1s"
)

# Array to store class movies objects
movie_objects = [
    toy_story,
    avatar,
    bahubali,
    bahubali_2,
    dirty_grandpa,
    wizard_of_lies]

# function to show the objects in a HTML page
fresh_tomatoes.open_movies_page(movie_objects)
