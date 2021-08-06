## Introduction
```
@article{li2019additive,
  title={Additive powers-of-two quantization: An efficient non-uniform discretization for neural networks},
  author={Li, Yuhang and Dong, Xin and Wang, Wei},
  journal={arXiv preprint arXiv:1909.13144},
  year={2019}
}
```

## Experiments

| method | dataset | backbone | node_num |W/A bit| Top-1(%)  | Top-5(%) | BS | CFG|
|--------|---------|----------|----------|-------|-----------|----------|----|----|
| APOT  |imagnet-1k |Res18   | 4   |  4 / 4|   70.60     |  89.71    |128  |[cfg](./res18/config3_res18_apot_m2_64_4w4f.py)  |
| APOT  |imagnet-1k |Res18   | 4    |  3 / 3|   69.55     |  89.12    |128 |[cfg](./res18/config2_res18_apot_m2_64_3w3f.py)  |
| APOT  |imagnet-1k |Res18   | 4    |  2 / 2|   -     |  -    |128  |[cfg](./res18/config1_res18_apot_m2_64_2w2f.py)  |  
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| APOT  |imagnet-1k |Res50   | 4    |  4 / 4| 76.41  | 93.09 |32  |[cfg](./res50/config3_res50_apot_m4_32_4w4f.py)  |
| APOT  |imagnet-1k |Res50   | 4    |  3 / 3|   75.77   |  92.60       |32  |[cfg](./res50/config2_res50_apot_m4_32_3w3f.py)  |
| APOT  |imagnet-1k |Res50   | 4    |  2 / 2|   73.38  |    91.41  |32  |[cfg](./res50/config1_res50_apot_m4_32_2w2f.py)  | 
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| APOT  |imagnet-1k |MobileNet   | 4     |  4 / 4|  67.98   |  88.16   |32  |[cfg](./mobilenetv2/config3_mobilenetv2_apot_m4_64_4w4f.py)  |
| APOT  |imagnet-1k |MobileNet   | 4    |  3 / 3|  N/A  |  N/A   |32  |[cfg](./mobilenetv2/config2_mobilenetv2_apot_m4_64_3w3f.py)    |
| APOT  |imagnet-1k |MobileNet   | 4    |  2 / 2|  -  |  -   |32  |[cfg](./mobilenetv2/config1_mobilenetv2_apot_m4_64_2w2f.py)    | 
