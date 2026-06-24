---
title: "leaps_panid_profile_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-panid-profile-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-panid-profile-set/"
order: 263
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-panid-profile-set">
<span id="id1"></span><h1>leaps_panid_profile_set</h1>
<p>アンカーの選択を支援するために、UWB ネットワーク識別子 (PANID) と ZONE ID を設定します。また、PANID が異なる複数の異なるネットワーク間でのタグ ローミングをサポートするために役立つ PANID マスクも設定します。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul>
<li><p class="sd-card-text">panid： 16ビットの符号なし整数（<em>UWBのpanid</em>）。</p></li>
<li><p class="sd-card-text">panid_mask： 16ビット符号なし整数 (<em>UWBパニッドマスク</em>)</p></li>
<li><p class="sd-card-text">zone_id: 8ビット符号なし整数（<em>ANのUWBゾーンID</em>）</p></li>
<li><p class="sd-card-text">flag: 8-bit unsigned integer optional flag</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">bit 0: skip writing values to the environment (1: skip writing, 0: write to the environment)</p></li>
</ul>
</div></blockquote>
</li>
<li><p class="sd-card-text">reserved: 8-bit unsigned integer (<em>reserved for future use</em>)</p></li>
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
<p><strong>例 1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 12%">
<col style="width: 25%">
<col style="width: 14%">
<col style="width: 11%">
<col style="width: 19%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="5"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>panid</p></td>
<td><p>パニードマスク</p></td>
<td><p>zone_id</p></td>
<td><p>flag</p></td>
<td><p>reserved</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x06</p></td>
<td><p>0xCD
0xAB</p></td>
<td><p>0xFF
0xFF</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x40 と入力すると、コマンド leaps_panid_profile_set を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV response</p></th>
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
