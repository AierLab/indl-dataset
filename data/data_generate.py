from generator import *
from planner import Planner
from concurrent.futures import ThreadPoolExecutor

def generate_dataset(dataset):
    planner.generate(dataset, size=2000)

planner = Planner()
datasets = [dataset01, dataset02, dataset03, dataset04, dataset05]

with ThreadPoolExecutor() as executor:
    executor.map(generate_dataset, datasets)