import sys

from scraper.scripts.scrape import start_spiders



def main():
    start_spiders({"keyword":sys.argv[1], "limit": 10})

if __name__ == '__main__':
    main()
