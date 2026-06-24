---
title: "leaps_uwb_cfg_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-set/"
order: 273
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-cfg-set">
<span id="id1"></span><h1>leaps_uwb_cfg_set</h1>
<p>设置 UWB 配置参数。</p>
<ul class="simple">
<li><p>DW1000: 可支持通道2, 3和通道5。</p></li>
<li><p>DW3000: 可支持频道 5 和 9。</p></li>
</ul>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">preamble_code: ‘9’ | ‘10’ | ‘11’ | ‘12’ (<em>UWB前置码</em>)</p></li>
<li><p class="sd-card-text">channel: ‘2’ | ‘3’ | ‘5’ | ‘9’ (<em>UWB 频道</em>)</p></li>
<li><p class="sd-card-text">pg_delay: 1字节（<em>发射机校准 - 脉冲发生器延迟</em>）。</p></li>
<li><p class="sd-card-text">lna_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">pa_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf1_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf2_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">tx_power: 4 字节 （<em>TX 功率控制</em>）。</p></li>
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
<p><strong>示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 18%">
<col style="width: 63%">
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
<tr class="row-odd"><td><div class="line-block">
<div class="line">(第1字节) preamble_code</div>
<div class="line">(第2字节) pg_delay</div>
<div class="line">(第3字节) channel</div>
<div class="line">(第3字节, bit 0) lna_enable</div>
<div class="line">(第4字节, bit 1) pa_enable</div>
<div class="line">(第4字节, bit 2) rf1_enable</div>
<div class="line">(第4字节, bit 3) rf2_enable</div>
<div class="line">(第4字节, bits 4-8) 保留</div>
<div class="line">(5th-8th byte) tx_power</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x17</p></td>
<td><p>0x08</p></td>
<td><p>0x09 0xC3
0x05 0x03
0x85 0x65
0x45 0x25</p></td>
</tr>
</tbody>
</table>
<p>类型0x17表示命令leaps_uwb_cfg_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV回复</p></th>
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
</div>


           </div>
