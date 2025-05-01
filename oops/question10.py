class Father:
    def __init__(self):
        pass
    
    def dance(self):
        print("Dance like Michael Jackson")
        
class Mother:
    def __init__(self):
        pass
    
    def dance(self):
        print("Dance like Marry James")
        
class Child(Father, Mother):
    def __init__(self):
        pass
    
    # def dance(self):
    #     print("Dance like Michael Jackson")
    
child = Child()
child.dance()