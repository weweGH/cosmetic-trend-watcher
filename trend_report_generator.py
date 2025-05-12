from jinja2 import Environment, FileSystemLoader
import os

# 템플릿 환경 설정
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('cosmetic_trend_report.html')

# 데이터 예시
videos = [
    {'title': '메이크업 초보를 위한 꿀팁', 'channel': '화장왕', 'views': '1.2M', 'video_id': 'abc123'},
    {'title': '2025 봄 신상 메이크업 리뷰', 'channel': '뷰티로그', 'views': '980K', 'video_id': 'def456'},
    # ... 총 5개
]

# 렌더링
html = template.render(videos=videos, wordcloud_path='wordcloud.png')

# 저장
with open('report_output.html', 'w', encoding='utf-8') as f:
    f.write(html)
