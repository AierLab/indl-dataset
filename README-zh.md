# InDL: In-Diagram Logic Interpretation

## 关于项目

此代码库托管了我们的项目代码和数据，该项目使用视觉错觉评估深度学习模型解读图形逻辑的能力。它包括我们独特的InDL数据集，展示我们实验的几个Jupyter笔记本，以及复现我们结果所需的Python脚本。

我们工作的目标是通过研究视觉错觉提供的感知和逻辑复杂交互，揭示深度学习模型的“黑盒”本质。有关我们的方法的更多详细信息，请参考我们的论文，链接在此：[InDL: A New Datasets and Benchmark for In-Diagram Logic Interpreting based on Visual Illusion
](https://arxiv.org/abs/2305.17716).

![The 5 dataset images, with the corresponding labels.](https://github.com/rabbit-magic-wh/InDL/assets/55401837/8ebdec35-d39b-4abf-a765-c282406e7f7c)
## 代码库结构

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

`data`目录包含数据生成的Python脚本。`models`目录托管了与多个数据集的基准测试结果，模型评估文件的命名格式为 `<模型名称>_eval.csv`。

Jupyter笔记本：

- `benchmark-report.ipynb`: 此笔记本分析并报告基准测试结果。
- `benchmarking-train.ipynb`: 此笔记本在数据集上训练模型。
- `benchmarking.ipynb`: 此笔记本对模型进行基准测试。

## 设置 & 复现步骤

要复现我们的结果，按照以下步骤操作：

1. 确保已安装所需的依赖。我们的项目主要依赖于`pyillusion`（可以通过pip安装：`pip install pyillusion`），以及`matplotlib`和`pandas`。

2. 克隆代码库：`git clone <仓库链接>`

3. 导航到克隆的代码库：`cd <仓库名称>`

4. 运行数据生成脚本：`python data/data_generate.py`

5. 使用提供的Jupyter笔记本（`benchmarking-train.ipynb`，`benchmarking.ipynb`，和 `benchmark-report.ipynb`）来训练模型，进行基准测试，以及分析结果。

## 许可证和贡献

该项目根据Apache-2.0许可证授权。我们欢迎对该项目的贡献

和改进。更多详细信息请参阅CONTRIBUTING.md文件。

## 联系信息

如有任何疑问或问题，请在GitHub上创建issue。我们会尽快回应。

## 参考文献

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
由 Rabbit Magic Workhouse 维护。
🌸QQ群：[兔叽の魔术工房](https://jq.qq.com/?_wv=1027&k=EaGddTQg) (942848525)
⭐B站账号：[白拾Official](https://space.bilibili.com/98639326)
