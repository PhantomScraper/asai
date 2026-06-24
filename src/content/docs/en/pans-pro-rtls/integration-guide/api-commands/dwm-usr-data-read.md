---
title: "dwm_usr_data_read"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-read"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-read/"
order: 217
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-usr-data-read">
<span id="id1"></span><h1>dwm_usr_data_read</h1>
<p>Reads user data from the node. The new data received on UWB causes the setting of a dedicated flag in the status (see <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-status-get#dwm-status-get"><span class="std std-ref">dwm_status_get</span></a>) and causes the generation of an event in the user applications (see <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-evt-listener-register#dwm-evt-listener-register"><span class="std std-ref">dwm_evt_listener_register</span></a>).</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_usr_data_read">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_usr_data_read</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (<em>none</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, data, len</p></li>
<li><p><strong>data</strong> – 1-34 bytes (<em>the user data</em>)</p></li>
<li><p><strong>len</strong> – 1 byte (<em>length of the data</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">uint8_t data[DWM_USR_DATA_LEN_MAX];</span>
<span class="go">uint8_t len;</span>
<span class="go">len = DWM_USR_DATA_LEN_MAX;</span>
<span class="go">dwm_usr_data_read(data, &amp;len);</span>
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
<tr class="row-odd"><td><p>0x19</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x19 means command dwm_usr_data_read</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 31%">
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
<td rowspan="2"><p>0x4B</p></td>
<td rowspan="2"><p>0x22</p></td>
<td><p>byte 0 - N: user data
(1 &lt;= N &lt;= 33)</p></td>
</tr>
<tr class="row-even"><td><p>0x01 0x02
0x03 …
0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>Type 0x4B means user data</p>
</div>


           </div>
