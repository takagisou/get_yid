import sys
import yt_dlp


def get_yid() -> str:
    url = sys.argv[1]
    params = {
        "playlist_items": "0",
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(params) as ydl:
        result = ydl.extract_info(url, download=False)
        return result["channel_url"]
