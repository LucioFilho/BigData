class Thingy:

    @property
    def val(self):
        # long computation
        ...
        return 42


def expensive_properties():
    thing = Thingy()

    val = thing.val  # if val is property, looks CHEAP

    val = thing.val()  # if val is function, looks maybe expensive

