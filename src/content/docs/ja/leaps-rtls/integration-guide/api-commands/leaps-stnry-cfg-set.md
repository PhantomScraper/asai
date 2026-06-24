---
title: "leaps_stnry_cfg_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-stnry-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-stnry-cfg-set/"
order: 267
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-stnry-cfg-set">
<span id="id1"></span><h1>leaps_stnry_cfg_set</h1>
<p>タグ ノードによって実行される静止検出の設定を書き込みます。静止検出が無効になっている場合でも設定を書き込むことができます (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set#leaps-cfg-tag-set"><span class="std std-ref">leaps_cfg_tag_set</span></a> を参照)。内部不揮発性メモリに書き込むため、慎重に使用する必要があります。静止モードが有効な場合、新しい感度設定はすぐに有効になります。デフォルトの感度は``高``です。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<p class="sd-card-text">感度: '0' | ‘1’ | ‘2’</p>
<ul class="simple">
<li><p class="sd-card-text">0 - 低 [512 mg]</p></li>
<li><p class="sd-card-text">1 - 正常[2048 mg]</p></li>
<li><p class="sd-card-text">2 - 高 [4064 mg]</p></li>
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
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x11</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>0x11 と入力すると、コマンド Leaps_stnry_cfg_set を意味します</p>
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
