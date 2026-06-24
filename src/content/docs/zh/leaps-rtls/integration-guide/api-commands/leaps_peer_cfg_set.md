---
title: "leaps_peer_cfg_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps_peer_cfg_set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps_peer_cfg_set/"
order: 287
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-peer-cfg-set">
<span id="id1"></span><h1>leaps_peer_cfg_set</h1>
<p>Sets the MQTT broker / peer server connection parameters including TLS options, port, and hostname.
The configuration is stored in non-volatile memory.
A network restart is triggered automatically after this command.</p>
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
<div class="line">Byte 0: flags</div>
<div class="line">- Bit 0=use_tls, Bit 1=mutual_auth, Bit 2=use_mac_filter,</div>
<div class="line">- Bit 3=auth_check_CN, Bits[7:4]=reserved</div>
<div class="line"><br></div>
<div class="line-block">
<div class="line">- use_tls: Enable TLS for the connection.</div>
<div class="line">- mutual_auth: Enable mutual TLS authentication (client cert required).</div>
<div class="line">- use_mac_filter: Enable MAC address filter.</div>
<div class="line">- auth_check_CN: Verify server Common Name (CN) in TLS certificate.</div>
<div class="line"><br></div>
</div>
<div class="line">Byte 1–2 (reserved): 0x00 0x00</div>
<div class="line">Byte 3–4 (port): little-endian uint16</div>
<div class="line">Byte 5 (host_len): number of host bytes that follow (no null)</div>
<div class="line">Byte 6..6+host_len-1 (host): ASCII string, no null terminator</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x9A</p></td>
<td><p>0x16</p></td>
<td><p>01 00 00 B3 22 10 6D 71 74 74 2E 65 78 61 6D 70 6C 65 2E 63 6F 6D</p></td>
</tr>
</tbody>
</table>
<p>In this example:</p>
<ul class="simple">
<li><p>LS enabled,</p></li>
<li><p>port 8883,</p></li>
<li><p>host “mqtt.example.com” (16 chars)</p></li>
</ul>
<p>Type 0x9A (154) means command leaps_peer_cfg_set</p>
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
