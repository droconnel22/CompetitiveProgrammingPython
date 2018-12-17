
import bisect

class BusStop:
    def __init__(self, *args, **kwargs):
        pass
    
    def minimumTimeToEnd(self, x, w, v, q):
        """
        :param self: reference to the class
        :param x: number of stops
        :param w: interval of bus in minutes
        :param v: speed of bus in meters.per.minute
        :param q: q-th passenger attributes array of integers
        :returns: integer of time for passenger.
        :note::Take the descriptions of the people from standard input and print the answers to standard output
        """
        for passenger in q:
            upper_bound = min([x for x in x if x > passenger[0]])


        # time to walk to bus abs(start pos - stop pos)/s
        # time for waiting for bus = bus number * w + bus_arrival_off_set
        # time on bus = last stop pos - sto pos / v

        

        print('in like flynn')
        return 10
        
