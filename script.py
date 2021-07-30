import agent
import json

class script:

    #loads data
    def load_data(self):
        f = open('data.json',)
        data = json.load(f)
        for d in data['agents']:
            return d

 
    # assuming data is an instance of the agent's class
    def push_data(self,data):
        with open('data2.json', 'w') as f:
            json.dump(data, f)
            f.write(data)
        f.close()
    
    # prints data
    def print_all(self):
        data = self.load_data()
        print (data)
    

    def main_function(self):
        f = open('data.json',)
        data = json.load(f)
        for d in data['agents']:
            print
    


        


        
    


