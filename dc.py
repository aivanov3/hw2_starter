""" starter file for hw2: dogcat """

import search       # AIMA module for search problems
import gzip         # read from a gzip'd file


# file name for the dictionary, with one word per line.  Each line
# will have a word followed by a tab followed by a number, e.g.
#   and     0.07358445
#   for     0.18200336

dict_file = "words34.txt.gz"
ScrabbleLetterCost = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "s": 1, "t": 1, "r": 1,
                      "d": 2, "g": 2,
                      "b": 3, "c": 3, "m": 3, "p": 3,
                      "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
                      "k": 5,
                      "j": 6, "x": 6,
                      "z": 10, "q": 10}

# dictionary is a dict to hold legal 3 and 4 letter words with their
# frequencies based on a sample of a large text corpus.  The dict's
# keys are the words and its values are their frequencies

# load words into the dictionary dict
dictionary = {}
for line in gzip.open(dict_file, 'rt'):
    word, n = line.strip().split('\t')
    n = float(n)
    dictionary[word] = n

def new_replace(n, letter, word):  # *
    chars = list(word)     # get a list of the chars
    chars[n] = letter      # replace nth chars in list with letter
    return ''.join(chars)  # turn list of chars to string and return

class DC(search.Problem):
    """DC is a subclass of the AIMA search files's Problem class
       It's init method takes three arguments: the initial word, goal word and cost method.

       A state is represented as a lowercase string of three or four
       ascii characters.  Both the initial and goal states must be
       words of the same length and they must be in the dict
       dictionary. The cost argument specifies how to measure the
       cost of an action and can be 'steps', 'scrabble' or 'frequency'
       """

    def __init__(self, initial='dog', goal='cat', cost='steps'):

        self.initial = initial
        self.goal = goal
        self.cost = cost
        # make sure the arguments are legal, raising an error if any are bad.

    def actions(self, state):
        """ Given a state (i.e., a word), return a list or iterator of
        all possible next actions.  An action is defined by position
        in the word and a character to put in that position.  But the
        result must be a legal word, i.e., in our dictionary, and it
        should not be the same as the state, i.e., don't replace a
        character with the same character """

        legalActions = []
        for i, letter in enumerate(state):
            Modalphabet = "abcdefghijklmnopqrstuvwxyz".replace(letter, "")
            for char in Modalphabet:
                wordAttempt = new_replace(i, char, state)
                if wordAttempt in dictionary:
                    legalActions.append((char, i))

        return legalActions

    def result(self, state, action):
        """ takes a state and an action and returns a new state """

        letter, index = action
        return new_replace(index, letter, state)


    def goal_test(self, state):
        """ returns True iff state is a goal state for this problem instance """

        return (state == self.goal)

    def path_cost(self, c, state1, action, state2):
        """ Returns the cost to get to state2 by applying action in
        state1 given that c is the cost to get from the state state to
        state1. For the the dc problem, you will have to check what
        the cost metric is being used for this problem instance, i.e.,
        is it steps, scrabble or frequency """

        if self.cost == "scrabble":
            return ScrabbleLetterCost[action[0]]
        if self.cost == "steps":
            return c+1 # change all values to 1 in letter cost
        if self.cost == "frequency":
            return dictionary[state2]

    def __repr__(self):
        """" return a suitable string to represent this problem instance """

        return f"Node: {self.initial}"

    def h(self, node):
        """Heuristic: returns an estimate of the cost to get from the
        state of this node to the goal state.  The heuristic's value
        should depend on the Problem's cost parameter (steps, scrabble
        or frequency) as this will effect the estimate cost to get to
        the nearest goal. """

        sum = 0
        # for loop to count # of chars that don't = correspond with goal string index char
        for letterA, letterB in zip(self.goal, node.state):
            if letterA != letterB:
                sum += 1
        return sum
