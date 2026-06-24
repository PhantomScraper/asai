---
title: "dwm_boot_cfg_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set/"
order: 171
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-boot-cfg-set">
<span id="id1"></span><h1>dwm_boot_cfg_set</h1>
<p>This call is available only on the ethernet gateway.
It sets the time for the device to stay in bootloader mode after reset.
The bootloader mode is used when doing firmware update using the serial interface.
The module will jump to normal operation after the time expires.
The firmware update can be initiated before the jump and the time can be set from
0 up to 4294967295 milliseconds.
However, it needs to be reset to take effect.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_boot_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_boot_cfg_set</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – boot_delay</p></li>
<li><p><strong>boot_delay</strong> – 32-bit unsigned integer (<em>the delay in milliseconds</em>)</p></li>
<li><p><strong>output</strong> – status_code</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value
1000 millisec</p></td>
</tr>
<tr class="row-odd"><td><p>0x26</p></td>
<td><p>0x04</p></td>
<td><p>0xE8 0x03 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x26 (38 dec) means command <a class="reference internal" href="#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Response</p></th>
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
