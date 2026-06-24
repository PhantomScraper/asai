---
title: "dwm_mac_addr_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-get/"
order: 199
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-get">
<span id="id1"></span><h1>dwm_mac_addr_get</h1>
<p>Gets the MAC address list used by the device. The device uses either the address
specified by the user or the default address. The default MAC address for each
interface can be changed only once by calling <em>dwm_mac_addr_set_once</em> which is
written to OTP memory and becomes a new default MAC address. The user can set a
custom MAC address by calling <em>dwm_mac_addr_set</em>. The default MAC address can be
recovered by factory reset (see <em>dwm_factory_reset</em>) after being modified by the user.
The device uses fixed mapping of the MAC address in list to the particular interface as follows:</p>
<ol class="arabic simple">
<li><p>UWB</p></li>
<li><p>BLE</p></li>
<li><p>Ethernet</p></li>
<li><p>Wi-Fi</p></li>
</ol>
<p>The BLE address can be a  Random BLE address or a Public BLE address. If a particular interface is not supported, the corresponding MAC address in the list is empty.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, type_0, type_1, type_2, type_3, mac_addr_0, mac_addr_1, mac_addr_2, mac_addr_3</p></li>
<li><p><strong>type_N</strong> – status, flags (<em>type describing the MAC address at index 0 in the list</em>)</p></li>
<li><p><strong>status</strong> – 2 bits (* status of the MAC address: MAC_ADDR_EMPTY = 0, MAC_ADDR_DEFAULT = 1, MAC_ADDR_USER_SPECIFIED = 2, MAC_ADDR_MUTABLE_DEFAULT = 3*)</p></li>
<li><p><strong>flags</strong> – 6 bits (<em>bit 0 is set if address is PUBLIC_BLE_ADDR, rest of the bits is reserved for future use</em>)</p></li>
<li><p><strong>mac_addr_N</strong> – 48-bits value (<em>little endian</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_list_t</span><span class="w"> </span><span class="n">mac_addr_list</span><span class="p">;</span>
<span class="nl">rv</span><span class="p">:</span><span class="w"> </span><span class="n">dwm_mac_addr_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"UWB MAC 0x%02x%02x%02x%02x%02x%02x status=x%02x</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">2</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">3</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">4</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">5</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">type</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">status</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't get MAC address list, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
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
<tr class="row-odd"><td><p>0x83</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x83 (131 dec) means command dwm_mac_addr_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 51%">
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
<td rowspan="2"><p>0xC1</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(byte 0-4) types of the MAC addresses in the list</div>
</div>
<div class="line-block">
<div class="line">(byte 5-10) MAC address 0 in little endian</div>
<div class="line">(byte 11-16) MAC address 1 in little endian</div>
<div class="line">(byte 17-22) MAC address 2 in little endian</div>
<div class="line">(byte 23-28) MAC address 3 in little endian</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>…</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
<div class="line">Type 0xC1(193 dec) means MAC address list</div>
</div>
<p><strong>MAC address flags encoding</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>flags of the MAC address list</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="2"><p>byte 0</p></td>
<td colspan="3"><p>byte 1</p></td>
<td colspan="2"><p>byte 2</p></td>
<td colspan="2"><p>byte 3</p></td>
</tr>
<tr class="row-odd"><td><p>bits
2-7</p></td>
<td><p>bits
0-1</p></td>
<td><p>bits
11-15</p></td>
<td><p>bit
10</p></td>
<td><p>bits
8-9</p></td>
<td><p>bits
18-23</p></td>
<td><p>bits
16-17</p></td>
<td><p>bits
26-31</p></td>
<td><p>bits
24-25</p></td>
</tr>
<tr class="row-even"><td><p>R</p></td>
<td><p>S_0</p></td>
<td><p>R</p></td>
<td><p>P_1</p></td>
<td><p>S_1</p></td>
<td><p>R</p></td>
<td><p>S_2</p></td>
<td><p>R</p></td>
<td><p>S_3</p></td>
</tr>
</tbody>
</table>
<p>The R means reserved for future use.
The S_0, S_1, S_2, S_3 describe the MAC address status.
Status can have the following values:</p>
<blockquote>
<div><ul class="simple">
<li><p>0 - Empty MAC address</p></li>
<li><p>1 - Default MAC address from OTP memory.</p></li>
<li><p>2 - User specified MAC address</p></li>
<li><p>3 - Mutable default MAC address can be rewritten only once using <em>dwm_mac_addr_set_once</em>.</p></li>
</ul>
</div></blockquote>
<p>P_1 is set if the BLE address is the Public BLE address. The flag is cleared if the BLE MAC address is random. Refer to BLE specification for more information on BLE address types.</p>
</div>


           </div>
