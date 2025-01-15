

def render(width, height, symbol):
    first_line = symbol*width + '\n'
    middle_line = (symbol+' '*(width-2) + symbol+'\n')*(height-2)
    last_line = symbol*width
    #return symbol*width+'\n' +(symbol+' '+'\n')*(width-2)+symbol*width
    return first_line+middle_line+last_line
print(render(10,5,'@'))