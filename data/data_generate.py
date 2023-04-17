from generator import *
from planner import Planner

planner = Planner()
for dataset in [dataset02]: # dataset04
    planner.generate(dataset, size=10000)