class Person:
    def __init__(self, name):
        self.name = name
        self.friends = set()

    def add_friend(self, friend):
        # Time complexity: O(1) - Adding to a set is O(1)
        # Space complexity: O(1) - Only a reference is added
        self.friends.add(friend)
        friend.friends.add(self)

    def get_friends(self):
        # Time complexity: O(1) - Returning a reference to the set
        # Space complexity: O(1) - Only the reference is returned
        return self.friends

    def __str__(self):
        return self.name


def find_common_friends(person1, person2):
    # Time complexity: O(min(f1, f2)) where f1 and f2 are the number of friends of person1 and person2
    # Space complexity: O(min(f1, f2)) for storing the common friends
    return person1.get_friends().intersection(person2.get_friends())

def find_nth_connection(person1, person2):
    from collections import deque

    # Time complexity: O(V + E) where V is the number of persons (vertices) and E is the number of friendships (edges)
    # Space complexity: O(V) for the visited set and O(V) for the queue in the worst case
    visited = set()
    queue = deque([(person1, 0)])

    while queue:
        current_person, level = queue.popleft()
        if current_person == person2:
            return level
        if current_person not in visited:
            visited.add(current_person)
            for friend in current_person.get_friends():
                queue.append((friend, level + 1))

    return -1


if __name__ == "__main__":
    # Creating Persons
    alice = Person("Alice")
    bob = Person("Bob")
    janice = Person("Janice")
    charlie = Person("Charlie")
    dave = Person("Dave")

    # Creating Friendships
    alice.add_friend(bob)
    bob.add_friend(janice)
    alice.add_friend(charlie)
    charlie.add_friend(dave)

    # Find friends of Alice and Bob
    # Time complexity: O(1) for each get_friends call
    # Space complexity: O(F) where F is the number of friends
    print(f"Friends of Alice: {[str(friend) for friend in alice.get_friends()]}")
    print(f"Friends of Bob: {[str(friend) for friend in bob.get_friends()]}")

    # Find common friends of Alice and Bob
    # Time complexity: O(min(f1, f2))
    # Space complexity: O(min(f1, f2))
    common_friends = find_common_friends(alice, bob)
    print(f"Common friends of Alice and Bob: {[str(friend) for friend in common_friends]}")

    # Find nth connection
    # Time complexity: O(V + E)
    # Space complexity: O(V)
    connection = find_nth_connection(alice, janice)
    print(f"Alice and Janice are connected with {connection} degree(s) of separation")

    connection = find_nth_connection(alice, dave)
    print(f"Alice and Dave are connected with {connection} degree(s) of separation")
    
    connection = find_nth_connection(alice, bob)
    print(f"Alice and Bob are connected with {connection} degree(s) of separation")

    connection = find_nth_connection(alice, alice)
    print(f"Alice and Alice are connected with {connection} degree(s) of separation")
