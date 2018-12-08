from main.bus_stops import BusStop
import unittest

class TestBusStopMethods(unittest.TestCase):   
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_bus_stop_is_In(self):
        # Arrange
        bs = BusStop()

        # Act
        bs.minimumTimeToEnd(0,1,2,3)

        # Assert

    def test_bus_stop_given_example(self):
        '''
        {self} reference to class
        {returns} void
        '''

        # Arrange
        bs = BusStop()
        num_bus_stops = 4
        bus_stop_locations = [0,10,40,100]
        bus_intervals = 20
        bus_speed = 10
        num_of_passengers = 3
        passenger_1 = [0,0,4]
        passenger_2 = [15,10,1]
        passenger_3 = [40,2,16]
        passengers = [passenger_1, passenger_2, passenger_3]
        expected = [10,30,5.75]

        # Act
        min = bs.minimumTimeToEnd(bus_stop_locations, bus_intervals, bus_speed, passengers)

       
