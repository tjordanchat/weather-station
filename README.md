# weather-station

This is a Weather Console for a Kindle or other readers or a computer. 

It uses the weather APIs from Darksky and Apixu

To install:

Rename pass.yml.EXAMPLE to pass.yml

Modify pass.yml with your actual Darksky key, coodinates and your Apixu key and zip

To run by executing launch.sh

View in Kindle with current.html

If you want to view it on your computer go to new.html. It rotates 90 degrees

Both the web pages refresh every 15 minutes to match the cron schedule.

I visit this page like this:

   	   http://192.168.0.1:8000/new.html

type ~ds in search window on reader and then visit

      http://blablabla:8000/new.html

on the device.  I serve this app by running:

	nohup python -m SimpleHTTPServer 8000 &

in the root directory of this project.

You don't need to us port 8000. You can use any port

PREREQUISITES:
   - ImageMagick
   - python
   - bash
   - yq
   - jq

Run this with crontab as below
	
	*/15 * * * * /<Directory-of-project>/launch.sh 2>/dev/null

I run this on OS X



