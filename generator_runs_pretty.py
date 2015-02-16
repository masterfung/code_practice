import time
start = time.time()
def inpu(n):
	for i in (x * x for x in xrange(n*n*n)):
		print i
	end = time.time()
	print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))
	print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
inpu(1000)