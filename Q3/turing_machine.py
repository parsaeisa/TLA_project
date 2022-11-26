
string = input("Enter String: ")
tape = ['B']*100
i = 1
tapehead = 1
for s in string:
    tape[i] = s
    i += 1

state = 0
# state 19 is final state

b, R, L, B , one = 'b' , 'R', 'L', 'B' , '1'
oldtapehead = -1
accept = False

def pprint(tape):
    for ch in tape :
        if(ch != 'B'):
            print(ch , end = " ")    
    print(" ")

def transition(left_t, right_t, move, new_state):
    global tapehead, state
    if tape[tapehead] == left_t:
        tape[tapehead] = right_t
        state = new_state
        if move == 'L':
            tapehead -= 1
        else:
            tapehead += 1
        return True
    return False

while(oldtapehead != tapehead): 
    oldtapehead = tapehead
    
    if(state == 15):
        pprint(tape)

    # number is odd or even -------------------------------------------------------

    if state == 0:
        if transition(B, B, L, 1) or transition( one ,one , R, 0 ) :
            pass

    elif state == 1:
        if transition( one , b, L, 2) or transition( b , b, L, 5) :
            pass
        
    elif state == 2:
        if transition(one, one, L, 2) or transition(b , b, R , 3) or transition(B , B , R , 3) :
            pass
            
    elif state == 3:
        if transition( one, b , R, 4) or transition( b , b , L , 22) :
            pass
    
    elif state == 4:
        if transition(one, one, R, 4) or transition(b, b, L , 1) :            
            pass

    elif state == 22 : 
        if transition(b , b , R , 11 ) or transition(B , B , R , 11):
            pass
        
    # if number is even part -------------------------------------------------------

    elif state == 5:
        if transition(b, b, L, 5) or transition(B, B, R, 6) :            
            pass
            
    elif state == 6:
        if transition(b, one, R, 6) or transition(B, B, L, 7) :
            pass          

    elif state == 7:
        if transition(one, B, L, 8) :
            pass          
    
    elif state == 8:
        if transition(one, one, L, 8) or transition(b , b , R , 9) or transition(B , B , R , 9):
            pass          
    
    elif state == 9:
        if transition(one, b, R, 21) or transition(one , one , R , 10)  :
            pass          
    
    elif state == 10:
        if transition(B, B, L, 7) or transition(one , one , R , 10) :
            pass      

    elif state == 21 :
        if transition(one , one , R , 10 ) or transition( B , B , L , 18):
            pass 

    # if number is odd part -------------------------------------------------------

    elif state == 11:
        if transition(B, B, L, 12) or transition(b ,b , R , 11) :            
            pass          
    
    elif state == 12:
        if transition(one, one, L, 12) or transition(b , one , R , 13) or transition(B , B , R , 20) :
            pass          
    
    elif state == 13:
        if transition(B, one , R, 14) or transition(one , one , R , 13) :
            pass          
    
    elif state == 14:
        if transition(B, one, L, 12) :
            pass          

    elif state == 20 :
        if transition( one , one , R , 20 ) or transition(B , one , L , 15):
            pass

    # if number is one part ---------------------------------------------------------
    
    elif state == 15:
        if transition(one, one, R, 16) or transition(b, one, R, 16) :
            pass          
    
    elif state == 16:
        if transition(B, B, L, 19) or transition(one , one , L , 17) :
            pass          
    
    elif state == 17:
        if transition(B, B, R, 0) or transition(one , one , L , 17) :
            pass          

    elif state == 18:
        if transition(b, one, L, 18) or transition(B , B , R , 15) :
            pass          
        
    else:
        accept = True        