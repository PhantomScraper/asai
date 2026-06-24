---
title: "leaps_panid_profile_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-panid-profile-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-panid-profile-get/"
order: 264
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-panid-profile-get">
<span id="id1"></span><h1>leaps_panid_profile_get</h1>
<p>アンカー選択を支援するために、ZONE IDとともにUWBネットワーク識別子（PANID）を取得する。PANIDマスクと実際のPANIDは、さまざまなPANIDを持つ複数の異なるネットワーク間でのタグローミングをサポートするのに役立ちます。</p>
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
<li><p class="sd-card-text">panid： 16ビットの符号なし整数（<em>UWBのpanid</em>）。</p></li>
<li><p class="sd-card-text">panid_mask： 16ビット符号なし整数 (<em>UWBパニッドマスク</em>)</p></li>
<li><p class="sd-card-text">actual_panid: 16ビット符号なし整数（<em>TNのUWB実panid</em>）</p></li>
<li><p class="sd-card-text">zone_id: 8ビット符号なし整数（<em>ANのUWBゾーンID</em>）</p></li>
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
<tr class="row-odd"><td><p>0x41</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x41 と入力すると、コマンド leaps_panid_profile_get を意味します</p>
<p>デバイスがANの場合、<cite>actual_panid</cite> は <cite>panid</cite> と同じになります。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 9%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 15%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="4"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>ステータスコード</p></td>
<td><p>panid</p></td>
<td><p>パニードマスク</p></td>
<td><p>actual
panid</p></td>
<td><p>zone id</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0xC2</p></td>
<td><p>0x06</p></td>
<td><p>0xCD
0xAB</p></td>
<td><p>0xFF
0xFF</p></td>
<td><p>0xCD
0xAB</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0xC2 は PANID プロファイルを意味する。</p>
</div>


           </div>
