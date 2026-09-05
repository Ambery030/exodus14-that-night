# 02 — 第一版模型契約

下表中的 `MOD` 是模型選擇，不是古代觀測；`OBS` 是外部資料提供的量級或機制先驗；`SYN` 是為了做機制實驗而宣告的幾何。

| 物理層 | 第一版設定 | 標籤 | 解讀邊界 |
|---|---:|---|---|
| 計算域 | 60 km × 20 km | `MOD-098-01` | 計算域，不是聖經路線長度 |
| 主要 crossing | 約 6.8 km（Stage 0.98）／7 km（Stage 0.99 input） | `MOD-098-02` | synthetic route，不是測繪結果 |
| 地形 | `MI_EAST_RELIEF_V1`；三條 resolved sandy backbones | `SYN-098-01` | map-informed family，不是 LBA DEM |
| nominal backbone width | 60、45、30 m | `SYN-098-02` | 假設；未被古代資料直接量出 |
| 低地 | mud／sabkha 不給 traffic capacity | `MOD-098-03` | 保守 substrate rule |
| 初始 mean relative stage | −0.20 m | `MOD-098-04` | initial sensitivity value，不是古 Ballah 測量 |
| 外海 tide amplitude | 0.15 m；range 0.30 m | `OBS-098-01` + `MOD-098-05` | 區域微潮類比轉成測試值；非古代 tide reconstruction |
| 外海 low-water clock | 02:30–06:00 phase sweep；代表約 04:30 | `MOD-098-06` | sensitivity，不是定年的天文潮 |
| 風向 | east → west | `MOD-098-07` | 依地理軸固定；不是陣風觀測 |
| peak wind | 18.5、19.0、19.5 m/s；19 m/s 作代表 | `MOD-098-08` | gale sensitivity；人畜操作性受限 |
| wind profile | 1 h ramp；17:00–22:00 peak；22:00–01:00 減到 12 m/s；tail；最後 0.5 h calm | `MOD-098-09` | text-compatible hypothetical profile，不是古代 weather record |
| mixed movement speed | 0.60 m/s | `MOD-098-10` | traffic surrogate，不是全人口平均 |
| mixed specific flow | 0.30 equivalent units/(m·s) | `MOD-098-11` | capacity surrogate，不是 census |
| peak-wind entry rule | wind < 13 m/s 才允許 mixed traffic | `MOD-098-12` | operability screen |
| water solver | depth-averaged shallow-water；wind stress、pressure gradient、friction、storage、boundary exchange、wet/dry | `MOD-098-13` | mechanism model；不是現地 calibrated solver |
| particle / bed | 第一版 Stage 0.98–1.00 沒有 finite morphodynamic sand layer | `MOD-098-14` | pursuit soil 是 reduced mobility index，不是 sediment Exner |
| chariot detachment | 600 chosen chariots | `TXT-14-07` + `MOD-099-01` | Exodus 明示 detachment 的保守下限，不是總軍力 |
| crew / horses | 2 crew、2 horses per chariot | `OBS-099-01` + `MOD-099-02` | Egyptian chariot norm／iconographic comparator |
| route vehicle width comparator | 約 1.75 m wheel-to-wheel | `OBS-099-02` | Tutankhamun archive comparator；不是 formation width |
| dynamic lateral envelope | 3.0 m central；2.5/4.0 m sensitivity | `MOD-099-03` | screening hypothesis |
| column count | 12 central；9/16 sensitivity | `MOD-099-04` | screening hypothesis |
| longitudinal pitch | 10 m central；7/14 m sensitivity | `MOD-099-05` | screening hypothesis |
| team length | 6 m | `MOD-099-06` | screening hypothesis |
| vehicle speed | 1.8 m/s central；1.5/2.2 sensitivity | `MOD-099-07` | screening hypothesis |
| entry time | 04:00 central | `MOD-099-08` | text-order-compatible model clock |
| recognition delay | 6 min central | `MOD-099-09` | operational hypothesis |
| turn success | 55% central；20/90% sensitivity | `MOD-099-10` | dominant unresolved variable |
| fatality model | disabled | `NEG-099-01` | no drowning、death、injury output |

## 單位定義

### Mixed-equivalent movement unit

`N_max` 是在 declared specific-flow、route width、movement speed、traffic horizon 下的等效流量。它不是「人數真值」，也不處理兒童、老人、牲畜、行李或實際隊形細節。

### `h|u|` screen

`h|u|` 是水深乘流速的診斷量。Stage 0.98 將 0.70 m²/s 留作 preliminary instability screen，1.32 m²/s 作外部 adult moment-instability comparator；兩者都不是死亡門檻。這一版的 return 只有 0.029–0.050 m²/s 的 local maximum range，不能從它推出沖走或溺水。

### Ground support

Stage 0.99 的 `kPa-equivalent support` 只是把 wheel／hoof demand 和會因反覆通行、復濕而下降的 surface index 比較；它不是對古代沙床做過校準的 Bekker／Wong terramechanics。

## 座標與時間護欄

第一版的報告曾發生過 wind direction 與 array axis 混讀，因此這個 repo 只接受下列語句：

- geographic x：west → east；
- true east wind：east → west；
- `model clock`：事件內部時計，不是歷史日期／經文分鐘翻譯；
- `sea-space`：模型中的 crossing water/route zone，不等於完整地中海。

Stage 0.96 原始錯向版本已撤回，見 [`docs/06_caveats_and_later_branches.md`](06_caveats_and_later_branches.md)。
