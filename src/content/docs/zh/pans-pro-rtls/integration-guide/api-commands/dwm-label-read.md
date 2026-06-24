---
title: "dwm_label_read"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-label-read"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-label-read/"
order: 195
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-label-read">
<span id="id1"></span><h1>dwm_label_read</h1>
<p>读取节点标签。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_label_read">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_label_read</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">label</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">len</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>无</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, data, len</p></li>
<li><p><strong>data</strong> – 0-16字节 (<em>标签</em>)</p></li>
<li><p><strong>len</strong> – 1 字节 (<em>标签长度</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">label</span><span class="p">[</span><span class="n">DWM_LABEL_LEN_MAX</span><span class="p">];</span>
<span class="kt">uint8_t</span><span class="w"> </span><span class="n">len</span><span class="p">;</span>
<span class="nl">len</span><span class="p">:</span><span class="w"> </span><span class="n">DWM_LABEL_LEN_MAX</span><span class="p">;</span>
<span class="n">dwm_label_read</span><span class="p">(</span><span class="n">label</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">len</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x1C</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x1C 表示指令 dwm_label_read</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 16%">
<col style="width: 16%">
<col style="width: 16%">
<col style="width: 16%">
<col style="width: 19%">
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
<td rowspan="2"><p>0x4C</p></td>
<td rowspan="2"><p>0x10</p></td>
<td><p>标签 - 最多 16 字节</p></td>
</tr>
<tr class="row-even"><td><p>0x01
0x02
0x03 …
0x0F
0x10</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x4C表示标签</div>
</div>
</div>


           </div>
