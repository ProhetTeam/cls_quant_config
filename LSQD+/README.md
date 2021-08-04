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
| LSQD+  | imagnet-1k |  Res18  | 4  |  8 / 8|           |          |64  |[cfg] |
| LSQD+  |imagnet-1k | Res18   | 4   |  4 / 4|  70.50   |89.49    |64  |[cfg](./config4_res18_lsqdplus_int4_updatelr4x_weightloss_4m.py)  |
| LSQD+  |imagnet-1k |Res18   | 4    |  3 / 3|   69.28   |88.83    |64 |[cfg](./config6_res18_lsqdplus_int3_allchangenoweightloss_coslr_4m.py)  |
| LSQD+  |imagnet-1k |Res18   | 4    |  2 / 2|        |     |64  |[cfg]  |  
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| LSQD+  |imagnet-1k |Res50   | 4   |  8 / 8|       |   |64   | [cfg]  |
| LSQD+  |imagnet-1k |Res50   | 4    |  4 / 4|   76.90   |93.16   |64   | [cfg](./config9_res50_lsqdplus_int4_addoffset_lr4x__4m.py.py) |
| LSQD+  |imagnet-1k |Res50   | 4    |  3 / 3|   76.08   |92.85      |64  | [cfg](./config10_res50_lsqdplus_int3_addoffset_coslr4x__4m.py)  |
| LSQD+  |imagnet-1k |Res50   | 4    |  2 / 2|      |     |64  |[cfg]  | 
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| LSQD+  |imagnet-1k |MobileNet   | 4     |  8 / 8|       |    |32  |[cfg]  |
| LSQD+  |imagnet-1k |MobileNet   | 4     |  4 / 4| 68.74   |88.48  |32  | [cfg](./config12_mobilenetv2_lsqdplus_int4_addoffset_lr4x_4m.py) |
| LSQD+  |imagnet-1k |MobileNet   | 4    |  3 / 3|   64.36   |85.65    |32  |[cfg](./config13_mobilenetv2_lsqdplus_int3_addoffset_lr4x_4m.py)  |
| LSQD+  |imagnet-1k |MobileNet   | 4    |  2 / 2|    |     |32  |[cfg]  | 









