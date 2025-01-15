
def drawing(x,y):
    print('#'*y)
    for i in range(x-2):
        print('#'+' '*(y-2)+'#')
    print('#'*y)

drawing(int(input("give the size_1: ")),int(input("\ngive the size_2: ")))  

#Version 2: we can use _ instead of i this is a convesion
def render_v1(width, height):
    print('#'*width)
    for _ in range(height-2):
        print('#'+' '*(width-2)+'#')
    print('#'*width)

render_v1(10,5)

#Same with while cycle
def render(width, height):
    print('#'*width)
    count = 0
    while count < height -2:
        print('#'+' '*(width-2)+'#')
        count += 1
    print('#'*width)

render(8,8)