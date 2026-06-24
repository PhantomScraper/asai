---
title: "dwm_cfg_anchor_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cfg-anchor-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-anchor-set/"
order: 174
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cfg-anchor-set">
<span id="id1"></span><h1>dwm_cfg_anchor_set</h1>
<p>Configures node as an anchor with given options. The BLE option cannot be enabled with encryption. Otherwise, the configuration is considered invalid and will not be used. Encryption cannot be enabled if encryption key is not set. This call requires a reset for the new configuration to take effect (<a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-reset#dwm-reset"><span class="std std-ref">dwm_reset</span></a>). Enabling encryption on the initiator will automatically enable encryption of all nodes with the same encryption key set (). This enables encryption for the whole network with the same pan ID (network ID) and encryption key remotely from one place.</p>
<div class="admonition caution">
<p class="admonition-title">Caution</p>
<p>Normally, this call writes to internal flash when setting a new value. Hence, it should not be used frequently and can take hundreds of milliseconds  in the worst case.!</p>
</div>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_cfg_anchor_set">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_cfg_anchor_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_cfg_anchor_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">cfg_anchor</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – cfg_anchor</p></li>
<li><p><strong>cfg_anchor</strong> – initiator, gateway, led_en, ble_en, uwb_mode, fw_update_en, enc_en</p></li>
<li><p><strong>initiator</strong> – ‘0’ | ‘1’ (<em>Initiator role enable</em>)</p></li>
<li><p><strong>gateway</strong> – ‘0’ | ‘1’ (<em>Gateway role enable</em>)</p></li>
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

<div class="admonition note">
<p class="admonition-title">Note</p>
<div class="line-block">
<div class="line">Available only when the firmware is compiled with UWB routing backhaul:</div>
<div class="line">uwb_bh_routing: ‘0’ | ‘1’ | ‘2’ (<em>0(OFF) - anchor will not become a routing anchor, 1(ON) - anchor will be preferred by the routing algorithm to be chosen as a routing anchor, 2(AUTO) - Whether anchor becomes routing or not depends entirely on the routing algorithm</em>)</div>
</div>
</div>
<p><strong>C code example</strong></p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_cfg_anchor_t</span><span class="w"> </span><span class="n">cfg</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">initiator</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">gateway</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="cm">/* [Available only when the firmware is compiled with UWB routing backhaul: cfg.uwb_bh_routing: DWM_UWB_BH_ROUTING_AUTO;] */</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">enc_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">led_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">ble_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">fw_update_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">uwb_mode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_UWB_MODE_OFF</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_cfg_anchor_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cfg</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_ERR_PERM</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"Error: either encryption or BLE can be enabled, encryption can be enabled only if encryption key is set</span><span class="se">\n</span><span class="s">”);</span>
<span class="p">}</span>
<span class="n">dwm_reset</span><span class="p">();</span>
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
<tr class="row-even"><td rowspan="2"><p>0x07</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><ul class="simple">
<li><p>(bits 0-#) uwb_mode</p></li>
<li><p>(bit 2) fw_update_en</p></li>
<li><p>(bit 3) ble_en</p></li>
<li><p>(bit 4) led_en</p></li>
<li><p>(bit 5) enc_en</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>0x9C 0x02</p></td>
</tr>
</tbody>
</table>
<p>Type 0x07 means command <a class="reference internal" href="#dwm-cfg-anchor-set"><span class="std std-ref">dwm_cfg_anchor_set</span></a></p>
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
