from pymongo import MongoClient
from pprint import pprint
import json
import paho.mqtt.client as mqtt
from time import gmtime, strftime, sleep
import os, sys
output_dir: str='c:/data/one'
if not os.path.isdir(output_dir) :
	oldmask = os.umask(000)
	os.makedirs( output_dir, 777 )
	os.umask(oldmask)

pprint("1")

mongo_client =  None
mongoDbConnected = False
while  not mongoDbConnected:
	try:
		mongo_client = MongoClient('127.0.0.1', 27017)
		mongoDbConnected = True
	except:
		sleep(1)
		mongoDbConnected = False
pprint("2")

def on_connect(client, userdata, flags, rc):
    client.subscribe("/anenometer/one")

def on_message(client, userdata, msg):
	pprint("5")

	data: str=msg.payload.decode()
	write_file(data)
	db = mongo_client.my_anenometer
	collection = db.my_collection_20181101
	pprint("6")
	collection.insert(data)
	pprint("7")


def write_file(data):
	newtimestamp: str =strftime("%Y%m%d%H", gmtime())
	file_name = output_dir+"/"+newtimestamp+".anemo"
	pprint("8") 
	with open(file_name, 'a') as x_file:
		pprint(data)
		x_file.write(data+"\n")

mqtt_client = None
mqtt_client_connected = False

while not mqtt_client_connected:
	try:
		mqtt_client = mqtt.Client()
		mqtt_client.connect("127.0.0.1",1883,60)
		mqtt_client_connected = True
		pprint("3")
	except:
		sleep(1)
		mqtt_client_connected = False


mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
pprint("4")

mqtt_client.loop_forever()


#d = json.loads("{\"dd\":11, \"dds\":\"ddw\"}")
#pprint(d);
