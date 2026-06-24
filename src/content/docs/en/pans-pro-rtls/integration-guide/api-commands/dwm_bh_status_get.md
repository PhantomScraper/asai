---
title: "dwm_bh_status_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm_bh_status_get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm_bh_status_get/"
order: 165
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-bh-status-get">
<span id="id1"></span><h1>dwm_bh_status_get</h1>
<p>Gets the current UWBMAC backhaul status. The node must be configured as a gateway.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_bh_status_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_bh_status_get</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>none</em>)</p></li>
<li><p><strong>output</strong> – sf_number, bh_seat_map, origin_cnt, {origin_info}</p></li>
<li><p><strong>sf_number</strong> – 16-bit integer (<em>current superframe number</em>)</p></li>
<li><p><strong>bh_seat_map</strong> – 32-bit integer (<em>seat map in the current superframe</em>)</p></li>
<li><p><strong>origin_cnt</strong> – 8-bit integer (<em>range is from 0 to 8</em>)</p></li>
<li><p><strong>origin_info</strong> – node_id, bh_seat, hop_lvl (<em>element in the list of origins</em>)</p></li>
<li><p><strong>node_id</strong> – 16-bit integer (<em>origin address</em>)</p></li>
<li><p><strong>bh_seat</strong> – 8-bit integer (<em>seat that the origin occupies, range from 0 to 8</em>)</p></li>
<li><p><strong>hop_lvl</strong> – 8-bit integer (<em>hop level</em>)</p></li>
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
<tr class="row-odd"><td><p>0x3A</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x3A means command dwm_bh_status_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 12%">
<col style="width: 39%">
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
<div class="line">(2 bytes) sf_number</div>
<div class="line">(4 bytes) bh_seat_map</div>
<div class="line">(1 byte) origin_cnt</div>
<div class="line">(N*4 bytes) N*origin_info</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5D</p></td>
<td><p>0x13</p></td>
<td><p>0x6c 0x00
0x07 0x00
0x00 0x00
0x03
0xf3 0x11
0x00 0x01
0xc3 0x11
0x01 0x01
0x66 0x11
0x02 0x01</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
<div class="line">Type 0x5D means UWBMAC status</div>
</div>
</div>


           </div>
