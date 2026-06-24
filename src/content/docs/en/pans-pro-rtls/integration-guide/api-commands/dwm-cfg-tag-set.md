---
title: "dwm_cfg_tag_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set/"
order: 176
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cfg-tag-set">
<span id="id1"></span><h1>dwm_cfg_tag_set</h1>
<p>Configures node as a tag with given options. The BLE option cannot be enabled with encryption.
Otherwise, the configuration is considered invalid and will not be used.
Encryption can’t be enabled if encryption key is not set. This call requires a reset for the
new configuration to take effect (<a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-reset#dwm-reset"><span class="std std-ref">dwm_reset</span></a>).</p>
<div class="admonition caution">
<p class="admonition-title">Caution</p>
<p>Normally, this call writes to internal flash when setting a new value.
Hence, it should not be used frequently and can take hundreds of milliseconds in the worst case,!</p>
</div>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_cfg_tag_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_cfg_tag_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_cfg_tag_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">cfg_tag</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – cfg_tag</p></li>
<li><p><strong>cfg_tag</strong> – stnry_en, low_power_en, meas_mode, loc_engine_en, led_en, ble_en, uwb_mode, fw_update_en, enc_en</p></li>
<li><p><strong>stnry_en</strong> – ‘0’ | ‘1’ (<em>Stationary detection enabled, if enabled, the stationary update rate is used instead of normal update rate if node is :param not moving</em>)</p></li>
<li><p><strong>meas_mode</strong> – ‘0’ | ‘1’ | ‘2’ | ‘3’ (<em>0 - Two way ranging, 1,2,3 - reserved</em>)</p></li>
<li><p><strong>low_power_en</strong> – ‘0’ | ‘1’ (<em>Low-power mode enable</em>)</p></li>
<li><p><strong>loc_engine_en</strong> – ‘0’ | ‘1’ (<em>0 means do not use internal Location Engine, 1 means internal Location Engine</em>)</p></li>
<li><p><strong>enc_en</strong> – ‘0’ | ‘1’ (<em>encryption enable</em>)</p></li>
<li><p><strong>led_en</strong> – ‘0’ | ‘1’ (<em>general purpose LEDs enable</em>)</p></li>
<li><p><strong>ble_en</strong> – ‘0’ | ‘1’ (<em>BLE enable</em>)</p></li>
<li><p><strong>uwb_mode</strong> – ‘0’ | ‘1’ | ‘2’ (<em>0-off, 1-passive, 2-active</em>)</p></li>
<li><p><strong>fw_update_en</strong> – ‘0’ | ‘1’ (<em>Firmware update enable</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_cfg_tag_t</span><span class="w"> </span><span class="n">cfg</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">stnry_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">meas_mode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_MEAS_MODE_TWR</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">low_power_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">loc_engine_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">enc_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">led_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">ble_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">fw_update_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">uwb_mode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_UWB_MODE_ACTIVE</span><span class="p">;</span>
<span class="n">dwm_cfg_tag_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cfg</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 50%">
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
<tr class="row-odd"><td rowspan="2"><p>0x05</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p><em>BYTE 1:</em></p>
<ul class="simple">
<li><p>bits 3-7: reserved</p></li>
<li><p>bit 2: stnry_en</p></li>
<li><p>bits 0-#. meas_mode: 0 -TWR, 1-3 reserved</p></li>
</ul>
<p><em>BYTE 0:</em></p>
<ul class="simple">
<li><p>bit 7: low_power_en</p></li>
<li><p>bit 6: loc_engine_en</p></li>
<li><p>bit 5: enc_en</p></li>
<li><p>bit 4: led_en</p></li>
<li><p>bit 3: ble_en</p></li>
<li><p>bit 2: fw_update_en</p></li>
<li><p>bits 0-#.uwb_mode</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>0x72 0x04</p></td>
</tr>
</tbody>
</table>
<p>Type 0x05 means command <a class="reference internal" href="#dwm-cfg-tag-set"><span class="std std-ref">dwm_cfg_tag_set</span></a></p>
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
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
</div>
</div>


           </div>
