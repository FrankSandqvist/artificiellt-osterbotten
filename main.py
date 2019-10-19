from textgenrnn import textgenrnn
from random import randint
from urllib import request
from os import environ
import json

from common_prefixes import common_prefixes
from html_template import html_template

model = None
common_prefixes_length = len(common_prefixes)

def artificiellt_osterbotten(_):
    # this allows not having to reload the model if the function is executing
    # while still warm
    if(model is None):
        textgen = textgenrnn(weights_path='./weights.hdf5')

    prefix = None
    # 50% chance that we use one of the common prefixes
    if(randint(0, 1) is 0):
        common_prefixes[randint(0, common_prefixes_length - 1)]

    # return one headline, with a random temperature ranging from 0.400 to 1.000
    headline = textgen.generate(
        return_as_list=True,
        n=1,
        temperature=(randint(400, 1000) / 1000),
        prefix=prefix
    )[0]

    print(headline)

    access_key= environ.get('unsplash', 'Unsplash key not set.')
    photo_url = ''
    photo_photographer = ''
    photo_photographer_url = ''
    try:
        photo_data = request.urlopen('https://api.unsplash.com/photos/random/?client_id=' + access_key + '&collections=162326,141077,1901880,3652995,4961056,235549,1927934,2079070,1816522,574198,208403,1157541,582659,329064,6827326,2550612,2095053,8465268,3735325,1784943,1696020,1414614,1362996,4573436,1224539,1956581,1598519,4287584,4703517').read()
        photo_json = json.loads(photo_data)
        photo_url = photo_json['urls']['regular']
        photographer = photo_json['user']['name']
        photographer_url = photo_json['user']['links']['html'] + '?utm_source=artificiellt_osterbotten&utm_medium=referral'
    except:
        print('Unsplash error')

    # generate an HTML document
    replaced = html_template.format(
        headline=headline,
        photo_url=photo_url,
        photographer=photographer,
        photographer_url=photographer_url
    )

    return replaced
