import requests
from bs4 import BeautifulSoup 

keyword = 'fountain+pen'

results =[]

for i in range(1,11): 
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i)) 
    #print('r.status_code=', r.status_code) #to check if everything is working well
    soup = BeautifulSoup(r.text, 'html.parser')
    boxes = soup.select('.s-item__info')
    for box in boxes:
        print('--') #test to see if working: one price per box
        result ={}
        names = box.select('.s-item__title')
        for name in names:
            print('name=', name.text)
            result['name'] = name.text
        prices = box.select('.s-item__price')
        for price in prices:
            print('prices=',price.text)
            result['price'] = price.text
        statuses = box.select('.SECONDARY_INFO')
        for status in statuses:
            print('status=',status.text)
            result['status'] = status.text
        print('result=',result)
        results.append(result)
    print(len(results)) #want to be equal to the results per page 

import json
j = json.dumps(results)
with open('items.json', 'w') as f:
    f.write(j)
#print('j=', j) #another check step 



