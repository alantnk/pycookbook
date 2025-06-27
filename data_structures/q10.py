#  Sorting Objects Without Native Comparison Support

# You want to sort objects of the same class, but they don’t natively support comparison
# operations.
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User({self.user_id})'


users = [User(23), User(2), User(9)]

sorted_users = sorted(users, key=attrgetter('user_id'))

print(sorted_users)