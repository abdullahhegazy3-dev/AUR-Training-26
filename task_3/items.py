from abc import ABC, abstractmethod
from enum import Enum, auto

class ItemStatus(Enum):
    AVAILABLE = auto()
    CHECKED_OUT = auto()
    LOST = auto()

class LibraryItem(ABC):
    def __init__(self, title):
        self._title = title            
        self._status = ItemStatus.AVAILABLE

    @property
    def status(self):                
        return self._status

    @property
    @abstractmethod
    def loan_period_days(self):      
        pass

    def checkout(self):
        if self._status != ItemStatus.AVAILABLE:
            raise ValueError(f"{self._title} is not available")
        self._status = ItemStatus.CHECKED_OUT

    def return_item(self):
        self._status = ItemStatus.AVAILABLE
   
    def __lt__(self, other):
     return self._title.lower() < other._title.lower()

    def __repr__(self):
     return f"{type(self).__name__}(title={self._title!r}, status={self._status.name})"

    def __str__(self):   
     return f"{self._title} ({type(self).__name__}) — {self._status.name}"
    _registry = {}

    def __init_subclass__(cls, type_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if type_name:
            LibraryItem._registry[type_name] = cls
            cls.type_name = type_name



    @classmethod
    def from_dict(cls, data):
        target_cls = LibraryItem._registry[data["type"]]
        return target_cls(data["title"])     
class Book(LibraryItem, type_name="Book"):
    @property
    def loan_period_days(self):
     return 21       
    @staticmethod
    def validate_isbn13(isbn):
        digits = [int(c) for c in isbn if c.isdigit()]
        if len(digits) != 13:
            return False
        total = sum(d * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits[:12]))
        check = (10 - total % 10) % 10
        return check == digits[12]
 
 
class DVD(LibraryItem, type_name="DVD"):
    @property
    def loan_period_days(self):
     return 5      
    
class Magazine(LibraryItem, type_name="Magazine"):
    @property
    def loan_period_days(self):
        return 14