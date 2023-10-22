from yt_dlp import YoutubeDL # Baixar videos yt
import threading as thr # Baixar músicas em segundo plano 


def ytdl(url):
    
    if url[1] != '':
        path = f'D:\\Lenda Viva\Music\\1musicas-baixadas\\{url[1]}\\%(title)s.%(ext)s'
    else:
        path = f'D:\\Lenda Viva\\Music\\1musicas-baixadas\\%(title)s.%(ext)s'
    
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
        'outtmpl': path,
    }
    

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url[0]])
        
    
    
def download(*url):
    thread = thr.Thread(target=ytdl, args=(url,))
    thread.start()