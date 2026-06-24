---
title: "dwm_fw_update_xfer"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer/"
order: 184
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-fw-update-xfer">
<span id="id1"></span><h1>dwm_fw_update_xfer</h1>
<p>该调用仅适用于以太网网关。 应在传输固件数据块的 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start#dwm-fw-update-start"><span class="std std-ref">dwm_fw_update_start</span></a> 之后反复调用该调用，直至传输完所有固件数据块。 返回状态 “ok”，随后返回数据请求帧，直到传输完固件更新所需的所有数据，在这种情况下返回状态 “ok”，随后不返回数据请求，或者直到更新以错误结束。 错误由 “o” 以外的状态表示。 固件更新失败的原因如下:</p>
<ul class="simple">
<li><p>内部错误</p></li>
<li><p>无效参数 - 例如长度为零的数据块</p></li>
<li><p>不允许 - 尚未启动，或整个更新过程失败</p></li>
<li><p>校验和错误 - 接收的图像已损坏。</p></li>
</ul>
<p>每次调用 <a class="reference internal" href="#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> 时，都会返回固件更新过程已经写入闪存的数据大小和偏移量，直到更新完成。</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">offset: 32 位整数 (<em>所有固件数据的偏移量.</em>)</p></li>
<li><p class="sd-card-text">data:从 4 到 32 字节 (<em>固件数据块。</em>)</p></li>
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
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="2"><p>价值</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><p>偏移</p></td>
<td><p>数据块</p></td>
</tr>
<tr class="row-even"><td><p>0x3F</p></td>
<td><p>0x24</p></td>
<td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0xA5 0xA5 0xA5
0xA5 0xA5 0xA5
0xA5 0xA5 ….
0xA5 0xA5 0xA5
0xA5</p></td>
</tr>
</tbody>
</table>
<p>类型 0x3F (63 dec)表示命令 dwm_fw_update_xfer</p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型长度</p></td>
<td><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="2"><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40
0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x7E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>偏移</p></td>
<td><p>大小</p></td>
</tr>
<tr class="row-even"><td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0x00 0x10
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型 0x40 表示状态代码</div>
<div class="line">类型 0x7E (126 dec)表示数据请求</div>
</div>
</div>


           </div>
