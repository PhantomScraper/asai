---
title: "dwm_boot_cfg_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-get/"
order: 170
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-boot-cfg-get">
<span id="id1"></span><h1>dwm_boot_cfg_get</h1>
<p>This call is available only on the ethernet gateway. Get the
bootloader configuration. Refer to <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a> for more
information.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_boot_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_boot_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>none</em>)</p></li>
<li><p><strong>output</strong> – status_code, boot_delay</p></li>
<li><p><strong>boot_delay</strong> – 32-bit unsigned integer (<em>the delay in milliseconds</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
</tr>
<tr class="row-odd"><td><p>0x27</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x27 (39) means command <a class="reference internal" href="#dwm-boot-cfg-get"><span class="std std-ref">dwm_boot_cfg_get</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
<td><p>Type</p></td>
<td><p>length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x60</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>The
booting
delay in
mill
iseconds</p></td>
</tr>
<tr class="row-even"><td><p>0xB8 0x0B
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means status code</div>
<div class="line">Type 0x60 (96) means bootloader configuration</div>
</div>
</div>


           </div>
