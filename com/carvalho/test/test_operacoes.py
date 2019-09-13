from unittest import TestCase
from com.kuma.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
	
	def test_soma(self):
		self.assertEqual(self.operacoes.soma([1, 5]), 6, 'Deveria ser 6')
