"""
Question Discribe:
You have m types of coins available in infinite quantities
where the value of each coins is given in the array S=[S0,... Sm-1]
Can you determine number of ways of making change for n units using
the given types of coins?
https://www.hackerrank.com/challenges/coin-change/problem
"""

def Coin_Changer(Amounts,Number,Value):
  """
    >>> Coin_Changer([1, 2, 3], 3, 4)
    4
    >>> Coin_Changer([1, 2, 3], 3, 7)
    8
    >>> Coin_Changer([2, 5, 3, 6], 4, 10)
    5
    >>> Coin_Changer([10], 1, 99)
    0
    >>> Coin_Changer([4, 5, 6], 3, 0)
    1
  """

  """
    In order to use Dynamic Programming
    Create a table to save historic result and use to compute the future
  """
    
  Table = [0]*(Value+1)
    
  # There is exactly 1 way to get to zero(You pick no coins).

  Table[0] = 1

  for coin_value in Amounts:
    for index in range(coin_value,Value+1):
      Table[index] +=Table[index-coin_value]
  return Table[Value]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
