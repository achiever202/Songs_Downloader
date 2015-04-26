import urllib2

def download(url, filename):

	# This sets the headers to act as a browser.
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	urllib2.install_opener(opener)

	# opening the file and retrieving the url.
	test_file = open(filename, 'wb')
	u = urllib2.urlopen(url)

	# extracting the file information.
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	file_size_mb = float(file_size)/(1000000.0)
	print "Downloading: %s (Total Size): %.2f MB" % (filename, file_size_mb)

	file_size_dl = 0
	block_sz = 8192

	# downloading the file and printing status.
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    test_file.write(buffer)

	    file_size_dl_mb = float(file_size_dl)/1000000.0
	    status = r"Downloaded: %.2f MB [%3.2f%%]" % (file_size_dl_mb, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,

	test_file.close()

download('http://link1.songspk.name/song1.php?songid=10556', "galliyan.mp3")