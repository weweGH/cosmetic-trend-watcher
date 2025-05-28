import argparse
import os
from googleapiclient.discovery import build
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
from dotenv import load_dotenv
import platform
import datetime

# === [1] API 키 설정 ===

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)
youtube

# === [2] 한글 폰트 설정 ===

font_path = "C:/Windows/Fonts/malgun.ttf"

if platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False


# # === [3] 영상 검색 함수 ===

def search_youtube_videos(query, max_results):
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=max_results,
        type="video",
        order="viewCount" # 인기순
    )
    response = request.execute()
    videos = []
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        published_at = item["snippet"]["publishedAt"]
        channel_title = item["snippet"]["channelTitle"]
        videos.append({
            "video_id": video_id,
            "title": title,
            "channel": channel_title,
            "published_at": published_at
        })
    return videos


# === [4] 댓글 수집 함수 ===

def get_video_comments(video_id, max_results=10):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )
    response = request.execute()
    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
    return comments


# === [5] 좋아요/조회수/댓글 수 수집 ===

def get_video_stats(video_id):
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()
    stats = response["items"][0]["statistics"]
    return {
        "views": int(stats.get("viewCount", 0)),
        "likes": int(stats.get("likeCount", 0)),
        "comments": int(stats.get("commentCount", 0))
    }

# === [7] 메인 실행 ===

def main(keyword):
    print(f"🔍 검색어: {keyword}")
    videos = search_youtube_videos(keyword, 3)

    results = []
    all_comments = []

    for video in videos:
        stats = get_video_stats(video["video_id"])
        comments = get_video_comments(video["video_id"])
        all_comments.extend(comments)

        video.update(stats)
        video["collected_comments"] = len(comments)
        results.append(video)

        print(f"📹 {video['title']} | 조회수: {video['views']} | 좋아요: {video['likes']} | 댓글 수: {video['comments']}")

    df = pd.DataFrame(results)
    os.makedirs("data", exist_ok=True)
    output_path = f"rawdata/videos/youtube_{keyword}_{datetime.datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"\n✅ 수집 완료! 데이터 저장: {output_path}")

    # 댓글 데이터 저장
    comment_rows = []
    for video in results:
        video_id = video["video_id"]
        title = video["title"]
        channel = video["channel"]
        published_at = video["published_at"]
        comments = get_video_comments(video_id)
        for comment in comments:
            comment_rows.append({
                "video_id": video_id,
                "title": title,
                "channel": channel,
                "published_at": published_at,
                "comment": comment
            })

    comment_df = pd.DataFrame(comment_rows)
    comment_path = f"rawdata/comments/comments_{keyword}_{datetime.datetime.now().strftime('%Y%m%d')}.csv"
    comment_df.to_csv(comment_path, index=False, encoding="utf-8-sig")
    print(f"✅ 댓글 데이터 저장: {comment_path}")



# === [8] CLI 인자 파싱 ===

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="YouTube cosmetics crawler")
#     parser.add_argument("--keyword", type=str, required=True, help="검색할 키워드")
#     args = parser.parse_args()
#     main(args.keyword)

if __name__ == "__main__":

    keywords = ['파운데이션', '틴트', '메이크업', 'kbeauty'] 

    for KeyWord in keywords:

        main(KeyWord)