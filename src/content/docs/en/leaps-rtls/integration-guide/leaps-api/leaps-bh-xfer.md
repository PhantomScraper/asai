---
title: "leaps_bh_xfer"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer/"
order: 149
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-bh-xfer">
<span id="id1"></span><h1>leaps_bh_xfer</h1>
<p>Writes downlink data and reads uplink data chunks. The module must be
configured as a gateway node.</p>
<p>Both the uplink and the downlink data are encoded into the tlv frames when
transferred by SPI interface as described in <a class="reference external" href="#example-interrupt-leaps_bh_xfer">multiple TVL over
SPI</a>.</p>
<p>SPI master tells slave how many downlink bytes it wants to transfer by
<strong>downlink_byte_cnt</strong>. The <strong>downlink_byte_cnt</strong> is read by slave in the
first SPI transfer. Slave has some uplink data ready that it wants to
transfer to the master as it is reading the downlink. To
transfer both the downlink from the master to the slave and the uplink
from the slave to the master, the slave has to calculate how many bytes
and how many SPI transfers are needed. The master reads the number of
the bytes and the number of the transfers in the second SPI transfer, as
explained in <a class="reference external" href="#example-interrupt-leaps_bh_xfer">multiple TVL over SPI</a>. Finally, the transfers are
executed, and uplink and downlink are transferred. A Maximum number of
transfers currently supported is 5 with a maximum payload of 253 bytes, which
is 255 - size of(TLV header). At most, 5 uplink frames and at most 2
downlink frames are supported in one call to leaps_bh_xfer.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">downlink_byte_cnt: 16 bit unsigned integer (<em>number of downlink data bytes without TLV header, 506 bytes max</em>)</p></li>
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
<li><p class="sd-card-text">downlink_chunk: max 253 bytes (<em>opaque data send as downlink to the slave</em>)</p></li>
<li><p class="sd-card-text">output: 5 <em>[uplink_chunk]</em></p></li>
<li><p class="sd-card-text">uplink_chunk: max 253 bytes (<em>opaque data send as uplink to the master</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>UART example</strong></p>
<p>Not available on the UART interface.</p>
<p><strong>SPI example other than Gateway</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 13%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p>
<p>downlink_byte_cnt = size of downlink data (244
bytes)</p>
</td>
</tr>
<tr class="row-odd"><td><p>0x37</p></td>
<td><p>0x02</p></td>
<td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x37 means command leaps_bh_xfer</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>TLV response</p></th>
<th class="head"></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
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
<col style="width: 15%">
<col style="width: 13%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV
request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value
downlink_byte_cnt = size of downlink data (244
bytes)</p></td>
</tr>
<tr class="row-odd"><td><p>0x37</p></td>
<td><p>0x02</p></td>
<td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x37 means command leaps_bh_xfer</div>
</div>
<p>This call has a variable number of consecutive transfers, which follows the
TLV Request, see <a class="reference external" href="#example-interrupt-leaps_bh_xfer">API over SPI interface
description</a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 15%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV downlink nr.1,2, 3,4,5</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length
(244
bytes)</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x64</p></td>
<td><p>0xF4
(244)</p></td>
<td><p>down link data chunk
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
<col style="width: 48%">
<col style="width: 15%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV uplink nr.1,2,3,4,5</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length
(980
bytes)</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x6E</p></td>
<td><p>0xFD
(253)</p></td>
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
<td><p>0xDD
(221)</p></td>
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
<div class="section" id="bh-transfer-over-usb">
<h1>BH Transfer over USB</h1>
<p>BH data transfer over USB is different from that over SPI. SPI data
transfer is based on interrupt, but the interrupt line would not be available
for a USB connection between LEAPS RTLS device and PC, so instead of
using the  request-response approach with TLV_TYPE_CMD_BH_XFER TLV command,
for the USB interface, LEAPS RTLS device would actively send notifications
(TLV_TYPE_NOTIF_STATUS, TLV_TYPE_NOTIF_BH_STATUS) and uplink data chunks
to gateway master (PC). The notifications and uplink data could be
enabled/disabled, similar to interrupts using
<a class="reference external" href="#leaps_int_cfg_set">leaps_int_cfg_set</a></p>
</div>


           </div>
