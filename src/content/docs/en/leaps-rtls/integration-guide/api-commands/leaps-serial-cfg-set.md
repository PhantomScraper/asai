---
title: "leaps_serial_cfg_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set/"
order: 240
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-serial-cfg-set">
<span id="id1"></span><h1>leaps_serial_cfg_set</h1>
<p>Enables/disables events on the UART interface. This call does a write to
internal non-volatile memory in case of new value being set, hence
should not be used frequently and can take up to hundreds of
milliseconds in the worst case!</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">(<em>none</em>)</p></li>
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
<li><p class="sd-card-text">uart_loc_ready_enable: 1-bit (<em>enables location ready event on UART interface if set to ‘1’</em>)</p></li>
<li><p class="sd-card-text">usb_bh_en: 1-bit (<em>enables USB interface for backhaul if set to ‘1’</em>)</p></li>
<li><p class="sd-card-text">uart_mode: 1-bit (<em>‘0’ means that UART enters binary mode after reset, ‘1’ means that UART enters shell mode after reset</em>)</p></li>
<li><p class="sd-card-text">uart_baudrate: ‘0’ | ‘1’ (<em>‘0’ = 115200 baud, ‘1’ = 1000000 baud</em>)</p></li>
<li><p class="sd-card-text">uart_loc_ready_include_my_pos: 1-bit (<em>0 disables and 1 enables including of my position in each location ready event</em>)</p></li>
<li><p class="sd-card-text">uart_loc_ready_include_ranging_pos: 1-bit (<em>0 disables and 1 enables including of positions to the ranging nodes in each location ready event</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 21%">
<col style="width: 63%">
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
<div class="line">(bits 18-31)
reserved</div>
<div class="line">(bit 17) location
ready event
includes positions
to ranging nodes</div>
<div class="line">(bit 16) location
ready event
includes my
position</div>
<div class="line">(bit 15)
uart_baudrate</div>
<div class="line">(bits 9-14)
reserved</div>
<div class="line">(bit 8) uart_mode,
default UART mode
0-binary, 1-shell</div>
<div class="line">(bits 2-7) reserved</div>
<div class="line">(bit 1) USB backhaul
enable</div>
<div class="line">(bit 0) location
ready event on UART
enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x38</p></td>
<td><p>0x04</p></td>
<td><p>0x01 0x00 0x01 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x38 (56 dec) means command leaps_serial_cfg_set</p>
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
