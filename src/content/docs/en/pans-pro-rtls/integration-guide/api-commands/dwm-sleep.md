---
title: "dwm_sleep"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-sleep"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-sleep/"
order: 130
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-sleep">
<span id="id1"></span><h1>dwm_sleep</h1>
<p>Enables the device to enter the sleep state (if it is in low-power mode).
The sleep mode may be delayed internally if necessary.
Simply put, the device is not guaranteed to enter sleep mode immediately after the call to dwm_sleep.
It should only be called from the thread context if used in a user application.
This function blocks until dwm_wake_up is called.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_sleep">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_sleep</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – none</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="cm">/* THREAD 1: sleep and block*/</span>
<span class="n">dwm_sleep</span><span class="p">();</span>
<span class="cm">/*do something*/</span>
<span class="p">...</span>
<span class="cm">/*THREAD 2: wait until event */</span>
<span class="n">dwm_evt_wait</span><span class="p">(</span><span class="o">&amp;</span><span class="n">evt</span><span class="p">);</span>
<span class="cm">/*unblock dwm_sleep()*/</span>
<span class="n">dwm_wake_up</span><span class="p">();</span>
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
<tr class="row-odd"><td><p>0x0A</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x0A means command dwm_sleep</p>
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
