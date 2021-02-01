




def script_author():
    print("Successful-- You are in pytoonz.py -  Hamza Hassan Khan")




class DLLNode:
    def __init__(self,item,prevnode,nextnode):
        self.element = item
        self.prevnode = prevnode
        self.nextnode = nextnode



class Track:
    def __init__(self,name,artiste,timesplayed):
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed


    def get_name(self):
        return self._name

    def get_artiste(self):
        return self._artiste

    def __str__(self):
        node  = DLLNode((""" %s %s %s""" %(self._name,self._artiste,self._timesplayed)),None,None)
        # return """ %s %s %s""" %(self._name,self._artiste,self._timesplayed)
        return node.element
    def play(self):
        self._timesplayed += 1
        return self.__str__()

    def test_track(self, track):
        print("""I am track My job is to test Track \n """)
        print(track)
        print(track.get_name())
        print(track.get_artiste())
        print(track.play())


class PyToonz:

    def __init__(self):
       # self._list_of_tracks = list_of_tracks
        self.head = DLLNode(None,None,None)
        self.tail = DLLNode(None,self.head,None)
        self.head.next = self.tail
        self.size = 0
        self.cursor = None

    def __str__(self):
        res = ""
        i = 0
        tar_node = self.head
        while i <  self.size:
            tar_node = tar_node.nextnode
            #tar_ele = str(tar_node.element)
            if tar_node == self.cursor:
                res+= "--> "+ str(tar_node.element)
            else:
                res+= str(tar_node.element)
            if i < self.size -1 :
                res+= "\n"
            i+=1
        return res


    def length(self):
        return self.size



    def add_track(self,track):
        if not isinstance(track,Track):
            return None
        previous_node  = self.tail.prevnode#the already existing node
        node = DLLNode(track, None, None)# new node

        node.nextnode = self.tail# next node is the dummy tail because we are appending at the end

        self.tail.prevnode = node # tails previous node now becomes new node

        node.prevnode = previous_node # node that is suppose to be before the new node is the one before the tail when node was not added

        previous_node.nextnode = node # the node before the new node --- > new node

        self.size += 1 # we increment the size
        if self.cursor == None:
            self.cursor = node #sConfirmation required  from Mr Brown
        return None

    def get_current(self):
        if self.cursor != None:
            return self.cursor.element
        return None


    def add_after(self,track):# - - - #
        current_node = self.cursor
        new_node = DLLNode(track,None,None)
        new_node.nextnode = current_node.nextnode
        new_node.prevnode = current_node
        current_node.nextnode = new_node
        new_node.nextnode.prevnode = new_node
        self.size += 1
        return None

    def next_track(self):
        if self.cursor == None:
            return None
        elif self.cursor.nextnode == self.tail:
            self.reset()
        else:
            self.cursor = self.cursor.nextnode
        return None

    def prev_track(self):
        if self.cursor == None:
            return None
        elif self.cursor.prevnode == self.head:
            self.cursor = self.tail.prevnode
        else:
            self.cursor = self.cursor.prevnode
        return None


    def reset(self):
        self.cursor = self.head.nextnode
        return None

    def play(self): # So According to all discussion with Mr Brown This method has to PRINT whatever track's play returns
        if self.cursor == None:
            print("Error")
        else:
            print(self.cursor.element.play())# Cursor points to a node. Node has the element. Element is the Track Object



    def remove_current(self): # -  -  - #
        if self.cursor != None:
           current_node = self.cursor
           current_node.prevnode.nextnode = current_node.nextnode
           current_node.nextnode.prevnode = current_node.prevnode
           if current_node.nextnode == self.tail:
                self.reset()
           else:
               self.cursor = current_node.nextnode
           self.size -= 1
        return None


    def test_pytoonz(self):
        print(""" I am A Pytoonz test My Job is to test pytooz basid on sequence of operation provided in the assignment \n """)
        pytoonz = PyToonz()
        track0 = Track("Looking for me", "Paul Woolford and Diplo/Lomax", 0)
        track1 = Track("Giants", "Dermot Kennedy", 0)
        track2 = Track("Holy", "Justin Bieber Ft Chance", 0)
        pytoonz.add_track(track0)
        pytoonz.add_track(track1)
        pytoonz.add_track(track2)
        print(pytoonz)
        print("\n---------------- TEST 1- 5 finish here --------------------\n")
        print(pytoonz.get_current(),"-----I am the Current Track----")
        print(pytoonz.play(), " (--I am Play Imy job is to play the current track i call out track's Play and return whatever it returns")
        pytoonz.next_track() # It moves to next track
        print(pytoonz.get_current(), "I am now the CUrrent Track ")
        print("\n")
        print(pytoonz)
        print("\n")
        pytoonz.prev_track()
        pytoonz.remove_current()
       # pytoonz.play()
        print("\n")
        print(pytoonz)
        print("\n")
        track3 = Track("Lemonade", "Internet Money / Gunna / Toliver", 0)
        pytoonz.add_track(track3)
        print("\n")
        print(pytoonz)
        print("\n")
        pytoonz.next_track()
        pytoonz.play()

        print("\n")
        print(pytoonz)
        print("\n")
        print("---------------- TESTING REMOVE ie ( If you delete the currently selected track, make whatever came afterit the new current track)")
        pytoonz0 = PyToonz()
        track0 = Track("Hey I am new track 0", "Zero", 0)
        track1 = Track("Hey I am new track 1", "One", 0)
        track2 = Track("Hey I am new track 2", "Two", 0)
        pytoonz0.add_track(track0)
        pytoonz0.add_track(track1)
        pytoonz0.add_track(track2)
        pytoonz0.next_track()  # if i delete this cursor should then point at track 2
        pytoonz0.remove_current()
        pytoonz0.remove_current()  # if i remove this cursor should reset
        print(pytoonz0)

        print("""--------------------------------\n My Job Is To Test Prev and NExt Track \n -------------------------------""")

        track0 = Track("Hey I am new track 0", "Zero", 0)
        track1 = Track("Hey I am new track 1", "One", 0)
        track2 = Track("Hey I am new track 2", "Two", 0)
        pytoonz1 = PyToonz()
        pytoonz1.add_track(track0)
        pytoonz1.add_track(track1)
        pytoonz1.add_track(track2)
        pytoonz1.next_track()
        pytoonz1.next_track()
        pytoonz1.next_track()
        pytoonz1.prev_track()
        print(pytoonz1)


















































