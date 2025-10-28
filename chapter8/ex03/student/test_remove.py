import unittest

from arrayqueue import ArrayQueue
from linkedqueue import LinkedQueue

class RemoveTestsBase:
    def assertQueueEquals(self, q, expected):
        self.assertEquals(list(q), expected)

class TestArrayQueueRemove(unittest.TestCase, RemoveTestsBase):
    def test_remove_existing(self):
        q = ArrayQueue(range(1, 11))
        # mimic testqueue sequence: pop two, add five
        q.pop(); q.pop()
        for count in range(5):
            q.add(count)
        # remove 6 and verify
        q.remove(6)
        expected = [3, 4, 5, 7, 8, 9, 10, 0, 1, 2, 3, 4]
        self.assertQueueEquals(q, expected)
        self.assertEqual(len(q), 12)

    def test_remove_only_element(self):
        q = ArrayQueue()
        q.add('x')
        removed = q.remove('x')
        self.assertEqual(removed, 'x')
        self.assertTrue(q.isEmpty())

    def test_remove_not_found(self):
        q = ArrayQueue(range(1,5))
        with self.assertRaises(KeyError):
            q.remove(99)

class TestLinkedQueueRemove(unittest.TestCase, RemoveTestsBase):
    def test_remove_existing(self):
        q = LinkedQueue(range(1, 11))
        q.pop(); q.pop()
        for count in range(5):
            q.add(count)
        q.remove(6)
        expected = [3, 4, 5, 7, 8, 9, 10, 0, 1, 2, 3, 4]
        self.assertQueueEquals(q, expected)
        self.assertEqual(len(q), 12)

    def test_remove_only_element(self):
        q = LinkedQueue()
        q.add('x')
        removed = q.remove('x')
        self.assertEqual(removed, 'x')
        self.assertTrue(q.isEmpty())

    def test_remove_not_found(self):
        q = LinkedQueue(range(1,5))
        with self.assertRaises(KeyError):
            q.remove(99)

if __name__ == '__main__':
    unittest.main()
