# email info
username = ''
pwd = ''
to_address = ''
mailServer = 'smtp.gmail.com'

# user agent header
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

# Best Buy product info
BB_prod = {
    'name': 'Playstation 5',
    'store': '[Best-Buy]',
    'url': 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149',
    'findClass': 'div',
    'classType': 'data-reactroot',
    'typeContent': '',
    'regex': '(?<="availability\\\\":).*?(?=,)',
    'availability': 0
}

# GameStop product info
GS_prod = {
    'name': 'Playstation 5',
    'store': '[Game-Stop]',
    'url': 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New',
    'findClass': 'button',
    'classType': 'class',
    'typeContent': 'add-to-cart btn btn-primary',
    'regex': '(?<="availability":).*?(?=,)',
    'availability': '"Not Available"'
}