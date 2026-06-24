---
title: "leaps_upd_rate_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-upd-rate-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-set/"
order: 234
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-upd-rate-set">
<span id="id1"></span><h1>leaps_upd_rate_set</h1>
<hr class="docutils">
<p>更新レートと固定更新レートをスーパーフレームの倍数で設定します。新しい値が設定される場合、内部フラッシュ メモリに書き込みます。そのため、頻繁に使用すべきではなく、最悪の場合、数百ミリ秒かかることがあります。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">update_rate_nominal: 16 ビット符号なし整数 (<em>スーパーフレームの倍数での位置公開レート、最大は 600、最小は 1</em>)</p></li>
<li><p class="sd-card-text">update_rate_stationary: 16 ビット符号なし整数 (<em>ノードが複数のスーパーフレームで移動していない場合の位置公開レート、最大は 600、最小は1</em>)</p></li>
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
<col style="width: 12%">
<col style="width: 37%">
<col style="width: 43%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>update_rate_nominal</p></td>
<td><p>update_rate_stationary</p></td>
</tr>
<tr class="row-even"><td><p>0x03</p></td>
<td><p>0x04</p></td>
<td><p>0x0A 0x00</p></td>
<td><p>0x14 0x00</p></td>
</tr>
</tbody>
</table>
<p>0x03 と入力すると、コマンド Leaps_upd_rate_set を意味します</p>
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
<hr class="docutils">
</div>


           </div>
