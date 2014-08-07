import unittest
import sys
sys.path.insert(0,'../');

from source.HelloWorld import HelloWorld

class TestHello ( unittest.TestCase):
	def setUp(self):
		pass
	def test_default( self):
		x = HelloWorld();
		self.assertEqual( x.func1(),'Hello world')
	def test_user( self):
		x = HelloWorld();
		self.assertEqual( x.func2('Jim'),'Hello Jim')

if __name__ == '__main__':
	unittest.main()

