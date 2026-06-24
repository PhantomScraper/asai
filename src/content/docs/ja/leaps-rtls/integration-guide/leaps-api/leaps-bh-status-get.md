---
title: "leaps_bh_status_get"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/leaps-bh-status-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-status-get/"
order: 290
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-bh-status-get">
<span id="id1"></span><h1>leaps_bh_status_get</h1>
<p>現在の UWBMAC バックホール ステータスを取得します。ノードはゲートウェイまたはアンカーとして設定されている必要があります。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">(<em>なし</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
出力</div>
<ul>
<li><p class="sd-card-text">sf_number: 16 ビット整数 (<em>現在のスーパーフレーム番号</em>)</p></li>
<li><p class="sd-card-text">bh_seat_map: 32 ビット整数 (<em>現在のスーパーフレームの座席マップ</em>)</p></li>
<li><p class="sd-card-text">Origin_cnt: 8 ビット整数 (<em>原点カウント0 から 8</em>)</p></li>
<li><p class="sd-card-text">origin_list: (node_id_0, bh_seat_0, hop_lvl_0), (node_id_1, bh_seat_1, hop_lvl_1), ...</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">node_id: 16 ビット整数 (<em>発信元の UWB アドレス</em>)</p></li>
<li><p class="sd-card-text">bh_seat: 8 ビット整数 (<em>原点が占めるシート、範囲は 0 ～ 8</em>)</p></li>
<li><p class="sd-card-text">hop_lvl: 8 ビット整数 (<em>ホップ レベル</em>)</p></li>
</ul>
</div></blockquote>
</li>
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
<tr class="row-odd"><td><p>0x3A</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x3A はコマンド Leaps_bh_status_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 12%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td rowspan="2"><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(2バイト) sf_number</div>
<div class="line">(4バイト) bh_seat_map</div>
<div class="line">(1バイト) origin_cnt</div>
<div class="line">(N*4 バイト)origin_list</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5D</p></td>
<td><p>0x13</p></td>
<td><p>0x6c 0x00
0x07 0x00
0x00 0x00
0x03
0xf3 0x11
0x00 0x01
0xc3 0x11
0x01 0x01
0x66 0x11
0x02 0x01</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x5D は UWBMAC バックホール ステータスを意味します</p>
</div>


           </div>
