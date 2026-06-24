---
title: "dwm_cert_update_start"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-start"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-start/"
order: 171
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cert-update-start">
<span id="id1"></span><h1>dwm_cert_update_start</h1>
<p>该调用仅适用于以太网网关. 它启动证书更新过程，应在调用 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-write#dwm-cert-update-write"><span class="std std-ref">dwm_cert_update_write</span></a> 之前调用. 如果请求被接受，则返回命令状态 =“ok”，然后是第一个数据请求. 用户应使用 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-write#dwm-cert-update-write"><span class="std std-ref">dwm_cert_update_write</span></a> 回应数据请求. 如果拒绝，更新将不会启动. 拒绝证书更新的原因如下:</p>
<ul class="simple">
<li><p>不允许 - 上传的证书大小无效</p></li>
<li><p>内部错误</p></li>
<li><p>无效参数 - 上载证书的 ID 未知</p></li>
</ul>
<p>证书必须是 der 格式。</p>
<p><strong>C代码示例</strong></p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">cert_type :8 位无符号整数（<em>证书标识符/类型，0 - CA 证书，1 - 我的证书，2 - 我的私钥。</em>）</p></li>
<li><p class="sd-card-text">size: 32位无符号整数 (<em>要上传的证书总大小，最多2048字节。</em>)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
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
<tr class="row-odd"><td rowspan="2"><p>0x36</p></td>
<td rowspan="2"><p>0x05</p></td>
<td><p>要上传的证书类型</p></td>
<td><p>大小</p></td>
</tr>
<tr class="row-even"><td><p>0x00</p></td>
<td><p>0xC4 0x26 0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x36（54 dec）表示命令 <a class="reference internal" href="#dwm-cert-update-start"><span class="std std-ref">dwm_cert_update_start</span></a></p>
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
<td><p>0xE4
0x03
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型 0x40 表示状态代码</div>
<div class="line">类型0x7E (126)表示数据请求</div>
</div>
</div>


           </div>
