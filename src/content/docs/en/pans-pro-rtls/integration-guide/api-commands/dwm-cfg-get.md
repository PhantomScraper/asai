---
title: "dwm_cfg_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-get/"
order: 175
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cfg-get">
<span id="id1"></span><h1>dwm_cfg_get</h1>
<p>Gets the current configuration options of the node.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_cfg_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_cfg_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">cfg</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output:</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, mode, initiator, gateway, low_power_en, meas_mode, loc_engine_en, led_en, ble_en, uwb_mode, fw_update_en, enc_en,</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Available only when the firmware is compiled with UWB routing backhaul: cfg.uwb_bh_routing</p>
</div>
<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_cfg_t</span><span class="w"> </span><span class="n">cfg</span><span class="p">;</span>
<span class="n">dwm_cfg_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cfg</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"mode %u </span><span class="se">\n</span><span class="s">”, cfg.mode);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"initiator %u </span><span class="se">\n</span><span class="s">”, cfg.initiator);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"gateway %u </span><span class="se">\n</span><span class="s">”, cfg.gateway);</span>
<span class="cm">/*[Available only when the firmware is compiled with UWB routing backhaul:* **printf("UWB mode %u \n”, cfg.uwb_bh_routing); */</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"motion detection enabled %u </span><span class="se">\n</span><span class="s">”, cfg.stnry_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"measurement mode %u </span><span class="se">\n</span><span class="s">”, cfg.meas_mode);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"low-power enabled %u </span><span class="se">\n</span><span class="s">”, cfg.low_power_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"internal location engine enabled %u </span><span class="se">\n</span><span class="s">”, cfg.loc_engine_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"encryption enabled %u </span><span class="se">\n</span><span class="s">”, cfg.common.enc_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"LED enabled %u </span><span class="se">\n</span><span class="s">”, cfg.common.led_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"BLE enabled %u </span><span class="se">\n</span><span class="s">”, cfg.common.ble_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"firmware update enabled %u </span><span class="se">\n</span><span class="s">”, cfg.common.fw_update_en);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"UWB mode %u </span><span class="se">\n</span><span class="s">”, cfg.common.uwb_mode);</span>
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
<tr class="row-odd"><td><p>0x08</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x08 means command <a class="reference internal" href="#dwm-cfg-get"><span class="std std-ref">dwm_cfg_get</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 55%">
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
<td><p>length</p></td>
<td><p>value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x46</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p><em>BYTE 1:</em> Available only when the firmware is compiled
with UWB routing backhaul: (bits 6-7)
uwb_bh_routing : 0 - OFF, 1 - ON, 2 - AUTO</p>
<ul class="simple">
<li><p>bits 0-1: meas_mode:  0 - TWR, 1-3 not supported</p></li>
<li><p>bit 2: stnry_en</p></li>
<li><p>bit 3: gateway</p></li>
<li><p>bit 4: initiator</p></li>
<li><p>bit 5: mode : 0 - tag, 1 - anchor</p></li>
</ul>
<p><em>BYTE 0</em></p>
<ul class="simple">
<li><p>bits 0-1: uwb_mode</p></li>
<li><p>bit 2: fw_update_en</p></li>
<li><p>bit 3: ble_en</p></li>
<li><p>bit 4: led_en</p></li>
<li><p>bit 5: enc_en</p></li>
<li><p>bit 6: loc_engine_en</p></li>
<li><p>bit 7: low_power_en</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>0x1C 0x20
(anchor, leds, ble, fwup, uwb mode off)</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
<div class="line">Type 0x46 means node configuration</div>
</div>
</div>


           </div>
