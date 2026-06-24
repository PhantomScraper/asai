---
title: "dwm_mac_addr_set_once"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set-once"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set-once/"
order: 200
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-set-once">
<span id="id1"></span><h1>dwm_mac_addr_set_once</h1>
<p>Writes the MAC address list to OTP memory and must be used carefully! The values
cannot be modified after they have been written! It is intended to be used in the
production phase to provide a MAC address pool for the device to be used by UWB,
BLE, Ethernet or Wi-Fi interface. Currently, the list of the MAC addresses is
assigned to various interfaces as follows:</p>
<ul class="simple">
<li><p>MAC address 0 is assigned to the UWB interface. The two least significant bytes must not be equal to 0x0000 or 0xFFFF.</p></li>
<li><p>MAC address 1 is assigned to the BLE interface. The address will be used as the Public BLE address.</p></li>
<li><p>MAC address 2 and MAC address 3 are assigned to the Ethernet and the Wi-Fi interface, respectively. The address should be in the EUI-48 format respecting the LAA/UAA and the U/I bit.</p></li>
</ul>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_set_once">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_set_once</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">addr</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">count</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – mac_addr_0, [mac_addr_1], [mac_addr_2], [mac_addr_3]</p></li>
<li><p><strong>mac_addr_0</strong> – 48-bits value (<em>UWB MAC address in little endian</em>)</p></li>
<li><p><strong>mac_addr_1</strong> – 48-bits value (<em>BLE MAC address in little endian</em>)</p></li>
<li><p><strong>mac_addr_2</strong> – 48-bits value (<em>Ethernet MAC address in little endian</em>)</p></li>
<li><p><strong>mac_addr_3</strong> – 48-bits value (<em>WIFI MAC address in little endian</em>)</p></li>
<li><p><strong>output:</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_list_t</span><span class="w"> </span><span class="n">mac_addr_list</span><span class="p">;</span>
<span class="n">dwm_mac_addr_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="n">memcpy</span><span class="p">(</span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="w"> </span><span class="p">(</span><span class="kt">uint8_t</span><span class="p">[</span><span class="n">DWM_MAC_ADDR_LEN</span><span class="p">]){</span><span class="mh">0xaa</span><span class="p">,</span><span class="w"> </span><span class="mh">0xbb</span><span class="p">,</span><span class="w"> </span><span class="mh">0xcc</span><span class="p">,</span><span class="w"> </span><span class="mh">0xdd</span><span class="p">,</span><span class="w"> </span><span class="mh">0xee</span><span class="p">,</span><span class="w"> </span><span class="mh">0xff</span><span class="p">},</span><span class="w"> </span><span class="n">DWM_MAC_ADDR_LEN</span><span class="p">);</span>
<span class="nl">rv</span><span class="p">:</span><span class="w"> </span><span class="n">dwm_mac_addr_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't set MAC address list, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 22%">
<col style="width: 56%">
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
<tr class="row-odd"><td rowspan="2"><p>0x82</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(byte 0-5) MAC address 0 in little endian</div>
<div class="line">(byte 6-11) MAC address 1 in little endian</div>
<div class="line">(byte 12-17) MAC address 2 in little endian</div>
<div class="line">(byte 18-23) MAC address 3 in little endian</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>…</p></td>
</tr>
</tbody>
</table>
<p>Type 0x82 (130 dec) means command dwm_mac_addr_set_once</p>
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
