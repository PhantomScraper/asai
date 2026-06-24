---
title: "dwm_dev_status_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-dev-status-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-dev-status-get/"
order: 177
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-dev-status-get">
<span id="id1"></span><h1>dwm_dev_status_get</h1>
<p>此命令读取设备状态。 在用户应用程序（片上库）中使用时，电池电量不可用，因为它允许使用 ADC 外设。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_dev_status_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_dev_status_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, 正常运行时间, battery_level, 温度</p></li>
<li><p><strong>uptime</strong> – 32 位无符号整数 (<em>以秒为单位的正常运行时间</em>)</p></li>
<li><p><strong>battery_level</strong> – 8 位无符号整数 (<em>电池电量，以百分比表示，用户应用程序库中没有提供</em>)</p></li>
<li><p><strong>temperature</strong> – 16位整数 (<em>温度，单位°C</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_dev_status_t</span><span class="w"> </span><span class="n">status</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="n">printf</span><span class="p">(</span><span class="s">"uptime=%lu</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">uptime</span><span class="p">);</span>
<span class="w">   </span><span class="n">printf</span><span class="p">(</span><span class="s">"temperature=%d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">temperature</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't read device status, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
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
<tr class="row-odd"><td><p>0x25</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x25 (37 dec) 表示命令 <a class="reference internal" href="#dwm-dev-status-get"><span class="std std-ref">dwm_dev_status_get</span></a>。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x59</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><div class="line-block">
<div class="line">运行时间（字节 0-3）</div>
<div class="line">battery_level (字节 4)</div>
<div class="line">保留（字节 5）</div>
<div class="line">温度（字节 6-7）</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x9d
0x16
0x00
0x00
0x64
0x00
0x21
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型 0x59 (89 dec) 表示设备状态</div>
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
</div>
</div>


           </div>
