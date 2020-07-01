"""Question 3A: Assuming we have a PrintsHW(P,x) function"""

"""Part A: We are reducing the TestHalt problem to the PrintsHW problem.
In other words, we use the PrintsHW problem to solve the TestHalt problem.
The function below uses the PrintsHW subroutine to solve TestHalt!
Yet since the notes prove to us that TestHalt cannot be solved (is uncomputable),
therefore it cannot be possible for the PrintsHW function to exist either."""

def TestHalt(P, x):
    """Returns True or False depending upon whether or not P called on x halts."""
    def P_prime(x):
        run P(x) while suppressing print statements
        print("Hello World!")   # prints HW if P(x) terminates
    if PrintsHW(P_prime, x):
        return True
    return False

"""Question 3B: Assume we have a PrintsHWByK(P, x, k)"""

"""Part B: We are reducing the PrintsHW problem (which we showed in part a to be uncomputable)
to the PrintsHWByK problem. In other words, we use the PrintsHWByK problem to solve the
PrintsHW problem. The function below uses the PrintsHWByK function as a subroutine
to solve the PrintsHW problem. Yet since we showed in part a that PrintsHW is
uncomputable, therefore it cannot be possible for the PrintsHWByK function to exist either!"""

def PrintsHW(P, x):
    """Returns True or False depending upon whether or not P called on x prints 'hello world'"""
    for i in range(len(P)):   # for however many lines the program P has,
        if Prints_HW_By_K(P,x,i):
            return True
    return False

"""Question 3C:"""
"""The task in the problem is computable, because we can easily count the number of instructions
that a machine has executed so far. However, it is impossible to tell whether or not a computer
program has reached a certain line in its process of execution. This is a subtle distinction that
is important to keep in mind!"""
