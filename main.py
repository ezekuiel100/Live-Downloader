import sys
from streamlink import Streamlink

def download_twitch_live(channel , output_filename):
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

    with open(output_filename, "wb") as f:
        print(f"Iniciando download de {channel} em '{output_filename}'... Pressione Ctrl+C para parar.")
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
    if len(sys.argv) != 3:
        print("Uso: python download_twitch.py <canal> <arquivo_saida.ts>")
        sys.exit(1)

    canal = sys.argv[1]
    arquivo = sys.argv[2]
    download_twitch_live(canal, arquivo)

               