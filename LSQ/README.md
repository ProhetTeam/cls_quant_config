## Introduction
```
@article{esser2019learned,
  title={Learned step size quantization},
  author={Esser, Steven K and McKinstry, Jeffrey L and Bablani, Deepika and Appuswamy, Rathinakumar and Modha, Dharmendra S},
  journal={arXiv preprint arXiv:1902.08153},
  year={2019}
}
```

## Experiments

| method | dataset | backbone | node_num |W/A bit| Top-1(%)  | Top-5(%) | BS | CFG|
|--------|---------|----------|----------|-------|-----------|----------|----|----|
| LSQ  |imagnet-1k | Res18   | 4   |  4 / 4|   70.36     |  89.57    |128  |[cfg](./res18/config2_res18_lsq_m2_64_4w4f.py)  |
| LSQ  |imagnet-1k |Res18   | 4    |  3 / 3|   69.35     |  88.99    |128 |[cfg](./res18/config2_res18_lsq_m2_64_3w3f.py)  |
| LSQ  |imagnet-1k |Res18   | 4    |  2 / 2|   66.31     |  86.98    |128  |[cfg](./res18/config1_res18_lsq_m2_64_2w2f.py)  |  
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| LSQ  |imagnet-1k |Res50   | 4    |  4 / 4| 76.88  | 93.29 |32  |[cfg](./res50/config3_res50_lsq_m4_32_4w4f.py)  |
| LSQ  |imagnet-1k |Res50   | 4    |  3 / 3|   75.48   |  92.58       |32  |[cfg](./res50/config2_res50_lsq_m4_32_3w3f.py)  |
| LSQ  |imagnet-1k |Res50   | 4    |  2 / 2|   72.00  |    90.70  |32  |[cfg](./res50/config1_res50_lsq_m4_32_2w2f.py)  | 
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| LSQ  |imagnet-1k |MobileNet   | 4     |  4 / 4|  67.98   |  88.16   |32  |[cfg](./mobilenetv2/config3_mobilenetv2_lsq_m4_64_4w4f.py)  |
| LSQ  |imagnet-1k |MobileNet   | 4    |  3 / 3|  64.41  |  85.45   |32  |[cfg](./mobilenetv2/config2_mobilenetv2_lsq_m4_64_3w3f.py)    |
| LSQ  |imagnet-1k |MobileNet   | 4    |  2 / 2|  -  |  -   |32  |-    | 
