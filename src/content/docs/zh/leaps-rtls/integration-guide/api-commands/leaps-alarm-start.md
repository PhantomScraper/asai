---
title: "leaps_alarm_start"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-alarm-start"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-alarm-start/"
order: 146
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-alarm-start">
<span id="id1"></span><h1>leaps_alarm_start</h1>
<p>激活指定时间段内的板载警报。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">LED, motor, buzzer: ‘0’ | ‘1’ (<em>1 启用特定警报</em>)</p></li>
<li><p class="sd-card-text">duration: 8 位无符号整数(警报时间段，200 ms 的倍数)</p></li>
<li><p class="sd-card-text">intensity: 8 位无符号整数 (<em>警报强度</em>)</p></li>
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
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 66%">
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
<tr class="row-odd"><td rowspan="2"><p>0x85</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>byte 0: 警报配置</p>
<ul class="simple">
<li><p>bit 0 - 启用 LED</p></li>
<li><p>bit 1 - 启用蜂鸣器</p></li>
<li><p>bit 2 - 启用电机</p></li>
<li><p>bit 3-7 保留</p></li>
</ul>
<div class="line-block">
<div class="line">1字节:保留</div>
<div class="line">byte 2: 持续时间，200毫秒的倍数</div>
<div class="line">3字节:强度</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x07 0x00 0x05 0xff</p></td>
</tr>
</tbody>
</table>
<p>0x85 表示命令 leaps_alarm_start</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 49%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值 <strong>(参见错误代码)</strong></p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x40 表示上一条命令的 err_code</p>
</div>


           </div>
