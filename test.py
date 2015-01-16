import unittest

import torpedo

class TorpedoTests(unittest.TestCase):

	def test(self):
		ip1 = torpedo.get_ip()
		torpedo.refresh_ip()
		ip2 = torpedo.get_ip()
		assert(ip1 != ip2)