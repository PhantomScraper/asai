---
title: "dwm_upd_rate_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-set/"
order: 216
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-upd-rate-set">
<span id="id1"></span><h1>dwm_upd_rate_set</h1>
<p>Sets the position update rate and stationary update rate in hundreds of milliseconds.
This call typically writes to internal flash when a new value is set.
Therefore, it should not be called frequently. The response may take up to several hundred milliseconds in the worst case.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_upd_rate_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_upd_rate_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">update_rate</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">update_rate_stationary</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>update_rate</strong> – 16-bit integer (<em>position publication rate in multiples of 100 milliseconds, maximum is 1 minute, minimum is 100 ms</em>)</p></li>
<li><p><strong>update_rate_stationary</strong> – 16-bit integer (<em>position publication rate when node is not moving in multiples of 100 milliseconds, maximum is 1 minute, minimum is 100 ms</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_upd_rate_set</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="w"> </span><span class="mi">50</span><span class="p">);</span><span class="w"> </span><span class="cm">/* update rate 1 second. 5 seconds stationary */</span>
<span class="n">dwm_upd_rate_set</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span><span class="w"> </span><span class="cm">/* ERROR - must not be a zero */</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 32%">
<col style="width: 37%">
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
<tr class="row-odd"><td><p>0x03</p></td>
<td><p>0x04</p></td>
<td><p>The first 2 bytes
represents 16 bit
value in little
endian which is
update rate in
multiples of 100
ms (e.g. 0x0A 0x00
means 10) the second 2
bytes represents
16 bit value in
little endian
which is
stationary update
rate in multiples
of 100 ms</p></td>
</tr>
<tr class="row-even"><td></td>
<td></td>
<td><p>0x0A 0x00 0x014 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x03 means command dwm_upd_rate_set</p>
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
