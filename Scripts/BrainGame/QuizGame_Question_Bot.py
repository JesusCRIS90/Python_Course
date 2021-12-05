#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:37:27 2021

This bot get Question from page: https://opentdb.com/

@author: jesus
"""

import QuizGame_Constants as const
from QuizGame_Constants import Difficulty
from QuizGame_Constants import Category

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class QuestionBot( webdriver.Chrome ):

    def __init__( self, driver_path = r'/home/jesus/SeleniumDrivers/chromedriver', teardown = False ):
        self.driver_path = driver_path
        self.teardown = teardown
        super(QuestionBot, self).__init__( executable_path = self.driver_path )
        self.implicitly_wait( 15 )
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

        
    def land_first_page( self ):
        self.get( const.QUIZ_API_URL )
        
 
    def set_number_of_questions( self, number:int = 10 ):
        
        number_question_field = self.find_element_by_id( 'trivia_amount' )
        number_question_field.clear()
        
        if self.__valid_number_of_questions__( number ):
            number_question_field.send_keys( number )
        else:
            number_question_field.send_keys( 10 )
    


    def set_difficulty( self, Difficulty:Difficulty ):
        # difficulty_element = self.find_element_by_class_name( "form-control" )
        difficulty_element = self.find_element(By.NAME, 'trivia_difficulty' )
        combobox_element = Select( difficulty_element )
        combobox_element.select_by_index( int( Difficulty) )
        
        
    
    def set_category( self, Category:Category ):
        category_element = self.find_element(By.NAME, 'trivia_category' )
        combobox_element = Select( category_element )
        combobox_element.select_by_index( int( Category) )
        
        
    
    def set_multiple_answer( self, type_answer:bool = False ):
        mult_ans_element = self.find_element(By.NAME, 'trivia_type' )
        combobox_element = Select( mult_ans_element )
        if( type_answer  ):    
            combobox_element.select_by_index( 1 )
        else:
            combobox_element.select_by_index( 2 )
    
    
    def click_generate_questions( self ):
        # gen_element = self.find_element(By.TAG_NAME, 'Generate API URL' )
        gen_element = self.find_element_by_xpath( '//button[@class="btn btn-lg btn-primary btn-block"]' )
        # gen_element = self.find_element_by_class_name('btn btn-lg btn-primary btn-block' )
        gen_element.click()
        pass
    
    def gather_questions( self ):
        elements = self.find_elements_by_class_name( "alert alert-success" )
        print( len( elements ) )
        # for element in elements:
        #     print( element )
            
            
    
    def __valid_number_of_questions__( self, number:int ):
        if( number < 10 or number > 50 ):
            return False
        return True
        
