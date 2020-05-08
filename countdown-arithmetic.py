import fileinput
from functools import reduce

"""
Talofa! countdown-arithmetic.py is a simple program designed to solve a simplified 
"countdown" style problem.

The program takes two lines of input: one containing a list of integers of arbitrary
size, and one containing a target value and either "L" or "N" designating the
operating mode of the problem.

A solution in "L" mode means the equation must be solved left to right ie. for
values [1, 2, 3], 1+2*3 would equal 9.

A solution in "N" mode means the equation must be solved "normally" ie. for values
[1, 2, 3], 1+2*3 would equal 7.

The program uses an unsorted binary tree to stores the results of the equation, so
the memory use is exponential with the length of the input. I have mitigated memory
usage using several "pruning" rules when building the tree- ie. preventing it from 
building unnecessary branches.

@Author Mickey Treadwell

"""

#___________________GLOBAL VARIABLES__________________________

#These are flags for dealing with user input
gotvalues = False
bad_input = False
bad_args = False

# Value to indicate a dead node
DEAD = -1

#_____________________________________NODE CLASSES_____________________________________

"""
Node class created when using the L method. The node is initialised with the result of
it's partent node + or * the next value in the input list.
"""
class L_Node:

    # Constructor (if this was Java)
    def __init__(self, val):

        # + child
        self.l = None
        # * child
        self.r = None
        
        self.result = val

        self.layer = 0

        self.operator = ''

        self.operations = ''

        # Return the result contained in the node
    def get(self):

        return self.result

"""
Node class created when using the N method. The node is initialised with "yin" and "yang"
values, which are determined differently if it is the result of addition or multiplication.
The result stored in the node is the sum of its yin and yang values.
"""
    
class N_Node:

    # Constructor (if this was Java)
    def __init__(self, yin, yang):

        # + child
        self.l = None
        # * child
        self.r = None

        self.yin = yin

        self.yang = yang
        
        self.result = self.yin + self.yang

        self.layer = 0

        self.operator = ''

        self.operations = ''

#_____________________________________BST CLASS_____________________________________

"""
BST data structure which consists of node objects and functions to
insert, search, and print them.
"""
class BST:

    # Constructor (if this was Java)
    def __init__(self, val_list, target, mode):

        self.mode = mode
        self.root = None
        self.val_list = val_list
        self.target = int(target)
        self.solved = False

        if self.mode == 'L':
            # Add the contents to the list to the tree (& pray it works)
            self.L_insert(self.val_list[0])

        elif self.mode == 'N':
            self.N_insert(self.val_list[0])
            
#_____________________________________L MODE METHODS_____________________________________

    
    # Call the recursive insertion method on the root node
    def L_insert(self, in_val):

        if self.root == None:
            self.root = L_Node(in_val)
            self.root.operations = str(self.val_list[0])
            if self.root.layer != len(self.val_list)-1:
                self.L_insert_node(self.root)

        else:
            print("something went wrong")

    def L_insert_node(self, current_node):

        #If the value has been found, stop building the tree
        if self.solved:
            return
        else:
            if current_node.layer != len(self.val_list)-1:
                self.L_insert_plus(current_node, self.val_list[current_node.layer+1])
                self.L_insert_times(current_node, self.val_list[current_node.layer+1])
            else:
                print("end of branch")
                return
            
    def L_insert_plus(self, current_node, in_val):
        
        # Prune 1: Is this is the second last layer, will the result of the operation result in the target?
        # if not, don't make it.
        if current_node.layer == len(self.val_list)-2:
            if (current_node.result + in_val) != self.target:
                return
                
        # Prune 2: Will this result in a value higher than the target?
        # If so: add a dead node.
        if (current_node.result + in_val) > self.target:
            return

        # If it's worth continuing, initalise the node with the result of the + operator.
        current_node.l = L_Node(current_node.result + in_val)
        current_node.l.layer = current_node.layer +1
        current_node.l.operations = "".join([current_node.operations, ' + ', str(self.val_list[current_node.layer+1])])
            
        # Prune 3: If the solution has been found, stop adding nodes
        if current_node.l.layer == len(self.val_list)-1 and current_node.l.result == self.target:
            self.solved = True

        self.L_insert_node(current_node.l)
        return
            

    def L_insert_times(self, current_node, in_val):

        # Prune 1: Is this is the second last layer, will the result of the operation result in the target?
        # if not, don't make it.
        if current_node.layer == len(self.val_list)-2:
            if (current_node.result * in_val) != self.target:
                return
            
        # Prune 2: Will this result in a value higher than the target?
        # If so: add a dead node.
        if (current_node.result * in_val) > self.target:
            return
            
        # If it's worth continuing, initalise the node with the result of the + operator.
        current_node.r = L_Node(current_node.result * in_val)
        current_node.r.layer = current_node.layer +1
        current_node.r.operations = "".join([current_node.operations, ' * ', str(self.val_list[current_node.layer+1])])

        # Prune 3: If the solution has been found, stop adding nodes
        if current_node.r.layer == len(self.val_list)-1 and current_node.r.result == self.target:
            self.solved = True

        self.L_insert_node(current_node.r)
        return

 #_____________________________________N MODE METHODS_____________________________________

    def N_insert(self, in_val):
                
        if self.root == None:
            self.root = N_Node(0, self.val_list[0])
            self.root.operations = str(self.val_list[0])
            if self.root.layer != len(self.val_list)-1:
                self.N_insert_node(self.root)

        else:
            print("something went wrong")
            
    def N_insert_node(self, current_node):

        #If the value has been found, stop building the tree
        if self.solved:
            return
        else:
            if current_node.layer != len(self.val_list)-1:
                self.N_insert_plus(current_node, self.val_list[current_node.layer+1])
                self.N_insert_times(current_node, self.val_list[current_node.layer+1])
            else:
                print("end of branch")
                return
            
    def N_insert_plus(self, current_node, in_val):
        
        # Prune 1: Is this is the second last layer, will the result of the operation result in the target?
        # if not, don't make it.
        if current_node.layer == len(self.val_list)-2:
            if (current_node.result + in_val) != self.target:
                return
            
        # Prune 2: Will this result in a value higher than the target?
        # If so: add a dead node.
        if (current_node.result + in_val) > self.target:
            return

        current_node.l = N_Node(current_node.result, in_val)
        current_node.l.layer = current_node.layer +1
        current_node.l.operator = '+'
        current_node.l.operations = "".join([current_node.operations, ' + ', str(self.val_list[current_node.layer+1])])

        # Prune 3: If the solution has been found, stop adding nodes
        if current_node.l.layer == len(self.val_list)-1 and current_node.l.result == self.target:
            self.solved = True
            
        self.N_insert_node(current_node.l)
        return


    def N_insert_times(self, current_node, in_val):

        # Prune 1: Is this is the second last layer, will the result of the operation result in the target?
        # if not, don't make it.
        if current_node.layer == len(self.val_list)-2:
            if (current_node.yin + (current_node.yang*in_val)) != self.target:
                return

        # Prune 2: Will this result in a value higher than the target?
        # If so: add a dead node.
        if (current_node.yin + (current_node.yang*in_val)) > self.target:
            return

        current_node.r = N_Node(current_node.yin, current_node.yang*in_val)
        current_node.r.layer = current_node.layer +1
        current_node.r.operations = "".join([current_node.operations, ' * ', str(self.val_list[current_node.layer+1])])

        # Prune 3: If the solution has been found, stop adding nodes
        if current_node.r.layer == len(self.val_list)-1 and current_node.r.result == self.target:
            self.solved = True
            
        self.N_insert_node(current_node.r)
        return

 #_____________________________________SEARCH_____________________________________
    
    def search(self, search_val):

        if (self.search_leaves(self.root, search_val)) == None:
            print(args[1] + ' ' + args[0] + ' ' +  "impossible")

        else:
            print(self.search_leaves(self.root, search_val))

    # Recursive search function for non-sorted binary tree
    def search_leaves(self, current, search_val):

        if current == None:
            return None

        if current.result == search_val and current.layer == len(self.val_list)-1:
            return (args[1] + ' ' + args[0] + ' ' + current.operations)

        X = self.search_leaves(current.l, search_val)

        if X is not None:
            return X

        X = self.search_leaves(current.r, search_val)

        if X is not None:
            return X

        return None

#___________________________________PRINT METHODS___________________________________

            
    # Calls the recursive print branch function on the root node
    def print_branch(self, leaf_val):

        self.print_branch_rec(self.root, leaf_val)

    # Prints the branch that results in the given value
    # assuming it exists
    def print_branch_rec(self, current, leaf_val):

        if current is None:
            print("Value does not exist")
            return
        
        elif leaf_val == current.result:
            print(current.result)
            return

        elif leaf_val > current.result:
            print(current.result)
            self.print_branch_rec(current.r, leaf_val)

        elif leaf_val < current.result:
            print(current.result)
            self.print_branch_rec(current.l, leaf_val)

    # Calls the recursive print inorder function on the root node
    def print_inorder(self, root):

        self.print_inorder_rec(self.root)

    # Recursively print the value of every node in the tree
    def print_inorder_rec(self, current):

        print('Operations: ' + str(current.operations))
        print('Result: ' + str(current.result))
        print('Layer: ' + str(current.layer))
        
        if current.l != None and current.l.result != DEAD:
            self.print_inorder_rec(current.l)

        if current.r != None and current.r.result != DEAD:
            self.print_inorder_rec(current.r)
            

#_____________________________________USER INPUT_____________________________________

#Dealing with inputs
for line in fileinput.input():

    # Receiving the first of the two input lines (the values)
    if not gotvalues:
    
        input_list = line.split()

        for value in input_list:
            
            if not value.isdigit():
                bad_input = True
                
            elif int(value) < 0:
                bad_input = True

        if not bad_input:
            input_list = list(map(int, input_list))
        
        gotvalues = True
        
    # Receiving the first of the two input lines (the arguments)
    else: 

        args = line.split()

        if len(args) != 2:
            bad_args = True

        elif args[1] != 'N' and args[1] != 'L':
            bad_args = True

        elif not args[0].isdigit():
            bad_args = True

        gotvalues = False

        if bad_input:
            print("Input list contains illegal items: " + str(input_list))
            bad_input = False
            
        elif bad_args:
            print("Invalid arguments: "+ str(args))
            bad_args = False
            
        else:
            target = args[0]
            
            mode = args[1]
            
            tree = BST(input_list, int(target), mode)

            # Handy for debugging
            #print("Tree built")

            tree.print_inorder
            
            tree.search(int(target))

            tree = None
