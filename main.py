# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from pip._vendor import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print()

    url = "http://jsonplaceholder.typicode.com/photos"

    # get
    print("01_01: get")
    response = requests.get(url)
    print(response.json())
    print()

    # post
    print("01_01: post")
    jsonPayload = {'albumId': 1, 'title': 'test', 'url': 'nothing.com', 'thumbnailUrl': 'nothing.com'}
    response = requests.post(url,json=jsonPayload)
    print(response.json())
    print()

    # put
    print("01_01: put")
    url = "http://jsonplaceholder.typicode.com/photos/100"
    response = requests.put(url, json=jsonPayload)
    print(response.json())
    print()

    # delete
    print("01_01: delete")
    # url = "http://jsonplaceholder.typicode.com/photos/100"
    response = requests.delete(url)
    print(response.json())
    print()

    # with authentication
    print("01_02: authentication without credentials")
    url = 'https://api.github.com/user'
    response = requests.get(url)
    print(response.json())
    print()

    # curl -i -u your_username https://api.github.com/user

    print("01_02:authentication with credentials")
    # response = requests.get(url, auth=('djw-test', 'password1'))
    your_username='djw-test@gmail.com'
    username='djw-test'
    password='password1'
    response = requests.get(url, auth=(username, password))  # does not work 20210301
    print(response.json())
    print()

    token='abc' # retrieve from token.GitHub.NotebookPWD

    print("01_02: authorization with token")
    response = requests.get(url,headers={'Authorization': 'Bearer ' + token})
    print(response.json())
    print()

    print("01_03: Analyzing the data: Parsing data")
    response = requests.get(url, headers={'Authorization': 'Bearer ' + token})
    my_json = response.json()
    for key in my_json.keys():
        print (key, my_json[key])

    print()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
