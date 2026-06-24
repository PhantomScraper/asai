---
title: "dwm_dev_status_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-dev-status-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-dev-status-get/"
order: 178
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-dev-status-get">
<span id="id1"></span><h1>dwm_dev_status_get</h1>
<p>This command reads the device status. The battery level is unavailable when used
in the user application (on-chip library), as it allows for the use of the ADC peripheral.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_dev_status_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_dev_status_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>none</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, uptime, battery_level, temperature</p></li>
<li><p><strong>uptime</strong> – 32-bit unsigned integer (<em>uptime in seconds</em>)</p></li>
<li><p><strong>battery_level</strong> – 8-bit unsigned integer (<em>battery level in percents, not available in the user application library</em>)</p></li>
<li><p><strong>temperature</strong> – 16-bit integer (<em>temperature in °C</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
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
<tr class="row-odd"><td><p>0x25</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x25 (37 dec) means command <a class="reference internal" href="#dwm-dev-status-get"><span class="std std-ref">dwm_dev_status_get</span></a>.</p>
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
<td rowspan="2"><p>0x59</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><div class="line-block">
<div class="line">uptime (byte 0-3)</div>
<div class="line">battery_level (byte 4)</div>
<div class="line">reserved (byte 5)</div>
<div class="line">temperature (byte 6-7)</div>
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
<div class="line">Type 0x59 (89 dec) means device status</div>
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
</div>
</div>


           </div>
