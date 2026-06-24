---
title: "leaps_mac_addr_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set/"
order: 256
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-set">
<span id="id1"></span><h1>leaps_mac_addr_set</h1>
<p>BLE、UWB、Ethernet、または Wi-Fi インターフェースの MAC アドレスを設定します。有効にするにはリセットが必要です。内部の不揮発性メモリに書き込むため、頻繁に使用しないでください。デフォルトの MAC アドレスを使用するには、工場出荷時設定にリセットする必要があります (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a>)。UWB MAC アドレスの下位 2 バイトは、0x0000 または 0xFFFF と等しくてはいけません。 BLE アドレスは、ランダム BLE アドレスまたはパブリック BLE アドレスのいずれかになります。イーサネット アドレスと Wi-Fi アドレスは EUI-48 形式に準拠する必要があり、U/I ビットはそれに応じて設定する必要があります。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">type_0、type_1、type_2、type_3: 8 ビット符号なし整数 (<em>リスト内の MAC アドレス番号 0、1、2、3 を表すタイプ</em>)</p></li>
<li><p class="sd-card-text">mac_addr_0、mac_addr_1、mac_addr_2、mac_addr_3: 48 ビット値 (<em>リトル エンディアンの MAC アドレス番号 0、1、2、3</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
出力</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p>SPI/UART の例</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 24%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><div class="line-block">
<div class="line">値</div>
<div class="line">リトルエンディアンのノードID</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>0x2D</p></td>
<td><p>0x07</p></td>
<td><p>0x00 0xEF
0xCD 0xAB
0x56 0x34
0x12</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x2D (45 dec) はコマンド <a class="reference internal" href="#leaps-mac-addr-set"><span class="std std-ref">leaps_mac_addr_set</span></a> を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 は、直前のコマンドの err_code を意味する</p>
</div>


           </div>
