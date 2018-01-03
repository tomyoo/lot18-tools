import httplib, sys, os, json
from urlparse import urlparse

def url_exists(url):
    _, host, path, _, _, _ = urlparse(url)
    conn = httplib.HTTPConnection(host)
    conn.request('HEAD', path)
    return conn.getresponse().status < 400

def main():
	path_to_json = 'json/'
	json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
	
	missing_files = []
	null_files_that_exist = []
	null_wines = []

	for js in json_files:
		print("Checking {}".format(js))
		with open(os.path.join(path_to_json, js)) as json_file:
			loaded_file = json.load(json_file)
			inventory_id = loaded_file['item_id']
			label = loaded_file['bottle']['image_urls']['label']
			bottle = loaded_file['bottle']['image_urls']['bottle']
			thumb = loaded_file['bottle']['image_urls']['bottle_thumb']
			if not label == None and not url_exists(label):
				missing_files.append(label)
			elif label == None and (url_exists("https://partner.wineassets.net/{}_label.jpg".format(inventory_id)) or url_exists("https://partner.wineassets.net/{}_label.jpeg".format(inventory_id)) or url_exists("https://partner.wineassets.net/{}_label.jpe".format(inventory_id))):
				null_files_that_exist.append("label for {}".format(inventory_id))
			elif label == None:
				null_wines.append("label for {}".format(inventory_id))
			if not bottle == None and not url_exists(bottle):
				missing_files.append(bottle)
			elif bottle == None and url_exists("https://partner.wineassets.net/{}_bottle.png".format(inventory_id)):
				null_files_that_exist.append("bottle for {}".format(inventory_id))
			elif bottle == None:
				null_wines.append("bottle for {}".format(inventory_id))
			if not thumb == None and not url_exists(thumb):
				missing_files.append(thumb)
			elif thumb == None and url_exists("https://partner.wineassets.net/{}_bottle_thumb.png".format(inventory_id)):
				null_files_that_exist.append("thumb for {}".format(inventory_id))
			elif thumb == None:
				null_wines.append("thumb for {}".format(inventory_id))

	if len(missing_files) > 0 or len(null_wines) > 0 or len(null_files_that_exist) > 0:
		if len(missing_files) > 0:
			print("Missing Files:")
			for file in missing_files:
				print(file)
		if len(null_wines) > 0:
			print("Null Wines:")
			for file in null_wines:
				print(file)
		if len(null_files_that_exist) > 0:
			print("Null Wines That Exist:")
			for file in null_files_that_exist:
				print(file)
	else:
		print("All URLs are Gucci! :)")

if __name__ == "__main__":
	main()
