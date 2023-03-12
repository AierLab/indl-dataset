from fastai.vision.all import *
import torch.nn as nn
from datetime import datetime

class Worker:
    def __init__(self, exp_name: str, model_name: str, model, trainloader, testloader, epochs=10, lr=1e-2) -> None:
        self.epochs = epochs
        self.lr = lr
        
        data = DataLoaders(trainloader, testloader)
        self.learner = Learner(data, model, loss_func=nn.CrossEntropyLoss(), opt_func=Adam, metrics=accuracy)
        self.model_path=f'./models/{exp_name}/{model_name}.pt'
        if not os.path.exists(f'./models/{exp_name}'): 
            os.mkdir(f'./models/{exp_name}')
        
    def train(self):
        if os.path.exists(self.model_path): 
            print(f"state dict found: {self.model_path}")
            return
        
        # self.learner.fit_one_cycle(self.epochs, self.lr)
        self.learner.fine_tune(self.epochs, self.lr)

        torch.save(self.learner.model.state_dict(), self.model_path)
    
    def eval(self):
        self.learner.freeze()
        self.learner.fit(1)
        self.learner.unfreeze()