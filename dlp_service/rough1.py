# import subprocess
# import sys

# path = sys.executable
# print(f"path: {path}")




# def func1():
#     try:
#         print(f"try block executed")
#         raise Exception("something went wrong")
#     except Exception as e:
#         print(f"manual error: {e}")
#         return {
#             "result": True,
#             "message": "except block returned this obj"
#         }

# print(f"func1 return statement: {func1()}")






from collections import namedtuple

User = namedtuple("User", ["name", "vision", "weapon"])
user1 = User("arlecchino", "pyro", "polearm")
user2 = User("neuvillette", "hydro", "catalyst")
user3 = User("mavuika", "pyro", "clatmore")
print(f"user1: {user1}")
print(f"user2: {user2}")
print(f"user3: {user3}")
combined = []
combined.append(user1)
combined.append(user2)
combined.append(user3)
print(f"combined: {combined}")

for item in combined:
    if "arlecchino" in item:
        print(f"yes, she is present")
    else:
        print(f"no, she is not present")