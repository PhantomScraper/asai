---
title: "leaps_usr_data_write"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-usr-data-write"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-usr-data-write/"
order: 271
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-usr-data-write">
<span id="id1"></span><h1>leaps_usr_data_write</h1>
<p>カスタム ユーザー データを不揮発性メモリに書き込むか、UWB または BLE インターフェイス経由でデータを送信します。新しいユーザー データに関する通知を受信するか、ユーザー データを読み取るには、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-usr-data-read#leaps-usr-data-read"><span class="std std-ref">leaps_usr_data_read</span></a> を参照してください。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<blockquote>
<div><ul>
<li><p class="sd-card-text">データ</p></li>
<li><p class="sd-card-text">type: 2 ビット (<em>ユーザー データ タイプ、‘0’ はユーザー データを UWB インターフェイスに書き込むことを意味し、‘1’ はユーザー データを BLE インターフェイスに書き込むことを意味し、‘2’ はユーザー データを不揮発性メモリに書き込むことを意味します</em>)</p></li>
<li><p class="sd-card-text">フラッグ: 上書き、テスト</p></li>
<li><p class="sd-card-text">上書き: 1 ビット</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">’0’ は上書きしないことを意味します</p></li>
<li><p class="sd-card-text">’1’ は現在送信中のデータを上書きすることを意味します</p></li>
</ul>
</div></blockquote>
</li>
<li><p class="sd-card-text">test: 1 bit (Applies only when type=0)</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">‘0’ means test data is disabled</p></li>
<li><p class="sd-card-text">‘1’ means device will send test user data (maximum size with first 4 bytes being frame counter). The input data length must be 4 and the input data is parsed as the number of test frames to send.</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
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
<blockquote>
<div><p class="sd-card-text">'ビジー' - 前のデータはまだ送信されていません。再試行するか、上書きフラグを 1 に設定して送信してください。</p>
<p class="sd-card-text">''無効なパラメータ' - ユーザー データのサイズが大きすぎるか、ユーザー データのタイプが不明です。</p>
<p class="sd-card-text">'内部エラー' - 予期しない内部エラー。</p>
<p class="sd-card-text">BLE</p>
<blockquote>
<div><p class="sd-card-text">'許可されていません' - BLE インターフェイス上にアクティブな接続がありません。</p>
</div></blockquote>
</div></blockquote>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p>例 (UWB ユーザーデータの書き込み)</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><div class="line-block">
<div class="line">フラグ</div>
<div class="line">(ビット 0 ～ 1) タイプ</div>
<div class="line">(ビット 2) 上書き</div>
<div class="line">(ビット3) テスト</div>
<div class="line">(ビット4-7 ) 予約済み</div>
</div>
</td>
<td><p>UWB、BLE ユーザー データ - 最大 26 バイトの不揮発性メモリ ユーザー データ - 最大 250 バイト</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x00</p></td>
<td><p>0x01 0x02 0x03 …. 0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x1A (26 dec) はコマンド leaps_usr_data_write を意味します</p>
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
<p>タイプ 0x40 はコマンドの <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</p>
<p>例(UWBユーザデータの書き込みテスト)</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><div class="line-block">
<div class="line">フラグ</div>
<div class="line">(ビット 0 ～ 1) タイプ</div>
<div class="line">(ビット 2) 上書き</div>
<div class="line">(ビット3) テスト</div>
<div class="line">(ビット4-7 ) 予約済み</div>
</div>
</td>
<td><p>Data length must be 4 bytes
Number of frames to be sent
(e.g 10 frames -
0x0A 0x00 0x00 0x00)</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x05</p></td>
<td><p>0x0C</p></td>
<td><p>0x0A 0x00 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x1A (26 dec) はコマンド leaps_usr_data_write を意味します</p>
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
<p>タイプ 0x40 はコマンドの <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</p>
<p>例 (BLE ユーザーデータを上書き)</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><div class="line-block">
<div class="line">フラグ</div>
<div class="line">(ビット 0 ～ 1) タイプ</div>
<div class="line">(ビット 2) 上書き</div>
<div class="line">(ビット3) テスト</div>
<div class="line">(ビット4-7 ) 予約済み</div>
</div>
</td>
<td><p>BLE ユーザーデータ最大 34 バイト</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x05</p></td>
<td><p>0x01 0x02 0x03 …. 0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x1A (26 dec) はコマンド leaps_usr_data_write を意味します</p>
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
<p>タイプ 0x40 はコマンドの <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</p>
<p>例 (ユーザーデータを不揮発性メモリに書き込む)</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><div class="line-block">
<div class="line">フラグ</div>
<div class="line">(ビット 0 ～ 1) タイプ</div>
<div class="line">(ビット 2) 上書き</div>
<div class="line">(ビット3) テスト</div>
<div class="line">(ビット4-7 ) 予約済み</div>
</div>
</td>
<td><p>の不揮発性メモリ ユーザー データ - 最大 250 バイト</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x02</p></td>
<td><p>0x01 0x02 0x03 …. 0xFA</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x1A (26 dec) はコマンド leaps_usr_data_write を意味します</p>
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
<p>タイプ 0x40 はコマンドの <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</p>
</div>


           </div>
