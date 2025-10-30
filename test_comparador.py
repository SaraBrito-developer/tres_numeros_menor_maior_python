# -*- coding: utf-8 -*-
import unittest
from comparador import encontrar_maior, encontrar_menor

class TestComparador(unittest.TestCase):

    # --- Testes para ENCONTRAR_MAIOR ---

    def test_maior_primeiro(self):
        """Testa o maior sendo o primeiro (Caso de falha original)"""
        self.assertEqual(encontrar_maior(10, 2, 5), 10)

    def test_maior_meio(self):
        """Testa o maior sendo o do meio"""
        self.assertEqual(encontrar_maior(2, 10, 5), 10)

    def test_maior_ultimo(self):
        """Testa o maior sendo o último"""
        self.assertEqual(encontrar_maior(2, 5, 10), 10)

    # --- Testes para ENCONTRAR_MENOR ---

    def test_menor_primeiro(self):
        """Testa o menor sendo o primeiro"""
        self.assertEqual(encontrar_menor(2, 10, 5), 2)

    def test_menor_meio(self):
        """Testa o menor sendo o do meio"""
        self.assertEqual(encontrar_menor(10, 2, 5), 2)

    def test_menor_ultimo(self):
        """Testa o menor sendo o último (Caso de falha original)"""
        self.assertEqual(encontrar_menor(10, 5, 2), 2)

    # --- Testes de Casos de Borda ---
    
    def test_numeros_iguais(self):
        """Testa se todos os números são iguais"""
        self.assertEqual(encontrar_maior(5, 5, 5), 5)
        self.assertEqual(encontrar_menor(5, 5, 5), 5)

    def test_com_negativos(self):
        """Testa com números negativos"""
        self.assertEqual(encontrar_maior(-10, -5, -20), -5)
        self.assertEqual(encontrar_menor(-10, -5, -20), -20)
        
    def test_com_zero(self):
        """Testa com zero"""
        self.assertEqual(encontrar_maior(0, -5, 10), 10)
        self.assertEqual(encontrar_menor(0, -5, 10), -5)

if __name__ == '__main__':
    unittest.main()
