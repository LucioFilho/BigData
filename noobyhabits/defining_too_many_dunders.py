def defining_too_many_dunders():
    class Person:
        def __init__(self, name: str, friends: set):
            self.name = name
            self.friends = friends

        def __hash__(self):  # fine
            return hash(self.name)

        def __iadd__(self, other): # why?
            self.friends.add(other)
            other.friends.add(self)
            return self

        def add_friend(self, other):
            self.friends.add(other)
            other.friends.add(self)

    p1 = Person("James", set())
    p2 = Person("Other James", set())

    p1 += p2  # friends!
    p1.add_friend(p2)