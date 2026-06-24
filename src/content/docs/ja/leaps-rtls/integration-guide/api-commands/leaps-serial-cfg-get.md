---
title: "leaps_serial_cfg_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-get/"
order: 250
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-serial-cfg-get">
<span id="id1"></span><h1>leaps_serial_cfg_get</h1>
<p>シリアル インターフェイス (UART、SPI など) の現在の構成を読み取ります。</p>
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
<li><p class="sd-card-text">uart_loc_ready_enable: 1 ビット (<em>‘1’ に設定すると、UART インターフェイスでの位置準備イベントが有効になります</em>)</p></li>
<li><p class="sd-card-text">usb_bh_en: 1 ビット (<em>‘1’ に設定するとバックホール用の USB インターフェイスが有効になります</em>)</p></li>
<li><p class="sd-card-text">uart_mode: 1 ビット (<em>‘0’ はリセット後に UART がバイナリ モードになることを意味し、‘1’ は UART がリセット後にコマンド ライン インターフェイス (CLI) モードになることを意味します</em>)</p></li>
<li><p class="sd-card-text">uart_baudrate: ‘0’ | ‘1’ (<em>‘0’: 115200 baud, ‘1’: 1000000 baud</em>)</p></li>
<li><p class="sd-card-text">uart_loc_ready_include_my_pos: 1 ビット (<em>0 は各位置準備イベントに自分の位置を含めることを無効にし、1 は有効にします</em>)</p></li>
<li><p class="sd-card-text">uart_loc_ready_include_ranging_pos: 1 ビット (<em>0 は各位置準備イベントにおける測距ノードへの位置の組み込みを無効にし、1 は有効にします</em>)</p></li>
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
<tr class="row-odd"><td><p>0x39</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x39 (5​​7 dec) は、コマンド Leaps_serial_cfg_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 6%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 8%">
<col style="width: 67%">
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
<div class="line">(ビット 18 ～ 31) 予約済み</div>
<div class="line">(ビット 17) ロケーションレディイベントには測距ノードへの位置が含まれます</div>
<div class="line">(ビット 16) 位置準備完了イベントには私の位置が含まれます</div>
<div class="line">(ビット 15) uart_baudrate</div>
<div class="line">(ビット 9 ～ 14) 予約済み</div>
<div class="line">(ビット 8) uar t_mode、デフォルトの UART モード 0-バイナリ、1-シェル</div>
<div class="line">(bits 2-7) 予約済み</div>
<div class="line">(ビット 1) USB バックホール有効化</div>
<div class="line">(ビット 0) UART の位置準備完了イベント有効にする</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x61</p></td>
<td><p>0x04</p></td>
<td><p>0x01
0x01
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x61 (97) はシリアルインターフェース構成を意味します</p>
</div>


           </div>
