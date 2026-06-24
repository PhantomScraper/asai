---
title: "leaps_dev_status_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-dev-status-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-dev-status-get/"
order: 276
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dev-status-get">
<span id="id1"></span><h1>leaps_dev_status_get</h1>
<p>デバイスのステータス情報を読み取ります。</p>
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
<li><p class="sd-card-text">稼働時間: 32 ビット符号なし整数 (<em>秒単位のデバイス稼働時間</em>)</p></li>
<li><p class="sd-card-text">温度: 16 ビット符号付き整数 (<em>摂氏単位の温度</em>)</p></li>
<li><p class="sd-card-text">Battery_voltage: 16 ビット符号なし整数 (<em>ミリボルト単位のバッテリー電圧</em>)</p></li>
<li><p class="sd-card-text">Battery_state: 4 ビット (バッテリー状態 = NO_BATTERY: 0、CHARGING: 1、CHARGED: 2、DISCHARGE: 3、VBAT_LOW: 4、VBAT_EMPTY= 5)</p></li>
<li><p class="sd-card-text">Battery_level: 7 ビット符号なし整数 (<em>パーセント単位のバッテリー レベル</em>)</p></li>
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
<tr class="row-odd"><th class="head"><p>TLV 要求</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
</tr>
<tr class="row-odd"><td><p>0x25</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x25 (10 進数 37) はコマンド Leaps_dev_status_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 15%">
<col style="width: 29%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td rowspan="2"><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="3"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>稼働時間</p></td>
<td><p>温度</p></td>
<td><div class="line-block">
<div class="line">バッテリー:</div>
<div class="line">(バイト 0-1) 電圧</div>
<div class="line">(バイト 2 ) レベル</div>
<div class="line">(バイト 3) 状態</div>
<div class="line">(バイト 4 ～ 5) 予約済み</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x59</p></td>
<td><p>0x0C</p></td>
<td><p>0x2C
0x00
0x00
0x00</p></td>
<td><p>0x22
0x00</p></td>
<td><p>0x2d 0x0f 0x3e</p>
<p>0x01 0x00 0x00</p>
</td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 (64 dec) はステータス コードを意味します</p>
<p>タイプ 0x59 (10 進数 89) はデバイスのステータスを意味します</p>
</div>


           </div>
