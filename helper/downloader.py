from yt_dlp import YoutubeDL

def download(url, outdir="downloads"):
    opts = {
        "outtmpl": f"{outdir}/%(title)s.%(ext)s",
        "merge_output_format": "mp4"
    }
    with YoutubeDL(opts) as ydl:
        ydl.download([url])
