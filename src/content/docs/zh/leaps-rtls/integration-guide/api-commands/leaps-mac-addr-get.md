---
title: "leaps_mac_addr_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-get/"
order: 255
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-get">
<span id="id1"></span><h1>leaps_mac_addr_get</h1>
<p>获取 MAC 地址列表. 设备使用用户指定的地址或默认地址. 每个接口的默认 MAC 地址只能通过调用 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a> 更改一次，更改后的地址将写入 OTP 内存并成为新的默认 MAC 地址. 用户可以通过调用 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set#leaps-mac-addr-set"><span class="std std-ref">leaps_mac_addr_set</span></a> 设置自定义 MAC 地址. 用户修改默认 MAC 地址后，可通过出厂重置恢复（参见 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-factory-reset#leaps-factory-reset"><span class="std std-ref">leaps_factory_reset</span></a>）. MAC 地址与特定接口的映射是基于列表中的顺序，如下所示：</p>
<ol class="arabic simple">
<li><p>UWB</p></li>
<li><p>BLE</p></li>
<li><p>以太网</p></li>
<li><p>无线网络</p></li>
</ol>
<p>BLE 地址可以是随机 BLE 地址或公共 BLE 地址. 如果不支持特定接口，列表中相应的 MAC 地址为空。</p>
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
<li><p class="sd-card-text">type_0, type_1, type_2, type_3: 8位无符号整数(<em>类型描述列表中的 MAC 地址编号0,1,2,3</em>)</p></li>
<li><p class="sd-card-text">mac_addr_0, mac_addr_1, mac_addr_2, mac_addr_3: 48-bit value (<em>MAC地址编号 0,1,2,3小端序</em>)</p></li>
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
<tr class="row-odd"><td><p>0x83</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x83 (131 dec) 表示命令 leaps_mac_addr_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 12%">
<col style="width: 7%">
<col style="width: 8%">
<col style="width: 57%">
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
<div class="line">(byte 0-4) MAC 地址列表的标志，以小端序表示</div>
<div class="line">(字节 5-10) MAC 地址 0，小端序</div>
<div class="line">(字节 11-16) MAC 地址 1，小端序</div>
<div class="line">(字节 17-22) MAC 地址 2，小端序</div>
<div class="line">(字节 23-28) MAC 地址 3，小端序</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>类型0x40 表示上一条命令的 err_code</p>
<p>类型 0xC1(193 dec) 表示 MAC 地址列表</p>
<p><strong>MAC地址标志编码</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 9%">
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p><strong>MAC地址列表标志</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="2"><p>字节 0</p></td>
<td colspan="3"><p>字节1</p></td>
<td colspan="2"><p>字节2</p></td>
<td colspan="2"><p>字节3</p></td>
</tr>
<tr class="row-odd"><td><p>2-7 位</p></td>
<td><p>0-1位</p></td>
<td><p>11-15位</p></td>
<td><p>字节10</p></td>
<td><p>8-9位</p></td>
<td><p>18-23位</p></td>
<td><p>16-17 位</p></td>
<td><p>26-31位</p></td>
<td><p>24-25位</p></td>
</tr>
<tr class="row-even"><td><p>保留</p></td>
<td><p>T_0</p></td>
<td><p>保留</p></td>
<td><p>P_1</p></td>
<td><p>T_1</p></td>
<td><p>保留</p></td>
<td><p>T_2</p></td>
<td><p>保留</p></td>
<td><p>T_3</p></td>
</tr>
</tbody>
</table>
<p>T_0, T_1, T_2, T_3 描述 MAC 地址类型。</p>
<ul class="simple">
<li><p>0 - 空 MAC 地址</p></li>
<li><p>1 - OTP 内存中的默认 MAC 地址。</p></li>
<li><p>2 - 用户指定的 MAC 地址</p></li>
<li><p>3 - 可变的默认 MAC 地址，只能使用 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a> 重写一次。</p></li>
</ul>
<p>如果 BLE 地址是公共 BLE 地址，则设置 P_1。 如果 BLE MAC 地址是随机的，该标志将被清零，有关 BLE 地址类型的更多信息，请参阅 BLE 规范。</p>
</div>


           </div>
