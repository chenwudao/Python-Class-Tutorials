# Python 课堂教程与练习

本仓库是 **Python 课程** 的课堂笔记、例题与作业代码集合，包含从基础语法到文件操作、文档生成等实践内容。

---

## 项目结构

```
Python_Class_Tutorials/
├── 1stclass.ipynb      # 第1课：条件与循环、算法、函数与作用域
├── 2stclass.ipynb      # 期中错题详解
├── 3stclass.ipynb      # 对象/标签、函数/方法/类、string/list/tuple/set 总结
├── 4stclass.ipynb      # 复习：传递机制、dict/哈希、正则、高阶函数
├── Assignment_Sou.ipynb # 作业：字符串变换、表格操作
├── 3.py                # 找字符串中第一个重复字符
├── 4.py                # 用 python-docx 生成课程论文 Word 文档
├── fileopr.py          # 文件读写示例（with / 手动 open-close）
├── helloworld.txt      # 供 fileopr.py 读写的示例文件
├── list.png            # 课程图：list 内置方法
├── rule.png            # 课程图：Python 传递机制
├── regax.png           # 课程图：正则表达式
├── python精选3.pdf     # 课程参考 PDF
├── python精选4.pdf
├── python精选5.pdf
└── README.md           # 本说明
```

---

## 内容概览

### 课堂笔记本（Jupyter）

| 文件 | 主要内容 |
|------|----------|
| **1stclass.ipynb** | `if-elif-else`、`for-else`、`while-else`；百分制转等级、双数之和、阶乘等例题 |
| **2stclass.ipynb** | 期中错题：函数执行、斐波那契、输入与运算、列表与函数参数等 |
| **3stclass.ipynb** | 对象与标签；函数、方法、类的区别；string/list/tuple/set 常用方法与示例 |
| **4stclass.ipynb** | 传递机制复习、dict 与哈希表、正则表达式、`map`/`filter`/`lambda`；两数之和哈希解法 |
| **Assignment_Sou.ipynb** | 作业：字符串变换（大小写交替 + 单词反转）、表格的 filter/append/delete 等操作 |

### Python 脚本

| 文件 | 功能 |
|------|------|
| **3.py** | 在字符串中查找**第一个重复出现**的字符（如 `"abccaz"` → `'c'`） |
| **4.py** | 使用 `python-docx` 按课程要求生成《根脉与革新：近现代中国现代化进程中传统与现代的辩证共生》论文 Word 文档（标题、作者、摘要、正文、参考文献等格式） |
| **fileopr.py** | 演示文件读写：`with` 读、手动 `open/close` 读、覆盖写、追加写；支持命令行指定路径与模式 |

---

## 环境与依赖

- **Python**：建议 3.7+
- **Jupyter**：用于运行 `.ipynb` 笔记本
- **python-docx**：仅 **4.py** 需要，用于生成 Word 文档  
  ```bash
  pip install python-docx
  ```

---

## 使用说明

- **笔记本**：在项目根目录下用 Jupyter 或 VS Code 打开对应 `.ipynb`，按顺序运行单元格即可。
- **3.py**：  
  ```bash
  python 3.py
  ```
  会运行内置示例（如 `"abccaz"`）并打印第一个重复字符。
- **4.py**：  
  ```bash
  python 4.py
  ```  
  会在当前目录生成论文 Word 文件（`.docx`）。
- **fileopr.py**：  
  ```bash
  python fileopr.py --mode read              # 默认读 helloworld.txt
  python fileopr.py --mode write --text "hi" # 覆盖写入
  python fileopr.py --mode append --text "hi" # 追加写入
  python fileopr.py --path "你的文件路径" --mode read
  ```

---

## 参考资源

- 课程配图：`list.png`（list 方法）、`rule.png`（传递机制）、`regax.png`（正则）
- 课程 PDF：`python精选3.pdf`、`python精选4.pdf`、`python精选5.pdf`

---

## 说明

- 仓库中的作业与例题仅供课程学习与复习使用。
- 若路径或文件名与你的环境不一致（如 `fileopr.py` 里默认的 `helloworld.txt` 路径），可根据需要修改脚本中的路径或通过命令行参数传入。
