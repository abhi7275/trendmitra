# topics.py

common_keywords = [
    "technology", "business", "bollywood", "hollywood",
    "cricket", "football", "AI", "artificial intelligence"
]

reddit_extra = [
    "OpenAI", "MachineLearning", "DeepLearning", "DataScience",
    "BigData", "NeuralNetworks", "NLP", "ComputerVision",
    "movies", "TVShows", "Gaming", "ScienceFiction", "Fantasy",
    "Documentaries", "Space", "History", "Politics", "WorldNews",
    "Economics", "Finance", "Investing", "Startups", "Entrepreneurship",
    "Marketing", "SocialMedia"
]

youtube_extra = [
    "Deep Learning", "Machine Learning", "Neural Networks",
    "Natural Language Processing", "Computer Vision", "Data Science",
    "Big Data", "Technology Trends", "Business Innovations",
    "Bollywood Movies", "Hollywood Movies", "Cricket Highlights",
    "Football Matches", "Gaming News", "Science Fiction Movies",
    "Fantasy Series", "Documentaries on AI", "Space Exploration Videos"
]

# Final keywords for each platform
NEWS_KEYWORDS = common_keywords
REDDIT_KEYWORDS = common_keywords + reddit_extra
YOUTUBE_KEYWORDS = common_keywords + youtube_extra
