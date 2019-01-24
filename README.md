# weather-station

This is a weather display for a Kindle. 

Rename pass.yml.EXAMPLE to pass.yml

Modify pass.yml with your actual Darksky key, coodinates and your Apixu key and zip

To run by executing launch.sh

View in Kindle with current.html

If you want to view it on your computer go to new.html

I do this like:

   	   http://192.168.0.1:8000/new.html

I serve this by running:

	nohup python -m SimpleHTTPServer 8000 &


PREREQUISITES:
   ImageMagick
   python
   bash
   yq
   jq

Run this with crontab as below
	
	*/15 * * * * /<Directory>/launch.sh 2>/dev/null

I run this on OS X
