import unittest

from molecular_weight.csv_reader import CSVReader
from molecular_weight.molecular_weight import MolecularWeight


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.reader = CSVReader('../resources/element_weights.csv')
        self.reader.read()
        self.mw = MolecularWeight(self.reader.data)

    def test_hydrogen(self):
        self.assertEqual(0, self.mw.process("H0"))
        self.assertEqual(1.008, self.mw.process("H"))
        self.assertEqual(2.016, self.mw.process("H2"))
        self.assertEqual(3.024, self.mw.process("H3"))
        self.assertEqual(4.032, self.mw.process("H4"))

    def test_oxygen(self):
        self.assertEqual(0, self.mw.process("O0"))
        self.assertEqual(15.999, self.mw.process("O"))
        self.assertEqual(31.998, self.mw.process("O2"))
        self.assertEqual(47.997, self.mw.process("O3"))
        self.assertEqual(63.996, self.mw.process("O4"))

    def test_h2o(self):
        self.assertEqual(18.015, self.mw.process("H2O"))

if __name__ == '__main__':
    unittest.main()
