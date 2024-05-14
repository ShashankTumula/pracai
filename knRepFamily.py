class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def create_family_tree():
    # Define family members
    john = Person("John", "Male")
    mary = Person("Mary", "Female")
    bob = Person("Bob", "Male")
    alice = Person("Alice", "Female")
    peter = Person("Peter", "Male")
    
    # Assign relationships
    john.add_child(bob)
    john.add_child(alice)
    mary.add_child(bob)
    mary.add_child(alice)
    bob.add_child(peter)

    # Return the root of the family tree
    return john


def find_children(person):
    return person.children


def find_siblings(person):
    if not hasattr(person, 'parent') or not person.parent:
        return "This person does not have any siblings."
    siblings = []
    for child in person.parent.children:
        if child != person:
            siblings.append(child)
    return siblings


def main():
    family_tree = create_family_tree()
    print("John's children:", [child.name for child in find_children(family_tree)])
    bob_siblings = find_siblings(family_tree.children[0])
    if isinstance(bob_siblings, list):
        print("Bob's siblings:", [sibling.name for sibling in bob_siblings])
    else:
        print(bob_siblings)


if __name__ == "__main__":
    main()
