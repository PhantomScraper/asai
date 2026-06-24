---
title: "leaps_inet_cfg_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps_inet_cfg_set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps_inet_cfg_set/"
order: 285
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-inet-cfg-set">
<span id="id1"></span><h1>leaps_inet_cfg_set</h1>
<p>Sets the local network interface mode: DHCP or static IP, and selects Ethernet or WiFi as the active interface.
The configuration is stored in non-volatile memory.
A system restart is required for the change to take effect.</p>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 78%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Byte 0 (flags): Bit 0 = is_static, Bit 1 = use_wifi, Bits[7:2] = reserved</div>
<div class="line"><br></div>
<div class="line-block">
<div class="line">- is_static: IP mode. 0 = DHCP (addr/netmask/gw ignored), 1 = static IP</div>
<div class="line">- use_wifi: Interface. 0 = Ethernet, 1 = WiFi</div>
<div class="line"><br></div>
</div>
<div class="line">Byte 1–3 (reserved): 0x00 0x00 0x00</div>
<div class="line">Byte 4–7 (addr): IPv4 address, little-endian uint32</div>
<div class="line">Byte 8–11 (netmask): IPv4 netmask, little-endian uint32</div>
<div class="line">Byte 12–15 (gw): IPv4 gateway, little-endian uint32</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x98</p></td>
<td><p>0x10</p></td>
<td><p>01 00 00 00 0A 01 A8 C0 00 FF FF FF 01 01 A8 C0</p></td>
</tr>
</tbody>
</table>
<p>In this example:</p>
<ul class="simple">
<li><p>Static IP is 192.168.1.10/24</p></li>
<li><p>Gateway is 192.168.1.1</p></li>
<li><p>via Ethernet (is_static=1, use_wifi=0)</p></li>
</ul>
<p>Type 0x98 (152) means command leaps_inet_cfg_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
</div>


           </div>
