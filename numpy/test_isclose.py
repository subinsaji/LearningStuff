import numpy
import math

def test_numsa_numsb():
    dwell_time = 0.0004



    nums_a = dwell_time*1000
    nums_b = numpy.rint(dwell_time*1000)



    is_it_close = numpy.isclose(nums_a, nums_b, rtol=1.e-5)
    
    if is_it_close is True:
        

test_numsa_numsb()

