
string = input("Enter String: ")
length = len(string) + 2
tape = ['B']*length
i = 1
tapehead = 1
for s in string: #loop to place string in tape
    tape[i] = s
    i += 1

state = 0
# state 7 is final state
#assigning characters to variable so that don't have to use characters each time
a, b, X, Z, U, V, R, L, B = 'a', 'b', 'X', 'Z', 'U', 'V', 'R', 'L', 'B' 
oldtapehead = -1
accept = False

def action(input_char, replace_with, move, new_state):
    global tapehead, state
    if tape[tapehead] == input_char:
        tape[tapehead] = replace_with
        state = new_state
        if move == 'L':
            tapehead -= 1
        else:
            tapehead += 1
        return True
    return False


while(oldtapehead != tapehead): 
    oldtapehead = tapehead    
        

    if state == 0:
        if action(a, b, R, 1) or action( B , B , L, 7 ) :
            pass

    elif state == 1:
        if action( B, B, L, 2) or action(a, a, R, 1) :
            pass
        
    elif state == 2:
        if action(a, B, L, 3) or action(b , B, L , 6) :
            pass
            
    elif state == 3:
        if action(a, a , L, 3) or action( b , b , R , 4) :
            pass
    
    elif state == 4:
        if action(a, b, R, 1) or action(B, B, L , 5) :
            pass
        
    elif state == 5:
        if action(b, a, L, 5) or action(B, B, R, 0) :
            pass
            
    elif state == 6:
        if action(B, B, L, 7) :
            pass          
    
    else:
        accept = True
        
            
if accept:
    print("accepted")
else:
    print("not accepted")