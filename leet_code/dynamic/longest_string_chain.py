from typing import List, Tuple


"""
1048. Longest String chain.

Given a list oof words, 

each word consists of english lowercase letters
ascii alphabet

word1 is a predecessor of word2 if and only if we
can add exactly one letter anywhere in word1 to 
make it equal to word2.

word1 -> word2 = +1 letter anywhere in [word1] == word2

Example:
abc -> abac [abc + 'a'] 

Now a word chain is a sequence of words 
[word_1, word_2, ... , word_k] with k >= 1
where word_1 is a predecessor of word_2.
word_2 is a predecessor of word_3
and so on.

Goal
Return the longest possible length of a word chain
with words chosen from the given list of [words].

Example 1:
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is
"a","ba","bda","bdca"

Initial thought:
Construct a Trie 
then return the maximum height of the trie.

Sort the list first.

Constraints:
1 <= words.length <= 1000
1 <= words[i].lengh <= 16
words[i] are only alpha ascii

word list validation

For each word in order of length, f
or each word2 which is word with one character removed, 
length[word2] = max(length[word2], length[word] + 1).

Hash Table, Dynamic Programming

The key idea here is that we can think of all the words we have, as a directed graph, where each node represents a word, 
and each node points to all nodes that are just one deletion away.

So in the first test case we'll have "bdca" pointing to both [bca,bda] because we can reach both strings by removing one character from "bdca".

We can then think of the problem as trying to find the longest path in the graph. 
This can be achieved by doing N dfs-s starting from each node, 
and taking the max path from each source node.

This brings up the idea of using memoization. 
Why not build a memo with longest path starting from each node. 
We can even build on this idea and argue that we don't need to build a graph at all.

-> We can just simply simulate a DFS without building a graph.

- yes not getting into the trap of building a full data structure but 
leveraging the essence of one.
"""

class Node:
    def __init__(self, char:str):
        self.char = char
        self.children  = []
        self.word_finished = False
        self.counter = 1



class Solution:
    def longestStrChain(self,words: List[str]) -> int:
        memo = {}
        word_set= set(words)
        for current_word in sorted(word_set,key=len, reverse=True):
             #print("====> ", current_word)
             for i in range(0,len(current_word)):
                prefix = current_word[:i] +current_word[i+1:] 
                #print(prefix)           
                for word in word_set:
                    if word == prefix:
                        #print(word,prefix)
                        if prefix in memo:
                            memo[prefix].append(word)
                        else:
                            memo[prefix] = [word]
                        
        print(memo)
        return 1
    
    def longestStrChain_2(self,words: List[str]) -> int:
        memo = {}
        for current_word in sorted(words,key=len, reverse=True):
             for i in range(0,len(current_word)):
                prefix = current_word[i:]
                if prefix in words:
                    if prefix not in memo:
                        memo[prefix] = set(prefix)
                    else:
                        for key in memo.keys():
                            if prefix.startswith(key):
                                memo[key].add(prefix)
        print(memo)
        return len(max(memo.values()))
                       


       
    
    def helper(self, words, counter):   
        if current_word not in words:
            return counter
        local_max = []
        for word in words:
            
            
            for i in range(1,len(current_word)):
                print(current_word[i:])
                print(words)
                local_max.append(self.helper(words,current_word[i:],counter+1))
        local_max.append(self.helper(words,current_word,counter+1))
        
        
        return max(local_max,[0])
                





    """
    def wrong(self):
        root = Node("*")
        for word in words:
            self.add(root,word)       
        self.print(root,[])
        print(self.find_max_height(root,0))
        return len(words)
    """

    def add(self, root, word:str):
        node = root
        for char in sorted(word):
            found = False
            for child in node.children:
                if child.char == char:
                    child.counter+=1
                    node = child
                    found = True
                    break
        
        if not found:
            new_node = Node(char)
            node.children.append(new_node)
            node = new_node
        node.word_finished = True
    
    def print(self, node,searched):
        if not node:
            return
        if node in searched:
            return
        searched.append(node)
        print(node.char , ": " , node.children)
        for child in node.children:
            self.print(child,searched)   

    def find_max_height(self, node, big):
        if not node.children:
            return big

        results = []
        for child in node.children:
            results.append(self.find_max_height(child,big+1))        
        return max(results)



if __name__ == "__main__":
    s = Solution()
    example_one = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
    r = s.longestStrChain(example_one)
    print(r)