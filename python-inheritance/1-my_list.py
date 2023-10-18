#!/usr/bin/python3
'''MyList class with a print_sorted method'''


class MyList(list):
    '''A custom list class that extends the built-in list class.'''

    def print_sorted(self):
        '''Print the elements of the list in sorted order.

        This method sorts the list in ascending order and prints it.
        '''
        print(sorted(self))
