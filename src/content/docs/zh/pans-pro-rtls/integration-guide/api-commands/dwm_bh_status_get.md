---
title: "dwm_bh_status_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm_bh_status_get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm_bh_status_get/"
order: 164
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-bh-status-get">
<span id="id1"></span><h1>dwm_bh_status_get</h1>
<p>获取当前 UWBMAC 回程状态。 节点必须配置为网关。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_bh_status_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_bh_status_get</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – sf_number, bh_seat_map, origin_cnt, {origin_info}</p></li>
<li><p><strong>sf_number</strong> – 16 位整数 (<em>当前超帧编号</em>)</p></li>
<li><p><strong>bh_seat_map</strong> – 32位整数 (<em>当前超帧中的座位图</em>)</p></li>
<li><p><strong>origin_cnt</strong> – 8位整数 (<em>范围从0到8</em>)</p></li>
<li><p><strong>origin_info</strong> – node_id, bh_seat, hop_lvl (<em>起源列表中的元素</em>)</p></li>
<li><p><strong>node_id</strong> – 16 位整数 (<em>起源地址</em>)</p></li>
<li><p><strong>bh_seat</strong> – 8位整数 (<em>跳转级别</em>)</p></li>
<li><p><strong>hop_lvl</strong> – 8位整数 (<em>跳转级别</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<p>模块上的用户应用程序不可用。</p>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0x3A</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x3A 表示命令 dwm_bh_status_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 12%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(2 字节) sf_number</div>
<div class="line">(4字节) bh_seat_map</div>
<div class="line">(1字节) origin_cnt</div>
<div class="line">(N*4字节) N*origin_info</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5D</p></td>
<td><p>0x13</p></td>
<td><p>0x6c 0x00
0x07 0x00
0x00 0x00
0x03
0xf3 0x11
0x00 0x01
0xc3 0x11
0x01 0x01
0x66 0x11
0x02 0x01</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
<div class="line">类型0x5D表示UWBMAC状态</div>
</div>
</div>


           </div>
