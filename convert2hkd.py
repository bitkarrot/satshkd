import json

path = "./"

try:
    my_file = open(path + 'static/historical', 'rt')
    lines = my_file.read()
    my_file.close()
    jlist = json.loads(lines)
    
    print(len(jlist))

    for i in jlist:
        price = i['satusd_rate']
        i['sathkd_rate'] = int(price/7.75)
        whole_price = i['btcusd_rate']
        i['btchkd_rate'] = whole_price*7.75

    print(jlist[len(jlist)-1])

    with open(path + 'static/hkd_historical', 'w') as output:
        output.write(json.dumps(jlist))
    output.close()
    
except Exception as e:
    print(e)
    print("Something unexpected occurred!")


