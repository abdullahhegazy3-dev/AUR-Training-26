from items import LibraryItem

class Database:
    def __init__(self, path="database.txt"):
        self.path = path

    def load(self):
        items = []
        with open(self.path) as f:
            for line in f:
                fields = dict(pair.split("=") for pair in line.strip().split("|"))
                items.append(fields)
        return items

    def save(self, items_as_dicts):
        with open(self.path, "w") as f:
            for d in items_as_dicts:
                f.write("|".join(f"{k}={v}" for k, v in d.items()) + "\n")