import unittest
from unittest.mock import patch
from service.pet_service import PetService

class TestPetService(unittest.TestCase):
    def setUp(self):
        self.pet_service = PetService()

    def test_coletar_nome(self):
        with patch('builtins.input', return_value='Bob'):
            nome = self.pet_service.coletar_nome()
            self.assertEqual(nome, 'Bob')

    def test_coletar_idade_valida(self):
        with patch('builtins.input', return_value='5'):
            idade = self.pet_service.coletar_idade()
            self.assertEqual(idade, 5)

    def test_coletar_peso_valido(self):
        with patch('builtins.input', return_value='5'):
            peso = self.pet_service.coletar_peso()
            self.assertEqual(peso, 5)

if __name__ == '__main__':
    unittest.main()