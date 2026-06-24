---
title: "dwm_pos_set"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-pos-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-pos-set/"
order: 206
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-pos-set">
<span id="id1"></span><h1>dwm_pos_set</h1>
<p>设置节点的默认位置。 默认位置在标签模式下不会被使用，但还是会被存储。 这样就可以在锚点模式下配置模块，并使用之前通过 dwm_pos_set 设置的值。 通常，在设置新值时，该调用会写入内部闪存。 因此，不应频繁使用。 在最坏的情况下，响应可能需要数百毫秒！</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_pos_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_pos_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_pos_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">pos</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pos-&gt;x</strong> – 32 位整数（以毫米为单位的位置坐标）</p></li>
<li><p><strong>pos-&gt;y</strong> – 32 位整数（以毫米为单位的位置坐标）</p></li>
<li><p><strong>pos-&gt;z</strong> – 32 位整数（以毫米为单位的位置坐标）</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C 代码示例 1</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_pos_t</span><span class="w"> </span><span class="n">pos</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">qf</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">100</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">121</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">50</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">z</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">251</span><span class="p">;</span>
<span class="n">dwm_pos_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">pos</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例 1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 19%">
<col style="width: 19%">
<col style="width: 19%">
<col style="width: 18%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>0x01</p></td>
<td><p>0x0D</p></td>
<td><p>int32_t小端序后是以毫米为单位的- x 坐标</p></td>
<td><p>int32_t小端序后是以毫米为单位的- y坐标</p></td>
<td><p>int32_t小端序后是以毫米为单位的- z坐标</p></td>
<td><p>uint8_t -</p>
<p>质量系数，单位为百分数（0-100）</p>
</td>
</tr>
<tr class="row-even"><td></td>
<td></td>
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
<p>类型0x01 表示指令 dwm_pos_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 31%">
<col style="width: 39%">
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
<p><strong>C 代码示例2</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">int32_t</span><span class="w"> </span><span class="n">x</span><span class="p">,</span><span class="n">z</span><span class="p">;</span>
<span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">121</span><span class="p">;</span>
<span class="n">z</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">251</span><span class="p">;</span>
<span class="n">dwm_pos_set_xyz</span><span class="p">(</span><span class="o">&amp;</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">z</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例 2</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 20%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x80</p></td>
<td rowspan="2"><p>0x0C</p></td>
<td rowspan="2"><p>0x42</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>int32_t小端序后是以毫米为单位的- x 坐标</p></td>
<td rowspan="2"><p>0x44</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>int32_t小端序后是以毫米为单位的- z坐标</p></td>
</tr>
<tr class="row-even"><td><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00</p></td>
<td><p>0x9c
0x0e
0x00
0x00
0x00
0x64
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x80 表示指令 dwm_pos_set_xyz</div>
<div class="line">类型0x42表示位置坐标x</div>
<div class="line">类型0x44表示位置坐标z</div>
</div>
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
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
