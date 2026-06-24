---
title: "leaps_pos_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-pos-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-pos-set/"
order: 226
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-pos-set">
<span id="id1"></span><h1>leaps_pos_set</h1>
<p>设置节点的默认位置。 在标签模式下，默认位置不会被使用，但还是会被存储起来，以便将模块配置为锚点模式，并使用之前通过 leaps_pos_set 设置的值。 此调用会在设置新值时写入内部闪存，因此不应频繁使用，最坏情况下可能需要数百毫秒！</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">x: 32位整数（以毫米为单位的位置坐标）</p></li>
<li><p class="sd-card-text">y: 32 位整数 (位置坐标，以毫米为单位)</p></li>
<li><p class="sd-card-text">z: 32位整数（以毫米为单位的位置坐标）</p></li>
<li><p class="sd-card-text">pqf: 8 位整数（位置质量因子）</p></li>
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
<p><strong>示例1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 18%">
<col style="width: 21%">
<col style="width: 20%">
<col style="width: 16%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="4"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">小端序,</div>
<div class="line">是 x</div>
<div class="line">坐标在</div>
<div class="line">毫米</div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">小端序,</div>
<div class="line">是y</div>
<div class="line">坐标在</div>
<div class="line">毫米</div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">小端序,</div>
<div class="line">是z</div>
<div class="line">坐标在</div>
<div class="line">毫米</div>
</div>
</td>
<td><div class="line-block">
<div class="line">uint8_t -</div>
<div class="line">是质量</div>
<div class="line">因素</div>
<div class="line">百分比</div>
<div class="line">(0-100)</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x01</p></td>
<td><p>0x0D</p></td>
<td colspan="4"><p>0x4b 0x0a
0x00 0x00
0x1f 0x04
0x00 0x00
0x9c 0x0e
0x00 0x00
0x64</p></td>
</tr>
</tbody>
</table>
<p>类型0x01表示命令leaps_pos_set</p>
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
<p>类型 0x40 表示状态代码</p>
</div>


           </div>
