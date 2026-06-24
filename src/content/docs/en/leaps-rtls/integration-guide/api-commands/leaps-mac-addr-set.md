---
title: "leaps_mac_addr_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set/"
order: 257
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-set">
<span id="id1"></span><h1>leaps_mac_addr_set</h1>
<p>Set MAC address of the BLE, UWB, Ethernet or Wi-Fi interface. Needs
reset to take effect. Should not be used frequently since it writes the
internal non-volatile memory. Factory reset is needed
(<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a>) to use the default MAC address. Two
least significant bytes of the UWB MAC address must not be equal to
0x0000 or to the 0xFFFF. The BLE address can be either the Random BLE
address or the Public BLE address. The Ethernet and the Wi-Fi address
must respect the EUI-48 format, and the U/I bits must be set
accordingly.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">type_0, type_1, type_2, type_3: 8-bit unsigned integer (<em>type describing the MAC address nr. 0,1,2,3 in the list</em>)</p></li>
<li><p class="sd-card-text">mac_addr_0, mac_addr_1, mac_addr_2, mac_addr_3: 48-bit value (<em>MAC address nr. 0,1,2,3 in little endian</em>)</p></li>
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
<col style="width: 22%">
<col style="width: 24%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><div class="line-block">
<div class="line">Value</div>
<div class="line">node ID in little endian</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>0x2D</p></td>
<td><p>0x07</p></td>
<td><p>0x00 0xEF
0xCD 0xAB
0x56 0x34
0x12</p></td>
</tr>
</tbody>
</table>
<p>Type 0x2D (45 dec) means command <a class="reference internal" href="#leaps-mac-addr-set"><span class="std std-ref">leaps_mac_addr_set</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 66%">
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
