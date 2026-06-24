---
title: "SYS"
lang: ja
slug: "leaps-rtls/integration-guide/shell-api/sys"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/shell-api/sys/"
order: 112
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="sys">
<h1>SYS</h1>
<hr class="docutils">
<div class="section" id="reset">
<span id="id1"></span><h2>リセット</h2>
<p>Reboot the system. The reset command immediately initiates a system reboot. Upon execution, the system will restart. The message reset ok confirms that the command has been received and executed.</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; reset</span>
<span class="go">reset ok</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>Unsaved data will be lost.</p></li>
<li><p>The system will be unavailable until the reboot completes.</p></li>
</ul>
</div>
<hr class="docutils">
</div>
<div class="section" id="frst">
<span id="id2"></span><h2>frst</h2>
<p>Performs a factory reset, restoring the system to its original default configuration.</p>
<p>The frst command initiates a factory reset of the system. All user settings, configurations, and stored data are erased, and the system is restored to its out-of-box state. The message frst ok confirms that the command has been received and executed.</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; frst</span>
<span class="go">frst ok</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>This action is irreversible. All user data and custom settings will be permanently lost.</p></li>
<li><p>The system may automatically reboot after the factory reset completes.</p></li>
<li><p>Ensure any critical data is backed up before issuing this command.</p></li>
</ul>
</div>
<hr class="docutils">
</div>
<div class="section" id="si">
<span id="id3"></span><h2>si</h2>
<p>The output provides detailed information about system status, configuration, UWB (Ultra-Wideband) parameters, connectivity, and enabled features at startup.</p>
<p>例:</p>
<ul>
<li><p><strong>Firmware &amp; System Information</strong></p>
<ul class="simple">
<li><p>Release Version: LEAPS RTLS v1.2.0-5eea93</p></li>
<li><p>Main Firmware Version: x02070001</p></li>
<li><p>Configuration Version: x01040000</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.104 INF] release: LEAPS RTLS v1.2.0-5eea93</span>
<span class="go">[085136.177 INF] sys: main main_ver=x02070001 cfg_ver=x01040000 ...</span>
</pre></div>
</div>
</li>
<li><p><strong>System Status</strong></p>
<ul class="simple">
<li><p>Battery: No battery (0 mV), no charger detected</p></li>
<li><p>Board Type: LC14_B</p></li>
<li><p>Product Type: LC14_B</p></li>
<li><p>Power Cycle Count: 0</p></li>
<li><p>Reset Count: 6</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[085136.177 INF] sys: main main_ver=x02070001 cfg_ver=x01040000 batt=empty:0mV:NoCharger board=LC14_B prod=LC14_B pwr_cnt=0 rst_cnt=6</span>
</pre></div>
</div>
</li>
<li><p><strong>UWB Radio Configuration</strong></p>
<ul class="simple">
<li><p>Channel: 5</p></li>
<li><p>PRF (Pulse Repetition Frequency): 64 MHz</p></li>
<li><p>Preamble Length: 128</p></li>
<li><p>PAC Size: 8</p></li>
<li><p>TX Code / RX Code: 9 / 9</p></li>
<li><p>Data Rate: 6.8 Mbps</p></li>
<li><p>PHR Mode: Extended</p></li>
<li><p>PHR Rate: Standard</p></li>
<li><p>SFD Type: IEEE 4a</p></li>
<li><p>SFD Timeout: 129</p></li>
<li><p>STS Mode: Off</p></li>
<li><p>STS Length: 64</p></li>
<li><p>PDOA Mode: Mode 0</p></li>
</ul>
<p>These parameters must match across all devices in the same RTLS network to ensure proper communication and ranging accuracy.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.105 INF] uwb: ch5 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0</span>
</pre></div>
</div>
</li>
<li><p><strong>UWB Device RF Settings</strong></p>
<ul class="simple">
<li><p>TX Power: x34 / xDADADADA</p></li>
<li><p>Signal Strength (STS/SHR/PHR/DATA): 24.6 dB</p></li>
<li><p>Compliance: FCC / ETSI</p></li>
<li><p>PG Count: 238</p></li>
<li><p>Temperature: 25°C</p></li>
<li><p>LNA (Low Noise Amplifier): Enabled</p></li>
<li><p>PA (Power Amplifier): Disabled</p></li>
<li><p>RF Paths: RF1 enabled, RF2 disabled</p></li>
<li><p>Crystal Trim: 32</p></li>
<li><p>TX Delay: 16431</p></li>
<li><p>RX Delay: 16431</p></li>
</ul>
<p>Regulatory compliance is required based on the deployment region. Verify which standard applies before operation.</p>
<p>Adjust TX power and RF settings if operating conditions change.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.106 INF] uwb: tx_pwr=x34/xDADADADA sts:shr:phr:data=24.6:24.6:24.6:24.6[dB] cpl=FCC/ETSI pgcnt=238 temp=25</span>
<span class="go">[000028.107 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16431 rx_delay=16431</span>
</pre></div>
</div>
</li>
<li><p><strong>UWB Network Identification</strong></p>
<ul class="simple">
<li><p>PAN ID: x1234</p></li>
<li><p>PAN ID Mask: xFFFF</p></li>
<li><p>Device Address: xDECA7561EB60D9B9</p></li>
</ul>
<p>Ensure all devices in the same network share the same PAN ID. The address must be unique for each device.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.110 INF] uwb: panid=x1234(sys_cfg=x1234) panid_mask=xFFFF addr=xDECA7561EB60D9B9</span>
</pre></div>
</div>
</li>
<li><p><strong>Operating Mode</strong></p>
<ul class="simple">
<li><p>Mode: tn (Tag Node)</p></li>
<li><p>Supported Modes: act, twr, np, le</p></li>
<li><p>uwb (0-off,1-pasv,2-act)</p>
<ul>
<li><p>off - UWB radio disabled</p></li>
<li><p>pasv - Passive mode (listen only, no transmissions)</p></li>
<li><p>act - Active mode (UWB active)</p></li>
</ul>
</li>
<li><p>mode (0-twr,1-ul-tdoa,2-dl-tdoa)</p>
<ul>
<li><p>twr - Two-Way Ranging (both ways ranging between devices)</p></li>
<li><p>ul-tdoa - Uplink Time Difference of Arrival (tags transmit, anchors receive)</p></li>
<li><p>dl-tdoa - Downlink Time Difference of Arrival (anchors transmit, tags receive)</p></li>
</ul>
</li>
<li><p>Mode of operations</p>
<ul>
<li><p>TN: Tag Node - Mobile node with moving location - It uses Anchors to measure, locate its position and depending on the mode it can exchange data at a specified update rate.</p></li>
<li><p>AN: Anchor Node  - Infrastructure node with fixed location - reference node capable of measuring location data, data offload and routing.</p></li>
<li><p>ANI: Anchor Node Initiator - Network Initiator and timekeeper.</p></li>
</ul>
</li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.126 INF] mode: tn (act,twr,np,le)</span>
</pre></div>
</div>
</li>
<li><p><strong>MAC &amp; Connectivity</strong></p>
<ul class="simple">
<li><p>UWBMAC: Connected (Profile 2 – manual)</p></li>
<li><p>Backhaul (bh): Disconnected</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.127 INF] uwbmac: connected prof=2 (auto)</span>
<span class="go">[000028.127 INF] uwbmac: bh disconnected</span>
</pre></div>
</div>
</li>
<li><p><strong>Device Configuration</strong></p>
<ul class="simple">
<li><p>Synchronization: Disabled</p></li>
<li><p>Firmware Update: Enabled</p></li>
<li><p>BLE: Enabled</p></li>
<li><p>LEDs: Enabled</p></li>
<li><p>Location Engine: Enabled</p></li>
<li><p>Low Power Mode: Disabled</p></li>
<li><p>UWB Auto-Bridge: Enabled</p></li>
<li><p>Stationary Detection: Enabled (Sensitivity: 2)</p></li>
<li><p>Mode: 0</p></li>
<li><p>Update Rate (Normal): 1</p></li>
<li><p>Update Rate (Stationary): 50</p></li>
<li><p>Device Label: IDD9B9</p></li>
</ul>
<p>Adjust update rates and stationary detection sensitivity depending on use case (e.g., asset tracking vs. real-time positioning).</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.152 INF] cfg: sync=0 fwup=1 ble=1 leds=1 le=1 lp=0 uab=1 stat_det=1 (sens=2) mode=0 upd_rate_norm=1 upd_rate_stat=50 label=IDD9B9</span>
</pre></div>
</div>
</li>
<li><p><strong>Security &amp; Encryption</strong></p>
<ul class="simple">
<li><p>Encryption: Disabled</p></li>
</ul>
<p>Ensure encryption keys are properly configured across devices to maintain secure communication.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.152 INF] enc: off</span>
</pre></div>
</div>
</li>
<li><p><strong>Bluetooth Low Energy (BLE)</strong></p>
<ul class="simple">
<li><p>BLE Address: D4:35:94:99:56:F9</p></li>
</ul>
<p>Use this address for BLE-based provisioning, diagnostics, or integration with mobile applications.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[000028.153 INF] ble: addr=D4:35:94:99:56:F9</span>
</pre></div>
</div>
</li>
</ul>
<p>Example: TN device with UWB profile 2 (auto).</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; si</span>
<span class="go">[000028.104 INF] release: LEAPS RTLS v1.2.0-5eea93</span>
<span class="go">[000028.104 INF] sys: main main_ver=x02070001 cfg_ver=x01040000 batt=empty:0mV:NoCharger board=LC14_B prod=LC14_B pwr_cnt=0 rst_cnt=2</span>
<span class="go">[000028.105 INF] uwb: ch5 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0</span>
<span class="go">[000028.106 INF] uwb: tx_pwr=x34/xDADADADA sts:shr:phr:data=24.6:24.6:24.6:24.6[dB] cpl=FCC/ETSI pgcnt=238 temp=25</span>
<span class="go">[000028.107 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16431 rx_delay=16431</span>
<span class="go">[000028.110 INF] uwb: panid=x1234(sys_cfg=x1234) panid_mask=xFFFF addr=xDECA7561EB60D9B9</span>
<span class="go">[000028.126 INF] mode: tn (act,twr,np,le)</span>
<span class="go">[000028.127 INF] uwbmac: connected prof=2 (auto)</span>
<span class="go">[000028.127 INF] uwbmac: bh disconnected</span>
<span class="go">[000028.152 INF] cfg: sync=0 fwup=1 ble=1 leds=1 le=1 lp=0 uab=1 stat_det=1 (sens=2) mode=0 upd_rate_norm=1 upd_rate_stat=50 label=IDD9B9</span>
<span class="go">[000028.152 INF] enc: off</span>
<span class="go">[000028.153 INF] ble: addr=D4:35:94:99:56:F9</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="f">
<span id="id4"></span><h2>f</h2>
<p>Show free memory on the heap. The <code class="docutils literal notranslate"><span class="pre">f</span></code> command displays the current memory usage statistics for the system heap. The output includes three values:</p>
<blockquote>
<div><ul class="simple">
<li><p>free — Amount of free (unused) memory on the heap</p></li>
<li><p>alloc — Amount of currently allocated memory</p></li>
<li><p>tot — Total heap memory available</p></li>
</ul>
</div></blockquote>
<p>All values are typically shown in bytes.</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; f</span>

<span class="go">[000014.560 INF] mem: free=3888 alloc=9184 tot=13072</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>Useful for monitoring memory usage and detecting leaks.</p></li>
<li><p>The timestamp and log level ([000014.560 INF]) may vary depending on system logging configuration.</p></li>
</ul>
</div>
<hr class="docutils">
</div>
<div class="section" id="stg">
<span id="id5"></span><h2>stg</h2>
<p>Displays system statistics. The <code class="docutils literal notranslate"><span class="pre">stg</span></code> command displays various system statistics. The following statistics are shown:</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 28%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>統計</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>稼働時間</p></td>
<td><p>再起動後のシステム時間 (秒単位)</p></td>
</tr>
<tr class="row-odd"><td><p>rtc_drift</p></td>
<td><p>UWB ネットワーク クロックに対する推定 RTC ドリフト (運用中に使用)</p></td>
</tr>
<tr class="row-even"><td><p>ble_con_ok</p></td>
<td><p>各BLE接続イベントは、このカウンタをインクリメントします。</p></td>
</tr>
<tr class="row-odd"><td><p>ble_dis_ok</p></td>
<td><p>各BLE切断イベントは、このカウンタをインクリメントします。</p></td>
</tr>
<tr class="row-even"><td><p>ble_err</p></td>
<td><p>最後の内部BLEエラーを特定する数</p></td>
</tr>
<tr class="row-odd"><td><p>api_err</p></td>
<td><p>最後の内部APIエラーを特定する数</p></td>
</tr>
<tr class="row-even"><td><p>api_err_cnt</p></td>
<td><p>API 错误计数器</p></td>
</tr>
<tr class="row-odd"><td><p>api_dl_cnt</p></td>
<td><p>API経由で受信したバックホールDownLinkパケット数（GNのみ）</p></td>
</tr>
<tr class="row-even"><td><p>uwb0_intr</p></td>
<td><p>DW1000からの割り込み回数</p></td>
</tr>
<tr class="row-odd"><td><p>uwb0_rst</p></td>
<td><p>エラーから回復するためにDW1000をリセットしようとした回数</p></td>
</tr>
<tr class="row-even"><td><p>uwb0_bpc: 1</p></td>
<td><p>帯域幅/温度補正回数</p></td>
</tr>
<tr class="row-odd"><td><p>rx_ok</p></td>
<td><p>時間通りに受信を有効にした数</p></td>
</tr>
<tr class="row-even"><td><p>rx_err</p></td>
<td><p>時間通りに受信できなかった回数</p></td>
</tr>
<tr class="row-odd"><td><p>tx_err</p></td>
<td><p>時間通りに送信できなかった数</p></td>
</tr>
<tr class="row-even"><td><p>tx_errx</p></td>
<td><p>TXバッファに関するエラー数</p></td>
</tr>
<tr class="row-odd"><td><p>bcn_tx_ok</p></td>
<td><p>ビーコン送信数</p></td>
</tr>
<tr class="row-even"><td><p>bcn_tx_err</p></td>
<td><p>ビーコン送信中のエラー数</p></td>
</tr>
<tr class="row-odd"><td><p>bcn_rx_ok</p></td>
<td><p>受信ビーコン数</p></td>
</tr>
<tr class="row-even"><td><p>alma_tx_ok</p></td>
<td><p>送信アルマナック数</p></td>
</tr>
<tr class="row-odd"><td><p>alma_tx_err</p></td>
<td><p>アルマナック送信中のエラー数</p></td>
</tr>
<tr class="row-even"><td><p>alma_rx_ok</p></td>
<td><p>受信アルマナック数</p></td>
</tr>
<tr class="row-odd"><td><p>cl_rx_ok</p></td>
<td><p>受信クラスタ結合数</p></td>
</tr>
<tr class="row-even"><td><p>cl_tx_ok</p></td>
<td><p>送信クラスタ結合数</p></td>
</tr>
<tr class="row-odd"><td><p>cl_coll</p></td>
<td><p>検出されたクラスタ衝突数</p></td>
</tr>
<tr class="row-even"><td><p>fwup_tx_ok</p></td>
<td><p>送信されたファームウェア・アップデート・フレームの数</p></td>
</tr>
<tr class="row-odd"><td><p>fwup_tx_err</p></td>
<td><p>ファームウェアアップデートフレームの送信失敗数</p></td>
</tr>
<tr class="row-even"><td><p>fwup_rx_ok</p></td>
<td><p>受信したファームウェアアップデートフレーム数</p></td>
</tr>
<tr class="row-odd"><td><p>svc_tx_ok</p></td>
<td><p>送信されたサービスフレーム数</p></td>
</tr>
<tr class="row-even"><td><p>svc_tx_err</p></td>
<td><p>サービスフレームの送信失敗数</p></td>
</tr>
<tr class="row-odd"><td><p>svc_rx_ok</p></td>
<td><p>受信サービスフレーム数</p></td>
</tr>
<tr class="row-even"><td><p>clk_sync</p></td>
<td><p>ノードの同期回数</p></td>
</tr>
<tr class="row-odd"><td><p>bh_rt</p></td>
<td><p>ルーティングテーブル切り替え時にANがルーティングしていた回数</p></td>
</tr>
<tr class="row-even"><td><p>bh_nort</p></td>
<td><p>ルーティングテーブル切り替え中にANがルーティングしなかった回数</p></td>
</tr>
<tr class="row-odd"><td><p>bh_ev</p></td>
<td><p>DWMカーネルモジュールに送信されたイベントの数</p></td>
</tr>
<tr class="row-even"><td><p>bh_buf_lost[0]</p></td>
<td><p>カーネルモジュールのために準備された失われたバッファの数</p></td>
</tr>
<tr class="row-odd"><td><p>bh_buf_lost[1]</p></td>
<td><p>カーネルモジュールのために準備された失われたバッファの数</p></td>
</tr>
<tr class="row-even"><td><p>bh_tx_err</p></td>
<td><p>バックホールフレームの送信に失敗した回数</p></td>
</tr>
<tr class="row-odd"><td><p>bh_dl_err</p></td>
<td><p>ダウンリンク・バックホール・フレームの処理中の失敗数</p></td>
</tr>
<tr class="row-even"><td><p>bh_dl_ok</p></td>
<td><p>ダウンリンク・バックホール・フレームの受信数</p></td>
</tr>
<tr class="row-odd"><td><p>bh_ul_err</p></td>
<td><p>アップリンク・バックホール・フレームの処理中の失敗数</p></td>
</tr>
<tr class="row-even"><td><p>bh_ul_ok</p></td>
<td><p>受信アップリンクバックホールフレーム数</p></td>
</tr>
<tr class="row-odd"><td><p>fwdl_tx_err</p></td>
<td><p>エッジノードへのダウンリンクデータ送信中の失敗数</p></td>
</tr>
<tr class="row-even"><td><p>fwdl_iot_ok</p></td>
<td><p>エッジノードへのダウンリンクデータ送信数</p></td>
</tr>
<tr class="row-odd"><td><p>fwul_loc_ok</p></td>
<td><p>エッジノードからのアップリンクロケーションデータ受信数</p></td>
</tr>
<tr class="row-even"><td><p>fwul_iot_ok</p></td>
<td><p>エッジノードからのアップリンクIoTデータ受信数</p></td>
</tr>
<tr class="row-odd"><td><p>ul_tx_err</p></td>
<td><p>エッジノードからのアップリンクデータ送信中の失敗数</p></td>
</tr>
<tr class="row-even"><td><p>dl_iot_ok</p></td>
<td><p>エッジノードへのダウンリンクデータ送信数</p></td>
</tr>
<tr class="row-odd"><td><p>ul_loc_ok</p></td>
<td><p>エッジノードからのアップリンクロケーションデータ受信数</p></td>
</tr>
<tr class="row-even"><td><p>ul_iot_ok</p></td>
<td><p>エッジノードからのアップリンクIoTデータ受信数</p></td>
</tr>
<tr class="row-odd"><td><p>enc_err</p></td>
<td><p>暗号化エラー数</p></td>
</tr>
<tr class="row-even"><td><p>再初期化</p></td>
<td><p>ノードの再初期化回数</p></td>
</tr>
<tr class="row-odd"><td><p>twr_ok</p></td>
<td><p>TWRサイクルの成功回数</p></td>
</tr>
<tr class="row-even"><td><p>twr_err</p></td>
<td><p>TWRサイクルの失敗回数</p></td>
</tr>
<tr class="row-odd"><td><p>res[0]
x00000000</p></td>
<td><p>予約済み</p></td>
</tr>
<tr class="row-even"><td><p>res[1]
x00000000</p></td>
<td><p>予約済み</p></td>
</tr>
<tr class="row-odd"><td><p>res[2]
x00000000</p></td>
<td><p>予約済み</p></td>
</tr>
<tr class="row-even"><td><p>res[3]
x00000000</p></td>
<td><p>予約済み</p></td>
</tr>
<tr class="row-odd"><td><p>res[4]
x00000000</p></td>
<td><p>予約済み</p></td>
</tr>
<tr class="row-even"><td><p>res[5]
x00000000</p></td>
<td><p>予約済み</p></td>
</tr>
</tbody>
</table>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; stg</span>
<span class="go">uptime: 85590</span>
<span class="go">rtc_drift: 0.000000</span>
<span class="go">ble_con_ok: 1</span>
<span class="go">ble_dis_ok: 1</span>
<span class="go">ble_err: 0</span>
<span class="go">api_err_cnt: 10</span>
<span class="go">api_dl_cnt: 0</span>
<span class="go">uwb_intr: 62669859</span>
<span class="go">rx_ok: 61479115</span>
<span class="go">rx_err: 1378</span>
<span class="go">tx_err: 633</span>
<span class="go">tx_errx: 0</span>
<span class="go">bcn_tx_ok: 854295</span>
<span class="go">bcn_tx_err: 585</span>
<span class="go">bcn_rx_ok: 5959105</span>
<span class="go">alma_tx_ok: 28494</span>
<span class="go">alma_tx_err: 1</span>
<span class="go">alma_rx_ok: 198776</span>
<span class="go">cl_rx_ok: 149</span>
<span class="go">cl_tx_ok: 6</span>
<span class="go">cl_coll: 0</span>
<span class="go">svc_tx_ok: 0</span>
<span class="go">svc_tx_err: 0</span>
<span class="go">svc_rx_ok: 0</span>
<span class="go">clk_sync: 16147</span>
<span class="go">bh_rt: 7124</span>
<span class="go">bh_nort: 0</span>
<span class="go">bh_ev: 0</span>
<span class="go">bh_buf_lost[0]: 0</span>
<span class="go">bh_buf_lost[1]: 0</span>
<span class="go">bh_tx_err: 0</span>
<span class="go">bh_dl_err: 0</span>
<span class="go">bh_dl_ok: 0</span>
<span class="go">bh_ul_err: 0</span>
<span class="go">bh_ul_ok: 0</span>
<span class="go">fw_dl_tx_err: 0</span>
<span class="go">fw_dl_iot_ok: 0</span>
<span class="go">fw_ul_iot_ok: 0</span>
<span class="go">ul_tx_err: 1</span>
<span class="go">dl_iot_ok: 23</span>
<span class="go">ul_loc_ok: 0</span>
<span class="go">ul_iot_ok: 28494</span>
<span class="go">enc_err: 0</span>
<span class="go">ani_ses_err: 0</span>
<span class="go">reinit: 3</span>
<span class="go">reinit_last: 42370</span>
<span class="go">tdoa_ok: 0</span>
<span class="go">tdoa_err: 0</span>
<span class="go">twr_ok: 279457</span>
<span class="go">twr_err: 50</span>
<span class="go">le_err: 0</span>
<span class="go">res[0]: 11 x0000000B</span>
<span class="go">res[1]: 21 x00000015</span>
<span class="go">res[2]: 0 x00000000</span>
<span class="go">res[3]: 0 x00000000</span>
<span class="go">res[4]: 1 x00000001</span>
<span class="go">res[5]: 1508 x000005E4</span>
<span class="go">tot_err: 2648</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>All statistics are read-only and updated in real time by the system.</p></li>
</ul>
</div>
<hr class="docutils">
</div>
<div class="section" id="stc">
<span id="id6"></span><h2>stc</h2>
<p>Clears system statistics. The <code class="docutils literal notranslate"><span class="pre">stc</span></code> command clears or resets all system statistics. This includes counters such as ble_con_ok and other accumulated statistical data. The response stc: ok confirms that the statistics have been successfully cleared.</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; stc</span>
<span class="go">stc: ok</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>This action resets counters to zero (or their default initial values).</p></li>
<li><p>The uptime and rtc_drift values may be unaffected depending on system implementation.</p></li>
<li><p>Useful for starting a fresh monitoring session or debugging.</p></li>
</ul>
</div>
<hr class="docutils">
</div>
<div class="section" id="rbv">
<span id="id7"></span><h2>rbv</h2>
<p>RReads the battery voltage. The <code class="docutils literal notranslate"><span class="pre">rbv</span></code> command reads and displays the current battery voltage level. The output may vary depending on the system's power source and hardware configuration.</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; rbv</span>
<span class="go">No battery</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>Useful for monitoring power status and estimating remaining battery life.</p></li>
<li><p>If the system is running on external power only, a "No battery" message may be returned.</p></li>
</ul>
</div>
<hr class="docutils">
</div>
<div class="section" id="rcs">
<span id="id8"></span><h2>rcs</h2>
<p>Reads the charger status. The <code class="docutils literal notranslate"><span class="pre">rcs</span></code> command reads and displays the current status of the battery charging system. The output depends on hardware support and configuration.</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; rcs</span>
<span class="go">No battery</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>Useful for monitoring power management and battery health.</p></li>
<li><p>The "Unsupport get charge state" message indicates that this feature is not available on the current platform.</p></li>
</ul>
</div>
<hr class="docutils">
</div>
<div class="section" id="ut">
<span id="id9"></span><h2>ut</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 75%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p>説明</p></td>
<td><p>デバイスの稼働時間を表示。</p></td>
</tr>
<tr class="row-even"><td><p>Parameters (In)</p></td>
<td><p>None</p></td>
</tr>
<tr class="row-odd"><td><p>Parameters (Out)</p></td>
<td><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">uptime</span></code>: the up-time of device</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>例</p></td>
<td><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ut</span>
<span class="go">[000003.680 INF] uptime: 00:07:49.210 0 days (469210 ms)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="sbl">
<span id="id10"></span><h2>sbl</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 75%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p>説明</p></td>
<td><p>Set the battery voltage level.</p></td>
</tr>
<tr class="row-even"><td><p>Parameters (In)</p></td>
<td><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">low</span></code>: Voltage threshold for Empty / Low battery detection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">med</span></code>: Voltage threshold for Low → Mid-transition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">high</span></code>: Voltage threshold for Mid → Full transition.</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>Parameters (Out)</p></td>
<td><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">SUCCESSED</span></code> if successful, <code class="docutils literal notranslate"><span class="pre">UNSUCCESSED</span></code> otherwise.</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>例</p></td>
<td><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; sbl 3800 3900 4200</span>
<span class="go">[INFO]: Update the battery levels: SUCCESSED</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>


           </div>
