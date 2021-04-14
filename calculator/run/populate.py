def populate(entry, num):
    current = entry.get()
    entry.delete(0)
    entry.insert(0, str(current) + str(num))