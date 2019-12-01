#!/usr/bin/env python

import unittest

import fuel_req

class FuelReqTests(unittest.TestCase):

    def test_calculate_fuel_req(self):
        self.assertEqual(fuel_req.calculate_fuel_req(12), 2)
        self.assertEqual(fuel_req.calculate_fuel_req(14), 2)
        self.assertEqual(fuel_req.calculate_fuel_req(1969), 654)
        self.assertEqual(fuel_req.calculate_fuel_req(100756), 33583)

    def test_calculate_fuel_req_recursively(self):
        self.assertEqual(
            fuel_req.calculate_fuel_req_recursively(14),
            2)
        self.assertEqual(
            fuel_req.calculate_fuel_req_recursively(1969),
            (654 + 216 + 70 + 21 + 5))
        self.assertEqual(
            fuel_req.calculate_fuel_req_recursively(100756),
            (33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2))


if __name__ == '__main__':
    unittest.main()
