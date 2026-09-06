# 外部來源與證據邊界

本文件把第一版散落在各份報告裡的來源集中起來。來源只回答它被指定的問題；任何外部資料都不能直接把 synthetic geometry、model clock 或 solver output 變成古代實測。

原始封存包沒有保存所有網頁的首次查閱日期。下列網址是報告內的 source anchors；後續正式引用時，應再補 access date、版本／頁碼與必要的存檔副本。

## 文本來源

| ID | 來源 | 用途 | 不支撐的內容 |
|---|---|---|---|
| SRC-TXT-01 | [Exodus 14:19–28, Mechon-Mamre](https://www.mechon-mamre.org/p/pt/pt0214.htm) | 核對埃及人進入、晨更擾動、車輪困難、回水與 no-remnant 的順序與範圍 | 不提供現代分鐘、潮相、風速或地形高程 |
| SRC-TXT-02 | Sefaria／BDB lexical anchors，見 Stage 0.98 report | 文字與詞義交叉閱讀 | 不把 morning watch 轉成唯一現代鐘點 |

## 區域水動力、潮汐與風

| ID | 來源 | 本包使用方式 | 邊界 |
|---|---|---|---|
| SRC-HYDRO-01 | [El-Geziry, Egyptian Mediterranean tide-gauge study](https://www.athensjournals.gr/mediterranean/2020-6-2-3-El-Geziry.pdf) | Port Said 區域潮差與季節水位的類比背景 | 不重建古 Ballah 天文潮 |
| SRC-HYDRO-02 | [Elshinnawy et al. 2021, Bardawil regional micro-tide analogue](https://doi.org/10.3390/su13137392) | 支持 0.15 m 級微潮測試幅度的區域類比 | 不證明古 Ballah 具有同一潮幅 |
| SRC-HYDRO-03 | [Drews & Han, wind-setdown mechanism/control model](https://doi.org/10.1371/journal.pone.0012481) | 風致水面傾斜、儲水與 setdown 的機制方向 | 不校準本包的 synthetic geometry 或 exact wind |
| SRC-HYDRO-04 | [Tulloch, historical report of the 1882 Lake Menzaleh easterly setdown](https://biblicalstudies.org.uk/articles_jtvi-02.php) | 歷史類比：東風可造成湖區水面重新分配 | 不等於本事件的古代直接觀測 |
| SRC-HYDRO-05 | [FAO, lagoon hydraulic controls](https://www.fao.org/4/t0369E/T0369E02.htm) | 潟湖、海口、風潮與交換的概念背景 | 不提供 Ballah 的局部參數 |
| SRC-WIND-01 | [U.S. National Weather Service Beaufort scale](https://www.weather.gov/mfl/beaufort) | 說明 19 m/s 屬於嚴重風力，提醒人畜操作性風險 | 不提供古代營地可操作門檻 |
| SRC-WIND-02 | [Jordan et al. 2008, human gust-response experiment](https://doi.org/10.1016/j.buildenv.2007.08.004) | 人類受風反應的方向性參考 | 不校準古代混合人畜速度 |
| SRC-HYDRO-06 | [Jonkman & Penning-Rowsell 2008, hydraulic-instability comparator](https://doi.org/10.1111/j.1752-1688.2008.00217.x) | h|u| 的外部成人穩定性比較尺度 | 不構成死亡或溺水門檻 |

### 0.15 m 潮幅的轉換規則

本包採用 0.15 m amplitude、0.30 m total range 作為 regional micro-tide analogue 的測試值。它是 OBS → MOD 的轉換：外部資料提供量級背景，模型選定一個可重現的 sensitivity value。這個值不應寫成「古 Ballah 實測潮差」。

## 車輛與土壤力學來源

| ID | 來源 | 本包使用方式 | 邊界 |
|---|---|---|---|
| SRC-VEH-01 | [Griffith Institute Tutankhamun Archive](https://www.griffith.ox.ac.uk/gri/4tutchar.html) | 車體／底盤寬度與兩馬輕型戰車的尺度、型式參考 | 不提供安全隊形寬度、轉彎半徑或濕砂速度 |
| SRC-VEH-02 | [Brown experimental reconstruction record](https://webhelper.brown.edu/joukowsky/courses/fightingpharaohs10/9985.html) | 車輛可操控性與重建尺度的質性參考 | 不校準本包的 turn fraction 或 turn time |
| SRC-VEH-03 | [NOVA Egyptian chariot reconstruction](https://www.pbs.org/video/nova-building-pharaohs-chariot-pro/) | 緊轉與機動性的質性參考 | 不提供古代戰場隊形數值 |
| SRC-VEH-04 | [National AgrAbility horse-drawn vehicle guidance](https://www.agrability.org/wp-content/uploads/2015/11/ps25.pdf) | 現代馬車轉向與操作空間的方向性參考 | 不校準埃及戰車或 Ballah 沙地 |
| SRC-SOIL-01 | [USACE EM 1110-2-5027, Appendix I](https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM_1110-2-5027.pdf) | 濕沉積物、地面承載與設備陷入的機制方向 | 不提供古代木輪、馬蹄或本地砂的數值校準 |
| SRC-SOIL-02 | [NASA, Mechanics of Wheel–Soil Interaction](https://ntrs.nasa.gov/api/citations/19730021941/downloads/19730021941.pdf) | sinkage、剪切與滑移的輪土力學背景 | 不把 reduced kPa-equivalent index 變成完整 Bekker/Wong 校準 |

## Ballah 地貌來源狀態

RESULTS_STAGE096_MAP_INFORMED_LOCK.md 使用了「1911 Ballah map audit」作為宏觀方向先驗：東側 contour-bounded sandy relief、較低較濕的湖側，以及 segmented/braided morphology 的允許性。

目前第一版 repo **沒有附上 1911 圖幅掃描、穩定 catalog URL、圖版頁碼或 georeferenced raster**。因此這個來源目前只能支撐：

- eastern sandy relief 是 map-informed broad prior；
- lower/wetter ground 與 segmented morphology 在宏觀尺度上未被排除；
- 精確 ridge count、寬度、高程、saddle、inlet 與 LBA connectivity 仍屬 SYN。

它不能支撐「古代有三條 60/45/30 m 沙脊」。正式研究版應另補一筆 SRC-GEO-01，附上圖幅名稱、收藏機構、掃描／catalog URL、圖版頁碼與座標處理方式。這裡先保留缺口，避免用未核驗網址假裝完成 provenance。

## 模型內部來源

| 類型 | 位置 | 角色 |
|---|---|---|
| RUN-098 | [data/stage098/](../data/stage098/) 與 [Stage 0.98 report](../reports/STAGE098_WIND_TIDE_RELEASE_CHECKPOINT.md) | Stage 0.98 的時間序列、capacity 與水動力輸出 |
| RUN-099 | [data/stage099/](../data/stage099/) 與 [Stage 0.99 report](../reports/RESULTS_STAGE099_CHARIOT_SOIL_PURSUIT.md) | frozen-hydro 戰車／濕砂 screen |
| RUN-100 | [data/stage100/](../data/stage100/) 與 [Stage 1.00 report](../reports/RESULTS_STAGE100_RETREAT_GEOMETRY.md) | 幾何轉向與人員退岸 bounds |
| MOD/SYN | [docs/02_model_contract.md](02_model_contract.md) | 模型參數與 synthetic geometry 的正式宣告 |
| ARCH | [provenance/source_manifest.json](../provenance/source_manifest.json) 與 [provenance/checksums.sha256](../provenance/checksums.sha256) | 封存檔案、hash 與來源角色 |

## 來源的使用原則

1. 外部資料先約束量級、方向或機制；它們不自動變成古 Ballah 的 exact parameter。
2. 模型參數若沒有直接外部量測，必須標成 MOD 或 SYN。
3. solver 輸出只能由本地 CSV、報告與 hash 支撐，不能用外部類比替代。
4. 解讀假說必須保留 HYP，尤其是馬匹推擠、視線混亂、誤入深水與死亡因果。
5. 後續 B0.5/B0.8/network 分支的來源與參數不可倒灌回這個第一版。
