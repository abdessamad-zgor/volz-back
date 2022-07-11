from scraper.providers.ProviderClass import Provider
from scraper.spiders.gen_spider import GenSpider
from pathlib import Path
import json
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

def start_spiders(search_params):
    
    try:
        settings = get_project_settings()
        process = CrawlerProcess(settings)
  
        path = Path(os.path.dirname(__file__)).parent
        new_path = os.path.join(path, 'providers/providers.json')
        f= open(new_path, 'r')
        data = json.loads(f.read())
        for provider in data['providers']:
            providerSpec = Provider(provider)
            process.crawl(GenSpider, search_params = search_params, provider_obj = providerSpec)
        process.start()     
    except:
        print('something went wrong')
