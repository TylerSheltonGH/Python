# Import necessary modules
import copy
import random

# Define the Hat class
class Hat:
    # Constructor to initialize the contents of the hat with colored balls and their quantities
    def __init__(self, **balls):
        self.contents = []

        # Populate the contents list with colored balls based on the input arguments
        for k, v in balls.items():
            self.contents.extend([k] * v)

    # Method to draw a specified number of balls randomly from the hat
    def draw(self, amount):
        balls = []
        # If the number of balls to draw exceeds the number of balls in the hat,
        # return all the balls in the hat (as there are no balls left after drawing)
        if amount >= len(self.contents):
            return self.contents

        for i in range(amount):
            # Randomly select a ball from the hat, remove it from the contents, and add it to the drawn balls list
            rng = random.randrange(len(self.contents))
            balls.append(self.contents[rng])
            self.contents.pop(rng)

        return balls


# Function to perform an experiment by drawing balls from the hat and checking if the expected balls are drawn
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0  # Counter to keep track of the number of successful experiments (where all expected balls are drawn)
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)  # Create a deep copy of the original hat to perform the experiment
        balls = new_hat.draw(num_balls_drawn)  # Draw a specified number of balls from the hat

        # Check if the expected balls are drawn in the experiment
        should_add = True
        for k, v in expected_balls.items():
            if balls.count(k) < v:
                should_add = False
                break

        if should_add:
            m += 1  # Increment the counter if all expected balls are drawn in the experiment

    # Calculate and return the probability of drawing the expected balls
    return m / num_experiments


# Use cases

# Example 1
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print("Probability:", probability)

# Example 2
random.seed(95)  # Set the random seed to ensure reproducibility of the experiment
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)

print("Probability:", probability)

# Example 3
random.seed(95)  # Set the random seed to ensure reproducibility of the experiment
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)

print("Probability:", probability)
