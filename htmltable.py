#Goal 2- html table
contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner'},
    'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}

for contact, info in contacts.items():
	print """<table border="1">\n<tr>\n<td colspan="2"> {0}\n</td>\n</tr>\n<tr>\n<td>Phone: {1}</td>\n<td> Twitter: {2}\n</td>\n<td> Github: {3} </td>\n</tr>\n</table>""".format(contact, info['phone'], info['twitter'], info['github'])
