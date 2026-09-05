# 03 — Stage 0.98–1.00 結果

## Stage 0.98：開路、儲水與清晨復濕

### 代表 case

條件：19.0 m/s east-to-west wind、0.15 m tide amplitude、external low water 04:30、wind calm 04:30、`MI_EAST_RELIEF_V1`。

| 網格 | 首條 route | route depth minimum | +2 cm local rewet | 全測試路段關閉 | safe mixed-equivalent by 05:30 |
|---:|---:|---:|---:|---:|---:|
| 80×64 | 00:50 | 05:10 | 05:50 | 06:00 | 54,000 |
| 120×96 | 01:00 | 05:10 | 05:40 | 06:40 | **43,200** |
| 160×128 | 01:00 | 05:10 | 06:10 | 06:50 | **43,200** |

證據：`RUN-098-A`；原始 CSV 在 [`data/stage098/`](../data/stage098/)。

### Stage 0.98 的 wind robustness

在 120×96、low water 04:30、calm 04:30：

| peak wind | 首條 route | +2 cm rewet | 全段關閉 | safe completion |
|---:|---:|---:|---:|---:|
| 18.5 m/s | 01:00 | 05:40 | 06:20 | 43,200 |
| 19.0 m/s | 01:00 | 05:40 | 06:40 | 43,200 |
| 19.5 m/s | 00:50 | 05:40 | 06:50 | 43,200 |

證據：`RUN-098-B`。

### 水動力診斷

| 量 | 結果 | 標籤 |
|---|---:|---|
| maximum pre-calm west-minus-east free-surface difference | 約 0.87 m | `RUN-098-C` |
| difference at calm | 約 0.62 m | `RUN-098-C` |
| west-zone storage gain at calm | 約 39 million m³ | `RUN-098-C` |
| west-zone volume lost 04:30–06:30 | 約 13 million m³ | `RUN-098-C` |
| post-calm route p95 speed | 0.106–0.141 m/s | `RUN-098-D` |
| local maximum `h|u|` | 0.029–0.050 m²/s | `RUN-098-D` |
| maximum median-route depth rise | 0.083–0.093 cm/min | `RUN-098-D` |

這組結果支持的是**漸進復濕／撤退警告**，不是急性水力掀翻或溺水。

## Stage 0.99：frozen-hydro pursuit screen

所有 row 都從 600 entrants 開始。`returned_to_origin` 是模型中回到出發岸的車輛數；`trapped_at_hydro_closure` 是在 archived closure clock 仍困在路網內的車輛數；兩者不是死亡數。

### 中央隊形與兩個主要 soil family

| soil / traffic | 到遠岸 | 回原岸 | 實際 immobilized | 06:40 仍困 | 首次失效 | conflict exposures |
|---|---:|---:|---:|---:|---|---:|
| marginal wet sand / central dense | 87 | **328** | 10 | 185 | 04:09:15 @ 1.0 km | 0 |
| patchy sand over soft / central dense | 8 | **327** | 18 | 265 | 04:09:15 @ 1.0 km | 0 |
| marginal wet sand / high turnability | 45 | 538 | 3 | 17 | 04:09:15 @ 1.0 km | 0 |
| marginal wet sand / low turnability | 48 | 120 | 12 | 432 | 04:09:15 @ 1.0 km | 0 |
| patchy / compressed disorder | 3 | 179 | 11 | 418 | 04:26:05 @ 1.0 km | 2 |

關鍵：firm-sand control 讓 600/600 到遠岸，因此「濕砂失效」是這一版 order mechanism 的必要 sensitivity；但低 turnability／compressed disorder 也只代表 declared hypothetical formation，不是古代隊形的測量。

### Stage 0.99 判讀

- `TXT-14-23` 順序：埃及人進入 sea-space，在 model 中成立。
- `RUN-099-A`：traffic-induced mobility failure 可早於 05:40 return cue 發生。
- `RUN-099-B`：大量 queue／partial return 可出現。
- `NEG-099-A`：firm sand control 讓所有車抵岸。
- `NEG-099-B`：沒有一個 row 同時滿足「無遠岸逃逸」與「無原岸逃逸」。
- `NEG-099-C`：central cases 的 collision conflict exposures 為 0；compressed cases 只有 2，不能變成大規模踩踏死亡證明。

## Stage 1.00：幾何撤退與 crew abandonment bounds

Stage 1.00 拿掉手設的 20/55/90% turn fraction，改用 swept-width、turn pockets、usable firm width 的幾何 bounds。

### 車輛

在 60/45/30 m nominal backbones、12 columns（5+4+3）、3 m dynamic envelope 下，formation 只佔 declared aggregate firm width 的約 27%。因此只要把 nominal width 都視為可用，vehicle entrapment 不穩健；必須再證明大部分寬度對轉向不可用，才能關閉退路。這是 `NEG-100-A`。

### 人員退岸距離

Stage 0.99 first failure 約在起點 1 km。若 04:15 認識撤退：

| 步行速度 | 05:40 前可走 | 06:40 前可走 |
|---:|---:|---:|
| 0.5 m/s | 2.55 km | 4.35 km |
| 0.8 m/s | 4.08 km | 6.96 km |
| 1.0 m/s | 5.10 km | 8.70 km |
| 1.3 m/s | 6.63 km | 11.31 km |

即使等到 05:40 才離車，0.5 m/s 仍可在 06:40 前走 1.80 km；因此最早失效點有大幅人員逃生餘裕。這支持「尾段有人能退回岸上」，也直接阻止我們把「車困住」翻成「人全死了」。

## 第一版的硬結論

| 問題 | 判定 |
|---|---|
| 夜間風—潮機制能否產生 travelling opening？ | 條件式可以 |
| 43,200 是否在兩個細網格重現？ | 是 |
| 路徑是否整個湖盆乾涸？ | 否；深水與側向水界保留 |
| 埃及人是否可在文本次序下進入？ | 條件式可以 |
| 濕砂／反覆交通能否造成機動失效？ | sensitivity family 中可以 |
| 戰馬碰撞／推擠是否已證明致命？ | 否 |
| 是否模擬溺水或傷亡？ | 否 |
| 是否達到 Exodus 14:28 的 no-remnant？ | 否 |

