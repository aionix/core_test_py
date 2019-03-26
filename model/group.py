from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    #Same as toString()
    def __repr__(self):
        return "name:%s, id:%s, header:%s, footer:%s" % (self.name, self.id, self.header, self.footer)

    #Same as equals()
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.name == other.name) #and self.header == other.header

    def sort_by_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

