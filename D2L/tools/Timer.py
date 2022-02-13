import time

import numpy


class Timer:
    def __init__(self):
        self.times = []
        self.start()

    def start(self) -> None:
        self.tik = time.time()

    def stop(self) -> float:
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def avg(self) -> float:
        return numpy.average(self.times)

    def sum(self) -> float:
        return numpy.sum(self.times)
    
    def cum_sum(self) -> numpy.ndarray:
        return numpy.cumsum(self.times)
