## Introduction
```
@article{
  title={LSQ+: Improving low-bit quantization through learnable offsets and better initialization},
  author={Yash Bhalgat},
  journal={arXiv preprint arXiv:2004.09576},
  year={2020}
}
```

## Experiments

| method | dataset | backbone | node_num |W/A bit| Top-1(%)  | Top-5(%) | BS | CFG|
|--------|---------|----------|----------|-------|-----------|----------|----|----|
| LSQD+  |imagnet-1k | Res18   | 4   |  4 / 4|  70.50   |89.49    |128  |[cfg](./res18/config1_res18_lsqdplus_m4_128_4w4f.py)  |
| LSQD+  |imagnet-1k |Res18   | 4    |  3 / 3|   69.28   |88.83    |128 |[cfg](./res18/config2_res18_lsqdplus_m4_128_3w3f.py))  |
| LSQD+  |imagnet-1k |Res18   | 4    |  2 / 2|    -    |  -   |128  |-  |  
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| LSQD+  |imagnet-1k |Res50   | 4    |  4 / 4|   76.90   |93.16   |32   | [cfg](./res50/config1_res50_lsqdplus_m4_32_4w4f.py) |
| LSQD+  |imagnet-1k |Res50   | 4    |  3 / 3|   76.08   |92.85      |32  | [cfg](./res50/config2_res50_lsqdplus_m4_32_3w3f.py)  |
| LSQD+  |imagnet-1k |Res50   | 4    |  2 / 2|    -  |   -  |32  |-  | 
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| LSQD+  |imagnet-1k |MobileNet   | 4     |  4 / 4| 68.74   |88.48  |32  | [cfg](./mobilenetv2/config1_mobilenetv2_lsqdplus_m4_32_4w4f.py) |
| LSQD+  |imagnet-1k |MobileNet   | 4    |  3 / 3|   64.36   |85.65    |32  |[cfg](./mobilenetv2/config2_mobilenetv2_lsqdplus_m4_32_3w3f.py)  |
| LSQD+  |imagnet-1k |MobileNet   | 4    |  2 / 2|  -  |   -  |32  |- | 









