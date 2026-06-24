---
title: "dwm_backhaul_xfer"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm_backhaul_xfer"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm_backhaul_xfer/"
order: 223
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-backhaul-xfer">
<span id="id1"></span><h1>dwm_backhaul_xfer</h1>
<p>Writes downlink data and reads uplink data chunks. The DWM module must be configured as a gateway.
The uplink and the downlink data are encoded into TLV frames and transferred by the SPI interface as described in.
The SPI master tells the slave how many downlink bytes it wants to transfer by <strong>downlink_byte_cnt</strong>.
The <strong>downlink_byte_cnt</strong> is read by the slave in the first SPI transfer.
The slave has some uplink data ready to transfer to the master as it reads the downlink.
To transfer both the downlink from the master to the slave and the uplink from the slave to the master,
the slave has to calculate how many bytes and SPI transfers are needed.
The master reads the number of the bytes and the number of the transfers in the second SPI transfer.
Finally, the transfers are executed and both uplink and downlink are transferred.
The maximum number of transfers currently supported is 5 with a maximum payload of 253 bytes, which is 255 - size of(TLV header).
At most, 5 uplink frames and 2 downlink frames are supported in one call to <a class="reference internal" href="#dwm-backhaul-xfer"><span class="std std-ref">dwm_backhaul_xfer</span></a>.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_backhaul_xfer">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_backhaul_xfer</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint16_t</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – downlink_byte_cnt, {downlink_chunk}</p></li>
<li><p><strong>downlink_byte_cnt</strong> – 16 bit unsigned integer (<em>number of downlink data bytes without TLV header, 506 bytes max</em>)</p></li>
<li><p><strong>downlink_chunk</strong> – max 253 bytes (<em>opaque data send as downlink to the slave, up to 2 chunks</em>)</p></li>
<li><p><strong>output</strong> – {uplink_chunk} (<em>up to 5 chunk of uplink data</em>)</p></li>
<li><p><strong>uplink_chunk</strong> – max 253 bytes (<em>opaque data send as uplink to the master</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<p>Not available for the user application.</p>
<p><strong>UART example</strong></p>
<p>Not available on the UART interface.</p>
<p><strong>SPI example other than Gateway</strong></p>
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
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x37</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>downlink_byte_cnt
= size of downlink
data (244 bytes)</p></td>
</tr>
<tr class="row-even"><td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x37 means command dwm_backhaul_xfer</p>
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
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p><strong>SPI example Gateway</strong></p>
<div class="line-block">
<div class="line">Downlink bytes count: 244</div>
<div class="line">Uplink bytes count: 980</div>
</div>
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
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x37</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>downlink_byte_cnt
= size of
downlink data
(244 bytes)</p></td>
</tr>
<tr class="row-even"><td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x37 means command dwm_backhaul_xfer</div>
</div>
<p>This call has a variable number of consecutive transfers that follow the TLV Request. See API over SPI interface description..</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p><strong>TLV downlink nr.1,2,3,4,5</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length
<strong>(244 bytes)</strong></p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x64</p></td>
<td><p>0xF4 (244)</p></td>
<td><p>downlink data chunk
nr.1</p></td>
</tr>
<tr class="row-even"><td><p>0x65</p></td>
<td><p>0x00</p></td>
<td><p>empty</p></td>
</tr>
<tr class="row-odd"><td><p>0x66</p></td>
<td><p>0x00</p></td>
<td><p>empty</p></td>
</tr>
<tr class="row-even"><td><p>0x67</p></td>
<td><p>0x00</p></td>
<td><p>empty</p></td>
</tr>
<tr class="row-odd"><td><p>0x68</p></td>
<td><p>0x00</p></td>
<td><p>empty</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p><strong>TLV uplink nr.1,2,3,4,5</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length
<strong>(980 bytes)</strong></p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x6E</p></td>
<td><p>0xFD (253)</p></td>
<td><p>uplink data chunk
nr.1</p></td>
</tr>
<tr class="row-even"><td><p>0x6F</p></td>
<td><p>0xFD</p></td>
<td><p>uplink data chunk
nr.2</p></td>
</tr>
<tr class="row-odd"><td><p>0x70</p></td>
<td><p>0xFD</p></td>
<td><p>uplink data chunk
nr.3</p></td>
</tr>
<tr class="row-even"><td><p>0x71</p></td>
<td><p>0xDD (22#.</p></td>
<td><p>uplink data chunk
nr.4</p></td>
</tr>
<tr class="row-odd"><td><p>0x72</p></td>
<td><p>0x00</p></td>
<td><p>empty</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x64 means downlink data chunk nr.1</div>
<div class="line">Type 0x65 means downlink data chunk nr.2</div>
<div class="line">…</div>
<div class="line">Type 0x68 means downlink data chunk nr.5</div>
<div class="line">Type 0x6E means uplink data chunk nr.1</div>
<div class="line">Type 0x6F means uplink data chunk nr.2</div>
<div class="line">…</div>
<div class="line">Type 0x72 means uplink data chunk nr.5</div>
</div>
</div>


           </div>
