---
title: "leaps_uwb_cfg_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-set/"
order: 273
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-cfg-set">
<span id="id1"></span><h1>leaps_uwb_cfg_set</h1>
<p>UWB 構成パラメータを設定します。</p>
<ul class="simple">
<li><p>DW1000: チャネル 2、3、およびチャネル 5 をサポートできます。</p></li>
<li><p>DW3000: チャネル 5 と 9 をサポートできます。</p></li>
</ul>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">プリアンブルコード: '9' | ‘10’ | ‘11’ | ‘12’ (<em>UWB プリアンブル コード</em>)</p></li>
<li><p class="sd-card-text">チャンネル: '2' | ‘3’ | ‘5’ | ‘9’ (<em>UWB チャンネル</em>)</p></li>
<li><p class="sd-card-text">pg_delivery: 1 バイト (<em>送信機のキャリブレーション – パルス発生器の遅延</em>)</p></li>
<li><p class="sd-card-text">lna_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">pa_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf1_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf2_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">tx_power: 4 バイト (<em>TX 電力制御</em>)</p></li>
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
<col style="width: 18%">
<col style="width: 18%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(1バイト目) preamble_code</div>
<div class="line">(2バイト目) pg_delay</div>
<div class="line">(3 バイト目) チャネル</div>
<div class="line">(4 番目のバイト、ビット 0) lna_enable</div>
<div class="line">(4 番目のバイト、ビット 1) pa_enable</div>
<div class="line">(4 番目のバイト、ビット 2) rf1_enable</div>
<div class="line">(4 番目のバイト、ビット 3) rf2_enable</div>
<div class="line">(4番目バイト、ビット 4 ～ 8) 予約済み</div>
<div class="line">(5th-8th byte) tx_power</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x17</p></td>
<td><p>0x08</p></td>
<td><p>0x09 0xC3
0x05 0x03
0x85 0x65
0x45 0x25</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x17 はコマンド leaps_uwb_cfg_set を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV回复</p></th>
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
</div>


           </div>
