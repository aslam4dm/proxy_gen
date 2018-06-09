import sys
import os
import re
import requests

OPTION = 0

def your_ip():
	link = requests.get("http://myip.dnsdynamic.org/")
	print("your current public ip addr is:", link.text)

def link_options():
	global OPTION
	num = 1
	for l in ["http://free-proxy-list.net", "https://free-proxy-list.net/anonymous-proxy.html", "your ip"]:
		print("{}: {}".format(num, l))
		num += 1
	opt = input("enter option [?]: ")
	if opt == "1": 
		OPTION = 1
		req = requests.get("http://free-proxy-list.net")
		return(req.text)
	elif opt == "2":
		OPTION = 2	
		req = requests.get("https://free-proxy-list.net/anonymous-proxy.html")
		return(req.text)
	elif opt == "3":
		your_ip()	
	else: print("invalid option!")

# technically, regardless of the site selection, the re process will be the same
def proxy_finder(html):
	global OPTION
	proxy_ips = []
	if OPTION == 1:
		print("option 1")
		ips = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td><td>\d{1,4}</td><td>..</td>", html)
		for ip in ips:
			proxy_ips.append(ip.split("</td><td>"))
		counter = 1
		for proxy in proxy_ips:
			print("[selection number: {}] ".format(counter), end="\n")
			for i in proxy:
				print(i.strip("</td>"))
			counter += 1
			print("\n")
		selection = input("enter a selection number [?]: ")
		your_proxy = proxy_ips[int(selection)-1]
		print("your new id: {} on port: {}".format(your_proxy[0], your_proxy[1]))
		return(your_proxy[0],your_proxy[1] )

	elif OPTION == 2:
		print("option 2")
		ips = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td><td>\d{1,4}</td><td>..</td>", html)
		for ip in ips:
			proxy_ips.append(ip.split("</td><td>"))
		counter = 1
		for proxy in proxy_ips:
			print("[selection number: {}] ".format(counter), end="\n")
			for i in proxy:
				print(i.strip("</td>"))
			counter += 1
			print("\n")
		selection = input("enter a selection number [?]: ")
		your_proxy = proxy_ips[int(selection)-1]
		print("your new id: {} on port: {}".format(your_proxy[0], your_proxy[1]))
		return(your_proxy[0], your_proxy[1])		

def set_proxy(proxy):
	# set the proxy up here
	print(proxy)

def main():
	set_proxy(proxy_finder(link_options()))

main()