# HW2 Questions
## UMBC CMSC 471 spring 2022

Please answer the following questions using the git [markdown syntax](https://guides.github.com/features/mastering-markdown/).  You should view this file on your repo on GitHub after pushing it to make sure it looks the way you want.  You can also use a browser extension (like [this one](https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl) for Chrome) to view your local file.

### (1) Describe in words the heuristic you used for the steps cost and explain why it is admissible

I had each letter change cost precisely 1. There would then be a list of possible equally valued node choices to decide from. Then the algorithm would decide which path would be shortest to the goal state. The A* algorithm implemented with it is admissible

### (2) Describe in words the heuristic you used for the scrabble cost and explain why it is admissible

I had it look through a dictionary list for each corresponding legal action letter value for a letter change for a state and note it. Then the algorithm would decide which path would be most cost efficient. The A* algorithm implemented with it is admissible

### (3) Describe in words the heuristic you used for the frequency cost and explain why it is admissible

I had it look through the included frequency for each word in the dictionary to note the value of the would-be transformed word. Then the algorithm would decide which possible word transformation pathway would be most efficient. The A* algorithm implemented with it is admissible.

### (4) Given an intiial word W1 and goal words W2, if there is a shortest path with N steps from W1 to W2, will there also be a shortest path of N steps from W2 to W1?  Explain why or why not.

Yes, by extension of a word letter change path existing, a reciprocal node path will have to also exist.

### (5) Using the steps cost, what is the longest path for a pair of three- and four-letter words you found?

26^4< possible cost length (English alphabet * 4 possible letters)
