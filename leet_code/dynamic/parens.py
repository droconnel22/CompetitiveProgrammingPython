


"""
Parens

Implemenet an alogrithm to print all valid () combinations
of n pairs of parenthesis

Example
Input: 3
Output ((())), (()()), (())(), ()()()

Example 1
()

Example 2
()(),  (())

We can this by inserting a pair of paratheses inside every existing pair of parenthese as well
as one at the begining of the string. 

Any other places that we could insert parathenses such as at the end of the string would 
reduce to earlier cases

We'll need to check for duplicates

"""

def add_parentheses(count):
    cases = set()
    # Base case we can build from
    # move up 
    if (count == 0):
        cases.add("")
    else:
        previous_cases = add_parentheses(count-1)
        # Can insert a piar of paren inside every existing
        # can also add one at the begininnig of each string
        for case in previous_cases:
            temp = "()"+case
            cases.add(temp)
            temp = ""
            for c in case:
                if c == '(':
                    temp += c + "()"
                else:
                    temp +=c
            cases.add(temp)
        cases.union(previous_cases)
    return cases
            




if __name__ == "__main__":
    for ans in add_parentheses(3):
        print(ans)
    pass