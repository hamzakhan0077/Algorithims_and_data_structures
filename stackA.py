""" Class definition for an array-based implementation of the Stack ADT.



"""


class Stack:
    """ An array-based stack. """

    def __init__(self):
        self._list = []      #Note that this is meant to be private
                             #_list should only be accessed from the
                             #methods defined in this class.

    def __str__(self):
        """ Display a stack as a string, by listing elements in sequence.

            |- denotes the bottom of the stack
            -> denotes the top of the stack.
            So '|-x-y-z-> denotes a stack with 3 elements, and z at the top.

        Normally, a method giving this lvel of detail in the string would not
        be provided - users of the class are only supposed to see the size
        of the stack and the top element. It is provided here so that we can
        use it for debugging and evaluation.
        """
        retstr = '|-'
        for element in self._list:
            retstr = retstr + str(element) + '-'
        retstr = retstr + '->'
        return retstr

    def pop(self):
        """ Remove and return the top element of the stack. """
        if len(self._list) == 0:
            return None
        return self._list.pop()

    def push(self, element):
        """ Place element onto the top of the stack. """
        self._list.append(element)

    def top(self):
        """ Return but don't remove the top element of the stack. """
        if len(self._list) == 0:
            return None
        return self._list[-1]

    def length(self):
        """ Return the number of elements on the stack. """
        return len(self._list)

    def test():
        """ Test the basic functionality of the stack. Class method. """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print('stack should be |-1-2-3-->, and is %s' % stack)
        print('stack.length should be 3, and is %d' % stack.length())
        print('stack.top() should be 3, and is %d' % stack.top())
        print('stack.pop() should be 3, and is %d' % stack.pop())
        print('stack should now be |-1-2-->, and is %s' % stack)
        print('stack.length() should be 2, and is %d' % stack.length())
        stack.pop()
        stack.pop()
        print('popped two more items; length() should be 0, and is %d' % (
                                                     stack.length()))
        print('stack.top() should be None, and is %s' % stack.top())
        print('stack.pop() should be None, and is %s' % stack.top())
        print('stack should be |-->, and is %s' % stack)



Stack.test()
#class card:
#    def __init__(self,card1,card2):
#        self.card1 = card1
#        self.card2 = card2



#
#     def reverse_stack(stack):
#
#         if not isinstance(stack, Stack):
#             return "This obj is not the instance of the class"
#         alist = stack._list[::-1]
#         for j in range(stack.length()):
#             stack.pop()
#         for i in range(len(alist)):
#             stack.push(alist[i])
#         return stack
#
# stack = Stack()
# stack.push(6)
# stack.push(1)
# stack.push(2)
# print(stack)
# print(card.reverse_stack(stack)) # working
# #
























