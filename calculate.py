from datetime import date
import json
import requests

def del_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year - years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


# generate 10 year historical prices based on today's date
def get_10year(lang):
#    path = '/home/bitkarrot/satshkd/static/hkd_historical'
    path = './static/hkd_historical'
    filep = open(path)
    historical = json.load(filep)
    hist_entries = []

    datelist = []
    years = list(range(1,11))
    for i in years:
        adate = str(del_years(date.today(), i))
        datelist.append(adate)

    for entry in historical:
        if entry['date'] in datelist:
            hist_entries.append(entry)
    hist_entries.reverse()

    final_list = []
    today_sats = get_bitfinex()

    i = 1
    text_array = []
    if lang == 'cn':
        text_array.append('年前')
        text_array.append('年前')
    elif lang =='en':
        text_array.append("year ago")
        text_array.append("years ago")


    for entry in hist_entries:
        year = entry['date']
        rawsat = entry['sathkd_rate']
        sats = "{:,}".format(rawsat)
        percentage = -100 * (rawsat - today_sats)/rawsat
        strp = "{:.3f}".format(percentage) + "%"
        #print(f'year: {year} sats: {sats} percent: {strp}')
        if i == 1:
            aset = {'year' : f"{i} {text_array[0]}", 'sats': sats + " sats", 'percent': strp}
        else:
            aset = {'year' : f"{i} {text_array[1]}", 'sats': sats + " sats", 'percent': strp}
        final_list.append(aset)
        i = i + 1
    return final_list


def get_bitfinex():
    url = "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD"
    res = requests.get(url)
    rates = res.json()
    last_price = rates[6]
    sathkd = round((1/last_price)*100000000/7.75)  # assume exch rate is 7.75
    #print(f'bitfinex last price: {last_price}, current sat rate: {sathkd}')
    return sathkd


lang = 'en'
lang = 'cn'
#final = get_10year(lang)
#print(final)

