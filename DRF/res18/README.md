### DoReFa Introduction
```
@article{zhou2016dorefa,
  title={Dorefa-net: Training low bitwidth convolutional neural networks with low bitwidth gradients},
  author={Zhou, Shuchang and Wu, Yuxin and Ni, Zekun and Zhou, Xinyu and Wen, He and Zou, Yuheng},
  journal={arXiv preprint arXiv:1606.06160},
  year={2016}
}
```

### Experinemnt

| method      | dataset   | backbone | bs  | node_num  | epoch |   W_bit/A_bit | top1_acc | top5_acc | cfg  |   
|:-----------:|:---------:|:-------:|:---:|:---------:|:-----:|:-------------:|:--------:|:--------:|:----:|
| DoReFa    | ImageNet  | Res18 | 128  | 1  | 100 | 2/2 | 48.9460 | 73.7360 | [cfg](./config14_res18_drf_m5_128_2w2f.py) | 
| DoReFa    | ImageNet  | Res18 | 128  | 1  | 100 | 3/3 | 63.8940 | 85.7160 | [cfg](./config22_res18_drf_m4_128_3w3f.py) |
| DoReFa    | ImageNet  | Res18 | 128  | 1  | 100 | 4/4 | 69.3260 | 88.9780 | [cfg](./config21_res18_drf_m5_128_4w4f.py) | 

### Experinemnt Analysis
