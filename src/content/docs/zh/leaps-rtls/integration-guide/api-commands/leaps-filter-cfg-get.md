---
title: "leaps_filter_cfg_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-filter-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-filter-cfg-get/"
order: 253
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-filter-cfg-get">
<span id="id1"></span><h1>leaps_filter_cfg_get</h1>
<p>读取其中一个过滤器的配置（例如位置过滤器或测量过滤器）。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">id: ?8-bit unsigned integer (<em>ID of the filter, 0 - measurement filter, 1 - location filter, 2 - measurement selection strategy, 3 - position coordinate</em>)</p></li>
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
<li><p class="sd-card-text">filter_id: 8-bits unsigned integer (<em>ID of the filter, 0 - measurement filter, 1 - location filter. 2 - measurement selection strategy, 3 - position coordinate</em>)</p></li>
<li><p class="sd-card-text">filter_val: byte array with maximum length 12 ?</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="filter-values">
<h2>筛选值</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>筛选器ID</p></th>
<th class="head"><p>过滤器Val</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>0（测量值）</p></td>
<td><p>TBD</p></td>
</tr>
<tr class="row-odd"><td><p>1（位置）</p></td>
<td><p>Byte[0] = Mode (0 - Disable Moving Average Filter, 1 - Enable Moving Average Filter)</p></td>
</tr>
<tr class="row-even"><td><p>2（测量选择策略）</p></td>
<td><p>字节[0]=类型（0-QUAD，1-RSSI，2-循环赛）</p></td>
</tr>
<tr class="row-odd"><td><p>3 (position coordinate)</p></td>
<td><div class="line-block">
<div class="line">Byte[0] = Type (0 - CARTESIAN, 1 - WSG84)</div>
<div class="line">If Type = 1(WSG84)</div>
<div class="line-block">
<div class="line">Byte[1]..Byte[4] = WSG84 Latitude of the Cartesian origin[0,0,0] * 10^7</div>
<div class="line">Byte[5]..Byte[8] = WSG84 Longitude of the Cartesian origin[0,0,0] * 10^7</div>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="measurement-selection-strategy">
<h2>度量选择策略</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 76%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>战略</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>QUAD</p></td>
<td><p>TN 最多可从 4 个象限中选择 4 个 AN 的测量值，用于计算最佳 TN 位置</p></td>
</tr>
<tr class="row-odd"><td><p>RSSI</p></td>
<td><p>TN 选择最多 4 个 RSSI 最高的 AN 的测量值</p></td>
</tr>
<tr class="row-even"><td><p>循环赛</p></td>
<td><p>TN 轮流以循环方式从其锚点列表中的所有 AN 中选择最多 4 个测量值。 (例如：锚点列表中有 6 个 AN（1,2,3,4,5,6），每轮 TN 选择 AN 的测量值: (1,2,3,4), (5,6,1,2), (3,4,5,6) 。。。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<p><strong>示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 26%">
<col style="width: 24%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>筛选器id</p></td>
</tr>
<tr class="row-even"><td><p>0x1B</p></td>
<td><p>0x01</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>类型0x1B（12月27日）表示命令leaps_filter_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 15%">
<col style="width: 12%">
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 18%">
<col style="width: 12%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="2"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>状态代码</p></td>
<td><p>筛选器id</p></td>
<td><p>过滤器val</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x54</p></td>
<td><p>0x0a</p></td>
<td><p>0x03</p></td>
<td><p>0x01
0x18
0x49
0xB7
0xFA
0xD3
0xE6
0xAF
0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型0x54 (84)表示过滤器配置</p>
</div>
</div>


           </div>
