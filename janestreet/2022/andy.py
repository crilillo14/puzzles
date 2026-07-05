import numpy as np
import math

def f(n: int) -> float:
    """
    probability of first return to 0 = 2n,
    for a non lazy random walk with p(x_{t+1} = x_t + 1) = 2/3 , 
    with the initial conditions of X_0 = 0, X_1 = 1.

    So really, it's the probability of first arrival to 0 from 1 being t = n steps"""  
    n = n // 2
    if n == 1:
        return 1 / 3
    return math.comb(2*n - 3, n - 1) * pow(2/3, n - 1) * pow(1/3, n)

def main():
    p_negation = sum(f(i) for i in range(2, 21, 2))
    print(f"p is {1 - p_negation}")

if __name__ == "__main__": 
    main()
