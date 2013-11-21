import unittest
from sometimes import (sometimes, sometimesish,
                       percent_of_the_time, rarely, mostly, times)


class TestSometimesDecorators(unittest.TestCase):

    def setUp(self):
        self.counter = 0

    def test_sometimes(self):
        """Test function is only run exactly half the times"""
        self.counter = 0

        @sometimes
        def add_one():
            self.counter += 1

        for x in range(0, 100000):
            add_one()

        self.assertEqual(self.counter, 50000)

    def test_sometimesish(self):
        """Test function is ran about 50% of the time"""
        self.counter = 0

        @sometimesish
        def add_one():
            self.counter += 1

        for x in range(0, 100000):
            add_one()

        self.assertTrue(self.counter in range(49500, 50500))

    def test_percent_of_the_time(self):
        """Test function runs a set percentage of the time, or fairly closely"""
        self.counter = 0

        @percent_of_the_time(10)
        def add_one():
            self.counter += 1

        for x in range(0, 100000):
            add_one()

        self.assertTrue(self.counter in range(9500, 10500))

    def test_rarely(self):
        """Test something occurs only rarely"""
        self.counter = 0

        @rarely
        def add_one():
            self.counter += 1

        for x in range(0, 100000):
            add_one()

        self.assertTrue(self.counter in range(4500, 5500))

    def test_mostly(self):
        """Test function runs most of the time"""
        self.counter = 0

        @mostly
        def add_one():
            self.counter += 1

        for x in range(0, 100000):
            add_one()

        self.assertTrue(self.counter in range(90000, 110000))

    def test_times_big(self):
        """Test that function runs a random number of times within a range"""
        self.counter = 0

        @times(10000, 50000)
        def add_one():
            self.counter += 1

        add_one()

        self.assertTrue(self.counter in range(10000, 50000))

    def test_times_small(self):
        """Test that function runs a random number of times within a small range"""
        self.counter = 0

        @times(1, 5)
        def add_one():
            self.counter += 1

        add_one()
        self.assertTrue(self.counter in range(1, 5))

    def test_times_doesnt_run(self):
        """Test that if given a range of zero times doesn't run"""
        self.counter = 0

        @times(0, 0)
        def add_one():
            self.counter += 1

        add_one()
        self.assertEqual(self.counter, 0)

if __name__ == '__main__':
    unittest.main()
