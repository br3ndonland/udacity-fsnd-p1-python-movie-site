# Udacity full-stack web developer nanodegree
# 01. Programming fundamentals and the web
# Project 01: Movie trailer website


class Movie():
    # add docstring that can be called with __doc__
    """This class provides a way to store movie information."""

    # add a class variable that can be shared by all instances of class Movie
    valid_ratings = ["G", "PG", "PG-13", "R"]

    # build a function to store info in instances of class Movie
    def __init__(self, movie_title, movie_year, movie_storyline,
                 poster_image, trailer_youtube_url):
        """This function creates a template to store movie information."""
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
        pass
