class CacheFunction:
    def __init__(self,func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        if args in self.cache:
            print(f"wynik w cache dla argumentów: {args}")
            return self.cache[args]
        
        print(f"wynik obliczeń dla argumentów: {args}")
        result = self.func(*args)
        self.cache[args] = result
        return result
