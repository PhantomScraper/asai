---
title: "leaps_loc_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-loc-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-loc-get/"
order: 225
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-loc-get">
<span id="id1"></span><h1>leaps_loc_get</h1>
<hr class="docutils">
<p>測距アンカーまでの最後の距離を取得し、位置を取得します。すべての TWR 測定が完了し、ユーザーが新しい位置データを利用できるようになると、イベントが生成され、ステータスが変更されます。低電力モードを使用する場合も同様に動作します。</p>
<p>アンカー ノードの場合、位置と距離は、自動位置決め手順が完了している場合にのみ使用できます。自動位置決め手順は、BLE インターフェイス経由で開始されます。</p>
<hr class="docutils">
<p><strong>タグ・ノード</strong></p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">8 ビット符号なし整数 (出力オプション、0 - 測距アンカーまでの距離、1 - 自分の位置 + 測距アンカーまでの距離、2 - 測距アンカーまでの位置と距離、3 - 自分の位置 + 測距アンカーまでの距離と位置)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a>, [my_position], [タイムスタンプ、フラグ、カウント、[{addr,アンカー距離, pqf}, ...]], [タイムスタンプ, フラグ, カウント, [{アンカー位置, アドレス, アンカー距離, pqf}, ..]]</p></li>
<li><p class="sd-card-text">タイムスタンプ: 32 ビット整数? (マイクロ秒単位のタイムスタンプ)</p></li>
<li><p class="sd-card-text">フラグ: 8 ビット符号なし整数? (is_moving 表示)</p></li>
<li><p class="sd-card-text">count: 8 ビット整数 (後続のリスト内の要素の数。リストには位置、距離、またはその両方を含めることができます)</p></li>
<li><p class="sd-card-text">my_position、anchor_position: 13 バイト (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#position"><span class="std std-ref">位置</span></a> を参照)</p></li>
<li><p class="sd-card-text">addr: 16 ビット整数 (対向ノードの UWB アドレス/ID)</p></li>
<li><p class="sd-card-text">距離: 32 ビット整数（対向車までの距離（ミリメートル））</p></li>
<li><p class="sd-card-text">pqf: 8 ビット整数 (品質係数)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p><strong>タグ ノード</strong> の場合 - 利用可能なパラメータ - 位置: <strong>位置</strong> (距離に対応する反対側のノードの位置)</p>
</div>
<hr class="docutils">
<p><strong>例 1 (自分の位置 + 測距アンカーまでの距離と位置)</strong></p>
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
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x0C はコマンド loc_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 16%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 19%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値のステータス</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>このノードの値の位置 (13 バイト)</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>測距アンカーまでの値の位置と距離 (86 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>...</p></td>
<td><p>0x49</p></td>
<td><p>0x56</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x41 は位置を意味します</p>
<p>タイプ 0x49 は、タグ ノード上の位置と距離を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 27%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 14%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>測距アンカーまでの位置と距離のエンコード</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>マイクロ秒単位のタイムスタンプ</p></td>
<td rowspan="2"><div class="line-block">
<div class="line">フラグ(1バイト)</div>
</div>
<div class="line-block">
<div class="line">(ビット 0) is_moving</div>
<div class="line">(ビット 1 ～ 7) 予約済み</div>
</div>
</td>
<td rowspan="2"><p>エンコードされた位置と距離の数 (1 バイト)</p></td>
<td colspan="2"><p>位置と距離番号。 1（20バイト）</p></td>
<td><p>位置と距離 nr.2、3、4 (60 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>距離番号 1</p>
<p>(7バイト)</p>
</td>
<td><p>位置番号 1</p>
<p>(13バイト)</p>
</td>
<td><p>...</p></td>
</tr>
<tr class="row-even"><td><p>0x64
0x0A
0x01
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x04</p></td>
<td><p>...</p></td>
<td><p>...</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x49 は、タグ ノード上の位置と距離を意味します。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 39%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>距離エンコーディング</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB アドレス</p>
<p>(2バイト)</p>
</td>
<td><p>ミリメートル単位の距離</p>
<p>(4バイト)</p>
</td>
<td><p>パーセント単位の距離品質係数 (1 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>0xAB 0xCD</p></td>
<td><p>0xE8 0x03 0x00 0x00</p></td>
<td><p>0x5F</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 23%">
<col style="width: 25%">
<col style="width: 28%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>位置エンコーディング</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x 座標 (ミリメートル単位)</p>
<p>(4バイト)</p>
</td>
<td><p>ミリメートル単位の y 座標 (4 バイト)</p></td>
<td><p>ミリメートル単位の Z 座標</p>
<p>(4バイト)</p>
</td>
<td><p>位置品質係数 (パーセント単位) (1 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>0x4b 0x0a 0x00
0x00</p></td>
<td><p>0x1f 0x04
0x00 0x00</p></td>
<td><p>0x9c 0x0e 0x00
0x00</p></td>
<td><p>0x64</p></td>
</tr>
</tbody>
</table>
<p><strong>例 2 (自分の位置 + 測距アンカーまでの距離)</strong></p>
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
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x0C はコマンド loc_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 16%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 19%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>ステータスコード</p></td>
<td><p>このノードの位置 (13 バイト)</p></td>
<td><p>測距アンカーまでの距離 (90 バイト)</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>...</p></td>
<td><p>0x48</p></td>
<td><p>0x5A</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x41 は位置を意味します</p>
<p>タイプ 0x48 は測距アンカーの距離を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 29%">
<col style="width: 13%">
<col style="width: 17%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>測距アンカーまでの距離のエンコーディング</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>マイクロ秒単位のタイムスタンプ (4 バイト)</p></td>
<td><div class="line-block">
<div class="line">フラグ(1バイト)</div>
</div>
<div class="line-block">
<div class="line">(ビット 0) is_moving</div>
<div class="line">(ビット 1 ～ 7) 予約済み</div>
</div>
</td>
<td><p>エンコードされた距離の数</p>
<p>(1バイト)</p>
</td>
<td><p>距離番号 1</p>
<p>(7バイト)</p>
</td>
<td><p>距離番号。 2、3、…、11、12</p>
<p>(77バイト)</p>
</td>
</tr>
<tr class="row-odd"><td><p>0x64
0x12
0x0E
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x04</p></td>
<td><p>...</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
