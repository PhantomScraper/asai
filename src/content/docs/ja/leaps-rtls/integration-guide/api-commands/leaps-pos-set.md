---
title: "leaps_pos_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-pos-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-pos-set/"
order: 226
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-pos-set">
<span id="id1"></span><h1>leaps_pos_set</h1>
<p>ノードのデフォルト位置を設定します。タグ モードではデフォルト位置は使用されませんが、いずれにせよ保存されるため、モジュールをアンカー モードに設定して、leaps_pos_set によって以前に設定された値を使用できます。この呼び出しは、新しい値が設定される場合、内部フラッシュに書き込みを行うため、頻繁に使用すべきではなく、最悪の場合、数百ミリ秒かかることがあります。</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">x: 32 ビット整数 (ミリメートル単位の位置座標)</p></li>
<li><p class="sd-card-text">y: 32 ビット整数 (位置座標ミリメートル)</p></li>
<li><p class="sd-card-text">z: 32 ビット整数 (ミリメートル単位の位置座標)</p></li>
<li><p class="sd-card-text">pqf: 8 ビット整数 (位置品質係数)</p></li>
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
<p><strong>例 1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 18%">
<col style="width: 21%">
<col style="width: 20%">
<col style="width: 16%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV リクエスト</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="4"><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">リトルエンディアン,</div>
<div class="line">x です</div>
<div class="line">座標</div>
<div class="line">ミリメートル</div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">リトルエンディアン,</div>
<div class="line">y です</div>
<div class="line">座標</div>
<div class="line">ミリメートル</div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">リトルエンディアン,</div>
<div class="line">z です</div>
<div class="line">座標</div>
<div class="line">ミリメートル</div>
</div>
</td>
<td><div class="line-block">
<div class="line">uint8_t -</div>
<div class="line">品質は良いです</div>
<div class="line">要素に含める</div>
<div class="line">パーセント</div>
<div class="line">(0-100)</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x01</p></td>
<td><p>0x0D</p></td>
<td colspan="4"><p>0x4b 0x0a
0x00 0x00
0x1f 0x04
0x00 0x00
0x9c 0x0e
0x00 0x00
0x64</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x01 はコマンド leaps_pos_set を意味します</p>
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
