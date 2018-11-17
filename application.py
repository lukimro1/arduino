from flask import Flask
import os, sys
import os.path
import time
application = Flask(__name__)
 
@application.route("/")
def hello():
	if os.path.isfile ("c:/data/one/"+time.strftime("%Y%m%d%H")+".anemo") :	
    		return "Saved "
	else :
		return "Not saved" 	

if __name__ == "__main__":
    application.run()
