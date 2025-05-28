import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# === [1] 템플릿 로딩 ===
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('cosmetic_trend_report.html')

# === [2] 키워드 목록 ===
keywords = ['파운데이션', '틴트', '메이크업', 'kbeauty']
today = datetime.today().strftime('%Y%m%d')

# === [3] 키워드별 섹션 데이터 구성 ===
keyword_sections = []

for keyword in keywords:
    # === (1) 영상 CSV 읽기 ===
    video_path = f"rawdata/videos/youtube_{keyword}_{today}.csv"
    if not os.path.exists(video_path):
        print(f"[경고] {video_path} 파일이 없습니다. 건너뜀.")
        continue
    video_df = pd.read_csv(video_path)

    # === (2) 딕셔너리 리스트로 변환 ===
    videos = video_df.to_dict(orient='records')

    # === (3) 워드클라우드 경로 지정 ===
    wordcloud_path = f"output/wordclouds/{keyword}_wordcloud.png"
    if not os.path.exists(wordcloud_path):
        print(f"[경고] {wordcloud_path} 워드클라우드 이미지가 없습니다.")

    keyword_sections.append({
        'keyword': keyword,
        'date': datetime.today().strftime('%Y-%m-%d'),
        'videos': videos,
        'wordcloud_path': wordcloud_path
    })

# === [4] 리포트 생성 ===
html = template.render(
    report_date=datetime.today().strftime('%Y-%m-%d'),
    keyword_sections=keyword_sections
)

# === [5] 저장 ===
os.makedirs("output/reports", exist_ok=True)
output_path = f"output/reports/cosmetic_trend_report_{today}.html"

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ 리포트 저장 완료: {output_path}")
