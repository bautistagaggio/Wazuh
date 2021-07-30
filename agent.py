
class agent:
    def __init__(self, id, name, version, os, inventory, modules, status):
        self.id = id
        self.name = name
        self.version = version       
        self.os = os
        self.inventory = inventory
        self.modules = modules    # ver esto de modules
        self.status = status


    def show_attributes(self):
        print(
        self.id,
        self.name,
        self.version,
        self.os,
        self.inventory,
        self.modules,
        self.status)
    
        
    

        


