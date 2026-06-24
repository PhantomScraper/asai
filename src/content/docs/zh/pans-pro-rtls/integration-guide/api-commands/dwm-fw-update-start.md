---
title: "dwm_fw_update_start"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start/"
order: 183
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-fw-update-start">
<span id="id1"></span><h1>dwm_fw_update_start</h1>
<p>此调用仅适用于以太网网关. 它会启动固件更新. 它应该在调用 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> 之前开始调用. 如果请求被接受，则返回命令状态: “ok”，然后是第一个数据请求. 数据请求应始终由 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> 处理. 如果被拒绝，更新将不会启动。</p>
<p>固件更新被拒绝的原因:</p>
<ul class="simple">
<li><p>不允许 - 给出了无效的硬件版本，或者模块未处于引导加载器模式（引导加载器模式总是在复位后短时间内进入:模块在引导加载器模式下停留的时间可以通过 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a> 进行配置）。</p></li>
<li><p>内部错误</p></li>
<li><p>忙 - 固件更新已在进行中。</p></li>
</ul>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">hw_version: 32 位整数 (<em>硬件版本</em>)</p></li>
<li><p class="sd-card-text">fw_version: 32 位整数 (<em>固件版本</em>)</p></li>
<li><p class="sd-card-text">fw_checksum: 32 位整数 (<em>要上传的固件的 crc32</em>)</p></li>
<li><p class="sd-card-text">fw_size: 32 位整数 (<em>固件大小</em>)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
<li><p class="sd-card-text">offset: 32 位整数 (<a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> 需要写入的数据的偏移量)</p></li>
<li><p class="sd-card-text">size: 32 位整数（<a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> 需要写入的数据大小）</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>硬件版本</p></td>
<td><p>固件版本</p></td>
<td><p>固件校验和</p></td>
<td><p>大小</p></td>
</tr>
<tr class="row-odd"><td><p>0x3E</p></td>
<td><p>0x10</p></td>
<td><p>0x2A
0x00
0xCA
0xDE</p></td>
<td><p>0x01 0x00
0x01 0x01</p></td>
<td><p>0xea
0xF5
0x67
0x6D</p></td>
<td><p>0xC4
0x26
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x3E（62 dec）表示命令 <a class="reference internal" href="#dwm-fw-update-start"><span class="std std-ref">dwm_fw_update_start</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="2"><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x7E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>偏移</p></td>
<td><p>大小</p></td>
</tr>
<tr class="row-even"><td><p>0x00
0x00
0x00
0x00</p></td>
<td><p>0x00
0x10
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40 表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></div>
<div class="line">类型0x7E (126)表示数据请求</div>
</div>
</div>


           </div>
