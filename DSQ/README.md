### DSQ Introduction
```
@inproceedings{gong2019differentiable,
  title={Differentiable soft quantization: Bridging full-precision and low-bit neural networks},
  author={Gong, Ruihao and Liu, Xianglong and Jiang, Shenghu and Li, Tianxiang and Hu, Peng and Lin, Jiazhen and Yu, Fengwei and Yan, Junjie},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={4852--4861},
  year={2019}
}
```

### Experinemnt

| method      | dataset   | backbone | bs  | node_num  | epoch |   W_bit/A_bit | top1_acc | top5_acc | cfg  |   
|:-----------:|:---------:|:-------:|:---:|:---------:|:-----:|:-------------:|:--------:|:--------:|:----:|
| DSQ         | ImageNet  | Res18 | 128  | 1  | 100 |   2/2 | 52.5740 | 76.9160 | [cfg](res18/config6_res18_dsq_m1_128_2w2f.py)  | 
| DSQ         | ImageNet  | Res18 | 128  | 1  | 100 |   3/3 | 66.7840 | 87.2600 | [cfg](res18/config1_res18_dsq_m1_128_3w3f.py)  | 
| DSQ         | ImageNet  | Res18 | 128  | 1  | 100 |   4/4 | 69.700 | 89.1140 | [cfg](res18/config5_res18_dsq_m2_128_4w4f.py)  | 
|:--------:|:---------:|:--------:|:--:|:--------:|:-----:|:-------------:|:--------:|:--------:|:----:|
| DSQ      | ImageNet  | Res50    | 16 | 1  |  100  |  2/2 |         |         | [cfg]           | 
| DSQ      | ImageNet  | Res50    | 16 | 1  |   70  |  3/3 | 74.2500 | 91.8580 | [cfg](res50/config7_res50_dsq_m9_16_3w3f.py)  | 
| DSQ      | ImageNet  | Res50    | 16 | 9  |   70  |  4/4 | 75.5680 | 92.6380 | [cfg](res50/config6_res50_dsq_m9_16_4w4f.py) | 
|:--------:|:---------:|:--------:|:--:|:--------:|:-----:|:-------------:|:--------:|:--------:|:----:|
| DSQ      | ImageNet  | mobilenetv2  | 16 | 1 |  100  |  2/2 |         |         | [cfg]           | 
| DSQ      | ImageNet  | mobilenetv2  | 16 | 1  |  70  |  3/3 | | | [cfg]()  | 
| DSQ      | ImageNet  | mobilenetv2  | 16 | 9  |  70  |  4/4 | 62.230 | 84.296 | [cfg](mobilenetv2/config6_res50_dsq_m9_16_4w4f.py) | 


### Experinemnt Analysis