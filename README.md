# 💄 cosmetic-trend-watcher

> A YouTube-based trend analysis pipeline for monitoring keywords, engagement, and customer sentiment in the cosmetics industry.

---

## 📌 Overview

`cosmetic-trend-watcher` is an automated pipeline that:
- Crawls YouTube videos related to a given cosmetic keyword
- Collects video metadata (views, likes, comments)
- Extracts and analyzes user comments
- Generates markdown-based HTML reports with keyword insights, wordclouds, and sentiment analysis

This tool helps cosmetic marketers, researchers, and data analysts stay ahead of emerging trends in the beauty industry.

---

## 🔧 Features

- 🔍 Keyword-based video search (top 3 videos)
- 📊 Aggregated stats: views, likes, comments
- 💬 Comment crawling (up to 100 per video)
- 🧠 Text analysis: top keywords, sentiment classification
- 🌥️ Wordcloud generation
- 📝 Weekly markdown report → auto-converted to HTML

---

## 🗂️ Project Structure
```
cosmetic-trend-watcher/ 
│ 
├─ data/ # Collected raw & processed data 
├─ reports/ # Weekly auto-generated reports (HTML) 
├─ templates/ # Markdown report template 
├─ yt_crawler.py # YouTube video & comment crawler 
├─ analyze_comments.py # Keyword + sentiment analysis 
├─ generate_report.py # Report generator (MD → HTML) 
└─ requirements.txt # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/cosmetic-trend-watcher.git
cd cosmetic-trend-watcher
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your YouTube API key

Create a .env file in the project root:

```env
YOUTUBE_API_KEY=your_api_key_here
```

Or pass the key directly as an argument in your script.

### 4. Run the pipeline

```bash
python yt_crawler.py --keyword "비건 크림"
python analyze_comments.py
python generate_report.py
```

---

## 🖼 Example Output

📄 HTML Report:

🌥 Wordcloud:

---

## 📈 Use Cases
- Discover rising beauty trends (e.g., “병풀”, “비건 화장품”)
- Analyze customer reactions to popular products
- Track marketing campaign engagement over time

---

## 📅 Roadmap
- Add Streamlit dashboard
- Expand to Instagram/Shorts
- Enable batch keyword processing
- Support multi-language sentiment analysis
- Add Google Trends & Naver DataLab integration

---

## 🧑‍💻 Author
- Your Name – @yourgithub





