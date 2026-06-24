---
title: "dwm_serial_cfg_set"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-serial-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-serial-cfg-set/"
order: 209
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-serial-cfg-set">
<span id="id1"></span><h1>dwm_serial_cfg_set</h1>
<p>该命令仅适用于以太网网关。 设置 UART/USB 等串行接口的配置。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_serial_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_serial_cfg_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">mode</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – 模式</p></li>
<li><p><strong>mode</strong> – ‘0’ | ‘1’ (<em>0 - 二进制模式 , 1 - shell 模式</em>)</p></li>
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
<col style="width: 29%">
<col style="width: 16%">
<col style="width: 55%">
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
<tr class="row-odd"><td rowspan="2"><p>0x38</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><div class="line-block">
<div class="line">字节 0: 保留</div>
<div class="line">字节 1:UART/USB 模式</div>
<div class="line">字节 2:保留</div>
<div class="line">字节 3:保留</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x00 0x10 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x38表示命令dwm_serial_cfg_set</div>
</div>
</div>


           </div>
