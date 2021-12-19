from math import *



def loop(start,stop,step):
    x = start
    while float(x) != float(stop):
        x += step
        x = round(x,3)
        yield x
class f:
    def __init__(self,func,interval = [-12,12]):
        self.func = func
        self.interval = interval
        self.points = []
        self.domain = loop(self.interval[0],self.interval[1],0.001)
    def generate_points(self):
        self.func = self.func.replace('x','{x}')
        for i in self.domain:

            try:
                y =  round(eval(self.func.format(x = str(i))),3)
            except:
                pass
            else:
                if -12 <= y <= 12:
                    self.points.append([int(i*50)+600, int(-y*50)+350 ])
        return self.points


 



