from yt_dlp import YoutubeDL # Baixar videos yt
import threading as thr # Baixar músicas em segundo plano 
import os


def ytdl(url):
    
    userName = os.getlogin()
    
    # if url[1] != '': # Significa que tem uma pasta
    #     path = f'D:\\{userName}\\Music\\{url[1]}\\%(title)s.%(ext)s'
    # else:
    #     path = f'D:\\{userName}\\Music\\%(title)s.%(ext)s'
         
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        '--audio-format': 'best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'outtmpl': f'D:\\{userName}\\Music\\%(title)s.%(ext)s',
    }
    

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url[0]])
        
    
    
def download(*url):
    thread = thr.Thread(target=ytdl, args=(url,))
    thread.start()

