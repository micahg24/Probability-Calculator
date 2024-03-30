import copy
import random
# Consider using the modules imported above.

class Hat:
  #Initializes balls in the hat and the list in content

  def __init__(self, **kwargs):
    self.contents = [key for key, value in kwargs.items() for _ in range(value)]

  #Draws random number of balls
  def draw(self,num_balls):
    num_balls = min(num_balls, len(self.contents))
    return [self.contents.pop(random.randrange(len(self.contents))) for i in range (num_balls)]

#Experiment function which determines the probability based on the hats, number of balls, and number of experiments
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for _ in range(num_experiments):
    more_hats = copy.deepcopy(hat)
    
    balls_drawn = more_hats.draw(num_balls_drawn)

    balls_needed = sum([1 for key, value in expected_balls.items() if balls_drawn.count(key) >= value])
  
    if balls_needed == len(expected_balls):
      m += 1

    else:
      0
  
  return m / num_experiments
