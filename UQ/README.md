### Uniform Quantization Introduction
 
Uniform quantization partitions the whole space in a uniform manner, and vice versa for the nonuniform quantization. 

**Citation**
**Experiments**

| method | dataset | backbone | node_num |W/A bit| Top-1(%)  | Top-5(%) | BS | CFG|LOG |
|--------|---------|----------|----------|-------|-----------|----------|----|----|----|
| UQ  |imagnet-1k | Res18   | 4   |  4 / 4|   70.48     |  89.69（146）    |64  |[cfg](./res18/config3_res18_lsq_m2_64_4w4f.py)  | 
| UQ  |imagnet-1k |Res18   | 4    |  3 / 3|   69.62     |  89.15（150）    |64 |[cfg](./res18/config2_res18_lsq_m2_64_3w3f.py)  | 
| UQ  |imagnet-1k |Res18   | 4    |  2 / 2|   65.80     |  86.70（120）    |64  |[cfg](./res18/config1_res18_lsq_m2_64_2w2f.py)  |
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| UQ  |imagnet-1k |Res50   | 4    |  4 / 4|   76.13   |   92.75 （116）   |64  |[cfg](.res50/config3_res50_uq_m4_32_4w4f.py)  |  
| UQ  |imagnet-1k |Res50   | 4    |  3 / 3|   75.31   | 92.29  （110）  |64  |[cfg](./res50/config2_res50_uq_m4_32_3w3f.py)  |      ||
| UQ  |imagnet-1k |Res50   | 4    |  2 / 2|    71.84  | 90.58  （112）   |64  |[cfg](./res50/config1_res50_uq_m4_32_2w2f.py)  |    ||
|----|--------|-----------|----------|-------|-------------|----------|---|------------|
| UQ  |imagnet-1k |MobileNet   | 4     |  4 / 4|  67.07     |  87.54 （120）   |64  |[cfg](./mobilenetv2/config3_mobilenetv2_uq_m4_32_4w4f.py)  |
| UQ  |imagnet-1k |MobileNet   | 4    |  3 / 3|  N/A  |  N/A   |64  |[cfg]](./mobilenetv2/config2_mobilenetv2_uq_m4_32_3w3f.py)  |
| UQ  |imagnet-1k |MobileNet   | 4    |  2 / 2|  -  |   -  |64  |[cfg]](./mobilenetv2/config1_mobilenetv2_uq_m4_32_2w2f.py)  | 
