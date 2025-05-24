import ijson

from classes import User


def fetch_bike():
    with open("bike.json", "rb") as f:
        bike = {k: v for k, v in ijson.kvitems(f, "")}
    return bike


def main():
    user: User = User(**fetch_bike())
    print(user)
    print(user.location)
    print(user.rides)
    print(f'user data in json')
    print(user.model_dump_json(indent=2))


if __name__ == '__main__':
    main()
