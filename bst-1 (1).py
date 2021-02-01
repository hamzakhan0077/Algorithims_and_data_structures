from functools import total_ordering

@total_ordering
class TestClass:
    """ Represents an arbitrary thing, for testing the BST. """

    def __init__(self, field1, field2=None):
        """ Initialise an object. """
        self._field1 = field1
        self._field2 = field2

    def __str__(self):
        """ Return a short string representation of this object. """
        outstr = self._field1
        return outstr

    def full_str(self):
        """ Return a full string representation of this object. """
        outstr = self._field1 + ": "
        outstr = outstr + str(self._field2)
        return outstr

    def __eq__(self, other):
        """ Return True if this object has exactly same field1 as other. """
        if (other._field1 == self._field1):
            return True
        return False

    def __ne__(self, other):
        """ Return False if this object has exactly same field1 as other. """
        return not (self._field1 == other._field1)

    def __lt__(self, other):
        """ Return True if this object is ordered before other.

        A thing is less than another if it's field1 is alphabetically before.
        """
        if other._field1 > self._field1:
            return True
        return False



class BSTNode:
    """ An internal node for a Binary Search Tree.  """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self): #calling str a particular node
        res = ''
        if self._leftchild:
            res += str(self._leftchild)
        res += ' ' + str(self._element)
        if self._rightchild:
            res += str(self._rightchild)
        return res


    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))
    

    def searchitem(self, searchitem):
        """ Return object matching searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST

        """
       
        return self.search_node(searchitem)._element

    def search_node(self, searchitem):
        """ Return the BSTNode (with subtree) containing searchitem, or None. 

        Args:
            searchitem: an object of any class stored in the BST
        """
     
        if self == None:
            return None
        if self._element > searchitem:
            if self._leftchild == None:
                return None
            return self._leftchild.search_node(searchitem)
        elif self._element < searchitem:
            if self._rightchild == None:
                return None
            return self._rightchild.search_node(searchitem)
        else:
            return self


    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.
        Returns the item added, or None if a matching object was already there.
        """
       

        if obj < self._element:
            if self._leftchild == None:
                Lnode = BSTNode(obj)
                self._leftchild = Lnode
                Lnode._parent = self
                return Lnode._element
                # Lnode = self._leftchild = BSTNode(obj)
                # Lnode._parent = self
            else:
                return self._leftchild.add(obj)
        elif obj > self._element:
            if self._rightchild == None:
                Rnode =  BSTNode(obj)
                self._rightchild = Rnode
                Rnode._parent = self
                return Rnode._element
            else:
                return self._rightchild.add(obj)
        else:
            return None
        # node = BSTNode(obj)
        # if node._element < self._element:
        #     if self._leftchild == None:
        #         self._leftchild = node
        #     else:
        #      self._leftchild.add(obj)
        # elif node._element > self._element:
        #     if self._rightchild == None:
        #         self._rightchild = node
        #     else:
        #        return self._rightchild.add(obj)
        # else:
        #     return None


    def findmaxnode(self):
        """ Return the BSTNode with maximal element at or below here. """
        
        # this node if it has no right child
        # if it has a rightm child it should be somewheere right there
        #

        big_node = self  #- we are alreday on the left chidl
        while big_node._rightchild != None:
            big_node = big_node._rightchild  # this is the biggest element # poinjting to node that i am intr in
        return big_node

    
    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
       
        lheight = -1
        if self._leftchild:
            lheight = self._leftchild.height()
        rheight = -1
        if self._rightchild:
            rheight = self._rightchild.height()
        return 1+ max(lheight,rheight)



    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree, 
        including this node.
        """
     
        return self.height()
    def leaf(self):
        """ Return True if this node has no children. """
      
        if not self._rightchild and not self._leftchild:
            return True
        return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
      
        if self.full():
            return False
        if self._rightchild:
            return True
        elif self._leftchild:
            return True

        return False

    def full(self):
        """ Return true if this node has two children. """

        if (self._leftchild and self._rightchild):
            return True
        return False

    def internal(self):
        """ Return True if this node has at least one child. """
     
        if self._rightchild or self._leftchild:
            return True
        return False


    def remove(self, searchitem):
        """ Remove and return the object matching searchitem, if there.

        Args:
            searchitem - an object of any class stored in the BST

        Remove the matching object from the tree rooted at this node.
        Maintains the BST properties.
        """
        
        out = self.search_node(searchitem)
        if out != None: # if search found something
            return out.remove_node()
        return None




    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        #if this is a full node
            #find the biggest item in the left tree
            #  - there must be a left tree, since this is a full node
            #  - the node for that item can have no right children
            #move that item up into this item
            #remove that old node, which is now a semileaf
            #return the original element
        #else if this has no children
            #find who the parent was
            #set the parent's appropriate child to None
            #wipe this node
            #return this node's element
        #else if this has no right child (but must have a left child)
            #shift leftchild up into its place, and clean up
            #return the original element
        #else this has no left child (but must have a right child)
            #shift rightchild up into its place, and clean up
            #return the original element
        # method body goes here
        # STEP1 ---> STORE self.element
        # STEP2 ---> Identify the node that contains the item that is biggest in the left subtree
        # STEP3 ---> Copy that node's element up into self
        # STEP4 ---> DO a recursive call to remove that node
        """ This happens first     
             B
            /
           A
            """
        elem = self._element # step one done
        if self.full():
            start_node = self._leftchild  # while right child
            # Now make start node point to  --biggest element--     --- > Its right child is none autom
            # Copy the vale from the start node to the full node that I am trying to remove
            # remove start node --- Recursive call  -- --
            while start_node._rightchild != None:
                start_node = start_node._rightchild # this is the biggest element # poinjting to node that i am intr in
            self._element = start_node._element
            """*******************---- WHAT HAPPENS IF WE ARE REMOVING THE ROOT CHECK FOR EVERY METHOD ----******************"""
            start_node.remove_node()
            # if start_node._rightchild != None:
            #     start_node._rightchild.remove_node()
            return elem
        elif self.leaf():#
            # print(self._element,self._parent)
            # self._rightchild._parent = self._parent

            if self  == self._parent._leftchild:
                self._parent._leftchild = None
            elif self  == self._parent._rightchild:
                self._parent._rightchild = None
            self._parent = None
            self._element = None
            return  elem

            #return self._element
        elif self._rightchild == None and self._leftchild != None:
            """ First case
                   B
                  /    
                 A  removing Him
                 
                 B (hgt=0)[left: *; right: *] -- parent: *
                 adding A
                 Ordered:  A B
                 B (hgt=1)[left: A; right: *] -- parent: *
                 A (hgt=0)[left: *; right: *] -- parent: B
                 removing A

            """

            # if self._leftchild._parent != None :
            #     self._leftchild._parent._leftchild = self._leftchild

            """
            Case Remove L
                 F
               /  \
               |   L
               | /   \
               H     None (L has No right child)
              / \
             G   I
            """
            """
            WHAT I DID 
            --> cOPIED THE ELEMENT 
            --> THEN TSO L BECOMES H
            --. BUT I STILL NEED TO FIX L CHILDREN REFERENCES 
            --. i will call is L node that has H element
            --> L node's Right child becomes L nodes leftchild,s right child
            --> L node's Left Child becomes L nodes's leftchild's leftchild
            --> i check if there is a right child them we make the l'node ie H becomes the parent
            -- similarly if there is a left child .....
            
            
            """

            self._element = self._leftchild._element #L becomes H
            self._rightchild = self._leftchild._rightchild
            self._leftchild = self._leftchild._leftchild
            if self._rightchild != None:
                self._rightchild._parent = self
            if self._leftchild != None:
                self._leftchild._parent = self


            # self._parent._rightchild = self._leftchild
            # self._leftchild._parent = self._parent
            # print(self._element)
            # print(self._leftchild._element)
            # print(self._rightchild._element)
            #l_parent = self._parent
            # self._leftchild._parent = self._parent# L's PArent Becomes H's Parent
            # l_parent._rightchild = self._leftchild
            # self._leftchild.remove_node()

            # self._leftchild.remove_node()
            return elem
        else:
            """
                semi leaf
                B
                 \
                  F
                """
            #### F's Parent should point to B,s Parent  --- > B is self , f is the right child
            # If f's parent exists
                # f's parent's rightchild  == f
            #' Do same above
            # if self._parent ==None: #If b parent is none
            #       # program will still point to b when called (issue)
            #     # issue handling #
            #     self._element = self._rightchild._element
            #     self._rightchild.remove_node()
            # else:
            #     self._rightchild._parent = self._parent
            #     if self._rightchild._parent != None : # If f's PArent Exists
                    # self._rightchild._parent._rightchild = self._rightchild
            self._element = self._rightchild._element
            # if self._rightchild.full():

            #Scanrio >>???????????
            # if self._rightchild.full():

            self._leftchild = self._rightchild._leftchild
            self._rightchild = self._rightchild._rightchild
            if self._rightchild != None:
                self._rightchild._parent = self
            if self._leftchild != None:
                self._leftchild._parent = self
            # self._rightchild._parent = self._parent
            # self._rightchild.remove_node()

            return elem

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if self._isthisapropertree() == False:
            print("ERROR: this is not a proper Binary Search Tree. ++++++++++")
        outstr = str(self._element) + ' (hgt=' + str(self.height()) + ')['
        if self._leftchild is not None:
            outstr = outstr + "left: " + str(self._leftchild._element)
        else:
            outstr = outstr + 'left: *'
        if self._rightchild is not None:
            outstr = outstr + "; right: " + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self._leftchild is not None:
            self._leftchild._print_structure()
        if self._rightchild is not None:
            self._rightchild._print_structure()

    def _properBST(self):
        """ Return True if this is the root of a proper BST; False otherwise. 

        First checks that this is a proper tree (i.e. parent and child
        references all link up properly.

        Then checks that it obeys the BST property.
        """
        if not self._isthisapropertree():
            return False
        return self._BSTproperties()[0]

    def _BSTproperties(self):
        """ Return a tuple describing state of this node as root of a BST.

        Returns:
            (boolean, minvalue, maxvalue):
                boolean is True if it is a BST, and false otherwise
                minvalue is the lowest value in this subtree
                maxvalue is the highest value in this subtree
        """
        minvalue = self._element
        maxvalue = self._element
        if self._leftchild is not None:
            leftstate = self._leftchild._BSTproperties()
            if not leftstate[0] or leftstate[2] > self._element:
                return (False,None,None)
            minvalue = leftstate[1]

        if self._rightchild is not None:
            rightstate = self._rightchild._BSTproperties()
            if not rightstate[0] or rightstate[1] < self._element:
                return (False,None,None)
            maxvalue = rightstate[2]

        return (True, minvalue,maxvalue)

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild is not None:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild is not None:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False          
        if self._parent is not None:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok

    def _testadd():
        node = BSTNode(TestClass("Memento", "11/10/2000"))
        node._print_structure()
        print('> adding Melvin and Howard')
        node.add(TestClass("Melvin and Howard", "19/09/1980"))
        node._print_structure()
        print('> adding a second version of Melvin and Howard')
        node.add(TestClass("Melvin and Howard", "21/03/2007"))
        node._print_structure()
        print('> adding Mellow Mud')
        node.add(TestClass("Mellow Mud", "21/09/2016"))
        node._print_structure()
        print('> adding Melody')
        node.add(TestClass("Melody", "21/03/2007"))
        node._print_structure()
        return node

    def _test():
        node = BSTNode(TestClass("B", "b"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "A")
        node.add(TestClass("A", "a"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "A")
        node.remove(TestClass("A"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove(TestClass("C"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "F")
        node.add(TestClass("F", "f"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove(TestClass("B"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "D")
        node.add(TestClass("D", "d"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "E")
        node.add(TestClass("E", "e"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove(TestClass("B"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "D")
        node.remove(TestClass("D"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove(TestClass("C"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "E")
        node.remove(TestClass("E"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "L")
        node.add(TestClass("L", "l"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "H")
        node.add(TestClass("H", "h"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "I")
        node.add(TestClass("I", "i"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "G")
        node.add(TestClass("G", "g"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "L")
        node.remove(TestClass("L"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "H")
        node.remove(TestClass("H"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "I")
        node.remove(TestClass("I"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "G")
        node.remove(TestClass("G"))
        print('Ordered:', node)
        node._print_structure()
        print(node)




# #
# BSTNode._testadd()
#
# print('++++++++++')
# BSTNode._test()
# #

