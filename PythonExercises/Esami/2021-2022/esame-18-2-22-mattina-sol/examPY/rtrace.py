class TraceRecursion:
    """ A decorator class to trace the recursive function calls.
        To enable it, type the following import statement
          from rtrace import trace
        and prepend
          @trace
        to the functions you want to monitor.
    """
    def __init__(self, f):
        self.f = f
        self.traceP = False
        self.countP = False
        self.indent = 0
        self.callsNum = 0

    def count(self, *args, **kargs):
        self.traceP = False
        self.countP = True
        self.callsNum = 0
        answer = self.__call__(*args, **kargs)
        print('Num calls:', self.callsNum)
        self.countP = False
        return answer

    def trace(self, *args, **kargs):
        self.traceP = True
        self.countP = True
        self.indent = 0
        self.callsNum = 0
        print('------------------- Starting recursion -------------------')
        answer = self.__call__(*args, **kargs)
        print('-------------------- Ending recursion --------------------')
        print('Num calls:', self.callsNum)
        self.countP = False
        self.traceP = False
        return answer

    def __call__(self, *args, **kargs):
        """Counts and traces (if requested) the function calls"""
        if self.traceP:
            indent     = '|--'*self.indent
            callString = self.f.__name__
            if args : callString += str(args)
            if kargs: callString += str(kargs)
            print(indent+" entering", callString, sep='\t')
            self.indent += 1
        if self.countP:
            self.callsNum += 1
        answer = self.f(*args, **kargs)
        if self.traceP:
            self.indent -= 1
            print(indent+' exiting ', callString, "returns", answer, sep='\t')
        return answer


trace = TraceRecursion