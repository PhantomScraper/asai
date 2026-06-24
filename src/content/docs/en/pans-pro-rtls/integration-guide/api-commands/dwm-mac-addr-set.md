---
title: "dwm_mac_addr_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set/"
order: 201
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-set">
<span id="id1"></span><h1>dwm_mac_addr_set</h1>
<p>Sets the  MAC address of the BLE, UWB, Ethernet or Wi-Fi interface and need reset
to take effect. It Should not be used frequently since it writes the internal non-volatile memory.
Factory reset is needed (<em>dwm_factory_reset</em>) to use the default MAC address.
The two least significant bytes of the UWB MAC address must not be equal to 0x0000 or 0xFFFF.
The BLE address can be either the Random or the Public BLE address.
The Ethernet and the Wi-Fi address must respect the EUI-48 format, and the U/I bits must be set accordingly.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_type_t</span></span><span class="w"> </span><span class="n"><span class="pre">type</span></span>, <span class="n"><span class="pre">dwm_mac_addr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">addr</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – addr_type, addr_value</p></li>
<li><p><strong>addr_type</strong> – 8-bit integer (<em>0=UWB address, 1=BLE Random address, 2=BLE Public address, 3=ETH address, 4= WIFI address, ETH and WIFI is supported only on the gateway</em>)</p></li>
<li><p><strong>addr_value</strong> – 6 bytes (<em>6 byte long MAC address</em>)</p></li>
<li><p><strong>output:</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_t</span><span class="w"> </span><span class="n">addr</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xAA</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xBB</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xCC</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xDD</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xEE</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xFF</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="o">:</span><span class="w"> </span><span class="n">dwm_mac_addr_set</span><span class="p">(</span><span class="n">NODE_ADDR_TYPE_UWB</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">addr</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't set node address, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 26%">
<col style="width: 26%">
<col style="width: 48%">
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
<tr class="row-odd"><td rowspan="2"><p>0x2D</p></td>
<td rowspan="2"><p>0x07</p></td>
<td><div class="line-block">
<div class="line">byte 0: MAC address type</div>
<div class="line">bytes 1-6: MAC address in little endian</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x00 0xEF 0xCD 0xAB
0x56 0x34 0x12</p></td>
</tr>
</tbody>
</table>
<p>Type 0x2D (45 dec) means command dwm_mac_addr_set</p>
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
