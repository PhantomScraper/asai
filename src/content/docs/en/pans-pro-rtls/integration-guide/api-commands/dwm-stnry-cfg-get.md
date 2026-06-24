---
title: "dwm_stnry_cfg_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-get/"
order: 212
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-stnry-cfg-get">
<span id="id1"></span><h1>dwm_stnry_cfg_get</h1>
<p>Reads configuration of the stationary mode that is used by the tag node.
The configuration can be read even if stationary detection is disabled (see <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set#dwm-cfg-tag-set"><span class="std std-ref">dwm_cfg_tag_set</span></a>).</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_stnry_cfg_get">
<span class="n"><span class="pre">uint16_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_stnry_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_stnry_sensitivity_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">sensitivity</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, sensitivity</p></li>
<li><p><strong>sensitivity</strong> – ‘0’ | ‘1’ | ‘2’ (<em>0 - LOW [512 mg] , 1 - NORMAL [2048 mg], 2 - HIGH [4064 mg]</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_stnry_sensitivity_t</span><span class="w"> </span><span class="n">sensitivity</span><span class="p">;</span>
<span class="n">dwm_stnry_cfg_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">sensitivity</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x12</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x12 means command dwm_stnry_cfg_get</p>
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
<td><p>length</p></td>
<td><p>Value
(see
error
codes)</p></td>
<td><p>Type</p></td>
<td><p>length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x4A</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
<div class="line">Type 0x4A means stationary sensitivity</div>
</div>
</div>


           </div>
