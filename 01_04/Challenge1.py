#Problem description
#Find out if there are any duplicate urls used in the
#json placeholder photo data

import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/photos'

    #get the data about the photos
    response = requests.get(url)

    #read that data into a variable
    json_data = response.json()

    #create a list for storing the url of each photo
    url_list = []    # Is a list of dictionaries.
    url_set = set()  # url_set is an empty set.
    for photo in json_data:
        #add the url for each photo to the url_list
        url_list.append(photo['url'])   # Do not add the entire list entry photo, but only the key: 'url'
                                        # and its value. Now the url_list is a list of urls. To extend a list,
                                        # you use the method append.
        print(photo)
        print(photo['url'])
        url_set.add(photo['url'])       # To add an element to a set, you use the method add. A set only has
                                        # unique values.
    #x = input("Proceed..")
    print()

    #How many items are in the url list (Should be 5000 since we have 5000 photos in our dataset)?
    print(url_list)
    print(len(url_list))
    x = input("Proceed..")

    #How many items are there if we turn that list into a set?
    print(url_set)
    print("length of url_set: ", len(url_set))
    x = input("Proceed..")
    print()
    print("Length of set of url_list: ", len(set(url_list)))    # you can also create the set outside the loop,
                                                                # by converting the list into a set with the set()
                                                                # function.

