#  Unpacking Elements from Iterables of Arbitrary Length

# You need to unpack N elements from an iterable, but the iterable may be longer than N
# elements, causing a “too many values to unpack” exception.
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')


# Python “star expressions” can be used to address this problem.
name, email, *phone_numbers = user_record

print(name)
print(email)
print(phone_numbers)
