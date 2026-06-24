---
title: "dwm_panid_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-panid-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-panid-get/"
order: 205
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-panid-get">
<span id="id1"></span><h1>dwm_panid_get</h1>
<p>Gets the UWB network identifier.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_panid_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_panid_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint16_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">panid</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>none</em>)</p></li>
<li><p><strong>output</strong> – 16-bit unsigned integer (<em>the PAN ID</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint16_t</span><span class="w"> </span><span class="n">panid</span><span class="p">;</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">DWM_OK</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">dwm_panid_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">panid</span><span class="p">))</span><span class="w"> </span><span class="p">{</span>
<span class="w"> </span><span class="n">printf</span><span class="p">(</span><span class="s">"panid=%u</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w"> </span><span class="n">printf</span><span class="p">(</span><span class="s">"FAILED</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
</tr>
<tr class="row-odd"><td><p>0x2F</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x2F means command dwm_panid_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value
(see
error
codes)</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x4D</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>2 bytes
in little
endian -
pan ID</p></td>
</tr>
<tr class="row-even"><td><p>0x01 0x02</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
<div class="line">Type 0x4D means PANID</div>
</div>
</div>


           </div>
