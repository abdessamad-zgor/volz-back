
# setup virtual enviroment on new machine
python3 -m pip install venv
python3 -m venv .
source ./bin/activate.sh
#install project dependencies and downlaod geckodriver and place it to a dir contained in $PATH
python3 -m pip install scrapy selenium
curl -s https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz --output geckodriver.tar.gz
tar -xvfz geckodriver.tar.gz 
mv geckodriver /usr/local/bin/geckodriver
