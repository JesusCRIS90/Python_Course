#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:52:17 2021

@author: jesus
"""

from QuizGame_Question_Bot import QuestionBot
from QuizGame_Constants import Difficulty
from QuizGame_Constants import Category



# from selenium import webdriver
# import QuizGame_Constants as const
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select

# path_chrome_driver = r'/home/jesus/SeleniumDrivers/chromedriver'


# driver = webdriver.Chrome( executable_path = path_chrome_driver )
# driver.get( const.QUIZ_API_URL )
# driver.implicitly_wait( 15 )

# difficulty_element = driver.find_element( By.NAME, 'trivia_difficulty' )
# combobox_element = Select( difficulty_element )

# print( len(  combobox_element.options ) )

# for opt in combobox_element.options:
#     print( opt.text )
    
# combobox_element.select_by_index( int( Difficulty.MEDIUM ) )


# https://opentdb.com/api.php?amount=15&category=27&difficulty=hard&type=boolean


with QuestionBot() as bot:
    bot.land_first_page()
    bot.set_number_of_questions( 18 )
    bot.set_difficulty( Difficulty.HARD )
    bot.set_category( Category.FILMS )
    bot.set_multiple_answer()
    bot.click_generate_questions()
    bot.gather_questions()