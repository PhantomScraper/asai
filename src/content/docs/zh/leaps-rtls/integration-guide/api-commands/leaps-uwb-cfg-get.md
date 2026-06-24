---
title: "leaps_uwb_cfg_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-get/"
order: 274
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-cfg-get">
<span id="id1"></span><h1>leaps_uwb_cfg_get</h1>
<p>获取 UWB 配置参数。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">(<em>无</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输出</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a></p></li>
<li><p class="sd-card-text">preamble_code: ‘9’ | ‘10’ | ‘11’ | ‘12’ (<em>UWB前置码</em>)</p></li>
<li><p class="sd-card-text">pg_delay: 1 字节(<em>发射机校准脉冲发生器延迟值</em>)</p></li>
<li><p class="sd-card-text">channel: ‘2’ | ‘3’ | ‘5’ | ‘9’ (<em>UWB 频道</em>)</p></li>
<li><p class="sd-card-text">lna_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">pa_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf1_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf2_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">tx_power: 4 字节(<em>传输功率控制单位</em>)</p></li>
<li><p class="sd-card-text">rf_compliance: ‘0’ | ‘1’ | ‘2’ (<em>射频兼容性选项, 0: FCC/ETSI, 1: ETSI + 10dB, 2: ARIB, 3: 自定义</em>)</p></li>
<li><p class="sd-card-text">pg_delay_comp: 1字节 (<em>发射机校准脉冲发生器延迟值，已补偿</em>)</p></li>
<li><p class="sd-card-text">tx_power_comp: 4 字节 (<em>传输功率控制单位，补偿</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 52%">
<col style="width: 48%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0x18</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x18（12月24日）表示命令leaps_uwb_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(第1字节) preamble_code</div>
<div class="line">(第2字节) pg_delay</div>
<div class="line">(第3字节) channel</div>
<div class="line">(第3字节, bit 0) lna_enable</div>
<div class="line">(第4字节, bit 1) pa_enable</div>
<div class="line">(第4字节, bit 2) rf1_enable</div>
<div class="line">(第4字节, bit 3) rf2_enable</div>
<div class="line">(第4字节, bits 4-8) 保留</div>
<div class="line">(第5至第8字节) tx_power</div>
<div class="line">(第9字节) rf_compliance</div>
<div class="line">(第10字节) pg_dela_comp</div>
<div class="line">(第11至第12字节) 保留</div>
<div class="line">(第13至第16字节) tx_power_comp</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x4F</p></td>
<td><p>0x10</p></td>
<td><p>0x09 0x34 0x05 0x03 0xfd 0xfd 0xfd 0xfd
0x00 0x34 0x00 0x00 0xfd 0xfd 0xfd 0xfd</p></td>
</tr>
</tbody>
</table>
<p>类型 0x4F 表示 UWB 配置</p>
</div>


           </div>
