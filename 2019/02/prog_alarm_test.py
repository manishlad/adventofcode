#!/usr/bin/env python

import unittest

import prog_alarm

class IntcodeTests(unittest.TestCase):

    def test_run_prog(self):
        self.assertEqual(prog_alarm.run_prog(
            [1,9,10,3,2,3,11,0,99,30,40,50]),
            [3500,9,10,70,2,3,11,0,99,30,40,50])
        self.assertEqual(prog_alarm.run_prog(
            [1,0,0,0,99]),
            [2,0,0,0,99])
        self.assertEqual(prog_alarm.run_prog(
            [2,3,0,3,99]),
            [2,3,0,6,99])
        self.assertEqual(prog_alarm.run_prog(
            [2,4,4,5,99,0]),
            [2,4,4,5,99,9801])
        self.assertEqual(prog_alarm.run_prog(
            [1,1,1,4,99,5,6,0,99]),
            [30,1,1,4,2,5,6,0,99])


if __name__ == '__main__':
    unittest.main()
