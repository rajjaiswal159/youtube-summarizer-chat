# Import transcript API
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

# Import URL parsing utilities
from urllib.parse import urlparse, parse_qs


# Extract video ID from a YouTube URL
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):

    # Handle short youtu.be URLs
    if "youtu.be" in url:
        video_id = url.split("/")[-1].split("?")[0]

        if not video_id:
            raise ValueError("Invalid YouTube URL.")

        return video_id

    # Handle youtube.com URLs
    query_params = parse_qs(urlparse(url).query)

    if "v" not in query_params:
        raise ValueError("Invalid YouTube URL.")

    return query_params["v"][0]


# Fetch transcript from a YouTube video
def get_transcript(video_url):

    if not video_url.strip():
        raise ValueError("Please enter a YouTube URL.")

    try:

        # Extract video ID from URL
        video_id = extract_video_id(video_url)

        # Create transcript API instance
        ytt_api = YouTubeTranscriptApi()
    
        # Fetch transcript data
        transcript_data = ytt_api.fetch(
            video_id,
            languages=["en", "hi"]
        )
    
        # Combine transcript snippets into a single string
        transcript_text = " ".join(snippet.text for snippet in transcript_data)
    
        # Return transcript text
        return transcript_text
    
    except (NoTranscriptFound, TranscriptsDisabled):
        raise ValueError("Transcript is unavailable for this video.")
    
    except VideoUnavailable:
        raise ValueError("This video is unavailable.")
    
    except Exception:
        raise RuntimeError("Failed to fetch transcript. Please try again later.")