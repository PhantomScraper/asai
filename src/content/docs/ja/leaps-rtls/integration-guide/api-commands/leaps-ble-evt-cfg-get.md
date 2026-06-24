---
title: "leaps_ble_evt_cfg_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-get/"
order: 249
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-ble-evt-cfg-get">
<span id="id1"></span><h1>leaps_ble_evt_cfg_get</h1>
<p>BLE イベントの現在の設定を読み取ります。</p>
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
<tr class="row-odd"><td><p>0x22</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x22 (34) は、コマンド Leaps_ble_evt_cfg_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 47%">
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
<div class="line">(ビット 1 0-15) 予約済み</div>
<div class="line">(ビット 9) ロケーションレディイベントには測距ノードへの位置が含まれます</div>
<div class="line">(ビット 8) 位置準備完了イベントには私の位置が含まれます</div>
<div class="line">(ビット3-7 ) 予約済み</div>
<div class="line">(ビット 2) BLE ユーザーデータ準備完了イベントの有効化</div>
<div class="line">(ビット 1) プロキシ位置準備完了イベントが有効になりました</div>
<div class="line">(ビット 0) 位置準備完了イベントが有効になりました</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5E</p></td>
<td><p>0x02</p></td>
<td><p>0x02
0x01</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x5E (94) は BLE イベント構成を意味します</p>
</div>


           </div>
