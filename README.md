# weather-station

This is a Weather Console for a Kindle or other readers or a computer. 

It uses the weather APIs from Darksky and Apixu

TO INSTALL:

Rename pass.yml.EXAMPLE to pass.yml

Modify pass.yml with your actual Darksky key, coodinates and your Apixu key and zip

TO RUN execut launch.sh using crontab like this

Type crontab -e and add this line

	*/15 * * * * /<Root-directory-of-project>/launch.sh 2>/dev/null

Serve this on the server (Mac) by typing this line in the root directory of this project.

	nohup python -m SimpleHTTPServer 8000 &

You will have to retype the above command every time you reboot your server.

View with Kindle at current.html

If you want to view it on your computer go to new.html. It rotates 90 degrees

Both the web pages refresh every 15 minutes to match the cron schedule.

I visit this page from my device by browsing to:

   	   http://192.168.0.1:8000/new.html  or

   	   http://192.168.0.1:8000/current.html

with a browser. Type ~ds in search window on reader and then visit

      http://192.168.0.1:8000/current.html or new.html

on the device. On the server I serve this applcation by running:

You don't need to us port 8000. You can use any port

PREREQUISITES:
   - ImageMagick
   - pngcrush
   - python
   - bash
   - yq
   - jq

PYTHON:
   - pip install webkit2png

This is unorgabized for now but is my bash history egrep install.

    3  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   14  brew install yq
   15  brew install jq
   20  brew install ImageMagick
   41  brew install pngcrush
   51  brew install pngcrush
  351  brew install node
  354  brew install node
  369  pip install webkit2png
  377  python python-webkit2png/setup.py install
  378  sudo python python-webkit2png/setup.py install
  379  brew flashplugin-installer
  380  brew install flashplugin-installer
  381  sudo python python-webkit2png/setup.py install
  382  npm install --save html-to-image
  383  sudo npm install npm
  384  sudo npm install --save html-to-image
  486  npm install xmlhttprequest
  488  npm install xmlhttp
  617  h | egrep install


I run this on OS X

- REL_0.10

-- Enjoy

----------------

![alt text](https://raw.githubusercontent.com/tjordanchat/weather-station/master/assets/img.png)


