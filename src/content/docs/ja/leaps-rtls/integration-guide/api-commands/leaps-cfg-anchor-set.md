---
title: "leaps_cfg_anchor_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set/"
order: 224
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-anchor-set">
<span id="id1"></span><h1>leaps_cfg_anchor_set</h1>
<p>指定されたオプションを使用してノードをアンカーとして構成します。暗号化キーが設定されていない場合は暗号化を有効にできません。この呼び出しでは、新しい構成を有効にするためにリセットが必要です (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a>)。イニシエータで暗号化を有効にすると、同じ暗号化キー セットを持つすべてのノードの暗号化が自動的に有効になります (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-enc-key-set#leaps-enc-key-set"><span class="std std-ref">leaps_enc_key_set</span></a>)。これにより、同じパン ID (ネットワーク ID) と同じ暗号化キーを持つネットワーク全体を 1 か所からリモートで暗号化できるようになります。</p>
<p>この呼び出しは、新しい値が設定された場合に内部フラッシュへの書き込みを行う, したがって、頻繁に使用すべきではなく、最悪の場合、数百ミリ秒かかることがある！</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">イニシエーター: 1 ビット (<em>‘0’ | ‘1’ - イニシエーターの役割の有効化</em>)</p></li>
<li><p class="sd-card-text">ゲートウェイ: 1 ビット (<em>‘0’ | ‘1’ - ゲートウェイの役割の有効化</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1 ビット (<em>‘0’ | ‘1’ - 暗号化有効</em>)</p></li>
<li><p class="sd-card-text">led_en: 1 ビット (<em>‘0’ | ‘1’ - 汎用 LED が有効</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1 ビット (<em>‘0’ | ‘1’ - BLE 有効</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2 ビット (<em>0-オフ、1-パッシブ、2-アクティブ</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1 ビット (<em>‘0’ | ‘1’- ファームウェア更新有効</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3 ビット (<em>プロファイルの ID</em>)</p></li>
<li><p class="sd-card-text">Clock_reference: 1 ビット (<em>ノード上でクロック リファレンスを有効にします</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble: 1 ビット (<em>ノード上で ble を介した uwb のアクティブ化を有効にします</em>)</p></li>
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
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">注釈</p>
<p><strong>uwb_bh_routing</strong>: ファームウェアが UWB ルーティング バックホールでコンパイルされている場合にのみ使用できます。</p>
<p>Value : ‘0’ | ‘1’ | ‘2’</p>
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
<col style="width: 13%">
<col style="width: 8%">
<col style="width: 23%">
<col style="width: 28%">
<col style="width: 29%">
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
<div class="line">(bit 7) イニシエーター</div>
<div class="line">(bit 6) gateway</div>
<div class="line">(ビット5) enc_en</div>
<div class="line">(ビット4) led_en</div>
<div class="line">(ビット3) ble_en</div>
<div class="line">(ビット2) fw_update_en</div>
<div class="line">(bits 0-1) uwb_mode</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 2-7) 予約済み</div>
<div class="line">(bits 0-1) uwb_bh_routing:</div>
<div class="line">0 – オフ</div>
<div class="line">1 – オン</div>
<div class="line">2 -オート</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(ビット 0 ～ 2) プロファイル ID</div>
<div class="line">(ビット 3) クロックリファレンス</div>
<div class="line">(ビット 4) uwb アクティベーション ble</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x07</p></td>
<td><p>0x03</p></td>
<td><p>0x9C</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x07 はコマンド Leaps_cfg_anchor_set を意味します</p>
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
