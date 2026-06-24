---
title: "leaps_panid_profile_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-panid-profile-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-panid-profile-set/"
order: 263
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-panid-profile-set">
<span id="id1"></span><h1>leaps_panid_profile_set</h1>
<p>设置UWB网络标识符（PANID）和区域ID，以协助锚点选择，以及PANID掩码，它有助于支持标签在具有不同PANID的多个不同网络上漫游。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul>
<li><p class="sd-card-text">panid:16位无符号整数（<em>UWB panid</em>）</p></li>
<li><p class="sd-card-text">panid_mask:16位无符号整数（<em>UWB panid掩码</em>）</p></li>
<li><p class="sd-card-text">zone_id: 8位无符号整数（<em>AN的UWB区域id</em>）</p></li>
<li><p class="sd-card-text">flag: 8-bit unsigned integer optional flag</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">bit 0: skip writing values to the environment (1: skip writing, 0: write to the environment)</p></li>
</ul>
</div></blockquote>
</li>
<li><p class="sd-card-text">reserved: 8-bit unsigned integer (<em>reserved for future use</em>)</p></li>
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
<p><strong>示例1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 12%">
<col style="width: 25%">
<col style="width: 14%">
<col style="width: 11%">
<col style="width: 19%">
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
<tr class="row-odd"><td><p>panid</p></td>
<td><p>panid_mask</p></td>
<td><p>zone_id</p></td>
<td><p>flag</p></td>
<td><p>reserved</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x06</p></td>
<td><p>0xCD
0xAB</p></td>
<td><p>0xFF
0xFF</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>0x40 表示命令 leaps_panid_profile_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
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
<p>类型 0x40 表示状态代码</p>
</div>


           </div>
