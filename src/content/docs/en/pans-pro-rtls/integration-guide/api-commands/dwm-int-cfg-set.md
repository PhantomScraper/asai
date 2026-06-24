---
title: "dwm_int_cfg_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-set/"
order: 195
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-int-cfg-set">
<span id="id1"></span><h1>dwm_int_cfg_set</h1>
<p>It enables or disables the setting of a dedicated GPIO pin in the event of an interrupt.
Additionally, interrupts or events are communicated to the user by setting the GPIO pin CORE_INT1.
Users can use this pin as a source for an external interrupt.
The interrupt can be processed by reading the status using dwm_status_get and reacting to the new status accordingly.
The status is cleared when read.
This call is available only on UART/SPI interfaces.
Normally, this call writes to internal flash when setting a new value, so it should not be used frequently, as it may take hundreds of milliseconds in the worst case!</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_int_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_int_cfg_set</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – spi_data_ready, loc_ready, bh_status_changed, bh_data_ready, bh_initialized_changed, uwb_scan_ready, usr_data_ready,    :param uwbmac_joined_changed</p></li>
<li><p><strong>spi_data_ready</strong> – ‘0’ | ‘1’ (<em>new SPI data generates interrupt on dedicated GPIO pin , 0=disable, 1=enable</em>)</p></li>
<li><p><strong>loc_ready</strong> – ‘0’ | ‘1’ (<em>interrupt is generated when location data are ready, 0=disable, 1=enable</em>)</p></li>
<li><p><strong>bh_status_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC status changed, 0=disable, 1=enable</em>)</p></li>
<li><p><strong>bh_data_ready</strong> – ‘0’ | ‘1’ (<em>UWBMAC backhaul data ready, 0=disable, 1=enable</em>)</p></li>
<li><p><strong>bh_initialized_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC route configured, 0=disable, 1=enable</em>)</p></li>
<li><p><strong>uwb_scan_ready</strong> – ‘0’ | ‘1’ (<em>UWB scan result is available</em>)</p></li>
<li><p><strong>usr_data_ready</strong> – ‘0’ | ‘1’ (<em>user data received over UWBMAC</em>)</p></li>
<li><p><strong>uwbmac_joined_changed</strong> – ‘0’ | ‘1’ (<em>UWBMAC joined, 0=disable, 1=enable</em>)</p></li>
<li><p><strong>usr_data_sent</strong> – ‘0’ | ‘1’ (<em>user data TX completed over UWBMAC</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<p>Not available in the on-module user application. Available only on external interfaces (SPI, UART)</p>
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 21%">
<col style="width: 21%">
<col style="width: 57%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Type</p></th>
<th class="head"><p>Length</p></th>
<th class="head"><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>0x34</p></td>
<td><p>0x02</p></td>
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
<tr class="row-odd"><td></td>
<td></td>
<td><p>0x0F 0x01</p></td>
</tr>
</tbody>
</table>
<p>Type 0x34 means command dwm_int_cfg_set</p>
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
<td><p>Value (see error
codes)</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
</div>
</div>


           </div>
