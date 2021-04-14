import json
import copy
import numpy as np

class api_infos():
    def __init__(self):
        self.name = 'api_keys.json'
        self.load_json_file()
        
    def load_json_file(self):
        self.data = {}
        try:
            with open(self.name,"r") as json_file:
                self.data = json.load(json_file)
        except IOError:
            self.save_api_infos()

    def add_api_infos(self,name,based_url,credentials,args,returned_args,sep_args,sep_arg_val,example): #keys doit être un dico
        self.data[name] = {"based_url":based_url,"credentials":credentials, "args":args,"returned_args":returned_args,"sep_args":sep_args,"sep_arg_val":sep_arg_val, "example":example}
        
    def save_api_infos(self):
        try:
            with open(self.name,'w') as json_file:
                json.dump(self.data,json_file,indent=4)
            return True
        except IOError:
            return False   

        
def example():
    api = api_infos()
    name = "News"
    based_url = "http://newsapi.org/v2/"
    keys = "d931f89016084e26aa8e0714ce06afbc"
    args = {"top-headlines?":{"args":["country","category","sources","q","page_size","page","apiKey"],"val":[["ae", "ar", "at", "au" ,"be", "bg", "br", "ca", "ch", "cn", "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se", "sg", "si", "sk", "th", "tr", "tw", "ua", "us", "ve", "za"],["business", "entertainment", "general", "health", "science", "sports", "technology"],None,None,[i for i in range(100)],None,None],"Required":[-1]},
            "everything?":{"args":["q","qInTitle","sources","domains","excludeDomains","from","to","language","sortBy","pageSize","page","apiKey"],"val":[None,None,None,None,None,None,None,["ar","de","en","es","fr","he","it","nl","no","pt","ru","se","ud","zh"],["relevancy", "popularity", "publishedAt"],[i for i in range(100)],None,None],"Required":[-1]},
            "sources?":{"args":["category","language","country","apiKey"],"val":[["business", "entertainment", "general", "health", "science", "sports", "technology"],["ar","de","en","es","fr","he","it","nl","no","pt","ru","se","ud","zh"],["ae", "ar", "at", "au" ,"be", "bg", "br", "ca", "ch", "cn", "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se", "sg", "si", "sk", "th", "tr", "tw", "ua", "us", "ve", "za"],None],"Required":[-1]}}
    returned_args = {"top-headlines?":["status","totalResults",{"articles":["source","author","title", "description","url","urlToImage","publishedAt","content"]}],
                     "everything":["status","totalResults",{"articles":["source","author","title", "description","url","urlToImage","publishedAt","content"]}],
                     "sources":["status",{"sources":["id","name","description", "url","category","language","country"]}]}
    sep_args = "&"
    sep_arg_val = "="
    example = "http://newsapi.org/v2/top-headlines?country=us&apiKey=d931f89016084e26aa8e0714ce06afbc"
    
    api.add_api_infos(name,based_url,keys,args,returned_args,sep_args,sep_arg_val,example)
    api.save_api_infos() 

import requests  

class api():
    def __init__(self,name):
        self.api_infos = api_infos()
        self.data = self.api_infos.data[name]
        
        class_ = [x for x in self.data["args"]]
        
        self.args = copy.deepcopy(self.data["args"])
        for element in class_:
            del self.args[element]["val"]
        self.returned_args = self.data["returned_args"]        
        
    def request(self,type_,args_list_with_indices,args_values,return_args_desired):
        args = np.array(self.args[type_]["args"])[args_list_with_indices]
        sepa = self.data["sep_args"]
        sepv = self.data["sep_arg_val"]
        url = self.data["based_url"]+type_
        for arg,arg_value in zip(args,args_values):
            url+=arg+sepv+arg_value+sepa
        url+="apiKey"+sepv+self.data["credentials"]
        response = requests.get(url)
        print(url)
        result={}
        if response.status() == 200:
            for element in return_args_desired:
                result[element]=response.json()[element] 
        else:
            print("Error")
        return result        

def top_news():
    api = api("News")
    result = api.request("top-headlines?",[0,1,4],["fr","general","3"],["articles"])

    i = 0
    while i < 3:
        print(result["articles"][i]["title"])
        print(result["articles"][i]["description"])
        print(result["articles"][i]["publishedAt"])
        i+=1

def lastest_news():
    api = api("News")
    result = api.request("top-headlines?",[0,1,4],["fr","general","3"],["articles"])

    i = 0
    while i < 3:
        print(result["articles"][i]["title"])
        print(result["articles"][i]["description"])
        print(result["articles"][i]["publishedAt"])
        i+=1