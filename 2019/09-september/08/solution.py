# Need a function to ensure that if we are pushing the max value of the stack
# onto the stack that the value added is always the largest in the stack

# let x be input val, and maxVal be the current maximum
#   x > maxVal
#   x - maxVal > 0
#   2x - maxVal > x
# If we insert 2x - maxVal instead, then it will always be larger than x, and
# therefore always the largest value in the stack

class MaxStack:
    def __init__(self):
        # Fill this in.
        self.stack = []
        self.contentCount = {}
        self.maxVal = None


    def push(self, val):
        # Fill this in.
        if self.maxVal == None:
            self.maxVal = val

        if val > self.maxVal:
            tmpVal = val
            val = 2*val - self.maxVal
            self.maxVal = tmpVal
        self.stack.append(val)


    def pop(self):
        # Fill this in.
        val = self.stack.pop()

        # The only way this is possible is if it is the max val that we popped
        # off because we modify the input value to be greater than maxVal
        if val > self.maxVal:
            ret = self.maxVal
            # val is 2*maxVal - prevMaxVal for previous max val. To get
            # previous maxVal:
            #   val = 2*maxVal - prevMaxVal
            #   prevMaxVal = 2*maxVal - val
            self.maxVal = 2*self.maxVal - val
        else:
            ret = val

        if len(self.stack) == 0:
            self.maxVal = None;
        return ret

    def max(self):
        # Fill this in.
        return self.maxVal

s = MaxStack()
print s.max() == None
s.push(1)
print s.max() == 1
s.push(2)
print s.max() == 2
s.push(3)
print s.max() == 3
s.push(2)
print s.max() == 3
s.pop()
print s.max() == 3
s.pop()
print s.max() == 2
s.pop()
print s.max() == 1
s.pop()
print s.max() == None
