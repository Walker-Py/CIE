import requests
import sys
import time
from colorama import init, Fore

init(autoreset=True)

def loading_animation():
    print(Fore.CYAN + "Iniciando, Agent.py...")
    for _ in range(10):
        for symbol in ['|', '/', '-', '\\']:
            sys.stdout.write('\r' + Fore.CYAN + "Carregando " + symbol)
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def check_username(username):
    platforms = {
        "Instagram": f"https://instagram.com/{username}",
        "Facebook": f"https://facebook.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "YouTube": f"https://www.youtube.com/user/{username}",
        "Roblox": f"https://www.roblox.com/users/username.aspx?username={username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "LinkedIn": f"https://www.linkedin.com/in/{username}/",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
    }

    print(Fore.CYAN + "\nVerificando usuários em várias plataformas...\n")

    for platform, url in platforms.items():
        try:
            response = requests.get(url, allow_redirects=False)
            if response.status_code == 404:
                print(f"{Fore.CYAN}{platform}: {Fore.CYAN}Disponível [+] - {url}")
            elif response.status_code == 200:
                print(f"{Fore.CYAN}{platform}: {Fore.BLUE}Não Disponível [-] - {url}")
            elif response.status_code in [301, 302]:
                print(f"{Fore.CYAN}{platform}: {Fore.CYAN}Redirecionado - pode indicar que o usuário existe - {url}")
            else:
                print(f"{Fore.CYAN}{platform}: Status {response.status_code} - {url}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.CYAN}{platform}: Erro ao acessar - {e}")

def main():
    loading_animation()
    
    while True:
        print(Fore.CYAN + "===========================")
        print(Fore.CYAN + "   Pesquisa de Usuário     ")
        print(Fore.CYAN + "===========================\n")
        
        username = input("Digite o nome de usuario que deseja investigar (ou 'sair' para encerrar): ")
        if username.lower() == 'sair':
            print("Saindo do programa...")
            break
        
        check_username(username)
        print()

if __name__ == "__main__":
    main()
