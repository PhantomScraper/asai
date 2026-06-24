---
title: "leaps_cfg_tag_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set/"
order: 149
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-tag-set">
<span id="id1"></span><h1>leaps_cfg_tag_set</h1>
<p>指定されたオプションを使用してノードをタグとして構成します。暗号化キーが設定されていない場合は、暗号化を有効にできません。この呼び出しでは、新しい構成を有効にするためにリセットが必要です (leaps_reset)。この呼び出しは、新しい値が設定されている場合、内部フラッシュへの書き込みを行うため、頻繁に使用すべきではなく、最悪の場合、数百ミリ秒かかることがあります。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">stnry_en: 1 ビット (<em>‘0’ | ‘1’ 定常検出が有効です。有効な場合、ノードが移動していない場合は、通常の更新レートの代わりに定常更新レートが使用されます</em>)</p></li>
<li><p class="sd-card-text">meas_mode: 2 ビット (<em>’0’ - TWR、双方向レンジング、‘1’ - TDOA、到着時間差、‘2’、‘3’ - 予約済み</em>)</p></li>
<li><p class="sd-card-text">low_power_en: 1 ビット (<em>‘0’ | ‘1’ 低電力モード有効</em>)</p></li>
<li><p class="sd-card-text">loc_engine_en: 1 ビット(<em>‘0’ | ‘1’ 0 は内部ロケーション エンジンを使用しないことを意味し、1 は内部ロケーション エンジンを意味します</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1 ビット (<em>‘0’ | ‘1’ 暗号化有効</em>)</p></li>
<li><p class="sd-card-text">led_en: 1 ビット (<em>‘0’ | ‘1’ の汎用 LED が有効になります</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1 ビット (<em>‘0’ | ‘1’ BLE 有効化</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2 ビット (<em>‘0’ | ‘1’ | ‘2’ 0-オフ、1-パッシブ、2-アクティブ</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1 ビット (<em>‘0’ | ‘1’ ファームウェア更新有効</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3 ビット符号なし整数 (<em>プロファイルの ID</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble: 1 ビット符号なし整数 (<em>BLE 経由の UWB アクティベーション</em>)</p></li>
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
<col style="width: 11%">
<col style="width: 9%">
<col style="width: 32%">
<col style="width: 31%">
<col style="width: 16%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="3"><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(ビット7) low_power_en</div>
<div class="line">(ビット6) loc_engine_en</div>
<div class="line">(ビット5) enc_en</div>
<div class="line">(ビット4) led_en</div>
<div class="line">(ビット3) ble_en</div>
<div class="line">(ビット2) fw_update_en</div>
<div class="line">(bits 0-1) uwb_mode</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 4-7) reserved</div>
<div class="line">(bit 3) uwb_act_ble</div>
<div class="line">(ビット2) stnry_en</div>
<div class="line">(bits 0-1) meas_mode</div>
</div>
</td>
<td><p>(ビット 0 ～ 2) プロファイル ID</p></td>
</tr>
<tr class="row-even"><td><p>0x05</p></td>
<td><p>0x03</p></td>
<td><p>0x72</p></td>
<td><p>0x04</p></td>
<td><p>0x05</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x05 はコマンド leaps_cfg_tag_set を意味します</p>
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
