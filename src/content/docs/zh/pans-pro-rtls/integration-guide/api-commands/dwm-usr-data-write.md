---
title: "dwm_usr_data_write"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-write"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-write/"
order: 217
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-usr-data-write">
<span id="id1"></span><h1>dwm_usr_data_write</h1>
<p>向 UWB 网络发送用户数据。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_usr_data_write">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_usr_data_write</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span>, <span class="n"><span class="pre">boolean_t</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – 数据, len, 重写</p></li>
<li><p><strong>data</strong> – 最大 34 字节 (<em>要写入的用户数据</em>)</p></li>
<li><p><strong>len</strong> – (<em>数据长度，最大 34 字节</em>)</p></li>
<li><p><strong>overwrite</strong> – bool (<em>强制写入，将覆盖尚未发送到网关的数据</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">len</span><span class="p">,</span><span class="w"> </span><span class="n">data</span><span class="p">[</span><span class="n">DWM_USR_DATA_LEN_MAX</span><span class="p">];</span>
<span class="n">len</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_USR_DATA_LEN_MAX</span><span class="p">;</span>
<span class="n">dwm_usr_data_write</span><span class="p">(</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">len</span><span class="p">,</span><span class="w"> </span><span class="nb">false</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 29%">
<col style="width: 29%">
<col style="width: 43%">
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
<tr class="row-odd"><td rowspan="2"><p>0x1A</p></td>
<td rowspan="2"><p>0x23</p></td>
<td><div class="line-block">
<div class="line">字节 0: 标志</div>
<div class="line-block">
<div class="line">- overwrite (bit 0)</div>
<div class="line">- reserved (bit 1 - bit 7)</div>
</div>
</div>
<div class="line-block">
<div class="line">字节 1 - N：用户数据 (2 &lt;= N &lt;= 34)</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x01 0x01 0x02 0x03
…. 0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>类型0x1A 表示指令 dwm_usr_data_write</p>
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
<p>类型0x40 表示命令的 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p>
</div>


           </div>
