---
title: "dwm_gpio_cfg_output"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output/"
order: 128
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-gpio-cfg-output">
<span id="id1"></span><h1>dwm_gpio_cfg_output</h1>
<p>将 GPIO 引脚配置为输出并设置值。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_gpio_cfg_output">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_gpio_cfg_output</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_idx</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">value</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>gpio_idx</strong> – 8 位整数（允许值见上一章）。</p></li>
<li><p><strong>value</strong> – 8 位整数（0 或 1）。</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C 代码示例 1</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_gpio_cfg_output</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_13</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">);</span>
<span class="n">dwm_gpio_cfg_output</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_13</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例 1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>引脚索引</p></td>
<td><p>引脚值</p></td>
</tr>
<tr class="row-even"><td><p>0x28</p></td>
<td><p>0x02</p></td>
<td><p>0x0D</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>类型 0x28 表示命令 <a class="reference internal" href="#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a></p>
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
<td><p>价值（参见错误代码）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</p>
<p><strong>SPI/UART 示例 2</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 24%">
<col style="width: 29%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="2"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>引脚索引(8:预留引脚）</p></td>
<td><p>引脚值</p></td>
</tr>
<tr class="row-even"><td><p>0x28</p></td>
<td><p>0x02</p></td>
<td><p>0x08</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>类型 0x28 表示命令 <a class="reference internal" href="#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a>。</p>
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
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td><div class="line-block">
<div class="line">0 OK</div>
<div class="line">1 Error</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</p>
</div>


           </div>
