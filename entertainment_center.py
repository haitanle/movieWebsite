import media
import fresh_tomatoes

# Create movie instance
avatar = media.Movie("Avatar", "A marine on an alien palent",
				"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
				"https://www.youtube.com/watch?v=5PSNL1qE6VY")

silence = media.Movie("Silence", "Two Jesuit priests look for a disappeared priest",
				"http://www.impawards.com/2016/posters/silence.jpg",
				"https://www.youtube.com/watch?v=TcNKM4TI41E&t=25s")

la_la_land = media.Movie("La La Land", "Two lovers find each other",
				"http://www.awardsdaily.com/wp-content/uploads/2016/08/1.jpg",
				"https://www.youtube.com/watch?v=0pdqf4P9MB8&t=6s")

toy_story = media.Movie("Toy Story", "A story of a boy blah blah blah", 
				"http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
				"https://www.youtube.com/watch?v=KYz2wyBy3kc")

hateful8 = media.Movie("Hateful 8", "8 people stranded in the mountain",
				"http://dl9fvu4r30qs1.cloudfront.net/05/ea/4f64ae7d4bd0b3db2891cd30c525/the-hateful-eight-poster-2.jpg",
				"https://www.youtube.com/watch?v=gnRbXn4-Yis")

revenant = media.Movie("The Revenant", "Fur trade in the early USA",
				"https://s-media-cache-ak0.pinimg.com/564x/2f/9c/a1/2f9ca1e7b5b42196fc0f6ba668b51757.jpg",
				"https://www.youtube.com/watch?v=LoebZZ8K5N0")

# Add movie instances to list
movies = [avatar,silence, la_la_land, toy_story, hateful8, revenant]

# Display movies on webpage
fresh_tomatoes.open_movies_page(movies)
