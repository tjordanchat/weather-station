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
   - python
   - bash
   - yq
   - jq

I run this on OS X

- REL_0.1

-- Enjoy

----------------

![alt text](https://raw.githubusercontent.com/tjordanchat/weather-station/master/assets/img.png)


