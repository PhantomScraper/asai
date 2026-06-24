---
title: "leaps_mac_addr_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-get/"
order: 255
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-get">
<span id="id1"></span><h1>leaps_mac_addr_get</h1>
<p>MAC アドレス リストを取得します。デバイスは、ユーザーが指定したアドレスまたはデフォルトのアドレスを使用します。各インターフェイスのデフォルトの MAC アドレスは、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a> を呼び出すことによって 1 回だけ変更できます。この場合、アドレスは OTP メモリに書き込まれ、新しいデフォルトの MAC アドレスになります。ユーザーは、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set#leaps-mac-addr-set"><span class="std std-ref">leaps_mac_addr_set</span></a> を呼び出すことによってカスタム MAC アドレスを設定できます。デフォルトの MAC アドレスは、ユーザーが変更した後、工場出荷時設定にリセットすることで復元できます (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-factory-reset#leaps-factory-reset"><span class="std std-ref">leaps_factory_reset</span></a> を参照)。特定のインターフェイスへの MAC アドレスのマッピングは、次のリストの順序に基づいています。</p>
<ol class="arabic simple">
<li><p>UWB</p></li>
<li><p>BLE</p></li>
<li><p>イーサネット</p></li>
<li><p>无线网络</p></li>
</ol>
<p>BLE アドレスは、ランダム BLE アドレスまたはパブリック BLE アドレスにすることができます。特定のインターフェースがサポートされていない場合、リスト内の対応する MAC アドレスは空になります。</p>
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
<li><p class="sd-card-text">type_0、type_1、type_2、type_3: 8 ビット符号なし整数 (<em>リスト内の MAC アドレス番号 0、1、2、3 を表すタイプ</em>)</p></li>
<li><p class="sd-card-text">mac_addr_0、mac_addr_1、mac_addr_2、mac_addr_3: 48 ビット値 (<em>リトル エンディアンの MAC アドレス番号 0、1、2、3</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p>SPI/UART の例</p>
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
<tr class="row-odd"><td><p>0x83</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x83 (131 dec) はコマンド Leaps_mac_addr_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 12%">
<col style="width: 7%">
<col style="width: 8%">
<col style="width: 57%">
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
<div class="line">(バイト 0 ～ 4) リトル エンディアンの MAC アドレス リストのフラグ</div>
<div class="line">(バイト 5-10) リトルエンディアンの MAC アドレス 0</div>
<div class="line">(バイト 11-16) リトルエンディアンの MAC アドレス 1</div>
<div class="line">(バイト 17-22) リトルエンディアンの MAC アドレス 2</div>
<div class="line">(バイト 23-28) リトルエンディアンの MAC アドレス 3</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>...</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 は、直前のコマンドの err_code を意味する</p>
<p>タイプ 0xC1(193 dec) は MAC アドレスリストを意味します</p>
<p><strong>MAC アドレス フラグのエンコーディング</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 9%">
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>MAC アドレス リストのフラグ**</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="2"><p>バイト 0</p></td>
<td colspan="3"><p>バイト1</p></td>
<td colspan="2"><p>バイト2</p></td>
<td colspan="2"><p>バイト3</p></td>
</tr>
<tr class="row-odd"><td><p>ビット 2 ～ 7</p></td>
<td><p>ビット0～1</p></td>
<td><p>ビット 11 ～ 15</p></td>
<td><p>ビット10</p></td>
<td><p>ビット 8 ～ 9</p></td>
<td><p>ビット 18 ～ 23</p></td>
<td><p>ビット 16 ～ 17</p></td>
<td><p>ビット 26-31</p></td>
<td><p>ビット 24-25</p></td>
</tr>
<tr class="row-even"><td><p>予約済み</p></td>
<td><p>T_0</p></td>
<td><p>予約済み</p></td>
<td><p>P_1</p></td>
<td><p>T_1</p></td>
<td><p>予約済み</p></td>
<td><p>T_2</p></td>
<td><p>予約済み</p></td>
<td><p>T_3</p></td>
</tr>
</tbody>
</table>
<p>T_0、T_1、T_2、T_3 は MAC アドレスのタイプを表します。</p>
<ul class="simple">
<li><p>0 - 空の MAC アドレス</p></li>
<li><p>1 - OTP メモリからのデフォルトの MAC アドレス。</p></li>
<li><p>2 - ユーザーが指定した MAC アドレス</p></li>
<li><p>3 - 変更可能なデフォルト MAC アドレス。<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a> を使用して 1 回だけ書き換えることができます。</p></li>
</ul>
<p>BLE アドレスがパブリック BLE アドレスの場合、P_1 が設定されます。 BLE MAC アドレスがランダムな場合、フラグはクリアされます。BLE アドレス タイプの詳細については、BLE 仕様を参照してください。</p>
</div>


           </div>
