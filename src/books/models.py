# database models

from typing import Optional

class Book():    
    def __init__(self, id, title, category):
        self.id = id
        self.title = title
        self.category = category
