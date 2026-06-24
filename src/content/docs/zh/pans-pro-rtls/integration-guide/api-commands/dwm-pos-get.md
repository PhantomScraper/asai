---
title: "dwm_pos_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-pos-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-pos-get/"
order: 220
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-pos-get">
<span id="id1"></span><h1>dwm_pos_get</h1>
<p>获取节点的位置。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_pos_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_pos_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_pos_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">pos</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, <strong>位置</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_pos_t</span><span class="w"> </span><span class="n">pos</span><span class="p">;</span>
<span class="n">dwm_pos_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">pos</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"%ld </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">pos</span><span class="p">.</span><span class="n">x</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"%ld </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">pos</span><span class="p">.</span><span class="n">y</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"%ld </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">pos</span><span class="p">.</span><span class="n">z</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"%u </span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">pos</span><span class="p">.</span><span class="n">qf</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x02</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x02 表示命令 pos_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 6%">
<col style="width: 19%">
<col style="width: 6%">
<col style="width: 7%">
<col style="width: 15%">
<col style="width: 0%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 0%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="6"><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x41</p></td>
<td rowspan="2"><p>0x0D</p></td>
<td><p>int32_t 小端序-</p>
<p>x坐标，单位为毫米</p>
</td>
<td colspan="2"><p>int32_t 小端序-</p>
<p>y坐标，单位为毫米</p>
</td>
<td colspan="2"><p>int32_t 小端序-</p>
<p>z坐标，单位为毫米</p>
</td>
<td><p>uint8_t -</p>
<p>质量因子，单位为百分数(0 -100)</p>
</td>
</tr>
<tr class="row-even"><td colspan="6"><p>0x4b 0x0a 0x00 0x00 0x1f 0x04</p>
<p>0x00 0x00 0x9c 0x0e 0x00</p>
<p>0x00 0x64</p>
</td>
</tr>
</tbody>
</table>
<p>类型0x40 表示前一个命令的 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p>
<p>类型0x41型表示位置（x,y,z,pqf）</p>
</div>


           </div>
