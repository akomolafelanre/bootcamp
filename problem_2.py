import webbrowser
import time

def open_websites(web_list):
	site =""
	tim = 0
	for item in web_list:
		site = item[0]
		tim = item[1]
		webbrowser.open(site)
		time.sleep(tim)

open_websites([["www.google.com", 10], ["www.google.com", 10]])