#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    first_flight = hash_table_retrieve(hashtable, 'NONE')

    route[0] = first_flight

    for i in range(len(route) - 1):
        route[i + 1] = hash_table_retrieve(hashtable, route[i])

    return route
