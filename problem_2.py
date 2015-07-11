import webbrowser
import time

def open_websites(web_list):
	site =""
	tim = 0
	for i in range(0,len(web_list)):
		site = web_list[i][0]
		tim = web_list[i][1]
		if i == len(web_list)-1:
			webbrowser.open(site)
		else:
			webbrowser.open(site)
			time.sleep(tim)

open_websites([["www.google.com", 10], ["www.bing.com", 10], ["www.google.com", 10]])