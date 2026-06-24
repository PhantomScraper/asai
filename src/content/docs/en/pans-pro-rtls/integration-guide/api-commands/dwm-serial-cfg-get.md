---
title: "dwm_serial_cfg_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-serial-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-serial-cfg-get/"
order: 209
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-serial-cfg-get">
<span id="id1"></span><h1>dwm_serial_cfg_get</h1>
<p>This command is available only on the ethernet gateway. Gets UART/USB interface configuration.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_serial_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_serial_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">mode</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>none</em>)</p></li>
<li><p><strong>output</strong> – status_code, mode</p></li>
<li><p><strong>mode</strong> – ‘0’ | ‘1’ (<em>0 - binary mode , 1 - shell mode</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<p>Not available in the on-module user application.</p>
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
<tr class="row-odd"><td><p>0x39</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x39 (57) means command dwm_serial_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 11%">
<col style="width: 10%">
<col style="width: 9%">
<col style="width: 11%">
<col style="width: 39%">
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
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x61</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><div class="line-block">
<div class="line">byte 0: reserved</div>
<div class="line">byte 1: UART/USB mode</div>
<div class="line">byte 2: reserved</div>
<div class="line">byte 3: reserved</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x00 0x10 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means status code</div>
<div class="line">Type 0x61 (97) means serial configuration</div>
</div>
</div>


           </div>
