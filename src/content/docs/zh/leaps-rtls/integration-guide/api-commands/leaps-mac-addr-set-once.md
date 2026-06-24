---
title: "leaps_mac_addr_set_once"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once/"
order: 257
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-set-once">
<span id="id1"></span><h1>leaps_mac_addr_set_once</h1>
<p>将MAC地址列表写入OTP存储器，必须小心使用！值写入后不能修改！它旨在用于生产阶段，为UWB, BLE, 以太网或Wi-Fi接口使用的设备提供MAC地址池。 目前，MAC地址列表被分配给各种接口，如下所示：</p>
<ul class="simple">
<li><p>MAC地址0已分配给UWB接口。 两个最低有效字节不得等于0x0000或0xFFFF。</p></li>
<li><p>MAC 地址 1 已分配给 BLE 接口. 该地址将用作公共 BLE 地址。</p></li>
<li><p>MAC地址2和MAC地址3分别分配给以太网和Wi-Fi接口. 地址应采用EUI-48格式，尊重LAA/UAA位和U/I位。</p></li>
</ul>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">mac_addr_0:48位值（<em>小端序的UWB mac地址</em>）</p></li>
<li><p class="sd-card-text">mac_addr_1:48位值（<em>小端序的BLE mac地址</em>）</p></li>
<li><p class="sd-card-text">mac_addr_2: 48位值(<em>小端序以太网MAC地址</em>)</p></li>
<li><p class="sd-card-text">mac_addr_3:48位值（<em>小端序WIFI MAC地址</em>）</p></li>
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
<p>SPI/UART 示例</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 17%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x82</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(字节0-5) MAC 地址 0，小端序</div>
<div class="line">(字节6-11) MAC 地址 1，小端序</div>
<div class="line">(字节12-17) MAC 地址 2，小端序</div>
<div class="line">(字节18-23) MAC 地址 3，小端序</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>…</p></td>
</tr>
</tbody>
</table>
<p>类型 0x82（130 dec）表示命令 <a class="reference internal" href="#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x40 表示上一条命令的 err_code</p>
</div>


           </div>
