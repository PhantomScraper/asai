---
title: "leaps_fw_update_xfer"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer/"
order: 238
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-fw-update-xfer">
<span id="id1"></span><h1>leaps_fw_update_xfer</h1>
<hr class="docutils">
<p>应在 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> 之后重复调用，以传输固件数据块，直至传输完所有固件。 如果数据块处理成功，则返回状态 “ok”，否则返回错误。 错误由 “ok” 以外的状态表示。 固件更新失败的原因有:</p>
<ul class="simple">
<li><p>内部错误</p></li>
<li><p>无效参数- 例如长度为零的数据块或损坏的数据</p></li>
<li><p>不允许 - 尚未启动或整个更新过程失败</p></li>
<li><p>校验和错误 - 接收到损坏的数据，或者在更新开始时由 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> 提供的校验和值与模块在更新结束时计算的校验和值不匹配</p></li>
</ul>
<p>每次调用 leaps_fw_update_xfer 时，都会返回固件更新过程中已经被 dq 处理过的数据的大小和偏移量作为响应，直到更新结束。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">offset: 32 位整数 (<em>所有固件数据的偏移量.</em>)</p></li>
<li><p class="sd-card-text">data: 从4到240 字节 (<em>固件数据块。</em>)</p></li>
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
<li><p class="sd-card-text">size: 32位整数 (<em>需要被 leaps_fw_update_xfer</em> 写入的固件数据块大小)</p></li>
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
<col style="width: 11%">
<col style="width: 24%">
<col style="width: 51%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="2"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>偏移</p></td>
<td><p>数据块</p></td>
</tr>
<tr class="row-even"><td><p>0x3F</p></td>
<td><p>0x24</p></td>
<td><p>0x00 0x00 0x00
0x00</p></td>
<td><p>0xA5 0xA5 0xA5 0xA5 0xA5 0xA5 0xA5
0xA5 …. 0xA5 0xA5 0xA5 0xA5</p></td>
</tr>
</tbody>
</table>
<p>类型 0x3F（63 位十进制）表示命令 leaps_fw_update_xfer</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 23%">
<col style="width: 23%">
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
<td><p>0x04</p></td>
<td><p>0x7E</p></td>
<td><p>0x08</p></td>
<td><p>0x00 0x00 0x00
0x00</p></td>
<td><p>0x00 0x10 0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型 0x7E（126 dec）表示固件数据请求</p>
</div>


           </div>
