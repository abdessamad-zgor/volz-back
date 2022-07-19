#install project dependencies and downlaod geckodriver and place it to a dir contained in $PATH
pkg add python3 curl nodejs 

python3 -m pip install scrapy selenium
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz --output geckodriver.tar.gz
tar -xvfz geckodriver.tar.gz 
mv geckodriver /usr/local/bin/geckodriver

#install node_modules in ./api

cd ./api && yarn install
