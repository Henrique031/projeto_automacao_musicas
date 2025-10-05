from __future__ import unicode_literals
from yt_dlp import YoutubeDL
import os
from tqdm import tqdm



progress_bar = None


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):

    global progress_bar
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total and not progress_bar:
            progress_bar = tqdm(total=total, unit='B', unit_scale=True, desc='Baixando')
        if progress_bar:
            progress_bar.n = downloaded
            progress_bar.refresh()
    elif d['status'] == 'finished':
        if progress_bar:
            progress_bar.close()
            print("Download concluído!")



def ytdl(url):
    nomeUsuario = os.getlogin()

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,  # Deixe `False` para ver os logs
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'outtmpl': f'D:\\{nomeUsuario}\\Music\\%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        duracaoSegundos = info.get('duration')

        minutos = duracaoSegundos // 60
        segundos = duracaoSegundos % 60
        print(f'Duração do vídeo: {minutos}m {segundos}s')

        ydl.download([url])
