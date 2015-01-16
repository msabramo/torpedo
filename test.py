import unittest

import torpedo

class TorpedoTests(unittest.TestCase):

	def test_ip(self):
		ip1 = torpedo.get_ip()
		torpedo.refresh_ip()
		ip2 = torpedo.get_ip()
		assert(ip1 != ip2)

	def test_fetch(self):
		b = torpedo.headless()
		p1 = b.get('http://example.com')
		s = torpedo.session()
		p2 = s.get('http://example.com')
		assert True
