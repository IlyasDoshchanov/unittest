import unittest
import model

class Testmodel(unittest.TestCase):
    

    def test_updateAlbums(self):
        self._model = model.Model()
        self._model.updateAlbums(5, "Luck")
        test = self._model.getAlbumsSQL()
        self.assertIn(['Luck', 5], test)



if __name__ == '__main__':
    unittest.main()