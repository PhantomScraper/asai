---
title: "LC13とLC14の仕様"
lang: ja
slug: "udk/specification/lc13-lc14-specification"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/specification/lc13-lc14-specification/"
order: 54
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc13-and-lc14-specifications">
<h1>LC13とLC14の仕様</h1>
<hr class="docutils">
<div class="section" id="overview">
<h2>概要</h2>
<p>このセクションでは、LC13 および LC14 デバイスの技術的な詳細を説明します。LC13/LC14 デバイスは、アンカーノード (AN)、アンカーイニシエータノード (ANI)、タグノード (TN)、およびリアルタイムロケーションシステム (RTLS) のゲートウェイを作成するために使用できます。また、FiRa Nearby Interactionおよび双方向到達角（TWR-AoA）デモにも対応しています。さらに、このオープン・プラットフォームはUWBまたはBluetoothアプリケーションの開発にも使用できます。</p>
</div>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>Murata 2AB SIP (MCU nRF52840、Bluetooth、UWB QM33120W IC、LIS2DW 加速度センサ、水晶振動子、内蔵電源レギュレータ) に基づいています。</p></li>
<li><p>Qorvo QM33120W - ウルトラワイドバンド(UWB)：</p>
<ul>
<li><p>IEEE802.15.4z標準に基づき、強化されたセキュリティ機能を実装しています。</p></li>
<li><p>チャンネル 5 (6.5 GHz) とチャンネル 9 (8 GHz) の両方をサポートし、FCC、日本の ARIB、ETSI、および CE の +10dB ETSI と互換性のある UWB RF コンプライアンスを備えています。</p></li>
<li><p>ローノイズアンプ（LNA）とパワーアンプ（PA）を内蔵し、UWB範囲を拡大（最大150m）。</p></li>
<li><p>非 AoA (LC14) と AoA アンテナ (LC13) が統合されています。</p></li>
<li><p>FiRa™ PHY および MAC 互換。Apple U1 チップおよび Android FiRa 互換スマートデバイスと相互運用可能です。</p></li>
<li><p>DW1000 IEEE802.15.4a UWB IC のチャンネル 5 との下位互換性。</p></li>
</ul>
</li>
<li><p>双方向測距（TWR）に対応、 到着時間差（TDoA）および到着位相差（PDoA）をサポート。</p></li>
<li><p>Nordic Semiconductor nRF52840 - アンテナ内蔵Bluetooth® Low-Energy (BLE) 5.3 RFテクノロジ。</p></li>
<li><p>NFC タグアンテナコネクタをサポートします。</p></li>
<li><p>2つのUSB Cポートは、データ通信用の仮想COMおよびUSBデバイスインターフェースを備えたDAPLinkプログラマを統合します。</p></li>
<li><p>あるいは、J-Link はオンボードの6ピン Tag Connect 互換コネクタを経由して使用することもできます。</p></li>
<li><p>RGB LED、2x <span class="green-text">GREEN</span> LED、フロントボタン、2つのサイドボタン、nRF52 USBデバイス用USBコネクタ、ブザー、ハプティックモーター、外部センサーやIOと接続するための追加GPIOを搭載しています。</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>詳細は <a class="reference external" href="https://www.murata.com/en-global/products/connectivitymodule/ultra-wide-band/qorvo">Murata 2AB module</a> と <a class="reference external" href="https://www.qorvo.com/products/wireless-connectivity/ultra-wideband">Qorvo DW3000 IC</a> のページを参照してください。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="software-compatibility">
<h2>ソフトウェアの互換性</h2>
<p>LEAPS UWBS、Qorvo FiRa互換UWBS（Nearby Interaction、TWR AoA）、PANS PRO UWBS、サードパーティ製スタック（オープンプラットフォーム）と互換性があります。デフォルトのファームウェアはLEAPS UWBSで、Qorvo FiRa互換のデモが製品から提供されています。</p>
</div>
<hr class="docutils">
<div class="section" id="electrical-parameters">
<h2>電気パラメータ</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>パラメータ</p></th>
<th class="head"><p>値</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>バッテリー電源</p></td>
<td><p>+3.7V (バッテリーはキットに含まれていません。Fenix RCR123A をお勧めします)</p></td>
</tr>
<tr class="row-odd"><td><p>USB C (電源とデータ)</p></td>
<td><p>5V @ 500mA最大</p></td>
</tr>
<tr class="row-even"><td><p>動作温度 (なし)バッテリー）</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-odd"><td><p>動作温度 (バッテリーあり)</p></td>
<td><p>-20°C - +45°C</p></td>
</tr>
<tr class="row-even"><td><p>UWB がサポートするチャンネル</p></td>
<td><div class="line-block">
<div class="line">チャンネル 5 (6240-6739.2 MHz, CF=6489.6 MHz)</div>
<div class="line">チャンネル 9 (7738-8237.2 MHz, CF=7987.2 MHz, FiRa 互換)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>UWB 送信電力</p></td>
<td><div class="line-block">
<div class="line">FCC/ARIB/ETSI: -41.3 dBm/MHz max</div>
<div class="line">ETSI (+10 dB)：-31.3 dBm/MHz max</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>ターゲット精度</p></td>
<td><div class="line-block">
<div class="line">測距精度： ±9 [cm]</div>
<div class="line">PDoA精度： ± 5 [deg]</div>
<div class="line">AoA 精度： ±2.5 [deg]</div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>最低消費電力を達成するには、SWD_DIOジャンパをカットしてください。スリープ電流は3.7Vで約24uAになります。カットしない場合、スリープ電流は約370uA @ 3.7Vになります。</p></li>
<li><p>外部Jlinkを使用できるようにするには、SWD_DIOジャンパをカットしてください。</p></li>
<li><p>他のジャンパはそのままで大丈夫です。</p></li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="mechanical-parameters">
<h2>機械的パラメータ</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>パラメータ</p></th>
<th class="head"><p>値</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>サイズ</p></td>
<td><p>W=72 x H=120 x D=30 mm</p></td>
</tr>
<tr class="row-odd"><td><p>重量</p></td>
<td><div class="line-block">
<div class="line">バッテリーなし: 82g</div>
<div class="line">バッテリーあり: 101g</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>色</p></td>
<td><p>LC13 - グレー, LC14 - ホワイト</p></td>
</tr>
<tr class="row-odd"><td><p>マウント中</p></td>
<td><p>1/4"-20 スクリューカメラマウントに対応</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>デバイスの概要</h2>
<p>以下の写真は、LC13 と LC14 デバイスの主なコンポーネントの概要です。</p>
<p><strong>LC14 デバイスの前面図/背面図です</strong></p>
<p><a class="reference internal" href="../../../_images/for-buttons.png"><img alt="pic3" src="/docs-assets/ja/_images/for-buttons.png" style="width: 47%;"></a> <a class="reference internal" href="../../../_images/for-usb-type-c.png"><img alt="pic4" src="/docs-assets/ja/_images/for-usb-type-c.png" style="width: 44%;"></a></p>
<hr class="docutils">
<p><strong>LC13デバイスの前面/背面図です</strong></p>
<a class="reference internal image-reference" href="../../../_images/lc13_device.png"><img alt="../../../_images/lc13_device.png" class="align-center" src="/docs-assets/ja/_images/lc13_device.png" style="width: 477.90000000000003px; height: 389.7px;"></a>
<hr class="docutils">
<p><strong>ボードの上面図</strong></p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/lc14_b2-top-view.png"><img alt="pic1" src="/docs-assets/ja/_images/lc14_b2-top-view.png" style="width: 100%;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/lc13_b2-top-view.png"><img alt="pic2" src="/docs-assets/ja/_images/lc13_b2-top-view.png" style="width: 93%;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>安全上の注意事項</h2>
<ul class="simple">
<li><p>動作中はデバイスを水や湿気にさらさないでください。</p></li>
<li><p>デバイスを熱源にさらさないでください。</p></li>
<li><p>製品の機械的または電気的損傷を避けるため、取り扱いには十分注意してください。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="warnings">
<h2>警告</h2>
<ul class="simple">
<li><p>このデバイスはDC5V/0.5Aの外部電源または3.7Vのバッテリーのみに接続してください。</p></li>
<li><p>誤ったタイプのバッテリーと交換すると、セーフガードを破る可能性があります (例えば、一部のリチウムバッテリーの場合)。</p></li>
<li><p>バッテリーを火や高温のオーブンに廃棄したり、機械的にバッテリーを押しつぶしたり切断したりすると、爆発を引き起こす可能性があります。</p></li>
<li><p>周囲が極端に高温の環境にバッテリーを放置すると、爆発したり、可燃性の液体やガスが漏れたりする可能性があります。</p></li>
<li><p>バッテリーの気圧が極端に低いと、爆発したり、可燃性の液体やガスが漏れたりする可能性があります。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="important-notice">
<h2>重要なお知らせ</h2>
<ul class="simple">
<li><p>キットのハードウェアとソフトウェアはデモンストレーションのみを目的としています。産業グレードのシステムを入手するには、特定のニーズや要件についてご相談ください。</p></li>
<li><p>Qorvo の FiRa 互換スタック、Qorvo Nearby Interaction、UWB Ranging &amp; AoA Demo Application など、Qorvo ソフトウェアツールの詳細情報については、<a class="reference external" href="https://www.qorvo.com">Qorvo website</a> から入手可能な適切なドキュメントやリソースを参照してください。</p></li>
</ul>
<hr class="docutils">
</div>
</div>


           </div>
