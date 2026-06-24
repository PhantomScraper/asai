---
title: "leaps_serial_cfg_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-get/"
order: 251
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-serial-cfg-get">
<span id="id1"></span><h1>leaps_serial_cfg_get</h1>
<p>Reads current configuration of the serial interfaces (e.g. UART, SPI).</p>
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
<li><p class="sd-card-text">uart_mode: 1-bit (<em>‘0’ means that UART enters binary mode after reset, ‘1’ means that UART enters Command Line Interface (CLI) mode after reset</em>)</p></li>
<li><p class="sd-card-text">uart_baudrate: ‘0’ | ‘1’ (<em>‘0’: 115200 baud, ‘1’: 1000000 baud</em>)</p></li>
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
<col style="width: 52%">
<col style="width: 48%">
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
<p>Type 0x39 (57 dec) means command leaps_serial_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 6%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 8%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bits 18-31) r eserved</div>
<div class="line">(bit 17) location ready event includes positions to ranging nodes</div>
<div class="line">(bit 16) location ready event includes my position</div>
<div class="line">(bit 15) uart_baudrate</div>
<div class="line">(bits 9-14) reserved</div>
<div class="line">(bit 8) uar t_mode, default UART mode 0-binary, 1-shell</div>
<div class="line">(bits 2-7) reserved</div>
<div class="line">(bit 1) USB backhaul enable</div>
<div class="line">(bit 0) location ready event on UART enable</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x61</p></td>
<td><p>0x04</p></td>
<td><p>0x01
0x01
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x61 (97) means serial interfaces configuration</p>
</div>


           </div>
