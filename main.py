import sys
import os
import secrets
import subprocess

def generate_file_name(channel):     
    while True:
        id = secrets.randbelow(1_000_000)
        file_name = f"{channel}_{id}.ts"
        if not os.path.exists(file_name):
            return file_name

def download_twitch_live(channel):
    file_name = generate_file_name(channel)
    url = f"https://www.twitch.tv/{channel}"

    print(f"Iniciando download de {channel} em '{file_name}'... Pressione Ctrl+C para parar.")

    try:
        subprocess.run([
            "streamlink",
            "--twitch-disable-ads",
            "--retry-streams", "3",
            "-o", file_name,
            url,
            "best"
        ], check=True)
        print("Download finalizado.")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o streamlink:", e)
    except KeyboardInterrupt:
        print("\nDownload interrompido pelo usuário.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python download_twitch.py <canal>")
        sys.exit(1)

    canal = sys.argv[1]
    download_twitch_live(canal)
