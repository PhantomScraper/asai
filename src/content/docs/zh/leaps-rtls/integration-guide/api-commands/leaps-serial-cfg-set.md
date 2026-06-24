---
title: "leaps_serial_cfg_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set/"
order: 239
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-serial-cfg-set">
<span id="id1"></span><h1>leaps_serial_cfg_set</h1>
<p>启用/禁用UART接口上的事件。 在设置新值的情况下，此调用会写入内部非易失性存储器，因此不应频繁使用，在最坏的情况下可能需要数百毫秒！</p>
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
<li><p class="sd-card-text">uart_loc_ready_enable: 1-bit (<em>如果设置为‘1’，则在uart接口上启用位置就绪事件</em>)</p></li>
<li><p class="sd-card-text">usb_bh_en: 1-bit (<em>如果设置为‘1’，则启用USB接口用于回程</em>)</p></li>
<li><p class="sd-card-text">uart_mode: 1-bit (<em>‘0’表示uart复位后进入二进制模式，’1’表示uart重置后进入shell模式</em>)</p></li>
<li><p class="sd-card-text">uart_baudrate: ‘0’ | ‘1’ (<em>‘0’ = 115200 baud, ‘1’ = 1000000 baud</em>)</p></li>
<li><p class="sd-card-text">uart_loc_ready_include_my_pos: 1-bit (<em>0 禁用，1启用在每个位置就绪事件中包含我的位置</em>)</p></li>
<li><p class="sd-card-text">uart_loc_ready_include_ranging_pos: 1-bit (<em>0禁用，1启用在每个位置就绪事件中向测距节点包含位置</em>)</p></li>
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
<col style="width: 16%">
<col style="width: 21%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bits 18-31) 保留</div>
<div class="line">(bit 17) 位置就绪事件包括到测距节点的位置</div>
<div class="line">(bit 16) 位置就绪事件包括我的位置</div>
<div class="line">(bit 15)
uart_baudrate</div>
<div class="line">(bits 9-14) 保留</div>
<div class="line">(bit 8) uart_mode, 默认UART模式0-二进制，1-shell</div>
<div class="line">(bits 2-7) 保留</div>
<div class="line">(bit 1) USB回程启用</div>
<div class="line">启用时的（位0）位置就绪事件</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x38</p></td>
<td><p>0x04</p></td>
<td><p>0x01 0x00 0x01 0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x38(56 dec)表示命令leaps_serial_cfg_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
</div>


           </div>
