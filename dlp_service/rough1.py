# import subprocess
# import sys

# path = sys.executable
# print(f"path: {path}")




def func1():
    try:
        print(f"try block executed")
        raise Exception("something went wrong")
    except Exception as e:
        print(f"manual error: {e}")
        return {
            "result": True,
            "message": "except block returned this obj"
        }

print(f"func1 return statement: {func1()}")