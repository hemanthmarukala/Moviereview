#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:38:38 2017
@author: hemanthrahulmarukala
"""
import media
import fresh_tomatoes
toy_story = media.Movie("ToyStory", "Toys", "https://tinyurl.com/ybwq7sfo", "hhttps://tinyurl.com/y79gg5n3")
avatar = media.Movie("Avatar", "S", "https://tinyurl.com/y8x4tzd7", "https://tinyurl.com/kqfs54e")
bahubali = media.Movie("Bahubali", "prince", "https://tinyurl.com/ycjetn3b", "https://tinyurl.com/npw9zkz")
bahubali_2 = media.Movie("Bahubali2", "flashback", "https://tinyurl.com/ycar6arj", "https://tinyurl.com/hkkfaef")
dirty_grandpa = media.Movie("Dirty Grandpa", "Roadtrip", "https://tinyurl.com/yc9or6lc", "https://tinyurl.com/qyn46p4")
wizard_of_lies = media.Movie("Wizard of lies", "A chronicle of Bernie.", "https://tinyurl.com/ycsgouej", "https://tinyurl.com/yd2z4uee")
# Array to store class movies objects
movie_objects = [toy_story, avatar, bahubali, bahubali_2, dirty_grandpa, wizard_of_lies]
# function to show the objects in a HTML page
fresh_tomatoes.open_movies_page(movie_objects)
