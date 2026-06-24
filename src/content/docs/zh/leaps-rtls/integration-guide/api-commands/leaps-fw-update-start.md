---
title: "leaps_fw_update_start"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-fw-update-start"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start/"
order: 237
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-fw-update-start">
<span id="id1"></span><h1>leaps_fw_update_start</h1>
<p>启动固件更新进程. 应在 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> 之前调用，可能需要数秒. 如果请求被接受，则返回命令状态： “ok”，然后是第一个数据请求. 数据请求应由 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> 处理. FW 更新的目标可以是 FW ID 等于 1 的 ELDR（扩展加载器）或 FW ID 等于 2 的主 FW. 并非所有硬件平台都支持 ELDR，请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get#leaps-dev-info-get"><span class="std std-ref">leaps_dev_info_get</span></a> 命令了解如何读取设备信息. 在 FW 更新过程中，由于固件无法自行更新，因此需要重新启动进入引导加载程序或 ELDR。</p>
<p>如果更新被拒绝，则不会启动更新. 固件更新被拒绝的原因如下：</p>
<ul class="simple">
<li><p>不允许 - 作为固件更新目标的 FW ID 需要进入引导加载器模式（引导加载器模式总是在复位后短时间内进入，模块在引导加载器模式下停留的时间可以通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-boot-cfg-set#leaps-boot-cfg-set"><span class="std std-ref">leaps_boot_cfg_set</span></a> 进行配置）。</p></li>
<li><p>再次 - 需要重置才能切换到 ELDR/FW，设备重置后需要再次发送更新启动请求. 可以通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a> 重置设备。</p></li>
<li><p>内部错误</p></li>
<li><p>无效参数 - 硬件版本无效或 FW ID 无效。</p></li>
</ul>
<p>正在进行的固件更新会通过此命令重新启动。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">hw_version: 32 位整数 (<em>硬件版本</em>)</p></li>
<li><p class="sd-card-text">fw_id: ‘1’ | ‘2’ (<em>1表示ELDR-扩展加载器，2表示主固件</em>)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a></p></li>
<li><p class="sd-card-text">offset: 32 位整数 (<em>leaps_fw_update_xfer 下一步需要写入的数据的偏移量</em>)</p></li>
<li><p class="sd-card-text">size: 32位整数（<em>需要leaps_fw_update_xfer</em> 写入的数据大小）</p></li>
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
<col style="width: 13%">
<col style="width: 12%">
<col style="width: 18%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="5"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>硬件版本</p></td>
<td><p>固件ID</p></td>
<td><p>保留</p></td>
<td><p>固件校验和</p></td>
<td><p>大小</p></td>
</tr>
<tr class="row-even"><td><p>0x3E</p></td>
<td><p>0x10</p></td>
<td><p>0x2A 0x00
0xCA 0xDE</p></td>
<td><p>0x02</p></td>
<td><p>0x00
0x00
0x00</p></td>
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
<p>类型 0x3E（62 分）表示命令 leaps_fw_update_start</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 9%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 26%">
<col style="width: 26%">
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
<tr class="row-odd"><td><p>偏移</p></td>
<td><p>大小</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x7e</p></td>
<td><p>0x08</p></td>
<td><p>0x00 0x00 0x00 0x00</p></td>
<td><p>0x00 0x10 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型0x7E（126）表示固件数据请求</p>
</div>


           </div>
