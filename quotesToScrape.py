#! /usr/bin/env python3
from bs4 import BeautifulSoup
import requests

for i in range(1,6):
	res = requests.get('http://quotes.toscrape.com/page/' + str(i))
	soup = BeautifulSoup(res.text, 'html.parser')

	quotes = soup.find_all('div', {'class':'quote'})
	print("Page No:" + str(i))
	print()
	for q in quotes:
		msg = q.find('span', {'class':'text'})
		auth = q.find('small')
		print(msg.text)
		print(auth.text)
		print()