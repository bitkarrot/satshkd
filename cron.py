import subprocess
import aiocron
import asyncio
import os
import logging
import yaml
import requests

logging.basicConfig(filename='rates.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('rateslogger').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)

path = "./"
config_file = path + 'config.yml'
rate_file = path + "rates.yml"


def get_rates():
    """
    get exchange rates only once an hour from free API
    and save to yaml file
    """
    with open(config_file, 'rb') as f:
        config = yaml.safe_load(f)
    f.close()
    
    forexURL = config['forex']
    print(forexURL)
    hkdRates = requests.get(forexURL).json()
    hkdrate = hkdRates['conversion_rates']['USD']
    return hkdrate


#### cron job every hour #### 
#@aiocron.crontab('0 * * * *')
@aiocron.crontab('* * * * *')
async def attime():
    try:
        sats = get_rates()
        dict_file = {'hkdrate': sats}
        logger.info(f"attempting to write to rates file: {dict_file}")
        with open(rate_file, 'w') as file:
            documents = yaml.dump(dict_file, file)
        file.close()

    except Exception as e:
        logger.info(e)


attime.start()
asyncio.get_event_loop().run_forever()