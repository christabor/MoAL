class strlist(list):

    """A list that only allows strings,
    and adds some useful helper methods."""

    def up(self):
        map(lambda x: x.upper(), self)

    def down(self):
        map(lambda x: x.lower(), self)


class intlist(list):
    pass

