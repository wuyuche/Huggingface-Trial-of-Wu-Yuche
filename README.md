# Trial-1-of-Wu-Yuche
2D与3D是两种模型

2D对应的json文件分别是：2D.json学长给的原数据；2D_new.json将type加入后的结果；2D_norm.json对指标归一化并计算均值后的结果
3D对应的json文件同理

eval_ctrate_text.py是学长给的计算指标的源代码

generate.py是用于生成2D_new.json文件的，将type加入（3D同理，改一下路径名即可，就没有另写一个脚本）

normalize.py是用于生成2D_norm.json文件的，max-min归一化，并计算了均值（3D同理，改一下路径名即可，就没有另写一个脚本）

evaluate1.py是用于计算：2种模型在不同type的问题上的表现情况。得到的是对于所有的问答，2种模型在不同问题type上各种指标的平均得分（归一化后的平均）。结果存储在model_comparison.txt文件中。

model_comparison_result.txt文件是经过手动调整、对齐之后的结果，没有数据上的变化，只是排版好看了一些

find_example.py是用于寻找两种模型表现差别较大的问题id。能够找出每种type问题中，两种模型平均得分差别最大的两个问题的id
