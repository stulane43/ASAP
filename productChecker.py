import requests
import re
import config
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from time import localtime, strftime, sleep
from send_email import send_mailBB, send_mailGS

init()

class lookupProduct:
    def __init__(self, name, store, url, findClass, classType, typeContent, regex, availability, storeColor):
        self.name = name
        self.store = store
        self.url = url
        self.findClass = findClass
        self.classType = classType
        self.typeContent = typeContent
        self.regex = regex
        self.availability = availability
        self.storeColor = storeColor

p1 = lookupProduct(config.BB_prod["name"], config.BB_prod["store"], config.BB_prod["url"], config.BB_prod["findClass"], config.BB_prod["classType"], config.BB_prod["typeContent"], config.BB_prod["regex"], config.BB_prod["availability"], Fore.BLUE)
p2 = lookupProduct(config.GS_prod["name"], config.GS_prod["store"], config.GS_prod["url"], config.GS_prod["findClass"], config.GS_prod["classType"], config.GS_prod["typeContent"], config.GS_prod["regex"], config.GS_prod["availability"], Fore.MAGENTA)
products = (p1, p2)
        
def product_checker():
    i = 0
    while True:
        for product in products:
            if i < 720:
                cur_time = strftime("%H:%M:%S", localtime())
                page = requests.get(product.url, headers=config.headers)
                soup = BeautifulSoup(page.text, 'html.parser')
                result = str(soup.find(product.findClass, {product.classType:product.typeContent}))
                buttonState = re.compile(product.regex)
                availabilityMatch = buttonState.search(result).group()
                if product.availability == 0:
                    availability = int(availabilityMatch)
                else:
                    availability = availabilityMatch
                if availability == product.availability:
                        print(cur_time, Fore.WHITE + "::", product.storeColor + product.store, Style.RESET_ALL,
                            Fore.CYAN + product.name, Fore.WHITE + "::", Fore.RED + "Sold-Out")
                        print(Fore.WHITE + "-------------------------------------------------------------")
                        print(Style.RESET_ALL)
                        sleep(1)
                        i += 1
                elif availability != product.availability:
                        print(cur_time, Fore.WHITE + "::", product.storeColor + product.store, Style.RESET_ALL,
                            Fore.CYAN + product.name, Fore.WHITE + "::", Fore.GREEN + "Available")
                        print(Fore.WHITE + "-------------------------------------------------------------")
                        print(Style.RESET_ALL)
                        if product.store == config.BB_prod["store"]:
                            send_mailBB()
                        elif product.store == config.GS_prod["store"]:
                            send_mailGS()
                        print(Fore.GREEN + "Sent!")
                        sleep(5)
            else:
                send_mailBB()
                print(Fore.WHITE + "Product Update")
                i = 0

product_checker()