#!/usr/bin/env python

import json

class Path_Generator:
    def __init__(self, js, path):
        self.path = path.split("/")
        self.json = js
        self.generate_json(self.json, self.path, 1)

    def generate_json(self, json, path, index):
        if index < len(path):
            if path[index] == "angle":
                json["angle"] = 0
                return json
            
            if path[index] in json.keys():
                self.generate_json(json[path[index]], path, index + 1)
            else:
                json[path[index]] = {}
                self.generate_json(json, path, index)

class Value_Finder:
    def __init__(self, js, path):
        self.value = None
        self.path = path.split("/")
        self.get_value_from_path(js, self.path[1], 1)
    
    def get_value_from_path(self, js, key, index):
        for i in range(1, len(self.path)):
            key = self.path[i]
            js = js[key]
        self.value = js

class Path_Finder:
    def __init__(self, json):
        self.json = json
        self.path = []
        self.get_path_by_key(json, [])

    def get_path_by_key(self, json, path):
        for key, value in json.items():
            if "control" in json.keys() and path:
                self.path.append(self.list_to_string(path, "/"))
                break

            if isinstance(value, dict):
                path.append(key)
                self.get_path_by_key(json[key], path)

        if path:
            path.pop()

    def list_to_string(self, liste, split_key):
        string = ""

        for key in liste:
            string += split_key + key

        return string

class Writer:
    def __init__(self, js, json_file_path):
        self.file = open(json_file_path, 'w')
        self.file.write(json.dumps(js, indent=4))

class Reader:
    def __init__(self, json_file_path):
        self.file = open(json_file_path, 'r')
        self.js = json.load(self.file)