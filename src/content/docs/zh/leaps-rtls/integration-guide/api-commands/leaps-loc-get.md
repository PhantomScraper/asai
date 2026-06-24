---
title: "leaps_loc_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-loc-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-loc-get/"
order: 225
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-loc-get">
<span id="id1"></span><h1>leaps_loc_get</h1>
<hr class="docutils">
<p>当完成所有 TWR 测量并向用户提供新的位置数据时，将生成事件并更改状态. 当使用低功耗模式时，其工作方式与此相同。</p>
<p>对于锚节点，只有在完成自动定位程序后，才能获得位置和距离数据。 自动定位程序是通过 BLE 接口启动的。</p>
<hr class="docutils">
<p><strong>标签节点</strong></p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">8 位无符号整数（输出选项，0 - 与测距锚的距离，1 - 我的位置 + 与测距锚的距离，2 - 位置和与测距锚的距离，3 - 我的位置 + 与测距锚的距离和位置）</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a>, [my_position], [timestamp, flags, count, [{addr, anchor_distance, pqf}, …]], [timestamp, flags, count, [{anchor_position, addr, anchor_distance, pqf}, …]]</p></li>
<li><p class="sd-card-text">timestamp: 32 位整数？（以微秒为单位的时间戳）</p></li>
<li><p class="sd-card-text">flags: 8位无符号整数？(is_moving indication)</p></li>
<li><p class="sd-card-text">count: 位整数(后面列表中的元素个数，列表可以包含位置, 距离或两者)</p></li>
<li><p class="sd-card-text">my_position, anchor_position: 13 个字节(参见 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#position"><span class="std std-ref">位置</span></a>)</p></li>
<li><p class="sd-card-text">addr: 16 位整数（对端节点的 UWB 地址/ID</p></li>
<li><p class="sd-card-text">distance: 32 位整数（到对面的距离，以毫米为单位）</p></li>
<li><p class="sd-card-text">pqf: 8 位整数（质量因子）</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>如果 <strong>标记节点</strong> - 可用参数 - pos: <strong>位置</strong> (与距离相对应的节点位置)</p>
</div>
<hr class="docutils">
<p><strong>示例 1 (我的位置 + 到测距锚的距离和位置)</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 32%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>类型0x0C 表示 loc_get 命令</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 16%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 19%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>值状态</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>此节点的值位置（13 字节）</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>值的位置和到测距锚的距离（86 字节）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>…</p></td>
<td><p>0x49</p></td>
<td><p>0x56</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型0x41表示位置</p>
<p>0x49 型表示标签节点上的位置和距离</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 27%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 14%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>测距锚的位置和距离编码</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>以微秒为单位的时间戳</p></td>
<td rowspan="2"><div class="line-block">
<div class="line">标志（1字节）</div>
</div>
<div class="line-block">
<div class="line">(bit 0) is_moving</div>
<div class="line">(bits 1-7) 保留</div>
</div>
</td>
<td rowspan="2"><p>编码位置和距离的数量（1字节）</p></td>
<td colspan="2"><p>位置和距离编号 1 (20 字节)</p></td>
<td><p>位置和距离 nr.2, 3, 4 (60 字节)</p></td>
</tr>
<tr class="row-odd"><td><p>距离 nr.1</p>
<p>（7字节）</p>
</td>
<td><p>位置 nr.1</p>
<p>（13字节）</p>
</td>
<td><p>…</p></td>
</tr>
<tr class="row-even"><td><p>0x64
0x0A
0x01
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x04</p></td>
<td><p>…</p></td>
<td><p>…</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>0x49型表示标签节点上的位置和距离。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 39%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>距离编码</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB 地址</p>
<p>(2 字节)</p>
</td>
<td><p>距离为毫米</p>
<p>（4字节）</p>
</td>
<td><p>距离质量因子，以百分比表示（1字节）</p></td>
</tr>
<tr class="row-odd"><td><p>0xAB 0xCD</p></td>
<td><p>0xE8 0x03 0x00 0x00</p></td>
<td><p>0x5F</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 23%">
<col style="width: 25%">
<col style="width: 28%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>位置编码</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x坐标，单位为毫米</p>
<p>（4字节）</p>
</td>
<td><p>以毫米为单位的 y 坐标（4 字节）</p></td>
<td><p>z坐标，单位为毫米</p>
<p>（4字节）</p>
</td>
<td><p>以百分比为单位的位置质量因子（1 字节）</p></td>
</tr>
<tr class="row-odd"><td><p>0x4b 0x0a 0x00
0x00</p></td>
<td><p>0x1f 0x04
0x00 0x00</p></td>
<td><p>0x9c 0x0e 0x00
0x00</p></td>
<td><p>0x64</p></td>
</tr>
</tbody>
</table>
<p><strong>示例 1 (我的位置 + 到测距锚的距离和位置)</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 32%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>类型0x0C 表示 loc_get 命令</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 16%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 19%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>状态代码</p></td>
<td><p>此节点的位置（13字节）</p></td>
<td><p>到测距锚的距离（90 字节）</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>…</p></td>
<td><p>0x48</p></td>
<td><p>0x5A</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型0x41表示位置</p>
<p>类型0x48表示测距锚的距离</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 29%">
<col style="width: 13%">
<col style="width: 17%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>测距锚的距离编码</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>以微秒为单位的时间戳（4 字节）</p></td>
<td><div class="line-block">
<div class="line">标志（1字节）</div>
</div>
<div class="line-block">
<div class="line">(bit 0) is_moving</div>
<div class="line">(bits 1-7) 保留</div>
</div>
</td>
<td><p>编码的距离数</p>
<p>（1 字节）</p>
</td>
<td><p>距离 nr.1</p>
<p>（7字节）</p>
</td>
<td><p>距离nr. 2, 3, … , 11, 12</p>
<p>（77 字节）</p>
</td>
</tr>
<tr class="row-odd"><td><p>0x64
0x12
0x0E
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x04</p></td>
<td><p>…</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
