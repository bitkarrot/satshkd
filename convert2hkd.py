import json
import requests

path = "./"

def convert():
    try:
        # grab file from site
        r = requests.get("http://usdsat.com/historical")
#        data = json.dumps(r)
#        print(data)
        with open(path + "static/historical", "wb") as f: 
            f.write(r.content)
        f.close()

        
        # convert to hkd
        my_file = open(path + 'static/historical', 'rt')
        lines = my_file.read()
        print(lines)
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



convert()