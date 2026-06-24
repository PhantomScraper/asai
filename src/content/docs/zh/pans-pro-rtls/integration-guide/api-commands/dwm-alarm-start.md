---
title: "dwm_alarm_start"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-alarm-start"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-alarm-start/"
order: 166
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-alarm-start">
<span id="id1"></span><h1>dwm_alarm_start</h1>
<p>在指定的时间段内激活电路板警报。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_alarm_start">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_alarm_start</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_alarm_start_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – : led_0, led_1, led_2, 电机, 蜂鸣器, 持续时间, 强度</p></li>
<li><p><strong>input</strong> – led_0, led_1, led_2, motor, buzzer: ‘0’ | ‘1’ (<em>1启用特定警报</em>)</p></li>
<li><p><strong>duration</strong> – 8 位无符号整数（警报时间段，200 毫秒的倍数）</p></li>
<li><p><strong>intensity</strong> – 8 位无符号整数（<em>警报强度</em>）。</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<p>模块上的用户应用程序不可用。</p>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 50%">
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
<td><ul class="simple">
<li><p>字节 0:警报配置:</p>
<ul>
<li><p>位0 - 启用 LED 0,</p></li>
<li><p>位 1 - 启用 LED1,</p></li>
<li><p>位 2 - 启用 LED2,</p></li>
<li><p>位 3 - 启用蜂鸣器,</p></li>
<li><p>位4 - 启用电机</p></li>
</ul>
</li>
<li><p>1字节:保留</p></li>
<li><p>2字节:持续时间，100 毫秒的倍数</p></li>
<li><p>3字节:强度</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>0x19 0x00 0x05 0xff</p></td>
</tr>
</tbody>
</table>
<p>类型0x85 表示指令 <a class="reference internal" href="#dwm-alarm-start"><span class="std std-ref">dwm_alarm_start</span></a>。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
</div>
</div>


           </div>
