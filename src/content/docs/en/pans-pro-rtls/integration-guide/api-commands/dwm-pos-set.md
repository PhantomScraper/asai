---
title: "dwm_pos_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-pos-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-pos-set/"
order: 207
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-pos-set">
<span id="id1"></span><h1>dwm_pos_set</h1>
<p>Sets the default position of the node.
The default position is not used in tag mode but is stored anyway.
This allows the module to be configured in anchor mode and use the value previously set by dwm_pos_set.
Normally, this call writes to internal flash when setting a new value.
Hence, it should not be used frequently. The response can take hundreds of milliseconds in the worst case!</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_pos_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_pos_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_pos_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">pos</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pos-&gt;x</strong> – 32-bit integer (position coordinate in millimeters)</p></li>
<li><p><strong>pos-&gt;y</strong> – 32-bit integer (position coordinate in millimeters)</p></li>
<li><p><strong>pos-&gt;z</strong> – 32-bit integer (position coordinate in millimeters)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example 1</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_pos_t</span><span class="w"> </span><span class="n">pos</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">qf</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">100</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">121</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">50</span><span class="p">;</span>
<span class="n">pos</span><span class="p">.</span><span class="n">z</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">251</span><span class="p">;</span>
<span class="n">dwm_pos_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">pos</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART example 1</strong></p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>0x01</p></td>
<td><p>0x0D</p></td>
<td><p>int32_t
in little
endian -
x
coordinate
in millimeters</p></td>
<td><p>int32_t
in little
endian -
y
coordinate
in millimeters</p></td>
<td><p>int32_t
in little
endian -
z
coordinate
in millimeters</p></td>
<td><p>uint8_t -</p>
<p>quality
factor
in percents
(0-100)</p>
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
<p>Type 0x01 means command dwm_pos_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 31%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value (see error codes)</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</p>
<p><strong>C code example 2</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">int32_t</span><span class="w"> </span><span class="n">x</span><span class="p">,</span><span class="n">z</span><span class="p">;</span>
<span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">121</span><span class="p">;</span>
<span class="n">z</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">251</span><span class="p">;</span>
<span class="n">dwm_pos_set_xyz</span><span class="p">(</span><span class="o">&amp;</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">z</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART example 2</strong></p>
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
<tr class="row-odd"><th class="head" colspan="8"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x80</p></td>
<td rowspan="2"><p>0x0C</p></td>
<td rowspan="2"><p>0x42</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>int32_t
in
little
endian -
x
coordinate
in millimeters</p></td>
<td rowspan="2"><p>0x44</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>int32_t
in
little
endian -
z
coordinate
in millimeters</p></td>
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
<div class="line">Type 0x80 means command dwm_pos_set_xyz</div>
<div class="line">Type 0x42 means position coordinate x</div>
<div class="line">Type 0x44 means position coordinate z</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
