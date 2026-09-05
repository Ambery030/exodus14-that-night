# Exodus–Ballah：第一版物理平行世界

這是一個**封存的第一版研究包**，整理 Stage 0.98–1.00 的結果：先在固定的、地圖啟發但仍是 synthetic 的 Ballah-like 世界中，測試風、潮、水面儲存、路徑開關，再把一個明示的埃及戰車分隊放進同一個 frozen water world。

這不是 Late Bronze Age Ballah 的重建，也不是對經文歷史性的證明。它保存的是一個可重跑、可檢查、能被後人繼續修正的平行世界。

## 這一版最後留下什麼

### 1. 以色列側的通行上限

在 Stage 0.98 的代表案例（19 m/s、低水約 04:30、風於 04:30 平靜）中：

- 80×64 粗網格：54,000 個 **mixed-equivalent movement units**；
- 120×96：43,200；
- 160×128：43,200。

所以這個「五萬以內」版本的正式封存基準是 **43,200 units**，不是 54,000。54,000 是較粗網格的 comparison upper benchmark。這個數字不是人口普查，也不是「六十萬人」的證明；它是固定模型、固定速度與單位通量假設下的安全通行容量。

### 2. 時間順序

代表模型時鐘約為：

`17:00–22:00 東風峰值`
→ `22:00–01:00 風減弱`
→ `約 01:00 首條 travelling route 出現`
→ `04:00 埃及戰車進入 sea-space`
→ `04:09 左右先出現移動失效`
→ `約 04:15 認識到應撤退`
→ `05:30 morning-watch diagnostic`
→ `05:40 初始復濕 cue`
→ `06:40 左右所有測試路段關閉`。

它保留了經文要求的最低順序：埃及人先進入，之後才是晨更擾動；移動／駕駛困難與撤退判斷先於大規模回水。現代時鐘是模型時鐘，不是把 `morning watch` 硬翻成一個歷史分鐘。

### 3. 埃及側不是「水淹死」模型

Stage 0.99–1.00 **沒有模擬死亡、溺水或傷亡**。它只測：600 個明示選出的戰車是否能進入、濕砂是否在反覆通過後降低輪／馬蹄機動性、隊伍是否形成排隊、撤退時有多少仍能回到出發岸。

在 central dense、marginal wet sand 案例中，600 輛中：

- 87 到達遠岸；
- 328 回到原岸；
- 10 輛實際失去機動性；
- 185 輛在水動力關閉時仍受困。

這是一個**次序相容、但完整「無一遺留」失敗**的結果。它支持「追兵可能在水中失去機動、隊伍失序、部分人／車退回岸上」；它不支持把馬匹推擠、視線混亂或誤入深水區寫成已被模型證明的死因。

因此本包把你的敘事拆成三層：

| 敘事 | 本包狀態 |
|---|---|
| 夜間開路、清晨逐段復濕、路網關閉 | **RUN：模型輸出** |
| 埃及人先進入，之後發生機動困難與撤退判斷 | **RUN：條件式次序相容** |
| 尾段有人／車退回出發岸 | **RUN：在多個 sensitivity rows 中直接出現** |
| 戰馬推擠／碰撞 | **HYP：只有低頻 conflict exposure，未證明致命** |
| 視線迷茫、誤入較深水區 | **HYP：目前沒有 visibility／route-choice 物理層** |
| 埃及人被水淹死、全軍無遺留 | **未證明；Stage 1.00 明確判 fail** |

## 證據標籤

所有數字與概念都應配合下列標籤閱讀：

- `TXT`：經文次序或文字約束。
- `OBS`：外部觀測、歷史紀錄或現代類比；只約束量級／機制方向。
- `MOD`：模型輸入、參數、synthetic geometry 或操作性假設。
- `RUN`：程式直接產生的輸出。
- `HYP`：解讀假說，不能冒充輸出。
- `NEG`：未通過、未模擬或不能推出的命題。
- `ARCH`：封存檔案、hash 或來源追蹤資訊。

完整 ledger 在 [`docs/04_evidence_ledger.md`](docs/04_evidence_ledger.md)。

## 研究邊界

這個 repo **刻意不包含**後來的 B0.5 distributed-lagoon network、B0.8 analogue-derived topology、G2 sediment continuity 或人流 agent world。那些是另一條模型階梯；如果混進來，第一版就不再是第一版。

同樣，Stage 0.91 的 paired 2-D screen 曾得到 `Opening ∩ Closure = 0/1,440`。它不是本包的成功輸出，而是後續重要的反證分支；詳見 [`docs/06_caveats_and_later_branches.md`](docs/06_caveats_and_later_branches.md)。

## 目錄

- [`docs/01_scope_and_status.md`](docs/01_scope_and_status.md)：這一版到底聲稱什麼、不能聲稱什麼。
- [`docs/02_model_contract.md`](docs/02_model_contract.md)：所有固定物理設定與單位。
- [`docs/03_results_stage098_100.md`](docs/03_results_stage098_100.md)：Stage 0.98、0.99、1.00 的結果表。
- [`docs/04_evidence_ledger.md`](docs/04_evidence_ledger.md)：逐數字、逐概念的來源與證據層級。
- [`docs/05_text_sequence.md`](docs/05_text_sequence.md)：經文次序與模型時鐘的對照。
- [`docs/06_caveats_and_later_branches.md`](docs/06_caveats_and_later_branches.md)：撤回結果、後續反證與分支政策。
- [`docs/sources.md`](docs/sources.md)：外部參照與其可／不可支撐的內容。
- [`provenance/source_manifest.json`](provenance/source_manifest.json)：原始報告、程式與輸出的封存對應。

程式在 [`src/`](src/)；原始報告在 [`reports/`](reports/)；精選 CSV/JSON 在 [`data/`](data/)。

## 重跑

```bash
python -m pip install -r requirements.txt

# Stage 0.98：重新產生一個選定網格的水動力／通行 screen
python src/stage098_wind_tide_release.py \
  --outdir outputs_reproduced_stage098_120 \
  --nx 120 --ny 96 \
  --selected phase_w19.0_low04.5_stop04.0 \
  --wind-filter 19.0

# Stage 0.99：讀取封存的 Stage 0.98 input，不改寫水動力
python src/stage099_chariot_soil_pursuit.py \
  --outdir outputs_reproduced_stage099

# Stage 1.00：讀取 Stage 0.99 結果，產生 retreat bounds
python src/stage100_retreat_geometry.py

# 最小測試
PYTHONPATH=src python -m pytest -q tests
```

Stage 0.99／1.00 的 input hash 與 package 內資料一致性，見 [`provenance/checksums.sha256`](provenance/checksums.sha256)。

## 一句話版本

> 在一個以東風、微潮、風致水面傾斜與 synthetic sandy backbones 組成的條件式世界裡，約 43,200 個混合移動單位可以在清晨前完成安全通行；同一個 frozen world 能讓追入的戰車在濕砂上失去機動並形成撤退，但目前只得到部分回岸與失序，沒有得到「全軍被水覆蓋」的結果。

這正是第一版值得留下來的地方：它把「開路可能」與「完整追兵毀滅」分開了。
