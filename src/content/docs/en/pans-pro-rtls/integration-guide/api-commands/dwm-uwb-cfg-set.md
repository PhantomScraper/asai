---
title: "dwm_uwb_cfg_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-uwb-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-uwb-cfg-set/"
order: 222
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-uwb-cfg-set">
<span id="id1"></span><h1>dwm_uwb_cfg_set</h1>
<p>Sets UWB configuration parameters.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_uwb_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_uwb_cfg_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_uwb_cfg_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">cfg</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – pg_delay, tx_power</p></li>
<li><p><strong>pg_delay</strong> – 1 byte (<em>Transmitter Calibration – Pulse Generator Delay</em>)</p></li>
<li><p><strong>tx_power</strong> – 4 bytes (<em>TX Power Control</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_uwb_cfg_t</span><span class="w"> </span><span class="n">cfg</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">pg_delay</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">197</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">tx_power</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0xD0252525</span><span class="p">;</span>
<span class="n">dwm_uwb_cfg_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cfg</span><span class="p">);</span>
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
<tr class="row-odd"><td rowspan="2"><p>0x17</p></td>
<td rowspan="2"><p>0x05</p></td>
<td><div class="line-block">
<div class="line">1st byte:
pg_delay</div>
<div class="line">2nd-5th byte:
tx_power</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0xC3 0x85 0x65 0x45
0x25</p></td>
</tr>
</tbody>
</table>
<p>Type 0x17 means command dwm_uwb_cfg_set</p>
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
</div>


           </div>
