---
title: "leaps_cfg_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-get/"
order: 152
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-get">
<span id="id1"></span><h1>leaps_cfg_get</h1>
<p>ノードの現在の構成オプションを取得します。</p>
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
<li><p class="sd-card-text">イニシエーター: 1 ビット (<em>‘0’ | ‘1’ - イニシエーターの役割の有効化</em>)</p></li>
<li><p class="sd-card-text">ゲートウェイ: 1 ビット (<em>‘0’ | ‘1’ - ゲートウェイの役割の有効化</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1 ビット (<em>‘0’ | ‘1’ - 暗号化有効</em>)</p></li>
<li><p class="sd-card-text">led_en: 1 ビット (<em>‘0’ | ‘1’ - 汎用 LED が有効</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1 ビット (<em>‘0’ | ‘1’ - BLE 有効</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2 ビット (<em>0-オフ、1-パッシブ、2-アクティブ</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1 ビット (<em>‘0’ | ‘1’- ファームウェア更新有効</em>)</p></li>
<li><p class="sd-card-text">stnry_en: 1 ビット (<em>‘0’ | ‘1’ 定常検出が有効です。有効な場合、ノードが移動していない場合は、通常の更新レートの代わりに定常更新レートが使用されます</em>)</p></li>
<li><p class="sd-card-text">meas_mode: 2 ビット (<em>‘0’ | ‘1’ | ‘2’ | ‘3’ 、0 - 双方向レンジング、1 - UL-TDoA、2 - DL-TDoA、3 - 予約済み</em>)</p></li>
<li><p class="sd-card-text">low_power_en: 1 ビット (<em>‘0’ | ‘1’ 低電力モード有効</em>)</p></li>
<li><p class="sd-card-text">loc_engine_en: 1 ビット(<em>‘0’ | ‘1’ 0 は内部ロケーション エンジンを使用しないことを意味し、1 は内部ロケーション エンジンを意味します</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3 ビット (<em>プロファイルの ID</em>)</p></li>
<li><p class="sd-card-text">Clock_reference: 1 ビット (<em>ノード上でクロック リファレンスを有効にします</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble:1 位（<em>节点上的 uwb 激活超过 ble 状态</em>）</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">注釈</p>
<p><strong>uwb_bh_routing</strong>: ファームウェアが UWB ルーティング バックホールでコンパイルされている場合にのみ使用できます。</p>
<p>値: '0' | ‘1’ | ‘2’:</p>
<ul class="simple">
<li><p>0- オフ - アンカーはルーティングアンカーになりません</p></li>
<li><p>1- オン - アンカーは、ルーティング アンカーとして選択されるルーティング アルゴリズムによって優先されます。</p></li>
<li><p>2- AUTO - アンカーがルーティングになるかどうかは、ルーティング アルゴリズムに完全に依存します。</p></li>
</ul>
</div>
</div></blockquote>
<hr class="docutils">
<p><strong>例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 53%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
</tr>
<tr class="row-odd"><td><p>0x08</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x08 と入力すると、コマンド Leaps_cfg_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 20%">
<col style="width: 30%">
<col style="width: 26%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td rowspan="2"><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
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
<div class="line">(bits 0-1) uwb_mode:</div>
<div class="line">0 - オフライン、</div>
<div class="line">1 - パッシブ、、</div>
<div class="line">2 - アクティブ</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(ビット 6-7) uwb_bh_routing:</div>
<div class="line">0 -オフ、</div>
<div class="line">1 - オン、</div>
<div class="line">2 -オート</div>
<div class="line">(ビット 5) モード:</div>
<div class="line">0 - タグ</div>
<div class="line">1 - アンカー</div>
<div class="line">(ビット 4) イニシエーター</div>
<div class="line">(ビット 3) ゲートウェイ</div>
<div class="line">(ビット2) stnry_en</div>
<div class="line">(ビット 0 ～ 1)測定モード:</div>
<div class="line">0 - TWR,</div>
<div class="line">1 - UL-TDoA</div>
<div class="line">2 - DL-TDoA</div>
<div class="line">3保留</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(ビット 0 ～ 2) プロファイル ID</div>
<div class="line">(ビット 3) クロックリファレンス</div>
<div class="line">(bit 4) uwb_act_ble</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x46</p></td>
<td><p>0x03</p></td>
<td><p>0x1C</p></td>
<td><p>0x20</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x46 はノード構成を意味します</p>
</div>


           </div>
