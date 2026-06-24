---
title: "dwm_hw_ver_set_once"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-hw-ver-set-once"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-hw-ver-set-once/"
order: 191
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-hw-ver-set-once">
<span id="id1"></span><h1>dwm_hw_ver_set_once</h1>
<p>Sets the hardware version in the One-Time Programmable memory.
The hardware version cannot be changed after it is successfully set by this call!
Supported HW versions are:</p>
<blockquote>
<div><ul class="simple">
<li><p>LC8A_A - 0x01100811 (LC8 with DWM1001)</p></li>
<li><p>LC8A_B - 0x01100812 (LC8 with DWM1001)</p></li>
<li><p>MDEK1001 - 0x02100111 (DWM1001-DEV with DWM1001C)</p></li>
<li><p>LC5A_E - 0x01100515 (LC5 with DWM1001)</p></li>
</ul>
</div></blockquote>
<p>UWB must be in offline mode for the write operation to complete successfully.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_hw_ver_set_once">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_hw_ver_set_once</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_hw_ver_t</span></span><span class="w"> </span><span class="n"><span class="pre">ver</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hw_version</strong> – 32-bits integer</p></li>
<li><p><strong>output</strong> – none</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_hw_ver_t</span><span class="w"> </span><span class="n">ver</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_hw_ver_set_once</span><span class="p">(</span><span class="n">ver</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"HW version set (%d)</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="o">?</span><span class="w"> </span><span class="s">"ok"</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="s">"failed"</span><span class="p">));</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x84</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>Hardware version
in little endian
(e.g. 0x02110100)</p></td>
</tr>
<tr class="row-even"><td><p>0x00 0x01 0x11
0x02</p></td>
</tr>
</tbody>
</table>
<p>Type 0x84 (132 dec) means command dwm_hw_ver_set_once</p>
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
<td><p>Value (see error
codes)</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</p>
</div>


           </div>
