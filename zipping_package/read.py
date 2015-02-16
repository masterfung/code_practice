import os

from zipping_package.compressed import bzipped, gzipped

extension_mapping = {
	'.bz2': bzipped.opener,
	'.gz': gzipped.opener
}

class Read:
	def __init__(self, filename):
		extension = os.path.sqlitext(filename)[1]
		opener = extension_mapping.get(extension, open)
		self.f = opener(filename, 'rt')

	def close(self):
		self.f.close()

	def read(self):
		return self.f.read()