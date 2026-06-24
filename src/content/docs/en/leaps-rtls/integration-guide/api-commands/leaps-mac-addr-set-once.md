---
title: "leaps_mac_addr_set_once"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once/"
order: 258
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-set-once">
<span id="id1"></span><h1>leaps_mac_addr_set_once</h1>
<p>Writes MAC address list to OTP memory and must be used carefully! The
values cannot be modified after they have been written! It is intended
to be used in the production phase to provide a MAC address pool for the
device to be used by UWB, BLE, Ethernet or Wi-Fi interface. Currently
the list of the MAC addresses is assigned to various interfaces as
follows:</p>
<ul class="simple">
<li><p>MAC address 0 is assigned to the UWB interface. Two least significant bytes must not be equal to 0x0000 or to 0xFFFF.</p></li>
<li><p>MAC address 1 is assigned to the BLE interface. The address will be used as the Public BLE address.</p></li>
<li><p>MAC address 2 and MAC address 3 are assigned to the Ethernet and to the Wi-Fi interface respectively. The address should be in th EUI-48 format respecting the LAA/UAA bit and the U/I bit.</p></li>
</ul>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">mac_addr_0: 48-bits value (<em>UWB MAC address in little endian</em>)</p></li>
<li><p class="sd-card-text">mac_addr_1: 48-bits value (<em>BLE MAC address in little endian</em>)</p></li>
<li><p class="sd-card-text">mac_addr_2: 48-bits value (<em>Ethernet MAC address in little endian</em>)</p></li>
<li><p class="sd-card-text">mac_addr_3: 48-bits value (<em>WIFI MAC address in little endian</em>)</p></li>
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
<col style="width: 16%">
<col style="width: 17%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x82</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(byte 0-5) MAC address 0 in little endian</div>
<div class="line">(byte 6-11) MAC address 1 in little endian</div>
<div class="line">(byte 12-17) MAC address 2 in little endian</div>
<div class="line">(byte 18-23) MAC address 3 in little endian</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>…</p></td>
</tr>
</tbody>
</table>
<p>Type 0x82 (130 dec) means command <a class="reference internal" href="#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value (see error codes)</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means err_code of the previous command</p>
</div>


           </div>
