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

	for js in json_files:
		print(js)
		with open(os.path.join(path_to_json, js)) as json_file:
			loaded_file = json.load(json_file)
			label = loaded_file['bottle']['image_urls']['label']
			bottle = loaded_file['bottle']['image_urls']['bottle']
			thumb = loaded_file['bottle']['image_urls']['bottle_thumb']
			if not label == None and not url_exists(label):
				missing_files.append(label)
			if not bottle == None and not url_exists(bottle):
				missing_files.append(bottle)
			if not thumb == None and not url_exists(thumb):
				missing_files.append(thumb)

	if len(missing_files) > 0:
		print("Missing Files:")
		for file in missing_files:
			print(file)
	else:
		print("All URLs are Gucci! :)")

if __name__ == "__main__":
	main()
