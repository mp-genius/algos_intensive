string = input()
if string[0] == ')':
    out = 'Ne ok'
else:
    counter = 1
    for i in range(1, len(string)):
        if string[i] == ')':
            counter -= 1
            if counter < 0:
                break
        elif string[i] == '(':
            counter += 1

    if counter == 0:
        out = 'Ok'
    else: 
        out = 'Ne ok'

print(out)
    
        
