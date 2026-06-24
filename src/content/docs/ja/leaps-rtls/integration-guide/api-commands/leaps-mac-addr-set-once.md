---
title: "leaps_mac_addr_set_once"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once/"
order: 257
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-set-once">
<span id="id1"></span><h1>leaps_mac_addr_set_once</h1>
<p>MAC アドレスリストを OTP メモリに書き込むため、慎重に使用する必要があります。値を書き込んだ後は変更できません。これは、UWB、BLE、イーサネット、または Wi-Fi インターフェイスで使用されるデバイスの MAC アドレス プールを提供するために、運用段階で使用されることを目的としています。現在、MAC アドレスのリストは次のようにさまざまなインターフェイスに割り当てられています:</p>
<ul class="simple">
<li><p>MAC アドレス 0 が UWB インターフェイスに割り当てられます。最下位 2 バイトは 0x0000 または 0xFFFF と等しくであってはなりません。</p></li>
<li><p>MAC アドレス 1 が BLE インターフェイスに割り当てられます。このアドレスはパブリック BLE アドレスとして使用されます。</p></li>
<li><p>MAC アドレス 2 はイーサネットに、MAC アドレス 3 は Wi-Fi インターフェイスにそれぞれ割り当てられます。アドレスは、LAA/UAA ビットおよび U/I ビットに関して EUI-48 形式である必要があります。</p></li>
</ul>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">mac_addr_0: 48 ビット値 (<em>リトルエンディアンの UWB MAC アドレス</em>)</p></li>
<li><p class="sd-card-text">mac_addr_1: 48 ビット値 (<em>リトル エンディアンの BLE MAC アドレス</em>)</p></li>
<li><p class="sd-card-text">mac_addr_2: 48 ビット値 (<em>イーサネット MACリトルエンディアンのアドレス</em>)</p></li>
<li><p class="sd-card-text">mac_addr_3: 48 ビット値 (<em>リトルエンディアンの WIFI MAC アドレス</em>)</p></li>
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
<p>SPI/UART の例</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 17%">
<col style="width: 67%">
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
<tr class="row-odd"><td rowspan="2"><p>0x82</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(バイト 0-5) リトルエンディアンの MAC アドレス 0</div>
<div class="line">(バイト 6-11) リトルエンディアンの MAC アドレス 1</div>
<div class="line">(バイト 12-17) リトルエンディアンの MAC アドレス 2</div>
<div class="line">(バイト 18-23) リトルエンディアンの MAC アドレス 3</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>...</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x82 (130 dec) はコマンド <a class="reference internal" href="#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a> を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 は、直前のコマンドの err_code を意味する</p>
</div>


           </div>
