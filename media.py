# Udacity full-stack web developer nanodegree
# 01. Programming fundamentals and the web
# Lesson 09: Make classes: movie website


class Movie():
    # add documentation that can be called with __doc__
    """This class provides a way to store movie information."""
    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_year, movie_storyline, poster_image,
                 trailer_youtube_url):
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
        pass
