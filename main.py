import json
from classes import User


def fetch_bike():
    with open('bike.json') as f:
        return json.load(f)


def main():
    user: User = User(**fetch_bike())
    print(user)
    print(user.location)
    print(user.rides)


if __name__ == '__main__':
    main()
