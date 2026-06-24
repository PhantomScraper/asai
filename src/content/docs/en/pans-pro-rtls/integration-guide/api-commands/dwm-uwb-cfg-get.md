---
title: "dwm_uwb_cfg_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-uwb-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-uwb-cfg-get/"
order: 219
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-uwb-cfg-get">
<span id="id1"></span><h1>dwm_uwb_cfg_get</h1>
<p>Gets UWB configuration parameters.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_uwb_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_uwb_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_uwb_cfg_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">uwb_cfg</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>node</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, pg_delay, tx_power</p></li>
<li><p><strong>pg_delay</strong> – 1 byte (<em>Transmitter Calibrati Pulse Generator Delay value</em>)</p></li>
<li><p><strong>tx_power</strong> – 4 bytes (<em>Units of transmission power control</em>)</p></li>
<li><p><strong>pg_delay_comp</strong> – 1 byte (<em>Transmitter Calibrati Pulse Generator Delay value,  Compensated</em>)</p></li>
<li><p><strong>tx_power_comp</strong> – 4 bytes (<em>Units of transmission power control, Compensated</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_uwb_cfg_t</span><span class="w"> </span><span class="n">uwb_cfg</span><span class="p">;</span>
<span class="n">dwm_uwb_cfg_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">uwb_cfg</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"delay=%x, power=%lx compensated(%x,%lx)</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span>
<span class="w">                     </span><span class="n">uwb_cfg</span><span class="p">.</span><span class="n">pg_delay</span><span class="p">,</span>
<span class="w">                     </span><span class="n">uwb_cfg</span><span class="p">.</span><span class="n">tx_power</span><span class="p">,</span>
<span class="w">                     </span><span class="n">uwb_cfg</span><span class="p">.</span><span class="n">compensated</span><span class="p">.</span><span class="n">pg_delay</span><span class="p">,</span>
<span class="w">                     </span><span class="n">uwb_cfg</span><span class="p">.</span><span class="n">compensated</span><span class="p">.</span><span class="n">tx_power</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x18</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x18 means command dwm_uwb_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 36%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>length</p></td>
<td><p>Value
(see
error
codes)</p></td>
<td><p>Type</p></td>
<td><p>length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x4F</p></td>
<td rowspan="2"><p>0x0A</p></td>
<td><div class="line-block">
<div class="line">1st byte: pg_delay</div>
<div class="line">2nd-5th byte: tx_power</div>
<div class="line">6th byte: pg_delay_comp</div>
<div class="line">7th-10th byte: tx_power_comp</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>hex: 0xC3
0x85 0x65 0x45
0x25 0xC4 0x85
0x65 0x45 0x25</p></td>
</tr>
</tbody>
</table>
<p>Type 0x4F means UWB configuration</p>
</div>


           </div>
