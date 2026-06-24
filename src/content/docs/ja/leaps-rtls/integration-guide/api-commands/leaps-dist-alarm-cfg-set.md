---
title: "leaps_dist_alarm_cfg_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-set/"
order: 251
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dist-alarm-cfg-set">
<span id="id1"></span><h1>leaps_dist_alarm_cfg_set</h1>
<p>距離アラーム検出の設定を変更します。内蔵フラッシュに書き込みます。頻繁に使用しないでください。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
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
<p><strong>例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 10%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 10%">
<col style="width: 9%">
<col style="width: 16%">
<col style="width: 18%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLVT 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="6"><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">距離のしきい値</div>
<div class="line">nr.1 (ミリメートル)</div>
</div>
</td>
<td><div class="line-block">
<div class="line">距離のしきい値</div>
<div class="line">nr.2 (ミリメートル)</div>
</div>
</td>
<td><p>mincon</p></td>
<td><p>minnocon</p></td>
<td><div class="line-block">
<div class="line">オプション ビット (3 ～ 7) - 予約済み</div>
<div class="line">ビット (0-2) - アラーム表示オプション</div>
</div>
</td>
<td><p>予約済み (8バイト)</p></td>
</tr>
<tr class="row-even"><td><p>0x33</p></td>
<td><p>0x13</p></td>
<td><p>0xDC 0x05
0x00 0x00</p></td>
<td><p>0xC4 0x09
0x00 0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
<td><p>0x01</p></td>
<td><p>0x00 0x00 0x00 0x00
0x00 0x00 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x33 (51 dec) はコマンド leaps_dist_alarm_cfg_set を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
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
<p>タイプ 0x40 はステータスコード</p>
</div>


           </div>
