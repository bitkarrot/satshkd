import json

def get_strings(lang):
    try:
        with open(f'./lang/{lang}.json', 'rb') as f: 
            data = f.read()
            json_data = json.loads(data)
            content = list(json_data.values())
        f.close()
        return content
    except Exception as e:
        print(e)


# test languages
#content = get_strings('en')
#print(content)

#get_strings('zh-hk')
#get_strings('zh-cn')
