from typing import Callable
from getpass import getpass

owner = {
    "login": "owner",
    "password": "1212"
}

def only_owner_allowed(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("before call ----------------")
        user_login = input("Enter your login: ")
        user_password = getpass("Enter your password: ")
        if user_login == owner["login"] and user_password == owner["password"]:
            result = func(*args, **kwargs)
            print("after call -----------------")
            return {"result": result}
        else:
            return {"status": 403}
    return inner


@only_owner_allowed
def total_clients(clients: list[int]) -> int:
    print("Calculating total number of clients...")
    return sum(clients)

if __name__ == "__main__":
    print(total_clients([5, 12, 8, 3]))
