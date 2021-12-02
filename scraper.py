import requests
import os
import time
from colorama import Fore


r = Fore.RED
w = Fore.WHITE
os.system('mode 83, 22')
f = open('proxies.txt','wb')

def http():
  r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
  f.write(r1.content)
  f.close()
  print(f'{r}[{r}{w}${w}{r}]{r} {w}Successfully scraped http proxies.')

def https():
  r2 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all")
  f.write(r2.content)
  f.close()
  print(f'{r}[{r}{w}${w}{r}]{r} {w}Successfully scraped https proxies.')

def socks4():
  r3 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
  f.write(r3.content)
  f.close()
  print(f'{r}[{r}{w}${w}{r}]{r} {w}Successfully scraped socks4 proxies.')

def socks5():
  r4 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=Socks5&timeout=10000&country=all")
  f.write(r3.content)
  f.close()
  print(f'{r}[{r}{w}${w}{r}]{r} {w}Successfully scraped socks5 proxies')

def main():
  os.system('cls')
  print(f'''
{r}╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╦═╗
╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ╚═╗║  ╠╦╝╠═╣╠═╝║╣ ╠╦╝
╩  ╩╚═╚═╝╩ ╚═ ╩   ╚═╝╚═╝╩╚═╩ ╩╩  ╚═╝╩╚═
[+]═════════════════════[+]
 ║ [1] - HTTP            ║
 ║ [2] - HTTPS           ║
 ║ [3] - Socks4          ║
 ║ [4] - socks5          ║
[+]═════════════════════[+]
  ''')
  choice = int(input(f"{r}[ {r}{w}>{w}{r} ]{r} CHOICE : "))
  if choice == 1:
    http()
    time.sleep(3)
    main()
  elif choice == 2:
    https()
    time.sleep(3)
    main()
  elif choice == 3:
    socks4()
    time.sleep(3)
    main()
  elif choice == 4:
    socks5()
    time.sleep(3)
    main()


if __name__ == "__main__":
  main()

