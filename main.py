import ijson

from classes import User


def fetch_bike():
    with open("bike.json", "rb") as f:
        bike = {}
        for field, data in ijson.kvitems(f, ""):
            bike[field] = data
    return bike


def main():
    user: User = User(**fetch_bike())
    print(user)
    print(user.location)
    print(user.rides)


if __name__ == '__main__':
    main()
