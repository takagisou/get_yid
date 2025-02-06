import yt_dlp


def hi() -> str:
    return "hi from yid"

def get_yid(url: str) -> str:
    yt_opts = {
        "playlist_items": 0,
        "quiet": True,
        "outtmpl": "playlist:channel_url"
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        return ydl.download(url)
