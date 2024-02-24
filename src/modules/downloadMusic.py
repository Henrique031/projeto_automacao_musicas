from yt_dlp import YoutubeDL # Baixar videos yt
import threading as thr # Baixar músicas em segundo plano 


def ytdl(url, video=False):
    
    if url[1] != '': # Significa que tem uma pasta
        path = f'D:\\rique\\Music\\musicas_baixadas\\{url[1]}\\%(title)s.%(ext)s'
    else:
        path = f'D:\\rique\\Music\\musicas_baixadas\\%(title)s.%(ext)s'
         
    # Video mp4
    """ ydl_opts = {
        'format': 'best[height<=480]',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'outtmpl': path,
    }  """
   
    
    #Música mp3
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
        'outtmpl': path,
    }
    

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url[0]])
        
    
    
def download(*url):
    thread = thr.Thread(target=ytdl, args=(url,))
    thread.start()