import os
import pystyle
from pystyle import *
import requests
import time
from rich import *
def choice_1():
        proxy = console.input("{[red]?[/red]} enter proxy [no port]= ")
        chek = requests.post(f"https://proxycheck.io/v2/{proxy}?vpn=1&asn=1")
        value = chek.json()["status"]
        if value == "ok":
            console.print("{[green]![/green]}[green]alive proxy[/green]")
        else:
            console.print("{[red]![/red]}[red]dead proxy[/red]")
        time.sleep(2)
        os.system('cls||clear')


def choice_2():
    alive = 0
    dead = 0
    hit = 0
    proxies = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all ").text
    proxies = proxies.splitlines()
    for proxy in proxies:
        os.system(f'Title - proxy tool v1 - hit:{hit} - alive:{alive} - dead:{dead}')
        proxies = proxy.split(':')[0]
        print(f"[yellow]proxy= {proxy}[/yellow]")
        chek = requests.post(f"https://proxycheck.io/v2/{proxies}?vpn=1&asn=1")
        value = chek.json()["status"]
        if value == "ok":
            console.print("{[green]![/green]}[green]alive proxy[/green]")
            hit = hit + 1
            alive = alive + 1
            with open("proxy.txt", "a+") as file:
                file.write(f"{proxy}\n")
                file.close
        
        else:
            hit = hit + 1
            dead = dead + 1
            console.print("{[red]![/red]}[red]dead proxy[/red]")
        time.sleep(1)
    os.system('cls||clear')

while True:
    banner = '''
  
    
        :::::::::  :::::::::   ::::::::  :::    ::: :::   :::      ::::::::::: ::::::::   ::::::::  :::        
        :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:   :+:          :+:    :+:    :+: :+:    :+: :+:        
        +:+    +:+ +:+    +:+ +:+    +:+  +:+  +:+   +:+ +:+           +:+    +:+    +:+ +:+    +:+ +:+        
        +#++:++#+  +#++:++#:  +#+    +:+   +#++:+     +#++:            +#+    +#+    +:+ +#+    +:+ +#+        
        +#+        +#+    +#+ +#+    +#+  +#+  +#+     +#+             +#+    +#+    +#+ +#+    +#+ +#+        
        #+#        #+#    #+# #+#    #+# #+#    #+#    #+#             #+#    #+#    #+# #+#    #+# #+#        
        ###        ###    ###  ########  ###    ###    ###             ###     ########   ########  ########## 

    
    
    
    '''
    os.system('Title - Proxy Tool - BKS#1958')
    console = get_console()
    console.print(banner, style="bold red")

    console.print("                                          {[red]1[/red]} try a proxy")
    console.print("                                          {[red]2[/red]} scrape and check proxies")

    print()
    print()
    choice = console.input("{[red]?[/red]} enter your choice : ")
    if choice == '1':
        print()
        print()
        print()
        choice_1()
    if choice == '2':
        print()
        print()
        print()
        choice_2()
    else:
        os.system('cls||clear')
