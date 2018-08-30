import fresh_tomatoes
import media

toystory = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                       'https://upload.wikimedia.org/wikipedia/en/1/13/'
                       'Toy_Story.jpg',
                       "https://www.youtube.com/watch?v=Ny_hRfvsmU8")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     'https://resizing.flixster.com/VTR4O6lIom9VDophBD2MQKvv'
                     'IsQ=/206x305/v1.bTsxMTE3Njc5MjtqOzE3ODE0OzEyMDA7ODAwOz'
                     'EyMDA',
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

harrypotter = media.Movie("Harry potter and half blood prince",
                          "A wizard boy and his life at a wizard school.",
                          'https://encrypted-tbn0.gstatic.com/images?q=tbn'
                          ':ANd9GcSHfZJk_VlHE25CMQ_Yy4uoIjrlaodkm2cDk5ZOKz'
                          'NGR5boH71K2w',
                          "https://www.youtube.com/watch?v=sg81Lts5kYY")

furious7 = media.Movie("Furious 7",
                       "All about illegal street racing, espionage.",
                       'https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/'
                       'Furious_7_poster.jpg/220px-Furious_7_poster.jpg',
                       "https://www.youtube.com/watch?v=Skpu5HaVkOc")

infinitywar = media.Movie("Infinity War",
                          "A group of superheroes try to save the world.",
                          'https://upload.wikimedia.org/wikipedia/en/4/4d/'
                          'Avengers_Infinity_War_poster.jpg',
                          "https://www.youtube.com/watch?v=QwievZ1Tx-8&t=10s")

faultstars = media.Movie("Fault in our stars",
                         "A love story of a 16 year old girl",
                         'http://www.pumaisdue.com/wp-content/'
                         'uploads/2017/05/the-fault-in-our-stars.jpg',
                         "https://www.youtube.com/watch?v=9ItBvH5J6ss")

movies = [toystory, avatar, harrypotter, furious7, infinitywar, faultstars]
fresh_tomatoes.open_movies_page(movies)
