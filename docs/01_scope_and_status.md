# 01 — 範圍與狀態

## 封存名稱

**Exodus–Ballah First-Version Physical Sandbox — Stage 0.98–1.00**

這個版本不是「最終歷史答案」，而是第一個把以下三件事放在同一條可追溯鏈上的封存世界：

1. 區域風—潮—淺水 storage 讓局部 sandy routes 在夜間形成；
2. 路網在風衰後於清晨逐段復濕；
3. 埃及追兵以一個明示的 600 輛戰車 detachment 做 frozen-hydro pursuit screen。

## 可以說的話

### `RUN-098`: 開路與容量

在 `MI_EAST_RELIEF_V1` synthetic geometry、19 m/s peak easterly、0.15 m tide amplitude、特定 phase 下，120×96 與 160×128 都得到 43,200 mixed-equivalent safe units by 05:30。這是有限條件下的數值結果，且細網格兩次相同，因此可保留成第一版 benchmark。

### `RUN-098`: 時序

代表 case 的 first route 約 01:00，route depth minimum 約 05:10，+2 cm local rewet 約 05:40–06:10，所有測試路段約 06:40–06:50 關閉。這提供「夜間開、清晨復濕／失效」的 model-clock sequence。

### `RUN-099/100`: 追兵次序與部分撤退

600 輛戰車可以在 04:00 進入 sea-space。marginal／patchy wet-sand sensitivity 可在約 04:09 發生第一個 mobility failure，約 04:15 認識撤退；多個 rows 有數百輛回到 origin。這是「進入 → 機動困難 → 撤退判斷 → 部分回岸」的條件式次序結果。

## 不能說的話

- 不能把 43,200 寫成古代人口數；它是 `person-equivalent movement capacity`。
- 不能把 54,000 寫成更可信的 final answer；它是粗網格 benchmark。
- 不能把 19 m/s 寫成普通人畜可舒適操作的天氣。
- 不能說模型證明埃及人溺水、死亡、被馬踩死或「無一遺留」。
- 不能把「戰馬推擠／視線混亂／誤入深水」寫成程式直接計算出的因果。
- 不能把 synthetic 60/45/30 m backbones 寫成已測得的 LBA 沙脊寬度。
- 不能把此 package 當作 B0.5/B0.8 distributed-lagoon world 的結果。

## 假說與結果的分層

| 層 | 內容 | 狀態 |
|---|---|---|
| 物理輸出 | wind setdown、route opening、stored head、progressive rewetting | `RUN-098` |
| 操作性輸出 | mixed-equivalent capacity、route closure、alarm proxy | `RUN-098`，依 synthetic mobility rule |
| 追兵輸出 | wheel/hoof mobility degradation、queue、return ledger | `RUN-099/100` |
| 敘事相容 | 先進入、後晨更擾動、先撤退決策、後大回水 | `TXT + RUN`，條件式 |
| 機制解讀 | crowded horses、視線不良、錯入深水、部分人退岸 | `HYP`；目前只部分由 output 提示 |
| 完整結局 | Exodus 14:28 no-remnant / mass fatality | `NEG`；未通過 |

## 為什麼仍值得封存

因為它不是把所有事情都宣稱成功，而是把成功與失敗切開：

`opening survives`
→ `timed return survives as a warning/closure process`
→ `chariot mobility can degrade`
→ `partial retreat remains`
→ `fatality/no-remnant is not explained`。

後續研究者可以在不重新猜整個世界的情況下，替換 stage、地形、風、砂或 crowd model，並清楚知道改動跨過哪一道證據邊界。
