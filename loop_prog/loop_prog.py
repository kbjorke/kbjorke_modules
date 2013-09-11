import sys

class ProgressBar():
    def __init__(self):
        self.rog_bar = '[]'
        self.fill_char = '='
        self.fill_tip = '>'
        self.width = 30
        self.fields = 0
        self.counter = 0
        self.prog_bar = list('['+ self.fill_tip +' '*(self.width-1) + ']'+
                             '   0%') 

    def __call__(self, steps):
        _fields = int(self.width*float(self.counter)/steps)
        if _fields-self.fields == 0:
            pass
        else:
            _percent_done = int(100*float(_fields)/self.width)
            self.fields += _fields-self.fields
            self.prog_bar[1:1+self.fields] = (self.fields-1)*self.fill_char +\
                    self.fill_tip
            self.prog_bar[-4:-1] = '%3d' % _percent_done

            sys.stdout.write('\r'+''.join(self.prog_bar))
            sys.stdout.flush()
                
        self.counter += 1

    def begin(self):
        sys.stdout.write('\r'+''.join(self.prog_bar))
        sys.stdout.flush()

    def end(self):
        self.prog_bar = list('['+ self.fill_char*self.width + ']'+
                             ' 100% - Complete!\n') 
        
        sys.stdout.write('\r'+''.join(self.prog_bar))
        sys.stdout.flush()

progress = ProgressBar()

        
if __name__ == '__main__':

    N = 1000000
    progress.begin()
    for i in range(1,N):
        progress(N)
    progress.end()
