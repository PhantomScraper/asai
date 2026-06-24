---
title: "leaps_ble_evt_cfg_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set/"
order: 223
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-ble-evt-cfg-set">
<span id="id1"></span><h1>leaps_ble_evt_cfg_set</h1>
<p>BLE インターフェイス上のイベントを有効または無効にします。この呼び出しは、新しい値が設定された場合に内部不揮発性メモリに書き込みを行うため、頻繁に使用すべきではなく、最悪の場合は数百ミリ秒かかることがあります。</p>
<hr class="docutils">
<p><strong>例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 78%">
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
<div class="line">(ビット 10 ～ 15) 予約済み</div>
<div class="line">(ビット 9) ロケーションレディイベントには測距ノードの位置が含まれます</div>
<div class="line">(ビット 8) 位置準備完了イベントには私の位置が含まれます</div>
<div class="line">(ビット3-7 ) 予約済み</div>
<div class="line">(ビット 2) BLE ユーザーデータ準備完了イベントの有効化</div>
<div class="line">(ビット 1) プロキシ位置準備完了イベントが有効になりました</div>
<div class="line">(ビット 0) 位置準備完了イベントが有効になりました</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x21</p></td>
<td><p>0x02</p></td>
<td><p>0x02 0x01</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x21 (33) は、コマンド Leaps_ble_evt_cfg_set を意味します</p>
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
