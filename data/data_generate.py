from generator import *
from planner import Planner

planner = Planner()
for dataset in [dataset01, dataset02, dataset03]:
    planner.generate(dataset, size=10000)