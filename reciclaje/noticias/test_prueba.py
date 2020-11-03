import unittest
from prueba import listar, contacto

class TestProbar(unittest.TestCase):
    def test_listar(self):
        self.assertEqual(listar(1),1)
        self.assertEqual(listar(0),1)

    def test_contacto(self):
        self.assertTrue(contacto('Juana', 'juana@gmail.com', 123345678, 'Hola', 2, False))
        self.assertFalse(contacto('Romia', 'romina@gmail.com', 'Sin numero', 'Chao', 1, True))