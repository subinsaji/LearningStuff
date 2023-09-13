
def parent(num):
    
    def first_child():
        return "Hi am first child "
    
    def second_child():
        return "Hi am second child"
    
    if num == 1:
        return first_child 
    
    else: return second_child
    
    
first = parent(1)
second = parent(2)

