import inspect
custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    return float((x**a + y**b) / c)

def fn_w_counter():
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.callers = {}

    fn_w_counter.total_calls += 1
    
    frame = inspect.currentframe().f_back
    caller_name = frame.f_globals.get('__name__', '__main__')
    
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1
    
    return (fn_w_counter.total_calls, fn_w_counter.callers)
