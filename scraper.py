"""Copyright © 2021 RICHY
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including limitation the rights to use, merge, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
# AUTHOR : RICHY                                              #
# WRITTEN ON : 23/10/2021                                     #
# GITHUB : https://github.com/rixhy                           #
# LANGUAGE : PYTHON 3.9.5                                     #
# THANKS FOR USING MY CODE, FEEL FREE TO CONTACT ME FOR HELP  #
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#



import requests
import os
import time
from colorama import Fore


#style--------------------------------------------------------
r = Fore.RED
w = Fore.WHITE
os.system('mode 83, 22')
f = open('proxies.txt','wb')
#--------------------------------------------------------------

# PROXY TYPES "http" "https" "socks4" "socks5"

#cmd-----------------------------------------------------------------------------------------------------------------
def http():
  r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
  f.write(r1.content)
  f.close()
  print(f'{r}[{r}{w}${w}{r}]{r} {w}Successfully scraped http proxies.')

def https():
  r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all")
  f.write(r1.content)
  f.close()
  print(f'{r}[{r}{w}${w}{r}]{r} {w}Successfully scraped https proxies.')

def socks4():
  r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
  f.write(r1.content)
  f.close()
  print(f'{r}[{r}{w}${w}{r}]{r} {w}Successfully scraped socks4 proxies.')

def socks5():
  r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=Socks5&timeout=10000&country=all")
  f.write(r1.content)
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
#------------------------------------------------------------------

if __name__ == "__main__":
  main()

#------------------------------------ THE END ---------------------------------------
