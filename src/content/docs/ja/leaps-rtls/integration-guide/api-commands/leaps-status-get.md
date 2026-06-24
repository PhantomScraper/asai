---
title: "leaps_status_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-status-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-status-get/"
order: 280
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-status-get">
<span id="id1"></span><h1>leaps_status_get</h1>
<p>システムステータスフラグを取得します。ステータス フラグは、 <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a> によって CORE_INT GPIO ピンの設定を有効にすることができます。以下を除くすべてのステータス フラグは、leaps_status_get の呼び出し後にクリアされます。</p>
<blockquote>
<div><ul class="simple">
<li><p>ble_conn_state</p></li>
<li><p>uwbmac_joined</p></li>
<li><p>bh_initialized</p></li>
<li><p>distance_alarm_th_1</p></li>
<li><p>distance_alarm_th_1</p></li>
</ul>
</div></blockquote>
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
<li><p class="sd-card-text">status: loc_ready, uwbmac_joined, bh_data_ready, bh_initialized, bh_status_changed, uwb_scan_ready, uwb_usr_data_ready, uwb_usr_data_sent, fwup_in_progress, proxy_pos_ready, ble_usr_data_ready, ble_usr_data_sent, ble_conn_state, distance_alarm_th_1,distance_alarm_th_2</p></li>
<li><p class="sd-card-text">loc_ready: ‘0’ | ‘1’ (<em>新しい位置データが準備完了</em>)</p></li>
<li><p class="sd-card-text">uwbmac_joined: ‘0’ | ‘1’ (<em>ノードは UWB ネットワークに接続されています</em>)</p></li>
<li><p class="sd-card-text">bh_data_ready: '0' | ‘1’ (<em>UWB MAC バックホール データ準備完了</em>)</p></li>
<li><p class="sd-card-text">bh_status_changed: ‘0’ | ‘1’ (<em>UWB MAC ステータスが変更され、バックホールで使用されます</em>)</p></li>
<li><p class="sd-card-text">bh_initialized: ‘0’ | ‘1’ (<em>ノードは UWB バックホール経由でルートを初期化しました</em>)</p></li>
<li><p class="sd-card-text">uwb_scan_ready: '0' | ‘1’ (<em>UWB スキャン結果は準備完了</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_ready: ‘0’ | ‘1’ (<em>通过UWB接收到的用户数据</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_ready: ‘0’ | ‘1’ (<em>UWB 経由で受信したユーザー データ</em>)</p></li>
<li><p class="sd-card-text">fwup_in_progress: ‘0’ | ‘1’ (<em>ファームウェアアップデート中</em>)</p></li>
<li><p class="sd-card-text">proxy_pos_ready: '0' | ‘1’ (<em>プロキシ位置は準備完了ですが、ユーザー アプリケーションではサポートされていません</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_ready: ‘0’ | ‘1’ (<em>BLE 経由でユーザー データを受信しました。ユーザー アプリケーションではサポートされていません</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_sent: ‘0’ | ‘1’ (<em>BLE 経由で送信されるユーザー データ、ユーザー アプリケーションではサポートされていません</em>)</p></li>
<li><p class="sd-card-text">ble_conn_state: '0' | ‘1’ (<em>ユーザーアプリケーションではサポートされていません</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_1: ‘0’ | ‘1’ (<em>しきい値 1 の距離アラーム</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_2: ‘0’ | ‘1’ (<em>しきい値 2 の距離アラーム</em>)</p></li>
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
<tr class="row-odd"><td><p>0x32</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x32 と入力すると、コマンド Leaps_status_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 7%">
<col style="width: 35%">
<col style="width: 35%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td rowspan="2"><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bit 0) loc_ready</div>
<div class="line">(bit 1) uwbmac_joined</div>
<div class="line">(bit 2) bh_status_changed</div>
<div class="line">(bit 3) bh_data_ready</div>
<div class="line">(bit 3) bh_data_ready</div>
<div class="line">(bit 5) uwb_scan_ready</div>
<div class="line">(bit 6) uwb_usr_data_ready</div>
<div class="line">(bit 7) uwb_usr_data_sent</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bit 8) fwup_in_progress</div>
<div class="line">(bit 9) proxy_pos_ready</div>
<div class="line">(bit 10) ble_usr_data_ready</div>
<div class="line">(bit 11) ble_usr_data_sent</div>
<div class="line">(bit 12) ble_conn_state</div>
<div class="line">(bit 13) distance_alarm_th_1</div>
<div class="line">(bit 14) distance_alarm_th_2</div>
<div class="line">(ビット 15) 予約済み</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5A</p></td>
<td><p>0x02</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x5A はステータスを意味します</p>
<p>タイプ 0x40 はステータスコード</p>
</div>


           </div>
