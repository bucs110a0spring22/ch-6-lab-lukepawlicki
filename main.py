
def seq3np1(n):
  """
  Print the 3n+1 sequence from n, terminating when it reaches 1.
  args: n (int) starting value for 3n+1 sequence
  return: None
  """  
  count = 0
  while(n != 1):
      if(n % 2) == 0:    
        n = n // 2
      else:                 
        n = n * 3 + 1
      count = count + 1
  return count
def main():
  upper_bound = int(input("What is the upper bound?: "))
  if upper_bound < 0:
    print("Value cannot be negative")
    return
  for start in range(1, upper_bound + 1):
    print("The value being plugged into the sequence is ", start)
    print("Number of iterations to get to 1: " , seq3np1(start))
   
  
main()
