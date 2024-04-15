## Visual Dataset

### 获取数据集

#### SWaT 数据集 WADI 数据集
可以通过填写以下表格来获取 SWaT 和 WADI 数据集：

https://docs.google.com/forms/d/1GOLYXa7TX0KlayqugUOOPMvbcwSQiGNMOjHuNqKcieA/viewform?edit_requested=true



#### PSM 数据集

数据集可在以下位置下载：

https://github.com/eBay/RANSynCoders/tree/main/data



### SMD 数据集

数据集可在以下位置下载：

https://github.com/NetManAIOps/OmniAnomaly/tree/master/ServerMachineDataset



### 处理数据集 -（贴处理代码+部署说明）

下载数据集放进对应文件夹，运行make_pk.py

运行 visual_dataset.ipynb 修改想看的数据集名称，运行查看

### 数据洞察 

**SWaT（安全水处理）：**SWaT 数据集是在 11 天内从具有 51 个传感器的小型水处理测试台收集的。 在过去 4 天内，使用不同的攻击方法注入了 41 个异常，而在前 7 天内仅生成正常数据。 

**WADI（水分配测试台）：**WADI 数据集是从一个精简的城市供水系统获取的，该系统有 123 个传感器和执行器，运行了 16 天。 前 14 天仅包含正常数据，其余两天有 15 个异常段。 

**PSM（池化服务器指标）：**PSM 数据集是从 eBay 的多个应用程序服务器节点内部收集的。 有 13 周的训练数据和 8 周的测试数据。 

**MSL（火星科学实验室）和SMAP（土壤湿度主动被动）：**MSL和SMAP数据集是NASA收集的公共数据集，包含来自航天器监测事件意外异常（ISA）报告的遥测异常数据系统。 数据集分别有 55 和 25 维。 训练集包含未标记的异常。 

**SMD（服务器机器数据集）：**SMD 是从一家大型互联网公司收集的，包含来自 28 台服务器机器和 38 个传感器的 5 周数据。 前 5 天仅包含正常数据，最后 5 天间歇性注入异常数据。 

**trimSyn（修剪合成数据集）：**原始合成数据集是使用三角函数和高斯噪声生成的。 我们从[39]获取数据集并修剪测试数据集，使得仅存在一段异常。

