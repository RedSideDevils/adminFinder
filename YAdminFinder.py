import requests as r
from colorama import Fore

RED = Fore.RED
GREEN = Fore.GREEN

__banner__ = """
██╗   ██╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
╚██╗ ██╔╝██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝ ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
  ╚██╔╝  ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
   ██║   ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                made by Trippingcarpet
"""

print(RED + __banner__)
print('\n' + "-" * 60 + '\n')
url = input("[~]Enter URL of website: ")

if not url.endswith('/'):
    url += '/'


variants = open("domens.txt","r").read().split()

if variants is not None:
    print('[~]Paths loaded({})'.format(len(variants)))

with r.get(url) as f:
    if f.status_code == 200:
        print('[~]Starting...')

    else:
        print('[~]Wrong url')
        exit()

for variant in variants:


    if variant.startswith('/'):
        variant = variant[1:]

    _full_url_ = url + variant

    with r.get(_full_url_) as request:

        if request.status_code == 200:
            print(GREEN + '[+]Found admin panel on: %s' % _full_url_)
            inpt = input("[~]Found panel in {}. Do you want continue scanning?(Y/n):")

            if inpt == "Y":
                continue

            else:
                break;

        elif request.status_code == 404:
            print(RED + '[-]Invaild: %s' % _full_url_)

        else:
            print(_full_url_)
