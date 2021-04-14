#!/usr/bin/env python 3

# Import libraries
import sqlite3
import numpy as np
import io
from datetime import datetime
import os

# Methods used so that the type numpy.ndarray can be stocked into the database
def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

# Converts np.array to TEXT when inserting
sqlite3.register_adapter(np.ndarray, adapt_array)

# Converts TEXT to np.array when selecting
sqlite3.register_converter("array", convert_array)

# Get database directory path
directory = os.path.join(os.path.realpath(os.path.dirname(__file__)),"database")

class database():
    """
    A class used to access to the database

    Attributes
    ----------
    connexion : sqlite3.Connection
        SQLite database connection object 
    cursor : sqlite3.Cursor
        SQLite database cursor object

    Methods
    -------
    load_database()
        Set the connexion with the database (creates the database if needed)
    update_database(name, emb)
        Prints the animals name and what sound it makes
    change_name(old_name,new_name)
        Change the name of a user
    check_name(name)
        Check if the user with the input name exists
    sup_name(name)
        Delete the user with the input name
    reset_database()
        Reset the dataset by deleting all elements of the table users
    """

    def __init__(self):
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.load_database()        

    def load_database(self):
        """
        Set the connexion with the database (creates the database if needed)

        Parameters
        ----------
        connexion : sqlite3.Connection
            SQLite database connection object 
        cursor : sqlite3.Cursor
            SQLite database cursor object
        """
        try:
            # Set the connexion and the cursor
            self.connexion = sqlite3.connect(os.path.join(directory,"database.db"), detect_types=sqlite3.PARSE_DECLTYPES)
            self.cursor = self.connexion.cursor()
            # Create the table users
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                name TEXT PRIMARY KEY ,
                genre INTEGER,
                age INTEGER,
                date NUMERIC,
                emb array
            )''')
            # Commit the changes
            self.connexion.commit()
        except Exception as err:
            print(f"Error: We didn't manage to open the database\n", err)
        
    
    def update_database(self, name, emb):
        """
        Add new users to the database

        Parameters
        ----------
        name : str or list
            the name(s) of the user(s) to add
        emb : numpy.ndarray
            the face embedding(s) of the user(s) to add 
        Returns
        -------
        bool
            result of the operation
        """    

        if type(name) != list:
            names = [name]
            embs = [emb]
            
        for name in names:
            if self.check_name(name):
                return False
        
        data = [(name.title(), datetime.now(), emb) for name, emb in zip(names, embs)]
        self.cursor.executemany("INSERT INTO users (name,date,emb) VALUES (?,?,?)", data)
        self.connexion.commit()
        return True
    
    def change_name(self, old_name, new_name):
        """
        Change the name of a user

        Parameters
        ----------
        old_name : str
            current name of the user to modify
        new_name : str
            new name of the user
        """
        self.cursor.execute("UPDATE users SET name = ? WHERE name = ?",
        (old_name.title(),new_name.title(),)) 
        self.connexion.commit()
    
    def check_name(self, name):
        """
        Check if the user with the input name exists

        Parameters
        ----------
        name : str
            name of the user to delete

        Returns
        -------
        bool
            whether the user is in the database
        """  
        self.cursor.execute("SELECT name FROM users WHERE name = ?", (name.title(),))
        if len(self.cursor.fetchall()) > 0:
            return True
        return False
    
    def sup_name(self,name):
        """
        Delete the user with the input name

        Parameters
        ----------
        name : str
            name of the user to delete
        """
        self.cursor.execute("DELETE FROM users WHERE name = ?", (name.title(),))
        self.connexion.commit()

    def get_image_emb(self):
        """
        
        """
        self.cursor.execute("SELECT name FROM users")
        names = self.cursor.fetchall()
        self.cursor.execute("SELECT emb FROM users")
        embs = self.cursor.fetchall()
        names = [name[0] for name in names]
        embs = [emb[0] for emb in embs]
        return names, embs
                    
    def reset_database(self):
        """
        Reset the dataset by deleting all elements of the table users
        """ 
        self.cursor.execute("DROP TABLE users")
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE,
                genre INTEGER,
                age INTEGER,
                date NUMERIC,
                emb array
            )''')
        self.connexion.commit()
