---
title: "dwm_dev_info_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-dev-info-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-dev-info-get/"
order: 177
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-dev-info-get">
<span id="id1"></span><h1>dwm_dev_info_get</h1>
<p>Gets the firmware ID, firmware version, configuration version, and hardware version of the module.
Firmware ID has a default value 1 on the gateway and a default value 2 on DWM1001.
Firmware with ID 0 on the gateway and firmware with ID 1 on the DWM1001 are used as possible backups.
The backup firmware is used during firmware updates.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_dev_info_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_dev_info_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_dev_info_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">info</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, fw_id, fw_bckp_version, fw_version, fw_bckp_cksum, fw_cksum, cfg_version, hw_version</p></li>
<li><p><strong>fw_id</strong> – 32-bits integer (<em>ID of a firmware that is currently active</em>)</p></li>
<li><p><strong>fw_bckp_version</strong> – 32-bits integer (<em>maj, min, patch, res, var</em>)</p></li>
<li><p><strong>fw_version</strong> – 32-bits integer (<em>maj, min, patch, res, var</em>)</p></li>
<li><p><strong>fw_bckp_cksum</strong> – 32-bits integer</p></li>
<li><p><strong>fw_cksum</strong> – 32-bits integer</p></li>
<li><p><strong>cfg_version</strong> – 32-bits integer</p></li>
<li><p><strong>hw_version</strong> – 32-bits integer</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_dev_info_t</span><span class="w"> </span><span class="n">info</span><span class="p">;</span>
<span class="n">dwm_dev_info_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">info</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"FW ID=%d</span><span class="se">\n</span><span class="s">”, info.fw_id);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"FW version: maj(%d) min(%d) patch(%d) res(%d) var(%d)</span><span class="se">\n</span><span class="s">”, info.fw_ver[1].maj, info.fw_ver[1].min, info.fw_ver[1].patch, info.fw_ver[1].res, info .fw_ver[1].var);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"CFG version: x%08x</span><span class="se">\n</span><span class="s">”, info.cfg_ver);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"HW version: x%08x</span><span class="se">\n</span><span class="s">”, info.hw_ver);</span>
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
<tr class="row-odd"><td><p>0x15</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x15 means command <a class="reference internal" href="#dwm-dev-info-get"><span class="std std-ref">dwm_dev_info_get</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 41%">
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
<td rowspan="2"><p>0x50</p></td>
<td rowspan="2"><p>0x1C</p></td>
<td><p>device information</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">0x07 0x01 0x00 0x02 0x11 0x01 0x00</div>
<div class="line">0x9d 0x59 0x9b 0x52 0x90 0x81 0x00</div>
<div class="line">0x01 0x01 0x01 0x03 0x01 0xd2 0x81</div>
<div class="line">0x01 0x00 0x00 0x00 0x01 0x01 0x03</div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
<div class="line">Type 0x50 means device information</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 27%">
<col style="width: 27%">
<col style="width: 21%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p><strong>Device information TLV encoding</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>fw_id</p></td>
<td><div class="line-block">
<div class="line">fw_bckp_version</div>
<div class="line">fw_version</div>
</div>
</td>
<td><div class="line-block">
<div class="line">fw_bckp_cksum</div>
<div class="line">fw_cksum</div>
</div>
</td>
<td><p>cfg_version</p></td>
<td><p>hw</p></td>
</tr>
<tr class="row-odd"><td><p>bytes 0-3</p></td>
<td><div class="line-block">
<div class="line">bytes 4-7</div>
<div class="line">bytes 8-11</div>
</div>
</td>
<td><div class="line-block">
<div class="line">bytes 12-15</div>
<div class="line">bytes 16-19</div>
</div>
</td>
<td><p>bytes 20-23</p></td>
<td><p>bytes 24-27</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p><strong>fw0_version and fw1_version TLV encoding</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>maj</strong></p></td>
<td><p><strong>min</strong></p></td>
<td><p><strong>patch</strong></p></td>
<td><p><strong>res</strong></p></td>
<td><p><strong>var</strong></p></td>
</tr>
<tr class="row-odd"><td><p>bits 24
- 31</p></td>
<td><p>bits 16
- 23</p></td>
<td><p>bits 8 -
15</p></td>
<td><p>bits 4 -
7</p></td>
<td><p>bits 0 -
3</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
