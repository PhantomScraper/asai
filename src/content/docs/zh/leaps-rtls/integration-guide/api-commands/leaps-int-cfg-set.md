---
title: "leaps_int_cfg_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set/"
order: 147
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-int-cfg-set">
<span id="id1"></span><h1>leaps_int_cfg_set</h1>
<p>在发生事件时启用/禁用专用GPIO引脚的设置。 中断/事件通过设置GPIO引脚CORE_INT传达给用户。 用户可以将该引脚用作外部中断的来源。 可以通过读取状态（leaps_status_get）并根据新状态做出反应来处理中断。 读取后，状态会自动清除。 此调用在设置新值时写入内部闪存，因此不应频繁使用，最坏的情况下可能需要数百毫秒！</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">spi_data_ready: ‘0’ | ‘1’ (<em>新的SPI数据就绪事件, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">loc_ready: ‘0’ | ‘1’ (<em>新位置数据就绪事件, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">bh_status_changed: ‘0’ | ‘1’ (<em>UWBMAC状态已更改, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">bh_data_ready: ‘0’ | ‘1’ (<em>UWBMAC 回程数据就绪, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">bh_initialized_changed: ‘0’ | ‘1’ (<em>已配置UWBMAC路由, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">uwb_scan_ready: ‘0’ | ‘1’ (<em>UWB 扫描结果可用</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_ready: ‘0’ | ‘1’ (<em>通过UWBMAC接收新用户数据时的事件, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">uwbmac_joined_changed: ‘0’ | ‘1’ (<em>UWBMAC已加入事件, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_sent: ‘0’ | ‘1’ (<em>用户数据传输已通过UWBMAC完成, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">proxy_pos_ready: ‘0’ | ‘1’ (<em>代理位置就绪时的事件,  0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_ready: ‘0’ | ‘1’ (<em>在BLE上接收用户数据时发生的事件, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_sent: ‘0’ | ‘1’ (<em>通过BLE发送用户数据时的事件, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">ble_conn_state_changed: ‘0’ | ‘1’ (<em>BLE连接状态更改时的事件, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_1: ‘0’ | ‘1’ (<em>阈值1发生距离报警时的事件, 0=禁用, 1=启用</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_2: ‘0’ | ‘1’ (<em>阈值2发生距离报警时的事件, 0=禁用, 1=启用</em>)</p></li>
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
<col style="width: 19%">
<col style="width: 19%">
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
<div class="line">(bit 15) 保留</div>
<div class="line">(bit 14) distance_alarm_th_2</div>
<div class="line">(bit 13) distance_alarm_th_1</div>
<div class="line">(bit 12) ble_conn_state_changed</div>
<div class="line">(bit 11) ble_usr_data_sent</div>
<div class="line">(bit 10) ble_usr_data_ready</div>
<div class="line">(bit 9) proxy_pos_ready</div>
<div class="line">(bit 8) uwb_usr_data_sent</div>
<div class="line">(bit 7) uwbmac_joined_changed</div>
<div class="line">(bit 6) uwb_usr_data_ready</div>
<div class="line">(bit 5) uwb_scan_ready</div>
<div class="line">(bit 4) bh_initialize d_changed</div>
<div class="line">(bit 3) bh_data_ready</div>
<div class="line">(bit 2) bh_status_changed</div>
<div class="line">(bit 1) spi_data_ready</div>
<div class="line">(bit 0) loc_ready</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x34</p></td>
<td><p>0x02</p></td>
<td><p>0x0F 0x01</p></td>
</tr>
</tbody>
</table>
<p>类型0x34表示命令 leaps_int_cfg_set</p>
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
