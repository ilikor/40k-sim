import unittest
import numpy
from DiceSim2 import RollingFunctions as RF


class RollingFunctionsTest(unittest.TestCase):

    def setUp(self):

        self.number = 10000
        self.reroll_target = 3

    def test_rollingd6_interface(self):
        values = RF.rollingd6s(self.number)
        self.assertTrue(len(values) == 6)

    def test_rollingd6_no_lost_dices(self):
        values = RF.rollingd6s(self.number)
        self.assertTrue(numpy.sum(values) == self.number)

    def test_rollingd6_dist(self):
        values = RF.rollingd6s(self.number)
        self.assertTrue(numpy.sqrt(self.number) > numpy.max(values) - numpy.average(values))
        self.assertTrue(numpy.sqrt(self.number) > numpy.average(values) - numpy.min(values))

    def test_rerolld6_interface(self):
        values = RF.rollingd6s(self.number)
        reroll = RF.reroll_d6s(values, self.reroll_target)
        self.assertTrue(len(reroll) == 6)

    def test_rerolld6_no_lost_dices(self):
        x = 1000
        values = [x, 0, 0, 0, 0, 0]
        reroll = RF.reroll_d6s(values, self.reroll_target)
        self.assertTrue(numpy.sum(reroll) == x)

    def test_rerolld6_negative_reroll(self):
        reroll_target = -2
        values = RF.rollingd6s(self.number)
        self.assertRaises(ValueError, RF.reroll_d6s, values, reroll_target)

    def test_rollingdX_time(self):
        self.assertTrue(len(RF.rollingdXs_time_dependant(self.number, 7)) == self.number)

def main():
    unittest.main()


if __name__ == '__main__':
    main()