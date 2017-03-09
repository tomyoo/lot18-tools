import csv
import json

def main():
	with open('infile.csv') as infile:
		reader = csv.DictReader(infile)
		rows = list(reader)

	for row in rows:
		if row['New?'] == 'Yes':
			item_id = row['item_id']
			grapes = str(row['grapes'].split(', ')).replace('\'', '"').lower()
			region = str(row['region'].split(', ')).replace('\'', '"')
			flavors = str(row['flavors'].split(', ')).replace('\'', '"').lower()
			pairings = str(row['pairings'].split(', ')).replace('\'', '"').lower()
			output = ''
			output += '{\n'
			output += '  "item_id": "{0}",\n'.format(item_id)
			output += '     "bottle": {\n'
			output += '         "name": "{0}",\n'.format(row['name'])
			output += '         "wine_type": "{0}",\n'.format(row['wine_type'])
			output += '         "vintage": {0},\n'.format(row['year'])
			output += '         "brand": "{0}",\n'.format(row['brand'])
			output += '         "classification": "{0}",\n'.format(row['classification'])
			output += '         "grapes": {0},\n'.format(grapes)
			output += '         "region": [{0}],\n'.format(region)
			output += '         "flavors": [{0}],\n'.format(flavors)
			output += '         "pairings": [{0}],\n'.format(pairings)
			output += '         "attributes": {\n'
			output += '             "body": {0},\n'.format(row['body']).lower()
			output += '             "fruit": {0},\n'.format(row['fruit']).lower()
			output += '             "earth": {0},\n'.format(row['earth']).lower()
			output += '             "tannin": {0},\n'.format(row['tannin']).lower()
			output += '             "oak": {0},\n'.format(row['oak']).lower()
			output += '             "acidity": {0}\n'.format(row['acidity']).lower()
			output += '         },\n'
			output += '         "tasting_note": "{0}"\n'.format(row['tasting_note'])
			output += '     }\n'
			output += '}'

			outfile = open("{0}.json".format(item_id), "w")
			outfile.write(output)
			outfile.close

if __name__ == "__main__":
	main()