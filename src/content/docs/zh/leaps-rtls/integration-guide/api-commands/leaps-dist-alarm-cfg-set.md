---
title: "leaps_dist_alarm_cfg_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-set/"
order: 251
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dist-alarm-cfg-set">
<span id="id1"></span><h1>leaps_dist_alarm_cfg_set</h1>
<p>更改距离警报检测配置。 会写入内部闪存，请勿频繁使用。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
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
<col style="width: 9%">
<col style="width: 10%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 10%">
<col style="width: 9%">
<col style="width: 16%">
<col style="width: 18%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLVT 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="6"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">距离阈值</div>
<div class="line">编号1（毫米）</div>
</div>
</td>
<td><div class="line-block">
<div class="line">距离阈值</div>
<div class="line">编号2（毫米）</div>
</div>
</td>
<td><p>mincon</p></td>
<td><p>minnocon</p></td>
<td><div class="line-block">
<div class="line">选项位(3-7) -保留</div>
<div class="line">位 (0-2) - 警报指示选项</div>
</div>
</td>
<td><p>保留（8字节）</p></td>
</tr>
<tr class="row-even"><td><p>0x33</p></td>
<td><p>0x13</p></td>
<td><p>0xDC 0x05
0x00 0x00</p></td>
<td><p>0xC4 0x09
0x00 0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
<td><p>0x01</p></td>
<td><p>0x00 0x00 0x00 0x00
0x00 0x00 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>0x33 (51 dec)型表示命令 leaps_dist_alarm_cfg_set</p>
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
