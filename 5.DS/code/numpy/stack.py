# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(11, 20).reshape(3, 3)
b = np.arange(21, 30).reshape(3, 3)
print(a, b, sep='\n')
c = np.vstack((a, b))
print(c)
a, b = np.vsplit(c, 2)
print(a, b, sep='\n')
c = np.hstack((a, b))
print(c)
a, b = np.hsplit(c, 2)
print(a, b, sep='\n')
c = np.dstack((a, b))
print(c)
a, b = np.dsplit(c, 2)
print(a.T[0].T, b.T[0].T, sep='\n')
a = a.ravel()
b = b.ravel()
print(a, b, sep='\n')
c = np.row_stack((a, b))
#c = np.vstack((a, b))
print(c)
#c = np.column_stack((a, b))
#c = np.hstack((a, b))
c = np.c_[a, b]
print(c)
