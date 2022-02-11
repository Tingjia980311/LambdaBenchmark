from datetime import datetime                                                   
from random import sample  
from os import path

from jinja2 import Template


def lambda_handler(event, context):
    name = 'username'
    # size = event.get('random_len')
    cur_time = datetime.now()
    random_numbers = sample(range(0, 1000000), 1024)
    template = Template( open(path.join('./templates', 'template.html'), 'r').read())
    html = template.render(username = name, cur_time = cur_time, random_numbers = random_numbers)
    return html
    
# print(lambda_handler({},{}))
