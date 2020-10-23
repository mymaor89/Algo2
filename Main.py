from linkedlist import LinkedList
from node import Node
from data import *

def main():
    myCities = []
    for city in cities: #populating the array  with 1 element LinkedList for each city
        myCities.append(LinkedList([city])) #had to pass a 1 element list to LinkedList constructor

    for road in roads:
        for city in myCities:
            if road[0] == city.head.data                :
                 city.append(Node(road[1]))
            if road[1] == city.head.data                :
                 city.append(Node(road[0]))

    for city in myCities:
        print(city)

if __name__ == "__main__":
    main()