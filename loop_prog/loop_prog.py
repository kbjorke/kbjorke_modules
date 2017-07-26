import sys
import time

class ProgressBar():
    def __init__(self):
        self.fill_char = '='
        self.fill_tip = '>'
        self.width = 30
        self.fields = 0
        self.percent = 0
        self.counter = 0
        self.prog_bar = list("[%s%s]   0%%" % (self.fill_tip, 
                                               ' '*(self.width-1)))

    def __call__(self, steps):
        _fields = int(self.width*float(self.counter)/steps)
        _percent_done = int(100*float(self.counter)/steps)
        if _fields-self.fields == 0:
            pass
        else:
            self.fields += _fields-self.fields
            self.prog_bar[1:1+self.fields] = (self.fields-1)*self.fill_char +\
                    self.fill_tip
            self._update()
        
        if _percent_done-self.percent == 0:
            pass
        else:
            self.percent += _percent_done-self.percent
            self.prog_bar[-4:-1] = '%3d' % self.percent
            self._update()
                
        self.counter += 1

    def begin(self):
        sys.stdout.write('\r'+''.join(self.prog_bar))
        sys.stdout.flush()

    def _update(self):
        sys.stdout.write('\r'+''.join(self.prog_bar))
        sys.stdout.flush()


    def end(self):
        self.prog_bar = list('['+ self.fill_char*self.width + ']'+
                             ' 100% - Complete!\n') 
        
        sys.stdout.write('\r'+''.join(self.prog_bar))
        sys.stdout.flush()

progress = ProgressBar()

        
if __name__ == '__main__':

    import cProfile
    import pstats
    import StringIO
    
    # Time test:
    N = 1000000
    
    pr = cProfile.Profile()
    pr.enable()
    # With progressbar:
    start_time = time.time()
    progress.begin()
    for i in range(1,N):
        a = 1 + 2
        progress(N)
    progress.end()
    elapsed_time_progress = time.time() - start_time
    pr.disable()

    #Without progressbar:
    start_time = time.time()
    for i in range(1,N):
        a = 1 + 2
    elapsed_time = time.time() - start_time

    print "Time with progressbar,    N=%d : %f s" % (N,elapsed_time_progress)
    print "Time without progressbar, N=%d : %f s" % (N, elapsed_time)    

    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print s.getvalue()

"""
kribjork@kribjork-laptop:loop_prog$ python loop_prog.py 
[==============================] 100% - Complete!
Time with progressbar,    N=10000000 : 21.780617 s
Time without progressbar, N=10000000 : 1.345005 s
"""
# Code need optimalization, 20x running time when using progressbar to high!
