from fastai.vision.all import *
import torch.nn as nn
from datetime import datetime

class Worker:
    def __init__(self, model, trainloader, testloader, epochs=10, lr=1e-2) -> None:
        self.epochs = epochs
        self.lr = lr
        
        data = DataLoaders(trainloader, testloader)
        self.learner = Learner(data, model, loss_func=nn.CrossEntropyLoss(), opt_func=Adam, metrics=accuracy)
        
        self.model_path=f'./model_{str(datetime.now())}.pt'
        
    def train(self):
        # learner.fit_one_cycle(epochs, lr) # fine tune is better
        self.learner.fine_tune(self.epochs, self.lr)

        torch.save(self.learner.model.state_dict(), self.model_path)
    
    def eval(self):
        self.learner.freeze()
        self.learner.fit(1)
        self.learner.unfreeze()