def parent():
    print("Printing from the parent() function")
    
    def first_child():
        print("printing from the first_child() function")
        
    def second_child():
        print("Printing from the second child funcion")
        
    second_child()
    first_child()
    
parent() 

        
        