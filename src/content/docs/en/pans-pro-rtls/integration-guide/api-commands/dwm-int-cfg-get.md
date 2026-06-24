---
title: "dwm_int_cfg_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-get/"
order: 194
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-int-cfg-get">
<span id="id1"></span><h1>dwm_int_cfg_get</h1>
<p>Reads configuration flags that, if set, enable the setting of a dedicated GPIO pin (CORE_INT) in the event of an internal event within the DWM module.</p>
<p>This call is available only on UART/SPI interfaces.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_int_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_int_cfg_get</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>none</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, spi_data_ready, loc_ready, bh_status_changed, bh_data_ready bh_initialized_changed, uwb_scan_ready, usr_data_ready,    :param uwbmac_joined_changed</p></li>
<li><p><strong>spi_data_ready</strong> – ‘0’ | ‘1’ (<em>new SPI data generates interrupt on dedicated GPIO pin , 0=disable, 1=enable</em>)</p></li>
<li><p><strong>loc_ready</strong> – ‘0’ | ‘1’ (<em>interrupt is generated when location data are ready, 0=disable, 1=enable</em>)</p></li>
<li><p><strong>bh_status_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC status changed, 0=disable, 1=enable</em>)</p></li>
<li><p><strong>bh_data_ready</strong> – ‘0’ | ‘1’ (<em>UWBMAC backhaul data ready, 0=disable, 1=enable</em>)</p></li>
<li><p><strong>bh_initialized_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC route configured, 0=disabled, 1=enabled</em>)</p></li>
<li><p><strong>usr_data_ready</strong> – ‘0’ | ‘1’ (<em>user data received over UWBMAC</em>)</p></li>
<li><p><strong>uwb_scan_ready</strong> – ‘0’ | ‘1’ (<em>UWB scan result is available</em>)</p></li>
<li><p><strong>uwbmac_joined_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC joined, 0=disabled, 1=enabled</em>)</p></li>
<li><p><strong>usr_data_sent</strong> – ‘0’ | ‘1’ (<em>user data TX completed over UWBMAC</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<p>Not available in the on-module user application. Available only on external interfaces (SPI, UART)</p>
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
<tr class="row-odd"><td><p>0x35</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x35 means command <a class="reference internal" href="#dwm-int-cfg-get"><span class="std std-ref">dwm_int_cfg_get</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>length</p></td>
<td><p>Value
(see
error
codes)</p></td>
<td><p>Type</p></td>
<td><p>length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x47</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><div class="line-block">
<div class="line">interrupt configuration flags:</div>
<div class="line">reserved (bits 9-15)</div>
<div class="line">usr_data_sent (bit 8)</div>
<div class="line">uwbmac_joined_changed (bit 7)</div>
<div class="line">usr_data_ready (bit 6)</div>
<div class="line">uwb_scan_ready (bit 5)</div>
<div class="line">bh_initialized_changed (bit 4)</div>
<div class="line">bh_data_ready (bit 3)</div>
<div class="line">bh_status_changed (bit 2)</div>
<div class="line">spi_data_ready (bit 1)</div>
<div class="line">loc_ready (bit 0)</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x0E 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x47 means interrupt configuration</div>
</div>
</div>


           </div>
