import unittest

class TestandoMetodosStrings(unittest.TestCase):
    
    def test_maiuscula(self):
        self.assertEqual('sapato'.upper(),'SAPATO')
    
    def test_emaiuscula(self):
        self.assertTrue('CADEIRA'.isupper())
        self.assertTrue('CHAMEGO'.isupper())
        
    def test_split(self):
        frase = 'tudo posso Naquele que me fortalece'
        self.assertEqual(frase.split(),['tudo','posso','Naquele','que','me','fortalece'])
        with self.assertRaises(TypeError):
            frase.split(10)


if __name__ == '__main__':
    unittest.main()
          
    
