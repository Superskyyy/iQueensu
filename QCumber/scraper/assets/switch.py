class Switch(object):
    # Copied from http://code.activestate.com/recipes/410692/
    # Created by Brian Beck on Mon, 25 Apr 2005 (PSF)
    # Efficiency: O(n)
    # Reason of why python have no switch: http://www.python.org/peps/pep-0275.html
    def __init__(self, expr):
        self.value = expr
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False
