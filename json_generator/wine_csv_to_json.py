import csv
import json

def main():
    with open('infile.csv') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    for row in rows:
        if row['New to club?'] == 'Yes':
            item_id = row['item_id']
            grapes = str(row['grapes'].split('; ')).replace('\'', '"')
            region = str(row['region'].split('; ')).replace('\'', '"')
            flavors = str(row['flavors'].split('; ')).replace('\'', '"').lower()
            pairings = str(row['pairings'].split('; ')).replace('\'', '"').lower()
            abv = str(row['abv'].replace('%', ""))
            output = ''
            output += '{\n'
            output += '     "item_id": "{0}",\n'.format(item_id)
            output += '     "sku_type": "bottle",\n'
            output += '     "bottle": {\n'
            output += '         "name": "{0}",\n'.format(row['name'])
            output += '         "wine_type": "{0}",\n'.format(row['wine_type'])
            output += '         "vintage": {0},\n'.format(row['year'])
            output += '         "brand": "{0}",\n'.format(row['brand'])
            output += '         "classification": "{0}",\n'.format(row['classification'])
            output += '         "abv": "{0}",\n'.format(abv)
            output += '         "grapes": {0},\n'.format(grapes)
            output += '         "region": {0},\n'.format(region)
            output += '         "flavors": {0},\n'.format(flavors)
            output += '         "pairings": {0},\n'.format(pairings)
            output += '         "attributes": {\n'
            output += '             "body": {0},\n'.format(row['body']).lower()
            output += '             "fruit": {0},\n'.format(row['fruit']).lower()
            output += '             "earth": {0},\n'.format(row['earth']).lower()
            output += '             "tannin": {0},\n'.format(row['tannin']).lower()
            output += '             "oak": {0},\n'.format(row['oak']).lower()
            output += '             "acidity": {0}\n'.format(row['acidity']).lower()
            output += '         },\n'
            output += '         "short_tasting_note": "{0}",\n'.format(row['short_tasting_note'])
            output += '         "tasting_note": "{0}",\n'.format(row['tasting_note'])
            output += '         "image_urls": {\n'
            output += '             "label": "https://partner.wineassets.net/{0}_label.jpeg",\n'.format(item_id)
            output += '             "bottle": "https://partner.wineassets.net/{0}_bottle.png",\n'.format(item_id)
            output += '             "bottle_thumb": "https://partner.wineassets.net/{0}_bottle_thumb.png"\n'.format(item_id)
            output += '         }\n'
            output += '     }\n'
            output += '}\n'

            outfile = open("{0}.json".format(item_id), "w")
            outfile.write(output)
            outfile.close

if __name__ == "__main__":
    main()