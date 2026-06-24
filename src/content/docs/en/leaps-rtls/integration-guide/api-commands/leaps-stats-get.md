---
title: "leaps_stats_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-stats-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-stats-get/"
order: 284
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-stats-get">
<span id="id1"></span><h1>leaps_stats_get</h1>
<p>Get statistics.</p>
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
<li><p class="sd-card-text">statistics: 204 bytes</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 23%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>Statistics (in order)</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Size
(bytes)</p></td>
<td rowspan="2"><p>Name</p></td>
</tr>
<tr class="row-odd"></tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>uptime</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>memfree</p></td>
</tr>
<tr class="row-even"><td><p>float</p></td>
<td><p>4</p></td>
<td><p>drift_avg_rtc</p></td>
</tr>
<tr class="row-odd"><td><p>int16_t</p></td>
<td><p>2</p></td>
<td><p>mcu_temp</p></td>
</tr>
<tr class="row-even"><td><p>uint8_t</p></td>
<td><p>1</p></td>
<td><p>api_err_cnt</p></td>
</tr>
<tr class="row-odd"><td><p>uint8_t</p></td>
<td><p>1</p></td>
<td><p>api_dl_cnt</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>ble_con_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>ble_dis_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>ble_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>clk_sync</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>uwb_intr</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>uwb_rst</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>uwb_bpc</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>rx_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>rx_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>tx_err</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>tx_errx</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>reinit</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>alma_tx_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>alma_rx_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>alma_tx_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>bcn_tx_err</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bcn_tx_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bcn_rx_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>cl_tx_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>cl_rx_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>cl_coll</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>fwup_tx_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>fwup_tx_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>fwup_rx_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>svc_tx_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>svc_tx_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>svc_rx_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>bh_ev</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bh_rt</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bh_nort</p></td>
</tr>
<tr class="row-even"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>bh_buf_lost[0]</p></td>
</tr>
<tr class="row-odd"><td><p>uint16_t</p></td>
<td><p>2</p></td>
<td><p>bh_buf_lost[1]</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bh_tx_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bh_dl_err</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bh_dl_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bh_ul_err</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>bh_ul_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>fw_dl_tx_err</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>fw_dl_iot_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>fw_ul_loc_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>fw_ul_iot_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>ul_tx_err</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>dl_iot_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>ul_loc_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>ul_iot_ok</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>enc_err</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>ani_ses_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>tdoa_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>tdoa_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>twr_ok</p></td>
</tr>
<tr class="row-even"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>twr_err</p></td>
</tr>
<tr class="row-odd"><td><p>uint32_t</p></td>
<td><p>4</p></td>
<td><p>le_err</p></td>
</tr>
<tr class="row-even"><td><p>int32_t</p></td>
<td><p>4</p></td>
<td><p>res[0]</p></td>
</tr>
<tr class="row-odd"><td><p>int32_t</p></td>
<td><p>4</p></td>
<td><p>res[1]</p></td>
</tr>
<tr class="row-even"><td><p>int32_t</p></td>
<td><p>4</p></td>
<td><p>res[2]</p></td>
</tr>
<tr class="row-odd"><td><p>int32_t</p></td>
<td><p>4</p></td>
<td><p>res[3]</p></td>
</tr>
<tr class="row-even"><td><p>int32_t</p></td>
<td><p>4</p></td>
<td><p>res[4]</p></td>
</tr>
<tr class="row-odd"><td><p>int32_t</p></td>
<td><p>4</p></td>
<td><p>res[5]</p></td>
</tr>
</tbody>
</table>
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
</tr>
<tr class="row-odd"></tr>
<tr class="row-even"><td><p>0x96</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x96 means command leaps_stats_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 46%">
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
<tr class="row-odd"><td><p>Statistics (204 byte)</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x80</p></td>
<td><p>0xCC</p></td>
<td><p>0xBE 0x0D 0x00 …. 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code
Type 0x80 means statistics</p>
</div>


           </div>
