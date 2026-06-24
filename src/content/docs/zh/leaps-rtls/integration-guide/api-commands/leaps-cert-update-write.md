---
title: "leaps_cert_update_write"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-cert-update-write"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-cert-update-write/"
order: 281
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cert-update-write">
<span id="id1"></span><h1>leaps_cert_update_write</h1>
<p>此呼叫仅在以太网网关上可用。 应在以下时间之后重复调用 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-cert-update-start#leaps-cert-update-start"><span class="std std-ref">leaps_cert_update_start</span></a> 以传输证书，直到传输完所有数据块。 返回状态“ok”，然后是数据请求，直到所有数据都被传输，在这种情况下，返回状态“ok”，然后没有数据请求，或者直到更新以某种错误结束。 错误由“正常”以外的状态代码表示。 更新失败的原因是：</p>
<ul class="simple">
<li><p>内部错误</p></li>
<li><p>无效参数 - 例如数据块长度为零，或数据块被跳过</p></li>
<li><p>不允许 - 尚未启动，或整个更新过程失败</p></li>
</ul>
<p>到目前为止，更新过程已写入闪存的数据的大小和偏移量在每次调用leaps_cert_update_write时作为响应返回，直到更新完成。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">offset: 32位无符号整数 (<em>证书数据偏移量。</em>)</p></li>
<li><p class="sd-card-text">data: 从4到240字节 (<em>前正在上传的证书数据块，最多240字节。</em>)</p></li>
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
<li><p class="sd-card-text">offset: 32 位无符号整数 (<em>下一个数据块的预期偏移量。</em>)</p></li>
<li><p class="sd-card-text">size:32 位无符号整数（<em>下一个数据块的预期大小。</em>）</p></li>
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
<tr class="row-odd"><td rowspan="2"><p>0x3B</p></td>
<td rowspan="2"><p>0x24</p></td>
<td><p>偏移</p></td>
<td><p>数据</p></td>
</tr>
<tr class="row-even"><td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0xA5 0xA5 0xA5
0xA5 0xA5 0xA5
0xA5 0xA5 ….
0xA5 0xA5 0xA5
0xA5</p></td>
</tr>
</tbody>
</table>
<p>类型0x3B（59 dec）表示命令leaps_cert_update_write</p>
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
<div class="line">类型 0x40 表示状态代码</div>
<div class="line">类型 0x7E (126 dec)表示数据请求</div>
</div>
</div>


           </div>
