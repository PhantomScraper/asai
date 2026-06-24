---
title: "leaps_upd_rate_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-upd-rate-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-get/"
order: 235
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-upd-rate-get">
<span id="id1"></span><h1>leaps_upd_rate_get</h1>
<p>获取位置更新率。</p>
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
<li><p class="sd-card-text">update_rate_nominal: 16位无符号整数(<em>位置发布速率为超帧的倍数，最大值为600，最小值为1</em>)</p></li>
<li><p class="sd-card-text">update_rate_stationary: 16位无符号整数(<em>节点不在多个超帧中移动时的位置发布速率，最大值为600，最小值为1</em>)</p></li>
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
<tr class="row-odd"><td><p>0x04</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x04表示命令leaps_upd_rate_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 24%">
<col style="width: 28%">
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
<tr class="row-odd"><td><p>update_rate_nominal</p></td>
<td><p>update_rate_stationary</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x45</p></td>
<td><p>0x04</p></td>
<td><p>0x0A 0x00</p></td>
<td><p>0x16 0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x45 表示更新率（正常和静止）</p>
<p>类型 0x40 表示状态代码</p>
</div>


           </div>
