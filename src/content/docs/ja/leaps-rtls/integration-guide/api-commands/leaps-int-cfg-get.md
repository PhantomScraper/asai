---
title: "leaps_int_cfg_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-int-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-get/"
order: 266
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-int-cfg-get">
<span id="id1"></span><h1>leaps_int_cfg_get</h1>
<p>設定されている場合、イベントの場合に専用 GPIO ピン (CORE_INT) の設定を有効にする構成フラグを読み取ります。この呼び出しは、UART/SPI インターフェイスでのみ使用できます。</p>
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
<li><p class="sd-card-text">spi_data_ready: '0' | ‘1’ (<em>新しい SPI データ準備完了イベント、0= 無効、1= 有効</em>)</p></li>
<li><p class="sd-card-text">loc_ready: '0' | ‘1’ (<em>新しい位置データ準備完了イベント、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">bh_data_ready: ‘0’ | ‘1’ (<em>UWBMAC バックホール データ準備完了、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">bh_data_ready: ‘0’ | ‘1’ (<em>UWBMAC バックホール データ準備完了、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">bh_initialized_changed: ‘0’ | ‘1’ (<em>UWBMAC ルート構成、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">uwb_scan_ready: '0' | ‘1’ (<em>UWB スキャン結果が利用可能</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_ready: ‘0’ | ‘1’ (<em>新しいユーザー データが UWBMAC 経由で受信されたときのイベント、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">uwbmac_joined_changed: ‘0’ | ‘1’ (<em>UWBMAC 参加イベント、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_sent: ‘0’ | ‘1’ (<em>UWBMAC を介したユーザー データ送信が完了、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">proxy_pos_ready: '0' | ‘1’ (<em>プロキシ位置の準備ができたときのイベント、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_ready: ‘0’ | ‘1’ (<em>BLE でユーザーデータを受信したときのイベント、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_sent: ‘0’ | ‘1’ (<em>BLE 経由でユーザー データが送信されるときのイベント、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">ble_conn_state_changed: ‘0’ | ‘1’ (<em>BLE 接続状態が変化したときのイベント、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">距離アラーム_th_1: '0' | ‘1’ (<em>閾値 1 に対して距離アラームが発生したときのイベント、0=無効、1=有効</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_2: ‘0’ | ‘1’ (<em>閾値 2 に対して距離アラームが発生したときのイベント、0=無効、1=有効</em>)</p></li>
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
<tr class="row-odd"><td><p>0x35</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x35 と入力すると、コマンド Leaps_int_cfg_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 49%">
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
<div class="line">(ビット 15) 予約済み</div>
<div class="line">(bit 14) distance_alarm_th_2</div>
<div class="line">(bit 13) distance_alarm_th_1</div>
<div class="line">(bit 12) ble_conn_state_changed</div>
<div class="line">(bit 11) ble_usr_data_sent</div>
<div class="line">(bit 10) ble_usr_data_ready</div>
<div class="line">(bit 9) proxy_pos_ready</div>
<div class="line">(bit 8) uwb_usr_data_sent</div>
<div class="line">(bit 7) uwbmac_joined_changed</div>
<div class="line">(bit 6) uwb_usr_data_ready</div>
<div class="line">(bit 5) uwb_scan_ready</div>
<div class="line">(bit 4) bh_initialized_changed</div>
<div class="line">(bit 3) bh_data_ready</div>
<div class="line">(bit 2) bh _status_changed</div>
<div class="line">(bit 1) spi_data_ready</div>
<div class="line">(bit 0) loc_ready</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x47</p></td>
<td><p>0x02</p></td>
<td><p>0x0E
0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x47 は割り込み設定を意味します</p>
</div>


           </div>
