# 06 — 反證、撤回結果與分支政策

## Stage 0.96 原始版本已撤回

原始 Stage 0.96 使用了錯誤的 wind/axis 對應，還允許 gale exposure 下的固定 mixed-population motion。它只能作 error audit，不能作 east-wind result。`RESULTS_STAGE096E_CORRECTED_EAST_WIND.md` 與 `RESULTS_STAGE096_ORIENTATION_AUDIT.md` 已把這件事寫清楚。

這也是本 repo 特別把 `geographic direction`、`model axis`、`synthetic geometry` 分開標註的原因。

## Stage 0.91：後續反證分支

Stage 0.91 在另一組 paired 2-D basin-topology family 中測了：

- 1,440 組總組合；
- Opening Gate 12 組；
- Closure Severity Gate 2 組；
- 交集 0 組。

這表示 Stage 0.9 reduced-order 的稀薄成功島沒有在那一組自然式 2-D topology 中重現。它不是對所有可能 Ballah 地貌的普遍否證，但它使第一版的 43,200 必須被稱作**條件式 synthetic-family result**，不能叫 robust historical mechanism。

## 後續 B0.5/B0.8 不混入本包

後續研究把 Pelusiac 總 Q 放進 distributed lagoon storage／bypass network，讓 local corridor Q 自己分配，並進一步加入 finite local sand、two-way sediment、terrain ensemble、analogue-derived topology 等。那些研究很重要，但它們改變了 hydraulic topology／state variables，不能倒灌回第一版的 43,200 結論。

本包採用的分支規則是：

```text
first-version benchmark (this repo)
        ├── opening / timing / frozen pursuit screen
        └── later branches: B0.5 → B0.8 → network / terrain ensemble
```

## 「埃及人不是被水淹死」的精確含義

這句在本包只能有兩層含義：

1. **建模含義**：本版沒有加入 drowning／casualty model，所以它不是靠「水淹死」來產生結果。
2. **輸出含義**：大量 rows 仍有 return-to-origin、far-shore escape 或 crew egress margin，因此「所有追入者被水覆蓋」沒有在本版出現。

不能把它升格成歷史判決：「埃及人確實沒有溺死」。模型沒有資格回答那麼強的命題。

## 可供後人接力的缺口

- Stage 0.98 的 directional route graph 尚未足以完全裁決每條 backward route 的提前關閉。
- Stage 0.99 的 soil support 是 sensitivity index，不是古代砂床 calibration。
- Stage 1.00 顯示 nominal firm width 留有很大轉向空間；若要主張人員被困，必須新增獨立、可辯護的 lateral obstruction evidence。
- visibility、crowd collision、horse panic、deep-water route error 尚未有物理 agent layer。
- full text-constrained no-remnant gate 仍然是未解問題。
