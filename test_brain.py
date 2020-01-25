import unittest
from brain import Brain
import numpy


class MyTestCase(unittest.TestCase):
    def test_getNewMutant(self):

        brain1 = Brain()
        weights_1 = brain1.model.get_weights()
        weights_2 = brain1.getNewMutant(0,0).model.get_weights()

        for i in range(len(weights_1)):
            if type(weights_1[i]) == numpy.ndarray:
                for j in range(len(weights_1[i]) ):
                    if type(weights_1[i][j]) == numpy.ndarray:
                        if type(weights_1[i][j]) == numpy.ndarray:
                            for k in range(len(weights_1[i][j]) ):
                                self.assertEqual(weights_1[i][j][k], weights_2[i][j][k], "This should be an exact clone but it is not.")

        brain1 = Brain()
        weights_1 = brain1.model.get_weights()
        weights_2 = brain1.getNewMutant(1,.1).model.get_weights()

        for i in range(len(weights_1)):
            if type(weights_1[i]) == numpy.ndarray:
                for j in range(len(weights_1[i]) ):
                    if type(weights_1[i][j]) == numpy.ndarray:
                        if type(weights_1[i][j]) == numpy.ndarray:
                            for k in range(len(weights_1[i][j]) ):
                                self.assertNotEqual(weights_1[i][j][k], weights_2[i][j][k], "Every weight should have been mutated")
                                self.assertAlmostEqual(weights_1[i][j][k], weights_2[i][j][k], delta=.1, msg="Too large of a mutation!")


    def test_name(self):
        brain = Brain()
        mutant = brain.getNewMutant()

        self.assertEqual(brain.first, mutant.first)
        self.assertNotEqual(brain.last, mutant.last)

if __name__ == '__main__':
    unittest.main()
