---
title: "leaps_wifi_cfg_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps_wifi_cfg_set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps_wifi_cfg_set/"
order: 289
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-wifi-cfg-set">
<span id="id1"></span><h1>leaps_wifi_cfg_set</h1>
<p>Sets the WiFi credentials (SSID and passphrase) and regulatory region.
The configuration is stored in non-volatile memory.
A system restart is required for the change to take effect.</p>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 80%">
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
<div class="line">Byte 0 (region): WiFi region code</div>
<div class="line">Byte 1–3 (reserved): 0x00 0x00 0x00</div>
<div class="line">Byte 4 (ssid_len): number of SSID bytes that follow</div>
<div class="line">Byte 5..5+ssid_len-1 (ssid): ASCII, no null</div>
<div class="line">Byte 5+ssid_len (psk_len): number of PSK bytes that follow</div>
<div class="line">Byte (5+ssid_len+1)..end (psk): ASCII, no null</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x9C</p></td>
<td><p>0x1C</p></td>
<td><p>00 00 00 00 09 4D 79 4E 65 74 77 6F 72 6B 0D 4D 79 50 61 73 73 77 6F 72 64 31 32 33</p></td>
</tr>
</tbody>
</table>
<p>In this example:</p>
<ul class="simple">
<li><p>region 0x00</p></li>
<li><p>SSID “MyNetwork” (9 bytes)</p></li>
<li><p>PSK “MyPassword123” (13 bytes)</p></li>
</ul>
<p>Type 0x9C (156) means command leaps_wifi_cfg_set</p>
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
