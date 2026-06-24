---
title: "leaps_mac_addr_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set/"
order: 256
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mac-addr-set">
<span id="id1"></span><h1>leaps_mac_addr_set</h1>
<p>设置 BLE, UWB, 以太网或 Wi-Fi 接口的 MAC 地址. 需要复位才能生效. 由于会写入内部非易失性存储器，因此不应频繁使用. 需要重置出厂设置(<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a>)才能使用默认 MAC 地址. UWB MAC 地址的两个最小有效字节不得等于 0x0000 或 0xFFFF. BLE 地址可以是随机 BLE 地址或公共 BLE 地址. 以太网和 Wi-Fi 地址必须遵守 EUI-48 格式，U/I 位必须相应设置。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">type_0, type_1, type_2, type_3: 8位无符号整数(<em>类型描述列表中的 MAC 地址编号0,1,2,3</em>)</p></li>
<li><p class="sd-card-text">mac_addr_0, mac_addr_1, mac_addr_2, mac_addr_3: 48-bit value (<em>MAC地址编号 0,1,2,3小端序</em>)</p></li>
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
<col style="width: 22%">
<col style="width: 24%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><div class="line-block">
<div class="line">价值</div>
<div class="line">节点 ID，小端序</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>0x2D</p></td>
<td><p>0x07</p></td>
<td><p>0x00 0xEF
0xCD 0xAB
0x56 0x34
0x12</p></td>
</tr>
</tbody>
</table>
<p>类型0x2D（45 dec）表示命令 <a class="reference internal" href="#leaps-mac-addr-set"><span class="std std-ref">leaps_mac_addr_set</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 18%">
<col style="width: 66%">
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
