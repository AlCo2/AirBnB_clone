#!/usr/bin/python3
""" 
Describes the review system of the console
Allows Users make reviews on Places
"""


class Review(BaseModel):
	""" Defines a review made """
	place_id = ""
	user_id = ""
	text = ""
