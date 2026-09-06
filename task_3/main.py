from items import Book, DVD, Magazine, LibraryItem
from database import Database
from library import Library

db = Database("database.txt")
lib = Library(db)

for record in db.load():
    item = LibraryItem.from_dict(record)
    lib.add_item(item)

print("Available items:")
for item in lib.list_available():
    print(" ", item)

lib.find_by_title("Dune").checkout()
print("After checkout:", lib.find_by_title("Dune"))