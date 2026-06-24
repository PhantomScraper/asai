---
title: "leaps_usr_data_write"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-usr-data-write"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-usr-data-write/"
order: 271
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-usr-data-write">
<span id="id1"></span><h1>leaps_usr_data_write</h1>
<p>将自定义用户数据写入非易失性存储器，或通过 UWB 或 BLE 接口发送数据. 要接收新用户数据的通知或读取用户数据，请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-usr-data-read#leaps-usr-data-read"><span class="std std-ref">leaps_usr_data_read</span></a>。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<blockquote>
<div><ul>
<li><p class="sd-card-text">数据</p></li>
<li><p class="sd-card-text">type: 2 位（<em>用户数据类型，‘0’表示将用户数据写入 UWB 接口，‘1’表示将用户数据写入 BLE 接口，‘2’表示将用户数据写入非易失性存储器</em>）。</p></li>
<li><p class="sd-card-text">标志：覆盖、测试</p></li>
<li><p class="sd-card-text">overwrite: 1 bit</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">‘0’表示不覆盖</p></li>
<li><p class="sd-card-text">‘1’表示覆盖当前发送的数据</p></li>
</ul>
</div></blockquote>
</li>
<li><p class="sd-card-text">test: 1 bit (Applies only when type=0)</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">‘0’ means test data is disabled</p></li>
<li><p class="sd-card-text">‘1’ means device will send test user data (maximum size with first 4 bytes being frame counter). The input data length must be 4 and the input data is parsed as the number of test frames to send.</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
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
<blockquote>
<div><p class="sd-card-text">‘忙’ - 之前的数据尚未发送，请重试或将覆盖标志设置为 1 后发送。</p>
<p class="sd-card-text">‘参数无效’ - 用户数据的大小过大或用户数据类型未知。</p>
<p class="sd-card-text">‘内部错误’ - 意外的内部错误。</p>
<p class="sd-card-text">BLE</p>
<blockquote>
<div><p class="sd-card-text">‘不允许’ - BLE 接口上没有活动连接。</p>
</div></blockquote>
</div></blockquote>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p>示例（写入 UWB 用户数据）</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
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
<td><div class="line-block">
<div class="line">标志</div>
<div class="line">(bits 0-1) 类型</div>
<div class="line">(bit 2) 重写</div>
<div class="line">(3位)测试</div>
<div class="line">(4-7 位)保留</div>
</div>
</td>
<td><p>UWB, BLE 用户数据 - 最多 26 字节 非易失性内存用户数据 - 最多 250 字节</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x00</p></td>
<td><p>0x01 0x02 0x03 …. 0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>0x1A (26 dec) 表示 leaps_usr_data_write 命令</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x40 表示 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a> 命令的状态码</p>
<p>示例（写入测试UWB用户数据）</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
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
<td><div class="line-block">
<div class="line">标志</div>
<div class="line">(bits 0-1) 类型</div>
<div class="line">(bit 2) 重写</div>
<div class="line">(3位)测试</div>
<div class="line">(4-7 位)保留</div>
</div>
</td>
<td><p>Data length must be 4 bytes
Number of frames to be sent
(e.g 10 frames -
0x0A 0x00 0x00 0x00)</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x05</p></td>
<td><p>0x0C</p></td>
<td><p>0x0A 0x00 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>0x1A (26 dec) 表示 leaps_usr_data_write 命令</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x40 表示 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a> 命令的状态码</p>
<p>示例（重写 BLE 用户数据）</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
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
<td><div class="line-block">
<div class="line">标志</div>
<div class="line">(bits 0-1) 类型</div>
<div class="line">(bit 2) 重写</div>
<div class="line">(3位)测试</div>
<div class="line">(4-7 位)保留</div>
</div>
</td>
<td><p>BLE 用户数据最多 34 字节</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x05</p></td>
<td><p>0x01 0x02 0x03 …. 0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>0x1A (26 dec) 表示 leaps_usr_data_write 命令</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x40 表示 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a> 命令的状态码</p>
<p>示例（将用户数据写入非易失性存储器）</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
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
<td><div class="line-block">
<div class="line">标志</div>
<div class="line">(bits 0-1) 类型</div>
<div class="line">(bit 2) 重写</div>
<div class="line">(3位)测试</div>
<div class="line">(4-7 位)保留</div>
</div>
</td>
<td><p>非易失性内存用户数据 - 最多 250 字节</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x02</p></td>
<td><p>0x01 0x02 0x03 …. 0xFA</p></td>
</tr>
</tbody>
</table>
<p>0x1A (26 dec) 表示 leaps_usr_data_write 命令</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x40 表示 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a> 命令的状态码</p>
</div>


           </div>
