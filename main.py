import sys
import os
import secrets
from streamlink import Streamlink

def generate_file_name(channel):     
    while True:
        id = secrets.randbelow(1_000_000)
        file_name = channel + str(id)

        if not os.path.exists(file_name):
            return file_name


def download_twitch_live(channel):
    file_name =  generate_file_name(channel)
    session = Streamlink()
    url = f"https://www.twitch.tv/{channel}"

    streams = session.streams(url)
    if not streams:
        print(f"O canal {channel} não está ao vivo ou não foi encontrado.")
        return
        
    stream = streams.get("best")
    if not stream:
        print("Não foi possível obter o fluxo com qualidade 'best'.")
        return

    fd = stream.open()

    with open(file_name, "wb") as f:
        print(f"Iniciando download de {channel} em '{file_name}'... Pressione Ctrl+C para parar.")
        try:
            while True:
                data = fd.read(1024)
                if not data:
                    break
                f.write(data)
        except KeyboardInterrupt:
            print("\nDownload interrompido pelo usuário.")
        finally:
            fd.close()
            print("Download finalizado.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python download_twitch.py <canal>")
        sys.exit(1)

    canal = sys.argv[1]
    download_twitch_live(canal)

               