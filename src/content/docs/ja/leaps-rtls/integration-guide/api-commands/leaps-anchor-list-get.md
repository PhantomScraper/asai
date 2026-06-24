---
title: "leaps_anchor_list_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get/"
order: 232
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-anchor-list-get">
<span id="id1"></span><h1>leaps_anchor_list_get</h1>
<p>周囲のアンカーのリストを読み取ります。アンカーに対してのみ機能します。リスト内のアンカーは、同じネットワークからのもの、または隣接ネットワークからのものでもかまいません。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">オフセット: 8ビットの符号なし整数 (<em>アンカー・リスト上のオフセット。リスト内に8つ以上のアンカーがある場合に使用。0 - オフセットなし</em>)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a>、タイムスタンプ、フラグ、カウント、[anchor_0、anchor_1、...]</p></li>
<li><p class="sd-card-text">timestamp: 32-bit unsigned integer (<em>up-time in microseconds</em>)</p></li>
<li><p class="sd-card-text">count： 1 バイト (<em>要素数。8 は、1 つの TLV 応答が搬送できるリストの最大要素数</em>)</p></li>
<li><p class="sd-card-text">アンカー_1、アンカー_2、...、アンカー_N: (<em>アンカーのリスト</em>)</p></li>
<li><p class="sd-card-text">anchor_N：node_id、position、rssi、seat、neighbor_network (<em>アンカーリスト要素、N は 0 ～ 8</em>)</p></li>
<li><p class="sd-card-text">ノード ID: 2 バイト (<em>アンカー ID</em>)</p></li>
<li><p class="sd-card-text">位置: 12バイト</p></li>
<li><p class="sd-card-text">rssi: 1 バイトの署名付き (<em>信号強度インジケーター</em>)</p></li>
<li><p class="sd-card-text">rx_rate: 1 byte unsigned (<em>packet error rate</em>)</p></li>
<li><p class="sd-card-text">座席: 5 ビット (<em>アンカーが占有する座席番号</em>)</p></li>
<li><p class="sd-card-text">neighbors_network: 1 ビット (<em>アンカーが現在のネットワークからのものであるか、近隣ネットワークからのものであるかを示すステータス フラグ</em>)</p></li>
<li><p class="sd-card-text">seens: 1 byte (<em>Number of BCN frames received from the anchor. This counter overflows at 255</em>)</p></li>
<li><p class="sd-card-text">rx_coll: 16-bit unsigned integer (<em>Number of seat collisions with this anchor</em>)</p></li>
<li><p class="sd-card-text">rx_consec: 1 byte (<em>Number of consecutive BCN frames received from the anchor</em>)</p></li>
<li><p class="sd-card-text">dist: 32-bit unsigned integer (<em>Distance from the anchor in millimeters</em>)</p></li>
<li><p class="sd-card-text">drift_avg: float (4 bytes) (<em>Average clock drift w.r.t the anchor</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 52%">
<col style="width: 48%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
</tr>
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x0B はコマンド Leaps_anchor_list_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 26%">
<col style="width: 41%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 3%">
<col style="width: 4%">
<col style="width: 9%">
<col style="width: 5%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 13%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 4%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="16"><p>TLV 応答（前テーブルのフレームの残り）</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="14"><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x56</p></td>
<td rowspan="3"><p>0xE1</p></td>
<td rowspan="2"><p>uint32 - タイムスタンプ (リトルエンディアン)</p></td>
<td rowspan="2"><p>uint8 - フラッグ</p></td>
<td rowspan="2"><p>uint8 - リスト内でエンコードされた要素の数</p></td>
<td colspan="10"><p>アンカー1番</p></td>
<td><p>アンカー番号。 2 ...番号8</p></td>
</tr>
<tr class="row-even"><td><p>uint16 - リトルエンディアンのUWBアドレス</p></td>
<td><p>3 x int32 - リトルエンディアンでの位置座標 x、y、z</p></td>
<td><p>int8 -
RSSI</p></td>
<td><p>uint8 -
rx_rate</p></td>
<td><div class="line-block">
<div class="line">uint8 - フラッグ</div>
</div>
<div class="line-block">
<div class="line">(ビット 0-4) 座席番号</div>
<div class="line">(ビット 5) 近隣ネットワーク</div>
<div class="line">(ビット 6-7) 予約</div>
</div>
</td>
<td><p>uint8 - 数値</p></td>
<td><p>uint16 -
rx_coll</p></td>
<td><p>uint8 -
rx_consec</p></td>
<td><p>uint8 - dist</p></td>
<td><p>float -
drift_avg</p></td>
<td><p>...</p></td>
</tr>
<tr class="row-odd"><td><p>0xe8
0x03
0x00
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x08</p></td>
<td colspan="10"><p>0xab 0xbc ...</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ0x56はアンカーリストを意味する</p>
</div>


           </div>
