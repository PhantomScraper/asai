---
title: "leaps_status_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-status-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-status-get/"
order: 280
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-status-get">
<span id="id1"></span><h1>leaps_status_get</h1>
<p>获取系统状态标志. 状态标志可以通过以下方式启用CORE_INT GPIO引脚的设置 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a>. 调用leaps_status_get后，所有状态标志都会被清除，但以下标志除外：</p>
<blockquote>
<div><ul class="simple">
<li><p>ble_conn_state</p></li>
<li><p>uwbmac_joined</p></li>
<li><p>bh_initialized</p></li>
<li><p>distance_alarm_th_1</p></li>
<li><p>distance_alarm_th_1</p></li>
</ul>
</div></blockquote>
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
<li><p class="sd-card-text">status: loc_ready, uwbmac_joined, bh_data_ready, bh_initialized, bh_status_changed, uwb_scan_ready, uwb_usr_data_ready, uwb_usr_data_sent, fwup_in_progress, proxy_pos_ready, ble_usr_data_ready, ble_usr_data_sent, ble_conn_state, distance_alarm_th_1,distance_alarm_th_2</p></li>
<li><p class="sd-card-text">loc_ready: ‘0’ | ‘1’ (<em>新位置数据已准备就绪</em>)</p></li>
<li><p class="sd-card-text">uwbmac_joined: ‘0’ | ‘1’ (<em>节点已连接到UWB网络</em>)</p></li>
<li><p class="sd-card-text">bh_data_ready: ‘0’ | ‘1’ (<em>UWB MAC回程数据就绪</em>)</p></li>
<li><p class="sd-card-text">bh_status_changed: ‘0’ | ‘1’ (<em>UWB MAC状态已更改，用于回程</em>)</p></li>
<li><p class="sd-card-text">bh_initialized: ‘0’ | ‘1’ (<em>节点已通过UWB回程初始化路由</em>)</p></li>
<li><p class="sd-card-text">uwb_scan_ready: ‘0’ | ‘1’ (<em>UWB扫描结果已就绪</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_ready: ‘0’ | ‘1’ (<em>通过UWB接收到的用户数据</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_sent: ‘0’ | ‘1’ (<em>通过UWB发送的用户数据</em>)</p></li>
<li><p class="sd-card-text">fwup_in_progress: ‘0’ | ‘1’ (<em>固件更新正在进行中</em>)</p></li>
<li><p class="sd-card-text">proxy_pos_ready: ‘0’ | ‘1’ (<em>代理位置已就绪，用户应用程序中不支持</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_ready: ‘0’ | ‘1’ (<em>接收到ble上的用户数据，用户应用程序中不支持</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_sent: ‘0’ | ‘1’ (<em>用户数据通过ble发送，用户应用程序不支持</em>)</p></li>
<li><p class="sd-card-text">ble_conn_state: ‘0’ | ‘1’ (<em>用户应用程序中不支持</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_1: ‘0’ | ‘1’ (<em>阈值1的距离报警</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_2: ‘0’ | ‘1’ (<em>阈值2的距离报警</em>)</p></li>
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
<tr class="row-odd"><td><p>0x32</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x32表示命令leaps_status_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 7%">
<col style="width: 35%">
<col style="width: 35%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="2"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bit 0) loc_ready</div>
<div class="line">(bit 1) uwbmac_joined</div>
<div class="line">(bit 2) bh_status_changed</div>
<div class="line">(bit 3) bh_data_ready</div>
<div class="line">(bit 3) bh_data_ready</div>
<div class="line">(bit 5) uwb_scan_ready</div>
<div class="line">(bit 6) uwb_usr_data_ready</div>
<div class="line">(bit 7) uwb_usr_data_sent</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bit 8) fwup_in_progress</div>
<div class="line">(bit 9) proxy_pos_ready</div>
<div class="line">(bit 10) ble_usr_data_ready</div>
<div class="line">(bit 11) ble_usr_data_sent</div>
<div class="line">(bit 12) ble_conn_state</div>
<div class="line">(bit 13) distance_alarm_th_1</div>
<div class="line">(bit 14) distance_alarm_th_2</div>
<div class="line">(bit 15) 保留</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5A</p></td>
<td><p>0x02</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x5A表示状态</p>
<p>类型 0x40 表示状态代码</p>
</div>


           </div>
