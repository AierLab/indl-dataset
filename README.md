# InDL: In-Diagram Logic Interpretation

## About The Project

This repository hosts code and data for our project evaluating deep learning models' capabilities for interpreting in-diagram logic using visual illusions. It encompasses our novel InDL dataset, several Jupyter notebooks showcasing our experiments, and Python scripts needed to reproduce our results.

The goal of our work is to shed light on the 'black box' nature of deep learning models by investigating their ability to handle complex interplay of perception and logic that visual illusions offer. For more details about our approach, refer to our paper linked here: [InDL: A New Datasets and Benchmark for In-Diagram Logic Interpreting based on Visual Illusion
](https://arxiv.org/abs/2305.17716).

![The 5 dataset images, with the corresponding labels.](https://github.com/rabbit-magic-wh/InDL/assets/55401837/3df04e09-ed85-45c9-a49c-6c717ec4443b)

## Repository Structure

```
.
│  .gitignore
│  benchmark-report.ipynb
│  benchmarking-train.ipynb
│  benchmarking.ipynb
│  LICENSE
│  README.md
│  result.pdf
│  scripts.py
│  torch_demo.py
│
├─data
│      data_generate.py
│      generator.py
│      planner.py
│
└─models
    ├─dataset01_benchmarking
    │  *.csv
    ├─dataset02_benchmarking
    │  *.csv
    ├─dataset03_benchmarking
    │  *.csv
    ├─dataset04_benchmarking
    │  *.csv
    └─dataset05_benchmarking
           *.csv
```

The `data` directory includes Python scripts for data generation. The `models` directory hosts benchmarking results for several datasets with model evaluation files named in the pattern `<model_name>_eval.csv`.

The Jupyter notebooks:

- `benchmark-report.ipynb`: This notebook analyses and reports the benchmarking results.
- `benchmarking-train.ipynb`: This notebook trains models on the datasets.
- `benchmarking.ipynb`: This notebook benchmarks the models.

## Setup & Reproduction Steps

To reproduce our results, follow these steps:

1. Ensure that you have the required dependencies installed. Our project primarily depends on `pyillusion` (which can be installed via pip: `pip install pyillusion`), along with `matplotlib` and `pandas`.

2. Clone the repository: `git clone <repo-url>`

3. Navigate into the cloned repository: `cd <repo-name>`

4. Run the data generation script: `python data/data_generate.py`

5. Use the provided Jupyter notebooks (`benchmarking-train.ipynb`, `benchmarking.ipynb`, and `benchmark-report.ipynb`) to train models, perform benchmarking, and analyze results respectively.

## Licensing & Contributions

This project is licensed under the Apache-2.0 license. We welcome contributions and improvements to the project. Please see the CONTRIBUTING.md file for more details.

## Contact Information

For any questions or issues, please open a GitHub issue. We'll respond as soon as possible.

## Reference

```bibtex
@misc{yang2023indl,
      title={InDL: A New Datasets and Benchmark for In-Diagram Logic Interpreting based on Visual Illusion}, 
      author={Haobo Yang and Wenyu Wang and Ze Cao and Zhekai Duan and Xuchen Liu},
      year={2023},
      eprint={2305.17716},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---
_Maintained by Rabbit Magic Workhouse, an open source group._
