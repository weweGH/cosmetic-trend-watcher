import os
import pandas as pd
from wordcloud import WordCloud
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# === [1] 기본 설정 ===
keywords = ['파운데이션', '틴트', '메이크업', 'kbeauty']
today = datetime.today().strftime('%Y%m%d')

font_path = "C:/Windows/Fonts/malgun.ttf"
output_dir = "output/wordclouds"
os.makedirs(output_dir, exist_ok=True)

okt = Okt()
stop_words = set(stopwords.words('english'))

# === [2] 한영 통합 워드클라우드 생성 ===
def extract_korean_words(text):
    nouns = okt.nouns(text)
    return [n for n in nouns if len(n) > 1]

def extract_english_words(text):
    tokens = word_tokenize(text)
    words = [w.lower() for w in tokens if w.isalpha() and w.lower() not in stop_words]
    return [w for w in words if len(w) > 1]

for keyword in keywords:
    comment_path = f"rawdata/comments/comments_{keyword}_{today}.csv"
    if not os.path.exists(comment_path):
        print(f"[경고] {comment_path} 없음. 건너뜀.")
        continue

    df = pd.read_csv(comment_path, encoding='utf-8-sig')
    text = " ".join(df['comment'].dropna().astype(str))

    # === 한글 + 영어 단어 추출 ===
    ko_words = extract_korean_words(text)
    en_words = extract_english_words(text)

    all_words = ko_words + en_words

    if not all_words:
        print(f"⚠️ '{keyword}' 워드클라우드 생략 - 단어 없음")
        continue

    count = Counter(all_words)
    wc = WordCloud(
        font_path=font_path,
        background_color='white',
        width=800,
        height=600
    ).generate_from_frequencies(count)

    output_path = os.path.join(output_dir, f"{keyword}_wordcloud.png")
    wc.to_file(output_path)
    print(f"✅ {keyword} 워드클라우드 저장: {output_path}")
