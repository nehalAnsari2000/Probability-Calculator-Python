import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # Initialize hat with ball colors and counts.
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # Draw balls randomly, return all if num_balls is more that or equal to available balls.
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Calculate probability of drawing expected balls.
    success_count = 0  
    
    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)  # Copy hat to preserve original 
        drawn_balls = temp_hat.draw(num_balls_drawn)  
        drawn_counts = {}
        
        # Count occurrences of drawn balls
        for ball in drawn_balls:
            if ball in drawn_counts:
                drawn_counts[ball] += 1
            else:
                drawn_counts[ball] = 1
        
        # Check if all expected counts are met
        success = True 
        for color, count in expected_balls.items():
            if not drawn_counts.get(color, 0) >= count:
                success = False
        if success:
            success_count += 1
    
    return success_count / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red':2,'green':1}, num_balls_drawn=5, num_experiments=2000)
print(probability)