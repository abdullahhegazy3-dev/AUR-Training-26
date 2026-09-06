from items import LibraryItem 
class Library:
    def __init__(self, database):
        self._items = []
        self._db = database

    def add_item(self, item):
        self._items.append(item)

    def find_by_title(self, title):
        for item in self._items:
            if item._title.lower() == title.lower():
                return item
        raise ValueError("not found")

    def list_available(self):
        return [i for i in self._items if i.status.name == "AVAILABLE"]