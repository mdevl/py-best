"""Unit-tests for best.linalg.

Author:
    Ilias Bilionis

Date:
    7/30/2013

"""


if __name__ == '__main__':
    import fix_path


import unittest
import numpy as np
import best.linalg

print '================================'
print 'Running Linear Algebra Unit Test'
print '================================'
print ''
print ''


class BestLinAlgTest(unittest.TestCase):

    def test_kron_prod(self):
        print '-------------------------------'
        print 'Testing best.linalg.kron_prod()'
        print '-------------------------------'
        A1 = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
        A2 = A1
        A = (A1, A2)
        x = np.random.randn(A1.shape[1] * A2.shape[1])
        y = best.linalg.kron_prod(A, x)
        z = np.dot(np.kron(A1, A2), x)
        print 'Compare best.linalg.kron_prod(A, x):'
        print y
        print 'with np.dot(np.kron(A1, A2), x):'
        print z

    def test_kron_solve(self):
        print '--------------------------------'
        print 'Testing best.linalg.kron_solve()'
        print '--------------------------------'
        A1 = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
        A2 = A1
        A = (A1, A2)
        y = np.random.randn(A1.shape[1] * A2.shape[1])
        x = best.linalg.kron_solve(A, y)
        z = np.linalg.solve(np.kron(A1, A2), y)
        print 'Compare best.linalg.kron_solve(A, y):'
        print x
        print 'with np.linalg.solve(np.kron(A1, A2), y):'
        print z


if __name__ == '__main__':
    unittest.main()