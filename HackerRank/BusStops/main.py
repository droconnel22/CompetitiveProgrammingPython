
#!/bin/python3

import os
import sys
import unittest
from test.bus_stops_test_fixture import TestBusStopMethods

# Run from Parent directoy so all module references are preserved.
if __name__ == '__main__':
    t = TestBusStopMethods()   
    unittest.main()    