
## File-Entropy-Calculator

File-Entropy-Calculator(文件熵计算器)：一款可计算exe文件熵的工具。

初衷：免杀测试途中查看文件熵可能会用到。

## 什么是文件熵

文件熵是信息理论中的一个概念，用于度量文件或数据的不确定性和随机性。文件熵与文件内容的分布有关，具体来说，它与文件中不同字节或符号的出现频率有关。

如果文件中的字节或符号的出现频率比较均匀、接近相等，那么文件的熵会比较高，表示文件的内容更加随机和不确定。相反，如果文件中的某些字节或符号的出现频率非常高，而其他字节或符号的出现频率非常低，那么文件的熵会比较低，表示文件的内容更加有结构和可预测。

因此，文件熵可以用作衡量文件的复杂程度、信息量以及数据压缩的潜力。对于加密算法、数据传输和存储等领域，文件熵的概念非常重要。

## 用法

1.python执行

```
python File-Entropy-Calculator.py -r xxx.exe路径
```

![image](https://github.com/langsasec/File-Entropy-Calculator/assets/45072131/004edac3-3f88-46a2-8b2f-81bf86bc80f6)


2.打包exe执行

```
fec.exe -r xxx.exe路径
```

![image](https://github.com/langsasec/File-Entropy-Calculator/assets/45072131/a1512189-860e-465f-9a3f-517fe496e2a3)


