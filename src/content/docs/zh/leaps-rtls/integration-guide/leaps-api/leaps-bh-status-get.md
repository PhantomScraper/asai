---
title: "leaps_bh_status_get"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/leaps-bh-status-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/leaps-bh-status-get/"
order: 290
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-bh-status-get">
<span id="id1"></span><h1>leaps_bh_status_get</h1>
<p>获取当前 UWBMAC 回程状态。 节点必须配置为网关或锚点。</p>
<hr class="docutils">
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
<ul>
<li><p class="sd-card-text">sf_number: 16位整数(<em>当前超帧编号</em>)</p></li>
<li><p class="sd-card-text">bh_seat_map: 32位整数(<em>当前超级帧中的座位图</em>)</p></li>
<li><p class="sd-card-text">origin_cnt: 8位整数(<em>从0到8的原点计数</em>)</p></li>
<li><p class="sd-card-text">origin_list: (node_id_0, bh_seat_0, hop_lvl_0), (node_id_1, bh_seat_1, hop_lvl_1), …</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">node_id: 16位整数(<em>原点的 UWB 地址</em>)</p></li>
<li><p class="sd-card-text">bh_seat: 8位整数(<em>原点占据的位置，范围从 0 到 8</em>)</p></li>
<li><p class="sd-card-text">hop_lvl: 8位整数(<em>跳转级别</em>)</p></li>
</ul>
</div></blockquote>
</li>
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
<tr class="row-odd"><td><p>0x3A</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x3A 表示命令 leaps_bh_status_get</p>
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
<div class="line">(N*4 字节) origin_list</div>
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
<p>类型 0x40 表示状态代码</p>
<p>类型0x5D 表示 UWBMAC 回程状态</p>
</div>


           </div>
