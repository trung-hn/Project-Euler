def time_this(func):
    def timer(*args,**kwargs):
        import time
        t0=time.time()
        return_value=func(*args,**kwargs)
        print(f"Time taken: {time.time()-t0} second(s)")
        return return_value
    return timer
# @time_this
# def testing(n):
#     return n*2

# print(testing(2))