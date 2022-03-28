import turtle

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

def graph(upper_limit=0, graphingTurtle=None, writingTurtle=None):
  '''
  Graphs the "n" value on the x-axis and iterations of the sequence on the y-axis, keeps track of maximum number of iterations so far
  args: upper_limit (int), highest value for n that the sequence goes up to
        graphingTurtle: turtle object used to make the graph
        writingTurtle: turtle object used to writingTurtle
  return: None
  '''
  max_so_far = 0
  for i in range(1,upper_limit + 1):
    result = seq3np1(i)
    graphingTurtle.goto(i, result)
    if result > max_so_far:
      max_so_far = result
      writingTurtle.clear()
      writingTurtle.up()
      writingTurtle.goto(0,max_so_far)
      writingTurtle.down()
      writingTurtle.write("Maximum so far: " + "Value- "+ str(i)+'\n'+ "Iterations of the sequence- " + str(max_so_far))
      turtle.setworldcoordinates(0,0,i+10,max_so_far+10)

def main():
  upper_bound = int(input("What is the upper bound?: "))
  if upper_bound < 0:
    print("Value cannot be negative")
    return
  for start in range(1, upper_bound + 1):
    print("The value being plugged into the sequence is ", start)
    print("Number of iterations to get to 1: " , seq3np1(start))
  t_graph = turtle.Turtle()
  t_write = turtle.Turtle()
  t_graph.shape('turtle')
  t_write.shape('turtle')
  window = turtle.Screen()
  turtle.setworldcoordinates(0,0,10,10)
  graph(upper_bound,t_graph,t_write)
  window.exitonclick()
   
  
main()
