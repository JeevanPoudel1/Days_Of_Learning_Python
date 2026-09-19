'''
#search problem
initial state
action
transition model
goal test
path cost function

#solution
node (a data structure that keeps track 
of a state, a parent, 
an action, a path cost)

#start
#repeat
#remove
#return solution
#expand node

'''

import sys


# --------------------------------
# NODE
# --------------------------------

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


# --------------------------------
# STACK FRONTIER (DFS)
# --------------------------------

class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")

        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]

        return node


# --------------------------------
# QUEUE FRONTIER (BFS)
# --------------------------------

class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")

        node = self.frontier[0]
        self.frontier = self.frontier[1:]

        return node


# --------------------------------
# SEARCH FUNCTION
# --------------------------------

def search():

    # Initial state
    start = "A"

    # Goal state
    goal = "G"

    # Create initial node
    start_node = Node(start, None, None)

    # Frontier
    frontier = QueueFrontier()

    # Add initial node
    frontier.add(start_node)

    # Explored states
    explored = set()

    # --------------------------------
    # Repeat
    # --------------------------------

    while True:

        # If frontier is empty
        if frontier.empty():
            raise Exception("No solution")

        # Remove a node
        node = frontier.remove()

        # Goal test
        if node.state == goal:

            # Build solution
            actions = []
            states = []

            while node.parent is not None:
                actions.append(node.action)
                states.append(node.state)

                node = node.parent

            states.append(node.state)

            actions.reverse()
            states.reverse()

            return actions, states

        # Mark state as explored
        explored.add(node.state)

        # --------------------------------
        # Expand node
        # --------------------------------

        neighbors = {
            "A": [("B", "go to B"), ("C", "go to C")],
            "B": [("D", "go to D"), ("E", "go to E")],
            "C": [("F", "go to F")],
            "D": [],
            "E": [("G", "go to G")],
            "F": [],
            "G": []
        }

        for state, action in neighbors[node.state]:

            if state not in explored and not frontier.contains_state(state):

                child = Node(
                    state=state,
                    parent=node,
                    action=action
                )

                frontier.add(child)


# --------------------------------
# RUN SEARCH
# --------------------------------

actions, states = search()

print("Solution:")
print("States:", states)
print("Actions:", actions)

