import json
import re

class JSON_generator:
    def __init__(self,path='inmoov_control.json'):
        self.path = path
        self.open_json()

    def flatten_json(self):
        """
            Flatten json object with nested keys into a single level.
            Args:
                nested_json: A nested json object.
            Returns:
                The flattened json object if successful, None otherwise.
        """
        out = {}

        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '/')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '/')
                    i += 1
            else:
                out[name[:-1]] = x
                    
        flatten(self.control_json)
        self.control_json = out            
    
    def open_json(self):
        with open(self.path) as f:
            self.control_json = json.load(f) 
        self.flatten_json() 
        
    def reset(self):
        for key in self.control_json.keys():
            self.control_json[key] = 0

    def change_values(self, control_dict):
        for key,value in control_dict.items():
            self.control_json[key] = value
            
    def save_json(self):
        temp_dict = {}
        for key, value in self.control_json.items():
            s = temp_dict
            tokens = re.findall(r'\w+', key)
            for count, (index, next_token) in enumerate(zip(tokens, tokens[1:] + [value]), 1):
                value = next_token if count == len(tokens) else [] if next_token.isdigit() else {}
                if isinstance(s, list):
                    index = int(index)
                    while index >= len(s):
                        s.append(value)
                elif index not in s:
                    s[index] = value
                s = s[index]
        self.control_json = temp_dict
                
        with open(self.path, 'w') as outfile:
            json.dump(self.control_json, outfile, indent=4)

        self.flatten_json()