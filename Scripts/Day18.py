#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:34:31 2021

Python Course Day 18

@author: jesus
"""

from turtle import Turtle, Screen


square_len = 300

jezz_the_turtle = Turtle()
jezz_the_turtle.shape("turtle")
jezz_the_turtle.color("blue")
jezz_the_turtle.speed( "slow" )


jezz_the_turtle.fd( square_len )
jezz_the_turtle.right( 90 )
jezz_the_turtle.fd( square_len )
jezz_the_turtle.right( 90 )
jezz_the_turtle.fd( square_len )
jezz_the_turtle.right( 90 )
jezz_the_turtle.fd( square_len )
jezz_the_turtle.right( 90 )


screen = Screen()
screen.exitonclick()