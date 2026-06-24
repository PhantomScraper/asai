---
title: "leaps_usr_data_read"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-usr-data-read"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-usr-data-read/"
order: 240
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-usr-data-read">
<span id="id1"></span><h1>leaps_usr_data_read</h1>
<p>ノードからユーザー データを読み取ります。 UART/SPI または BLE で受信した新しいユーザー データを通知するには、それぞれ <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a> と <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> で対応するイベントを有効にします。これにより、ステータスに専用フラグが設定され、UART/SPI または BLE でイベントが生成されます。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">タイプ: 2 ビット (<em>ユーザーデータタイプ</em>)</p>
<ul>
<li><p class="sd-card-text">‘0’ は、BLE、SPI、UART などの他のインターフェイスから UWB インターフェイスに書き込まれたユーザー データを読み取ることを意味します</p></li>
<li><p class="sd-card-text">‘1’ は、UWB、SPI、UART などの他のインターフェイスから BLE インターフェイスに書き込まれたユーザー データを読み取ることを意味します</p></li>
<li><p class="sd-card-text">‘2’ は不揮発性メモリからユーザーデータを読み取ることを意味します</p></li>
</ul>
</li>
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
<li><p class="sd-card-text">データ: (<em>ユーザー データ バイトは、データに応じて最大 250 バイトタイプ</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>例 1 (UWB ユーザー データの読み取り)</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 32%">
<col style="width: 32%">
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
<tr class="row-odd"><td><p>0x19</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x19 (12 進数 25) はコマンドを意味しますリープ_usr_data_read</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 16%">
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 16%">
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
<tr class="row-odd"><td><p>最大34バイト</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x4B</p></td>
<td><p>0x22</p></td>
<td><p>0x01
0x02
0x03
…
0x23
0x22</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x4B は UWB ユーザーデータを意味します</p>
<p><strong>例 2 (BLE ユーザー データの読み取り)</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 32%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値フラグ</p></td>
</tr>
<tr class="row-odd"><td><p>0x19</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x19 (12 進数 25) はコマンドを意味しますリープ_usr_data_read</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 16%">
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 16%">
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
<tr class="row-odd"><td><p>最大 128 バイト</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x51</p></td>
<td><p>0x80</p></td>
<td><p>0x01
0x02
0x03
…
0x7F
0x80</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x51 は BLE ユーザーデータを意味します</p>
<p><strong>例 3 (不揮発性メモリに保存されているユーザー データを読み取る)</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 32%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値フラグ</p></td>
</tr>
<tr class="row-odd"><td><p>0x19</p></td>
<td><p>0x01</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x19 (12 進数 25) はコマンドを意味しますリープ_usr_data_read</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 16%">
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 16%">
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
<tr class="row-odd"><td><p>最大 250 バイト</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x58</p></td>
<td><p>0x80</p></td>
<td><p>0x01
0x02
0x03
…
0xFA</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x58 (88 dec) は、不揮発性ファイルに保存されたユーザー データを意味します。メモリ</p>
</div>


           </div>
