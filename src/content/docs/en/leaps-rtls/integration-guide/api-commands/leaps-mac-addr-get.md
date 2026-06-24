---
title: "leaps_mac_addr_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-get/"
order: 256
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-get">
<span id="id1"></span><h1>leaps_mac_addr_get</h1>
<p>Get the MAC address list. Device uses either
address specified by the user or the default address. The default MAC
address for each interface can be changed only once by calling <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a>
in which case it is written to OTP memory and becomes a new default MAC
address. The user can set a custom MAC address by calling
<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set#leaps-mac-addr-set"><span class="std std-ref">leaps_mac_addr_set</span></a>. The default MAC address
can be recovered by factory reset (see
<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-factory-reset#leaps-factory-reset"><span class="std std-ref">leaps_factory_reset</span></a>) after being modified by
the user. Mapping of the MAC addresses to
the particular interface is based on the order in the list as follows:</p>
<ol class="arabic simple">
<li><p>UWB</p></li>
<li><p>BLE</p></li>
<li><p>Ethernet</p></li>
<li><p>Wi-Fi</p></li>
</ol>
<p>The BLE address can be Random BLE address or Public BLE address. If a
particular interface is not supported, the corresponding MAC address in
the list is empty.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">(<em>none</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Output</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a></p></li>
<li><p class="sd-card-text">type_0, type_1, type_2, type_3: 8-bit unsigned integer (<em>type describing the MAC address nr. 0,1,2,3 in the list</em>)</p></li>
<li><p class="sd-card-text">mac_addr_0, mac_addr_1, mac_addr_2, mac_addr_3: 48-bit value (<em>MAC address nr. 0,1,2,3 in little endian</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p>SPI/UART example</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 52%">
<col style="width: 48%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
</tr>
<tr class="row-odd"><td><p>0x83</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x83 (131 dec) means command leaps_mac_addr_get</p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(byte 0-4) flags of the MAC address list in little endian</div>
<div class="line">(byte 5-10) MAC address 0 in little endian</div>
<div class="line">(byte 11-16) MAC address 1 in little endian</div>
<div class="line">(byte 17-22) MAC address 2 in little endian</div>
<div class="line">(byte 23-28) MAC address 3 in little endian</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means err_code of the previous command</p>
<p>Type 0xC1(193 dec) means MAC address list</p>
<p><strong>MAC address flags encoding</strong></p>
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
<tr class="row-odd"><th class="head" colspan="9"><p><strong>flags of the MAC address list</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="2"><p>byte 0</p></td>
<td colspan="3"><p>byte 1</p></td>
<td colspan="2"><p>byte 2</p></td>
<td colspan="2"><p>byte 3</p></td>
</tr>
<tr class="row-odd"><td><p>bits 2-7</p></td>
<td><p>bits 0-1</p></td>
<td><p>bits 11-15</p></td>
<td><p>bits 10</p></td>
<td><p>bits 8-9</p></td>
<td><p>bits 18-23</p></td>
<td><p>bits 16-17</p></td>
<td><p>bits 26-31</p></td>
<td><p>bits 24-25</p></td>
</tr>
<tr class="row-even"><td><p>Reserved</p></td>
<td><p>T_0</p></td>
<td><p>Reserved</p></td>
<td><p>P_1</p></td>
<td><p>T_1</p></td>
<td><p>Reserved</p></td>
<td><p>T_2</p></td>
<td><p>Reserved</p></td>
<td><p>T_3</p></td>
</tr>
</tbody>
</table>
<p>T_0, T_1, T_2, T_3 describe the MAC address type.</p>
<ul class="simple">
<li><p>0 - Empty MAC address</p></li>
<li><p>1 - Default MAC address from OTP memory.</p></li>
<li><p>2 - User specified MAC address</p></li>
<li><p>3 - Mutable default MAC address which can be rewritten only once using <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a>.</p></li>
</ul>
<p>P_1 is set if the BLE address is the Public BLE address. The flag is
cleared if the BLE MAC address is random, refer to BLE specification for
more information on BLE address types.</p>
</div>


           </div>
