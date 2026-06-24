---
title: "leaps_dev_status_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-dev-status-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-dev-status-get/"
order: 276
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dev-status-get">
<span id="id1"></span><h1>leaps_dev_status_get</h1>
<p>读取设备状态信息。</p>
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
<li><p class="sd-card-text">uptime:32位无符号整数（<em>以秒为单位的设备正常运行时间</em>）</p></li>
<li><p class="sd-card-text">temperature: 16 位带符号整数（<em>温度，摄氏度</em>）。</p></li>
<li><p class="sd-card-text">battery_voltage: 16位无符号整数（<em>电池电压，单位为毫伏</em>）</p></li>
<li><p class="sd-card-text">battery_state: 4-bits (电池状态 = NO_BATTERY: 0,  充电: 1, 已充电: 2, 放电: 3, VBAT_LOW: 4, VBAT_EMPTY= 5)</p></li>
<li><p class="sd-card-text">battery_level: 7位无符号整数（<em>电池电量百分比</em>）</p></li>
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
<tr class="row-odd"><th class="head"><p>TLV 请求</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0x25</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x25（12月37日）表示命令leaps_dev_status_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 15%">
<col style="width: 29%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="3"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>正常运行时间</p></td>
<td><p>温度</p></td>
<td><div class="line-block">
<div class="line">battery:</div>
<div class="line">（字节0-1）电压</div>
<div class="line">（字节2）级别</div>
<div class="line">（字节3）状态</div>
<div class="line">（字节4-5）保留</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x59</p></td>
<td><p>0x0C</p></td>
<td><p>0x2C
0x00
0x00
0x00</p></td>
<td><p>0x22
0x00</p></td>
<td><p>0x2d 0x0f 0x3e</p>
<p>0x01 0x00 0x00</p>
</td>
</tr>
</tbody>
</table>
<p>类型0x40(64 dec)表示状态代码</p>
<p>类型 0x59 (89 dec) 表示设备状态</p>
</div>


           </div>
