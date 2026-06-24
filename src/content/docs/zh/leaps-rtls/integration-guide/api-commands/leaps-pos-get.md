---
title: "leaps_pos_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-pos-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-pos-get/"
order: 227
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <section id="leaps-pos-get">
<span id="id1"></span><h1>leaps_pos_get</h1>
<p>获取节点的实际位置。</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">(无)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#position"><span class="std std-ref">位置</span></a></p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p><strong>示例</strong></p>
<table class="custom-table docutils align-default">
<thead>
<tr class="row-odd"><th class="head"><p>TLV 请求</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0x02</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x02表示命令leaps_pos_get</p>
<table class="custom-table docutils align-default">
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="4"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">一点点</div>
<div class="line">字节序为</div>
<div class="line">x坐标</div>
<div class="line">为毫米</div>
<div class="line">/ WGS84</div>
<div class="line">latitude x10^7</div>
<div class="line"><br></div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">一点点</div>
<div class="line">字节序为</div>
<div class="line">y坐标</div>
<div class="line">为毫米</div>
<div class="line">/ WGS84</div>
<div class="line">longitude x10^7</div>
<div class="line"><br></div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">一点点</div>
<div class="line">字节序为</div>
<div class="line">z坐标</div>
<div class="line">为毫米</div>
<div class="line">为毫米</div>
<div class="line">/ 0 in WGS84</div>
<div class="line">coordinate</div>
</div>
</td>
<td><div class="line-block">
<div class="line">uint8_t -</div>
<div class="line">位置</div>
<div class="line">质量</div>
<div class="line">因素</div>
<div class="line">百分比（0-100）</div>
<div class="line"><br></div>
<div class="line"><br></div>
<div class="line"><br></div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td colspan="4"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00
0x9c
0x0e
0x00
0x00
0x64</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型0x41型表示位置（x,y,z,pqf）</p>
</section>


           </div>
