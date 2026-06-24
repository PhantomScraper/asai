---
title: "leaps_dist_alarm_cfg_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-get/"
order: 252
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dist-alarm-cfg-get">
<span id="id1"></span><h1>leaps_dist_alarm_cfg_get</h1>
<p>距離アラーム検出の設定を読み取ります。</p>
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
<ul class="simple">
<li><p class="sd-card-text">Threshold_1: 32 ビットの符号なし整数 (<em>距離のしきい値 (ミリメートル単位)</em>)</p></li>
<li><p class="sd-card-text">Threshold_2: 32 ビットの符号なし整数 (<em>ミリメートル単位の距離のしきい値</em>)</p></li>
<li><p class="sd-card-text">ミンコン: 8 ビット符号なし整数 (<em>更新レートの倍数の閾値ヒステリシス</em>)</p></li>
<li><p class="sd-card-text">minnoconn: 8 ビット符号なし整数 (<em>更新レートの倍数の閾値ヒステリシス</em>)</p></li>
<li><p class="sd-card-text">オプション: 8 ビット符号なし整数 (<em>アラーム表示オプション、0 - LED (個別)、1 - LED (連続)、2 - ブザー (連続)、3 - モーター (連続)</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
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
<tr class="row-odd"><td><p>0x31</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x31 (49 dec) はコマンド Leaps_serial_cfg_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 7%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 7%">
<col style="width: 8%">
<col style="width: 13%">
<col style="width: 10%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td rowspan="2"><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="6"><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">距離</div>
<div class="line">しきい値 nr.1</div>
<div class="line">（毫米）</div>
</div>
</td>
<td><div class="line-block">
<div class="line">距離</div>
<div class="line">(ミリメートル)</div>
<div class="line">（毫米）</div>
</div>
</td>
<td><p>mincon</p></td>
<td><p>minnocon</p></td>
<td><div class="line-block">
<div class="line">オプション ビット (3 ～ 7) 予約済み</div>
<div class="line">ビット (0 ～ 2) アラーム表示オプション</div>
</div>
</td>
<td><p>予約済み (8バイト)</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x52</p></td>
<td><p>0x13</p></td>
<td><p>0xDC
0x05
0x00
0x00</p></td>
<td><p>0xC4
0x09
0x00
0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
<td><p>0x01</p></td>
<td><p>0x00 0x00
0x00 0x00
0x00 0x00
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x52 (82) は距離アラーム設定を意味します</p>
</div>


           </div>
