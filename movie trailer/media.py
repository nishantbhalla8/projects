import webbrowser


class Movie():
    """ This class is used for store info about Video
    Attributes:
        - video_title(str):       The title of the video
        - video_duration(str):    The duration of the video
        - video_description(str): Brief description of the video
        - video_genre(str):       Category of the video
    """
    def __init__(self, mTitle, mStoryline, pImage, tYoutube):

        self.title = mTitle
        self.storyline = mStoryline
        self.poster_image_url = pImage
        self.trailer_youtube_url = tYoutube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
