
Get the YouTube Channel ID.

# Usage

```sh
# rye sync
$ rye run get_yid https://www.youtube.com/@YouTubeJapan
https://www.youtube.com/channel/UCrXUsMBcfTVqwAS7DKg9C0Q
```

This script simply executes the following script within python.

```sh
# pip install yt-dlp
$ yt-dlp --playlist-items 0 --print playlist:channel_id {url}
```
