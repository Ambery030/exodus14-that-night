# 04 — Evidence ledger：每個數字與概念的來源

閱讀規則：

- `source` 是它從哪裡來；
- `status` 是它在模型中的證據層級；
- `can_say` 是可以怎麼說；
- `cannot_say` 是不能偷換成什麼。

| ID | 數字／概念 | source | status | can_say | cannot_say |
|---|---|---|---|---|---|
| `TXT-14-07` | 600 chosen chariots | Exodus 14:7 | `TXT` | 600 可作明示 detachment 的 conservative screen | 不能說埃及總軍只有 600 |
| `TXT-14-23` | Egyptians enter after Israelites | Exodus 14:23 | `TXT` | entry must precede morning-watch disturbance | 不能把 entry 延後到日出才開始 |
| `TXT-14-24` | morning-watch disturbance | Exodus 14:24 | `TXT` | disturbance follows entry | 不能把 05:30 當字典唯一分鐘 |
| `TXT-14-25` | wheels／driving trouble、retreat decision | Exodus 14:25 | `TXT` | mobility trouble precedes major return | 不能指定唯一物理死因 |
| `TXT-14-28` | covered/no-remnant scope | Exodus 14:28 | `TXT` | 是完整事件的高門檻 | 本 package 沒有達到它 |
| `OBS-098-01` | 0.15 m tide amplitude | Elshinnawy et al. Bardawil regional micro-tide analogue；見 `docs/sources.md` | `OBS→MOD` | 支持 microtidal test scale | 不是 ancient Ballah tide measurement |
| `OBS-098-02` | 17.2–20.7 m/s Beaufort severe band | U.S. NWS Beaufort | `OBS` | 提醒 19 m/s 不是舒適人畜風 | 不能把 19 m/s 當普通營地天氣 |
| `MOD-098-04` | mean relative stage −0.20 m | Stage 0.98 contract | `MOD` | 是 bounded initial stage sensitivity | 不是古 Ballah 春季實測水位 |
| `MOD-098-08` | 18.5/19.0/19.5 m/s peak | Stage 0.98 contract | `MOD` | 可測 wind robustness | 不是古代氣象紀錄 |
| `SYN-098-02` | 60/45/30 m backbones | Stage 0.98 geometry | `SYN` | synthetic traffic widths | 不是古代沙脊測量 |
| `MOD-098-10` | 0.60 m/s mixed movement | Stage 0.98 mobility contract | `MOD` | 可把 capacity 轉成等效流量 | 不是所有人畜平均速度 |
| `MOD-098-11` | 0.30 units/(m·s) | Stage 0.98 mobility contract | `MOD` | 可產生 reproducible capacity | 不是人口密度觀測 |
| `RUN-098-A` | 54,000 at 80×64；43,200 at 120×96/160×128 | `data/stage098/screen_summary_*.csv` | `RUN` | 43,200 是第一版 fine-grid benchmark | 不能把 54,000 當 converged final |
| `RUN-098-B` | first route 01:00；minimum 05:10 | Stage 0.98 selected CSV/report | `RUN` | night opening and route minimum | 不是古代鐘表時間 |
| `RUN-098-C` | 0.87 m max head；0.62 m at calm | Stage 0.98 summary | `RUN` | wind stores a large internal head | 不是海水像牆一樣瞬間打回 |
| `RUN-098-D` | p95 speed 0.106–0.141 m/s | Stage 0.98 phase screen | `RUN` | gradual warning/return cue | 不是 acute hydraulic knockdown |
| `RUN-098-E` | local max `h|u|` 0.029–0.050 m²/s | Stage 0.98 phase screen | `RUN` | return is hydraulically mild in this screen | 不是 drowning or death threshold |
| `RUN-098-F` | depth rise 0.083–0.093 cm/min | Stage 0.98 phase screen | `RUN` | route closes progressively | 不是 sudden bore |
| `OBS-099-01` | ~1.75 m wheel-to-wheel comparator | Griffith Institute Tutankhamun Archive | `OBS` | vehicle scale comparator | 不是 safe formation width |
| `OBS-099-02` | 2-horse light chariot qualitative norm | Griffith / Brown reconstruction | `OBS→MOD` | motivates 2 horses and maneuverable vehicle | 不能校準 wet-sand turn time |
| `MOD-099-01` | 600 entrants | Stage 0.99 contract | `MOD` + `TXT` | explicit lower-bound pursuit screen | 不是 whole army |
| `MOD-099-03` | 3.0 m dynamic envelope | Stage 0.99 manifest | `MOD` | sensitivity hypothesis | 不是 ancient measured convoy width |
| `MOD-099-04` | 12 columns | Stage 0.99 manifest | `MOD` | declared formation screen | 不是 Egyptian battle order |
| `MOD-099-05` | 10 m pitch | Stage 0.99 manifest | `MOD` | queue-spacing screen | 不是 historical spacing |
| `MOD-099-07` | 1.8 m/s outbound speed | Stage 0.99 manifest | `MOD` | central traffic case | 不是 field-calibrated chariot speed |
| `MOD-099-08` | 04:00 entry | Stage 0.99 manifest | `MOD` | text-order-compatible clock | 不是 date-stamped ancient time |
| `MOD-099-09` | 6 min recognition delay | Stage 0.99 manifest | `MOD` | operational sensitivity | not source-observed |
| `MOD-099-10` | 55% turn success | Stage 0.99 manifest | `MOD` | central screening fraction | uncalibrated; dominant uncertainty |
| `RUN-099-A` | marginal/central: 87 far shore, 328 origin, 10 immobilized, 185 trapped | `data/stage099/chariot_soil_screen.csv` | `RUN` | partial return + mobility degradation | not deaths |
| `RUN-099-B` | patchy/central: 8 far shore, 327 origin, 18 immobilized, 265 trapped | same | `RUN` | same mechanism under softer patches | not no-remnant |
| `RUN-099-C` | compressed rows: 2 conflict exposures | same | `RUN` | queue interaction exists | not mass trampling proof |
| `NEG-099-A` | firm sand: 600/600 far shore | Stage 0.99 control | `NEG` | failure requires surface degradation | no universal Egyptian trap |
| `MOD-100-01` | first failure at 1 km | Stage 0.99/1.00 frozen input | `MOD/RUN` | geometry bound used for retreat | not measured ancient location |
| `RUN-100-A` | at 0.5 m/s, 2.55 km before rewet and 4.35 km before closure | Stage 1.00 output | `RUN` | early dismounted crew can retreat in model | not every person will choose or succeed |
| `RUN-100-B` | at 0.5 m/s after 05:40, 1.80 km before 06:40 | Stage 1.00 output | `RUN` | even late abandonment has escape margin | not proof of historical survival |
| `HYP-099-01` | horse crowding / visual confusion / deep-water misentry | interpretive layer | `HYP` | plausible candidates for future model | not computed or validated here |
| `NEG-099/100` | casualty model disabled | Stage 0.99/1.00 source code and manifests | `NEG` | package is non-fatality screen | cannot say nobody died historically |
| `NEG-091` | 0/1,440 paired opening+closure cases | Stage 0.91 | `NEG` | later 2-D family challenged the mechanism | not universal disproof of every Ballah-like terrain |

## 最容易被誤讀的三個數字

1. **43,200**：是 movement capacity，不是「出埃及人口真值」。
2. **600**：是 chosen chariots screen，不是 Pharaoh 全軍。
3. **0.70 m²/s**：是 preliminary instability screen，不是死亡線；本版 return output 遠低於它。
