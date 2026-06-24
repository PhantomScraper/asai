---
title: "leaps_uwb_cfg_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-get/"
order: 274
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-cfg-get">
<span id="id1"></span><h1>leaps_uwb_cfg_get</h1>
<p>設定パラメータを取得します。</p>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
<li><p class="sd-card-text">プリアンブルコード: '9' | ‘10’ | ‘11’ | ‘12’ (<em>UWB プリアンブル コード</em>)</p></li>
<li><p class="sd-card-text">pg_delivery: 1 バイト (<em>送信機校正パルス発生器遅延値</em>)</p></li>
<li><p class="sd-card-text">チャンネル: '2' | ‘3’ | ‘5’ | ‘9’ (<em>UWB チャンネル</em>)</p></li>
<li><p class="sd-card-text">lna_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">pa_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf1_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf2_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">tx_power: 4 bytes (<em>送信電力制御の単位</em>)</p></li>
<li><p class="sd-card-text">rf_compliance: '0' | ‘1’ | ‘2’ (<em>RF 準拠オプション、0: FCC/ETSI、1: ETSI + 10dB、2: ARIB、3: カスタム</em>)</p></li>
<li><p class="sd-card-text">pg_lay_comp: 1 バイト (<em>送信機校正パルス発生器遅延値、補償済み</em>)</p></li>
<li><p class="sd-card-text">tx_power_comp: 4 バイト (<em>送信電力制御の単位、補償済み</em>)</p></li>
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
<tr class="row-odd"><td><p>0x18</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x18 (12 進数 24) は、コマンド Leaps_uwb_cfg_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 55%">
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
<div class="line">(1バイト目) preamble_code</div>
<div class="line">(2バイト目) pg_delay</div>
<div class="line">(3 バイト目) チャネル</div>
<div class="line">(4 番目のバイト、ビット 0) lna_enable</div>
<div class="line">(4 番目のバイト、ビット 1) pa_enable</div>
<div class="line">(4 番目のバイト、ビット 2) rf1_enable</div>
<div class="line">(4 番目のバイト、ビット 3) rf2_enable</div>
<div class="line">(4番目バイト、ビット 4 ～ 8) 予約済み</div>
<div class="line">(5t h-8thバイト) tx_power</div>
<div class="line">(9バイト目) rf_compliance</div>
<div class="line">(10バイト目) pg_dela_comp</div>
<div class="line">(11 ～ 12 バイト目) 予約済み</div>
<div class="line">(13 ～ 16 バイト目) tx_power_comp</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x4F</p></td>
<td><p>0x10</p></td>
<td><p>0x09 0x34 0x05 0x03 0xfd 0xfd 0xfd 0xfd
0x00 0x34 0x00 0x00 0xfd 0xfd 0xfd 0xfd</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x4F は UWB 構成を意味する。</p>
</div>


           </div>
