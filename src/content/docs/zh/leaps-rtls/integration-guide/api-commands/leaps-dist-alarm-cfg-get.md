---
title: "leaps_dist_alarm_cfg_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-get/"
order: 252
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dist-alarm-cfg-get">
<span id="id1"></span><h1>leaps_dist_alarm_cfg_get</h1>
<p>读取距离报警检测的配置。</p>
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
<ul class="simple">
<li><p class="sd-card-text">threshold_1: 32位无符号整数（<em>距离阈值，单位为毫米</em>）</p></li>
<li><p class="sd-card-text">threshold_2: 32位无符号整数（<em>距离阈值，单位为毫米</em>）</p></li>
<li><p class="sd-card-text">mincon: 8 位无符号整数（<em>阈值滞后为更新率的倍数</em>）</p></li>
<li><p class="sd-card-text">minnoconn: 8位无符号整数（<em>阈值滞后为更新率的倍数</em>）</p></li>
<li><p class="sd-card-text">options: 8位无符号整数（<em>报警指示选项，0-LED（离散），1-LED（连续），2-蜂鸣器（连续）, 3-电机（连续）</em>）</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
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
<tr class="row-odd"><td><p>0x31</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x31（12月49日）表示命令leaps_serial_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 7%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 7%">
<col style="width: 8%">
<col style="width: 13%">
<col style="width: 10%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="6"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">距离</div>
<div class="line">阈值nr.1</div>
<div class="line">（毫米）</div>
</div>
</td>
<td><div class="line-block">
<div class="line">距离</div>
<div class="line">阈值nr.2</div>
<div class="line">（毫米）</div>
</div>
</td>
<td><p>mincon</p></td>
<td><p>minnocon</p></td>
<td><div class="line-block">
<div class="line">保留选项位（3-7）</div>
<div class="line">指示选项中的位（0-2）报警</div>
</div>
</td>
<td><p>保留（8字节）</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x52</p></td>
<td><p>0x13</p></td>
<td><p>0xDC
0x05
0x00
0x00</p></td>
<td><p>0xC4
0x09
0x00
0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
<td><p>0x01</p></td>
<td><p>0x00 0x00
0x00 0x00
0x00 0x00
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型0x52（82）表示距离报警配置</p>
</div>


           </div>
