---
title: "leaps_anchor_list_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get/"
order: 232
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-anchor-list-get">
<span id="id1"></span><h1>leaps_anchor_list_get</h1>
<p>读取周围锚点的列表。 仅适用于锚。 列表中的锚点可以来自同一网络，也可以来自邻居网络。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">offset：8位无符号整数（<em>锚点列表上的偏移，当列表中有8个以上锚点时使用；0-无偏移</em>）</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a>, 时间戳, 标志, 计数，[anchor_0, anchor_1, …]</p></li>
<li><p class="sd-card-text">timestamp: 32 位无符号整数 (<em>以微秒为单位的运行时间</em>)</p></li>
<li><p class="sd-card-text">count：1字节（<em>元素计数，8是列表中1个TLV响应可以携带的最大元素数</em>）</p></li>
<li><p class="sd-card-text">anchor_1, anchor_2, …, anchor_N: (<em>锚点列表</em>)</p></li>
<li><p class="sd-card-text">anchor_N: node_id, position, rssi, seat, neighbor_network (<em>锚点列表元素，N 可以是 0 到 8</em>)</p></li>
<li><p class="sd-card-text">node_id: 2 字节(<em>锚点 ID</em>)</p></li>
<li><p class="sd-card-text">position: 12 字节</p></li>
<li><p class="sd-card-text">rssi: 1 字节有符号（<em>信号强度指示符</em>）</p></li>
<li><p class="sd-card-text">rx_rate: 1 byte unsigned (<em>packet error rate</em>)</p></li>
<li><p class="sd-card-text">seat: 5 bits (<em>锚占用的座位号</em>)</p></li>
<li><p class="sd-card-text">neighbor_network: 1 bit (<em>状态标志，指示锚点是来自当前网络还是来自邻居网络</em>)</p></li>
<li><p class="sd-card-text">seens: 1 byte (<em>Number of BCN frames received from the anchor. This counter overflows at 255</em>)</p></li>
<li><p class="sd-card-text">rx_coll: 16-bit unsigned integer (<em>Number of seat collisions with this anchor</em>)</p></li>
<li><p class="sd-card-text">rx_consec: 1 byte (<em>Number of consecutive BCN frames received from the anchor</em>)</p></li>
<li><p class="sd-card-text">dist: 32-bit unsigned integer (<em>Distance from the anchor in millimeters</em>)</p></li>
<li><p class="sd-card-text">drift_avg: float (4 bytes) (<em>Average clock drift w.r.t the anchor</em>)</p></li>
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
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x0B表示命令leaps_anchor_list_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 26%">
<col style="width: 41%">
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
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 3%">
<col style="width: 4%">
<col style="width: 9%">
<col style="width: 5%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 13%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 4%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="16"><p>TLV 响应（上一表格中的帧残留量）</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="14"><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x56</p></td>
<td rowspan="3"><p>0xE1</p></td>
<td rowspan="2"><p>uint32 - 时间戳（小端序）</p></td>
<td rowspan="2"><p>uint8 - 标志</p></td>
<td rowspan="2"><p>uint8-列表中编码的元素数</p></td>
<td colspan="10"><p>锚点nr. 1</p></td>
<td><p>锚号2 。。。 号8</p></td>
</tr>
<tr class="row-even"><td><p>uint16 - UWB 地址，小端序</p></td>
<td><p>3 x int32 - 位置坐标x, y, z的小端序</p></td>
<td><p>int8 -
RSSI</p></td>
<td><p>uint8 -
rx_rate</p></td>
<td><div class="line-block">
<div class="line">uint8 - 标志</div>
</div>
<div class="line-block">
<div class="line">(0-4 位)座位号</div>
<div class="line">(bit 5) neighbor_network</div>
<div class="line">(6-7位) 保留</div>
</div>
</td>
<td><p>uint8 - 场景</p></td>
<td><p>uint16 -
rx_coll</p></td>
<td><p>uint8 -
rx_consec</p></td>
<td><p>uint32 -
dist</p></td>
<td><p>float -
drift_avg</p></td>
<td><p>…</p></td>
</tr>
<tr class="row-odd"><td><p>0xe8
0x03
0x00
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x08</p></td>
<td colspan="10"><p>0xab 0xbc …</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型 0x56 表示锚点列表</p>
</div>


           </div>
