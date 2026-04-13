# PRG-Mamba: Periodic Relational Graph-Mamba with OctaAug

> **Trustworthy Contactless Heart Rate Estimation Across Diverse Skin Tones, Viewpoints, and Frame Rates**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Authors:** Akoramurthy B¹, Surendiran B¹, Xiaochun Cheng²

¹ NIT Puducherry, India | ² Swansea University, UK

---

## Results (7 Datasets)

| Dataset | MAE ↓ | RMSE ↓ | r ↑ |
|---------|--------|--------|-----|
| PURE | **0.58** | 0.78 | 1.0000 |
| UBFC-rPPG | **0.19** | 0.26 | 1.0000 |
| MMPD | **4.38** | 8.02 | 0.7401 |
| VIPL-HR | **6.41** | 8.68 | 0.7120 |
| iBVP | **0.37** | 0.50 | 0.9998 |
| SCAMPS | **2.71** | 3.66 | 0.8730 |
| OBF | **0.24** | 0.32 | 1.0000 |

All improvements p<0.01 (Wilcoxon signed-rank).

---

## Quick Start

```bash
git clone https://github.com/akortheanchor/PRG-Mamba.git
cd PRG-Mamba
conda create -n prgmamba python=3.9 && conda activate prgmamba
pip install torch==2.0.0 torchvision==0.15.0 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
pip install -e .

# Train
python scripts/train.py --config configs/mmpd.yaml

# Evaluate
python scripts/evaluate.py --config configs/mmpd.yaml --checkpoint results/checkpoints/mmpd_best.pth
```

## Citation

```bibtex
@article{akoramurthy2026prgmamba,
  title   = {{PRG-Mamba}: Periodic Relational Graph-Mamba with {OctaAug}},
  author  = {Akoramurthy, B and Surendiran, B and Cheng, Xiaochun},
  journal = {Computers \& Electrical Engineering},
  year    = {2026}
}
```
