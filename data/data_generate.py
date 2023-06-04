from generator import *
from planner import Planner

planner = Planner()
for dataset in [dataset03]: # dataset02, dataset03, dataset04, dataset05
    planner.generate(dataset, size=2000)