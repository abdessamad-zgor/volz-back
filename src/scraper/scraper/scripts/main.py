import sys

from scraper.scripts.scrape import start_spiders



def main():
    start_spiders({"keyword":sys.argv[1], "limit": sys.argv[2]})

if __name__ == '__main__':
    main()
