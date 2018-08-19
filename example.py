from urllib.request import urlopen
from bs4 import BeautifulSoup as bsoup

website = urlopen("http://www.worldometers.info/world-population/population-by-country/")
page_source = website.read()
website.close()

source = bsoup(page_source,"html.parser")

data_table = source.findAll("tr")

population = {}
size = {}

for i in list(range(1,len(data_table))):

	all_td = data_table[i].findAll("td")

	name = all_td[1].text
	pop = all_td[2].text
	area = all_td[6].text

	population[name] = pop
	size[name] = area

def user_input():
	print ("Country Information Database\n\n")

	search = input("Enter Country Name : ")

	if search in population:

		print ("\n\nCountry Name : "+search)
		print ("Population   : "+population[search])
		print ("Area         : "+size[search])
		print ("\n\n")
		prompt_user()

	else:
		print ("Country Not Found !!\n\n")
		prompt_user()

def prompt_user():
	choice = int(input("1.Search For Country information\n2.Exit Program\n"))

	if choice == 1:
		user_input()

	elif choice == 2:
		quit()

	else:
		print ("Invalid Option !!!\n\n")
		prompt_user()

prompt_user()
