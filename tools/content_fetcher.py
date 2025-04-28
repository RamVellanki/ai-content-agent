from newspaper import Article
from youtube_transcript_api import YouTubeTranscriptApi
import re

def fetch_article_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Failed to fetch article: {url}, Error: {e}")
        return ""

def fetch_youtube_transcript(url):
    try:
        video_id = extract_youtube_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([x['text'] for x in transcript])
    except Exception as e:
        print(f"Failed to fetch YouTube transcript: {url}, Error: {e}")
        return ""

def extract_youtube_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None