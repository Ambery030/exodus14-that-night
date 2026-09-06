# 00 — 思想實驗與判讀協定

## 這個 repo 在問什麼

本包保存的是一個**條件式物理平行世界**：在一組受到區域地貌、風、潮與潟湖水動力啟發的設定下，夜間是否可能形成局部可通行路徑；若把埃及追兵放進同一個已凍結的水世界，車隊的機動與撤退會出現什麼結果。

它不試圖從現代資料倒推出唯一的晚青銅時代 Ballah，也不把模型輸出當成經文的歷史證明。它保存的是一個可以被後人替換、重跑、反駁的實驗沙盒。

## 反事實實驗的問題

第一版依序問四件事：

1. 一個地圖啟發、但仍明示為 synthetic 的 sandy-lagoon 世界，能否在夜間風—潮—storage forcing 下產生 travelling opening？
2. 路徑是否會在風衰與邊界水位變化後逐段復濕、關閉？
3. 在不修改已跑出的水世界之下，600 輛明示選出的戰車進入後，濕砂與重複通行能否造成機動失效與撤退判斷？
4. 幾何撤退界線是否仍留下大量車輛或人員的回岸餘裕？

每一問都可以得到「支持、收窄、失敗或尚未測試」。模型不必替文本每一個敘事結果都找到自然機制。

## 實驗階梯

    固定文本次序與第一版世界
            ↓
    Stage 0.98：風—潮—淺水 storage 與 opening/rewetting
            ↓ 凍結水世界
    Stage 0.99：戰車、濕砂、排隊、部分撤退
            ↓ 移除手設轉向比例
    Stage 1.00：車輛轉向界線與人員棄車退岸界線
            ↓
    保留成功與失敗，另開後續 B0.5/B0.8/network 分支

每一階段都應說清楚：哪些輸入被鎖住、新增了哪一層、哪些結果可以沿用、哪些結果必須重新測。

## 四種材料不要混成一種證據

| 層級 | 內容 | 在本包的角色 |
|---|---|---|
| TXT | Exodus 14:19–28 的先後與文字門檻 | 約束事件順序，不提供現代分鐘或數值地形 |
| OBS | 潮差、風力、車輛尺度、土壤力學等外部資料 | 提供量級或機制方向 |
| MOD | stage、水位、風場、速度、流量、延遲、轉向率 | 為了做可重現實驗而宣告的模型參數 |
| SYN | 60/45/30 m backbones、路線、平台與人工地形 | 可測的 synthetic realization，不是古代測量 |
| RUN | CSV、時間序列與 solver 直接輸出 | 本包真正跑出的結果 |
| HYP | 擁擠、視線、誤入深水、馬匹推擠等解讀 | 可作後續假說，不能倒寫成已測機制 |
| NEG | 控制組、未通過 gate、未實作的死亡模型 | 用來阻止過度解讀 |

完整來源與限制見 sources.md；逐項 evidence tag 見 04_evidence_ledger.md。

## 數字不是目標函數

第一版的 43,200 是在 120×96 與 160×128 細網格中重現的 mixed-equivalent movement capacity；54,000 是較粗網格 comparison benchmark。兩者都不是事前要逼出的歷史人口答案。

同樣地：

- 600 是 Exodus 14:7 明示的 chosen-chariot detachment screen，不是埃及全軍人口；
- 19 m/s 是模型中的 severe-wind sensitivity，不是古代當晚的觀測紀錄；
- 0.15 m 是區域微潮類比轉成的測試幅度，不是古 Ballah 的實測潮差；
- 04:00、04:15、05:30、05:40、06:40 是 model clock 或 frozen input clock，不是把 morning watch 直接翻成現代鐘點。

如果更細的世界自然跑出 17,000、43,000 或 60,000，三者都應先照收，再問差異來自地形、水動力、通行規則或數值解析度。不得先把 43,200 當成成功區間。

## 判讀規則

### survives

新增一層物理後，原本的宏觀現象仍存在，且沒有靠事後調參保住。

### narrows

現象仍可出現，但只在較窄的 topology、phase、wind、substrate 或 operational family 中成立。

### dies

新增一層後，原本的現象在預先宣告的 gate 下消失；這是對舊簡化的反證。

### unresolved

模型沒有足夠 state variables、資料或守恆帳回答。此時應保留問題，不用敘事補洞。

## 第一版最後能說到哪裡

這一包保留了以下條件式結果：

- synthetic first-version world 可以產生夜間 travelling opening；
- 風衰與水位重新分配後，路徑會逐段復濕、關閉；
- frozen-hydro pursuit screen 中，部分濕砂 sensitivity 會讓戰車失去機動並出現撤退與部分回岸；
- Stage 1.00 顯示車輛與人員仍有相當撤退餘裕；
- 碰撞、馬匹推擠、視線混亂、誤入深水與死亡沒有被完整模擬；
- Exodus 14:28 的 no-remnant 結果沒有在這個世界中被物理解釋。

因此，「埃及人不是被水淹死」在本包只能理解為：**模型沒有用溺水或死亡機制產生結果，且輸出仍保留部分回岸與人員退岸餘裕。**它不能被翻成歷史斷言。

## 分支政策

後續 B0.5、B0.8、distributed lagoon、finite sediment、terrain ensemble 與 agent world 可以重新使用問題、tag、帳務格式與部分物理規則；一旦它們改變 hydraulic topology、state variables 或通行介面，就必須另開分支，不能覆寫第一版 benchmark。

第一版的價值正在於它同時留下：

opening survives → pursuit ordering partly survives → retreat/fatality gate fails。

後人可以從這條鏈看出，哪一層被保留、哪一層被新物理淘汰。
