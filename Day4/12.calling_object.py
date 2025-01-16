class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
#up to this Cat object is not callable
#Make it callable
    def __call__(self, *args, **kwds):
        print('yes, Cat is callable')
#same result in easier way    
    def call_me(self, *args, **kwds): #kwds = keywords, args = arguments
        print('yes, Cat is callable in this way as well')
rino = Cat("Rino")
print(rino)

value = 10

rino()
rino.call_me()