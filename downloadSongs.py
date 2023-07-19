from yt_dlp import YoutubeDL # Baixar videos yt
import threading as thr # Baixar músicas em segundo plano


def downloadSongs(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        '--audio-format': 'best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'D:\Lenda Viva\Music\musicas-baixadas\%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
            
def segundoPlanoDownloadMusica(url):
    thread = thr.Thread(target=downloadSongs, args=(url,))
    thread.start()