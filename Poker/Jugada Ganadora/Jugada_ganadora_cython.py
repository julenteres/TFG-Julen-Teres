import trace
import sys
from Jugada_ganadora_cython_main import Jugada_ganadora_cy

if __name__ == "__main__":
    with open("trace_jugada_ganadora_cython.txt","w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer = trace.Trace(trace=True, count=False)
        tracer.runfunc(Jugada_ganadora_cy)
        sys.stdout = old_stdout

    Jugada_ganadora_cy()

