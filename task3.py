import json

role = str(input("Please choose admin(a) or (u): "))


def write_json(data, filename='/home/raissov/Desktop/lab5 files/task3/products.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

ifFound = False
if role == 'a':
    with open('/home/raissov/Desktop/lab5 files/task3/admin.json', 'r+') as f:
        data = json.load(f)

    username = str(input("Please write username: "))
    password = str(input("Please write password: "))

    if username == str(data["username"]) and password == str(data["password"]):
        print("Welcome to the system %s" % username)
        choice = (input("Search (s) - Add(a) - Delete (d) - Edit(e) - Exit(x): "))
        with open('/home/raissov/Desktop/lab5 files/task3/products.json', 'r') as m:
            products = json.load(m)
        print(products)
        size = len(products)
        if choice == 's':
            searching_word = (input("Please write your word for search: "))

            for i in range(size):
                if searching_word == (products[i]["title"]):
                    print(products[i]["id"])
                    print(products[i]["title"])
                    print(products[i]["price"])
                    ifFound = True
                else:
                    ifFound = False
            if ifFound:
                ud = str(input("Would you like to update this product (u) or delete(d)"))
                if ud == 'u':
                    id = int(input("Please write item ID: "))
                    title = str(input("Please rewrite you item name: "))
                    price = float(input("Pleas write item price: "))
                    newList = {"id": id, "title": title, "price": price}
                    products[i].update(newList)
                    write_json(products)
                elif ud == 'd':
                    id = int(input("Please write your item number in queue that you want to delete: "))
                    del products[id]
                    write_json(products)

            else:
                print("There is no such item in your list\n Would you like to add this item?")
                yn = str(input("Yes(y) or No(n): "))
                if yn == 'y':
                    id = int(input("Please write item ID: "))
                    title = str(input("Please rewrite you item name: "))
                    price = float(input("Pleas write item price: "))
                    newList = {"id": id, "title": title, "price": price}
                    products.append(newList)
                    write_json(products)
    else:
        print("Wrong username or password!")

elif role == 'u':
    nickname = str(input("Please write your nickname: "))
    print("Welcome %s" %nickname)
    searching_word = (input("Please write your word for search: "))
    with open('/home/raissov/Desktop/lab5 files/task3/products.json', 'r') as m:
        products = json.load(m)
    size = len(products)
    for i in range(size):
        if searching_word == (products[i]["title"]):
            print(products[i]["id"])
            print(products[i]["title"])
            print(products[i]["price"])
            ifFound = True
        else:
            ifFound = False

    if ifFound:

else:
    print("Error!")
