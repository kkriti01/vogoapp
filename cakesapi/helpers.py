import re
import requests
from lxml import html


from .models import Cake

base_url = 'http://www.justbake.in'


def scrap_categories(url='http://www.justbake.in/bangalore'):
    """parse home page and return dictionary of category name and url"""

    # download home page
    r = requests.get(url)
    # convert downloaded html into lxml tree
    tree = html.fromstring(r.text)
    # fetch all categories
    catgeory_parent_div = tree.xpath('//div[@class="menu container-fluid"]/div/div')[0]
    cat_dict = {}     # {'category name': '/href/of/category'}
    for div in catgeory_parent_div.getchildren():
        cat_href = div.xpath('.//a/@href')[0]
        name = div.xpath('.//a/@title')[0]
        print name, cat_href
        cat_dict[name] = base_url + cat_href
        print(cat_dict)
    return cat_dict


def scrap_category_page(category_url):
    """parse category page and scrap items and returns list of products"""

    # download category page
    r = requests.get(category_url)
    tree = html.fromstring(r.text)
    items_div = tree.xpath('//div[@class="col-lg-4 prodcol hidden-xs hidden-sm hidden-md"]')
    products = []
    for item in items_div:
        title = item.xpath('./div[@class="pimg"]/a/@title')[0]
        image_url = category_url + item.xpath('./div[@class="pimg"]/a/img/@src')[0]
        price = item.xpath('.//div[@class="green1"]')[0].text.replace('MRP: Rs.', '').strip()
        products.append({
            'title': title,
            'image': image_url,
            'price': price
        })
    return products


def save_products(category_name, cakes):
    category, created = Category.objetcts.get_or_create(name=category_name)
    for cake in cakes:
        cake, created = Cake.objetcts.get_or_create(title=cake['title'], price=cake['price'])
        cake.image = cake['image']
        cake.save()
        category.cake.add(cake)


def run():
    categories = scrap_categories()
    for name, url in categories.items():
        print(name, url)
        cakes = scrap_category_page(url)
        save_products(name, cakes)


