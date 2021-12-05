#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:47:26 2021

@author: jesus

"""

from enum import IntEnum

QUIZ_BASE_URL = "https://opentdb.com"
QUIZ_API_URL = "https://opentdb.com/api_config.php"



class Difficulty( IntEnum ):
   
    EASY   = 1
    MEDIUM = 2
    HARD   = 3
    
class Category( IntEnum ):
   
    ANY         = 0
    GENERAL     = 1
    BOOKS       = 2
    FILMS       = 3
    MUSIC       = 4
    MUSICALS    = 5
    TV          = 6
    VIDEOGAMES  = 7
    BOARDGAMES  = 8
    SCIENCE     = 9
    COMPUTERS   = 10
    MATH        = 11
    MYTHOLOGY   = 12
    SPORTS      = 13
    GEOGRAPHY   = 14
    HISTORY     = 15
    POLITICS    = 16
    ART         = 17
    CELEBRITIES = 18
    ANIMALS     = 19
    VEHICLES    = 20
    COMICS      = 21
    GADGETS     = 22
    ANIME       = 23
    CARTOON     = 24
    
    
    
    
    
    