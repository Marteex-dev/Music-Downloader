import yt_dlp
import os

class Download:
    def __init__(self):
        self.contador = 1

    @staticmethod
    def clear():
        """Limpa a tela do console."""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def download_music(self):
        """Baixa a música a partir da URL fornecida pelo usuário."""
        Download.clear()

        url = input("Digite a URL da música ou da playlist que você deseja baixar: ")
        print(' ')
        print('_____________________________________')

        options = {
            'format': 'bestaudio/best',
            'extractaudio': True,         
            'audioformat': 'mp3',         
            'outtmpl': 'C:\\Users\\user\\Downloads\\Musicas Baixadas\\%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            try:
                info_dict = ydl.extract_info(url, download=True)
                title = info_dict.get('title', None)
                if title:
                    print(f'Música "{title}" baixada com sucesso!')

                    numero = f"{self.contador:02}"
                    
                    original_filename = f'D:\\Post-X\\Storage\\audio\\{title}.mp3'
                    new_filename = f'D:\\Post-X\\Storage\\audio\\{numero}-{title}.mp3'

                    os.rename(original_filename, new_filename)
                    print(f'Arquivo renomeado para "{new_filename}".')

                    self.contador += 1

            except Exception as e:
                print(f'Erro ao baixar a música: {e}')
                
        Download.clear()
        print('Música(s) baixadas :)')

if __name__ == "__main__":
    downloader = Download()
    downloader.download_music()
