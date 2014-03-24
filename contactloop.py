#Goal 1 - print out contacts

contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner'},
    'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}

for contact, info in contacts.items():
	print "{0}'s contact infomation is: \n phone: {1} \n twitter: {2} \n github: {3}".format(contact, info['phone'], info['twitter'], info['github'])

#Goal 2- html table
for contact, info in contacts.items():
	print """<table border="1">\n<tr>\n<td colspan="2"> {0}\n</td>\n</tr>\n<tr>\n<td>Phone: {1}</td>\n<td> Twitter: {2}\n</td>\n<td> Github: {3} </td>\n</tr>\n</table>""".format(contact, info['phone'], info['twitter'], info['github'])