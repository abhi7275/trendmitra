# TrendMitra — What's Trending in India?

**TrendMitra** is a powerful personal project that showcases your end-to-end data engineering, NLP, and dashboarding skills by tracking what's trending daily across India — from News, Reddit, and YouTube. Built with Python and Streamlit, it delivers a clean, interactive experience with automatic topic classification.

---

## 🔥 Key Features

- ✅ Aggregates top trends from **News**, **Reddit**, and **YouTube**
- ✅ Automatically classifies each story into **Technology, Sports, Movies, Business, Miscellaneous**
- ✅ Clean and interactive **Streamlit UI** with custom CSS + query-based category filtering
- ✅ Real-time trending dashboard with **Top 10 Daily Stories**
- ✅ Fully local pipeline — **no scheduling or deployment required**
- ✅ Neatly organized into **frontend + backend** codebase

---

## 🧠 How It Works

1. **Data Collection**: Scripts pull data from public APIs using stored `.env` keys.
2. **NLP Processing**: Cleans text and uses rule-based logic to categorize stories.
3. **JSON Output**: Saves structured daily files like `trending_items_YYYY-MM-DD.json`
4. **Streamlit Dashboard**: Reads daily file and presents it with category-based filtering.

---

## 📂 Project Structure

TrendMitra/ ├── app.py # Frontend: Streamlit dashboard with HTML/CSS ├── backend/ │ ├── process_data.py # Loads + processes stories from all sources │ └── download.py # Downloads NLTK resources ├── data/ # Daily trending_items_YYYY-MM-DD.json files ├── nltk_data/ # NLTK tokenizers and stopwords ├── .env # API keys (not pushed) ├── requirements.txt └── README.md

---

## 🚀 Getting Started

**Clone the Repo**  
git clone https://github.com/yourusername/TrendMitra.git
cd TrendMitra

# Install dependencies
pip install -r requirements.txt

# Create your .env file and add the following keys
# (Replace with your actual keys)
"NEWS_API_KEY=your_news_key"
"REDDIT_CLIENT_ID=your_reddit_id"
"REDDIT_SECRET=your_reddit_secret"
"YOUTUBE_API_KEY=your_youtube_key"

# Download required NLTK resources
python backend/download.py

# Run the daily processing pipeline
python backend/process_data.py

# Launch the dashboard
streamlit run app.py
