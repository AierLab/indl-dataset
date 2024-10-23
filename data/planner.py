import os

class Planner:
    def __init__(self, train_dir: str = "train", test_dir: str = "test", split_ratio: float = 0.2, positive_ratio: float = 0.3):
        
        self.train_dir = train_dir
        self.test_dir = test_dir
        
        self.split_ratio = split_ratio
        self.positive_ratio = positive_ratio
        
    def generate(self, func, size: int = 100):
        test_size = (int) (size * self.split_ratio)
        train_size = size - test_size
        
        train_dir = os.path.join(self.train_dir, func.__name__)
        test_dir = os.path.join(self.test_dir, func.__name__)
                
        if not os.path.exists(train_dir): 
            os.makedirs(train_dir)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
        
        func(train_dir, train_size, self.positive_ratio)
        func(test_dir, test_size, self.positive_ratio)