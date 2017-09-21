#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:38:38 2017

@author: hemanthrahulmarukala
"""

import media 
import fresh_tomatoes

#-Objects created to show different movies
toy_story= media.Movie("ToyStory", "All toys come to life", "https://images-production.global.ssl.fastly.net/uploads/posts/image/46533/toy-story-hotel.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar= media.Movie("Avatar", "A soldier on alien planet", "http://pzrservices.typepad.com/.a/6a00d83451ccbc69e2012875ec78a9970c-400wi", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
bahubali= media.Movie("Bahubali", "Lost prince comes back", "http://cdn1.chitramala.in/wp-content/gallery/bahubali-movie-latest-posters/Baahubali-50-Days-Poster.jpg", "https://www.youtube.com/watch?v=sOEg_YZQsTI")
bahubali2= media.Movie("Bahubali 2", "Lost Price flashback", "http://data1.ibtimes.co.in/cache-img-900-0-photo/en/full/51351/1477284514_bahubali-aka-baahubali-2-first-look-poster-revealed.jpg","https://www.youtube.com/watch?v=G62HrubdD6o")
dirtygrandpa= media.Movie("Dirty Grandpa", "Grandpa and grand son roadtrip","http://t1.gstatic.com/images?q=tbn:ANd9GcTQe092LcZsV0CUMXnJNfrJici3o9aH_40nAVIVvxPMs6gKpuAa", "https://www.youtube.com/watch?v=aZSzMIFZT7Q")
wizard_of_lies= media.Movie("Wizard of lies", "A chronicle of Bernie Madoff's Ponzi scheme, which defrauded his clients of billions of dollars.","http://www.gstatic.com/tv/thumb/movieposters/13777342/p13777342_p_v8_aa.jpg","https://www.youtube.com/watch?v=05HK-z6HoHM")

#Array to store class movies objects 
movie_objects = [toy_story, avatar, bahubali, bahubali2, dirtygrandpa, wizard_of_lies]
#function to show the objects in a HTML page
fresh_tomatoes.open_movies_page(movie_objects)
