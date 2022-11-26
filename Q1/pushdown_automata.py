string = input("Enter String: ")
tape = ['B']*100
i = 1
tapehead = 1
accept = False
for s in string:
    tape[i] = s
    i += 1

state = 1
a , b , c , one , B , l = 'a' , 'b' , 'c' , '1' , '$' , 'lambda'
stack1 = []
stack2 = []
stack1.append(B)
stack2.append(B)

def shit():
    print(stack1)
    print(stack2 , " at state" , state)
    print('----------------------------------------------------------')

def transition(input_char , left_t_stack1 , right_t_stack1 , left_t_stack2 , right_t_stack2 , new_state):
    global state , tapehead
    if tape[tapehead] == input_char or input_char == 'lambda':
        
        s1 = stack1.pop()
        s2 = stack2.pop()

        is_S1_available , is_S2_available = False , False  

        # check stack 1 ================================================================================================
        if ( s1 == left_t_stack1 ):        
            if(right_t_stack1 != 'lambda'):
                stack1.append(right_t_stack1)            
            is_S1_available = True            

        if( left_t_stack1 == 'lambda' ):
            stack1.append(s1)
            if(right_t_stack2 != 'lambda'):
                stack1.append(right_t_stack1)            
            is_S1_available = True
        # check stack 2 ================================================================================================
        if ( s2 == left_t_stack2 ):        
            if(right_t_stack2 != 'lambda'):    
                stack2.append(right_t_stack2)             
            is_S2_available = True

        if( left_t_stack2 == 'lambda' ):
            stack2.append(s2)
            if(right_t_stack2 != 'lambda'):
                stack2.append(right_t_stack2)
            is_S2_available = True        

        # =============================================================================================================
        if is_S1_available and is_S2_available :
            if(input_char != 'lambda'):
                tapehead = tapehead + 1
            state = new_state
            return True
        else :            
            stack1.append(s1)
            stack2.append(s2)            
            return False     
    else:
        return False                 

oldtapehead = -1

while (True):    

    # first column ================================================================================================
    if(state == 1 ):
        if transition(a , l , one , l , one , 2 ) or transition(b , l , one , l , one , 3 ) or transition(c , l , one , l , one , 4 ) :
            shit()
            pass

    # second column ================================================================================================
    elif(state == 2):
        if transition(a , l , one , l , one , 2 ) or transition(b , one , l , l , one , 5 ) or transition(c , one , l , l , one , 6 ) :
            shit()
            pass

    elif(state == 3):
        if transition(b , l , one , l , one , 3 ) or transition(a , one , l , l , one , 7 ) or transition(c , one , l , l , one , 8 ) :
            shit()
            pass

    elif(state == 4):
        if transition(c , l , one , l , one , 4 ) or transition(a , one , l , l , one , 9 ) or transition(b , one , l , l , one , 10 ) :
            shit()
            pass
        
    # third column ================================================================================================
    elif(state == 5):
        if   transition(b, one , l , l , one , 5 ) or transition( l , B  , B , l , l , 11):            
            shit()
        else :
            print('breaking')
            break            

    elif(state == 6):
        if transition(c, one , l , l , one , 6 ) or transition( l , B  , B , l , l , 12):            
            shit()
            pass
        else :
            break
    
    elif(state == 7):
        if transition(a, one , l , l , one , 7 ) or transition( l , B  , B , l , l , 13):            
            shit()
            pass
        else :
            break
    
    elif(state == 8):
        if transition(c, one , l , l , one , 8 ) or transition( l , B  , B , l , l , 14):            
            shit()
            pass
        else :
            break

    elif(state == 9):
        if transition(a, one , l , l , one , 9 ) or transition( l , B  , B , l , l , 15):            
            shit()
            pass
        else :
            break

    elif(state == 10):
        if transition(b, one , l , l , one , 10 ) or transition( l , B  , B , l , l , 16):            
            shit()
            pass
        else :
            break

    # fourth column ================================================================================================

    elif( state == 11 ) :
        print("in state 11")
        if transition( c , B , B , one , l , 11 ) or transition( l , B  , B , B , B , 17 ):            
            shit()
            pass  
        else :
            break

    elif( state == 12 ) :
        if transition( b , B , B , one , l , 12 ) or transition( l , B  , B , B , B , 17 ):            
            shit()
            pass 
        else :
            break

    elif( state == 13 ) :
        if transition( c , B , B , one , l , 13 ) or transition( l , B  , B , B , B , 17 ):            
            shit()
            pass 
        else :
            break 

    elif( state == 14 ) :
        if transition( a , B , B , one , l , 14 ) or transition( l , B  , B , B , B , 17 ):            
            shit()
            pass 
        else :
            break 

    elif( state == 15 ) :
        if transition( b , B , B , one , l , 15 ) or transition( l , B  , B , B , B , 17 ):            
            shit()
            pass 
        else :
            break 

    elif( state == 16 ) :
        if transition( a , B , B , one , l , 16 ) or transition( l , B  , B , B , B , 17 ):            
            shit()
            pass 
        else :
            break 

    # fiveth column ================================================================================================

    else :
        accept = True
        break

print(accept)