---
title: "dwm_anchor_list_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-anchor-list-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-anchor-list-get/"
order: 168
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-anchor-list-get">
<span id="id1"></span><h1>dwm_anchor_list_get</h1>
<p>Reads the list of surrounding anchors and works for anchors only. Anchors in the list can be from the same network or neighbor network.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_anchor_list_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_anchor_list_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_anchor_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (SPI/UART) ‘0’ | ‘1’(<em>page number (only on SPI/UART, the user application reads whole list in 1 call), valid numbers are 0,1</em>)</p></li>
<li><p><strong>input</strong> – (user application) (<em>none</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, cnt, {node_id, position, rssi, seat, neighbor_network}</p></li>
<li><p><strong>cnt</strong> – 1 byte? (<em>element count, 15 is maximum for SPI/UART, 30 is maximum for user application</em>)</p></li>
<li><p><strong>node_id</strong> – 2 bytes (<em>anchor ID</em>)</p></li>
<li><p><strong>position</strong> – 12 bytes ?</p></li>
<li><p><strong>rssi</strong> – 1 byte signed? (<em>signal strength indicator</em>)</p></li>
<li><p><strong>seat</strong> – 5 bits (<em>seat number occupied by the anchor</em>)</p></li>
<li><p><strong>neighbor_network</strong> – 1 bit (<em>status flags that indicates if anchor is from current network or if it is from neighbor network</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_anchor_list_t</span><span class="w"> </span><span class="n">list</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="n">dwm_anchor_list_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">list</span><span class="p">);</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="o">:</span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">list</span><span class="p">.</span><span class="n">cnt</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">     </span><span class="n">printf</span><span class="p">(</span><span class="s">"%d. id=0x%04X pos=[%ld,%ld,%ld] rssi=%d seat=%u neighbor=%d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">node_id</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">x</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">y</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">z</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">rssi</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">seat</span><span class="p">,</span>
<span class="w">                     </span><span class="n">list</span><span class="p">.</span><span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">neighbor_network</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART example 1</strong></p>
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
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x0B means command dwm_an_list_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 9%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 9%">
<col style="width: 9%">
<col style="width: 11%">
<col style="width: 5%">
<col style="width: 19%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="3"><p>Type</p></td>
<td rowspan="3"><p>Length</p></td>
<td><p>Value</p></td>
<td rowspan="3"><p>Type</p></td>
<td rowspan="3"><p>Length</p></td>
<td colspan="6"><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>uint8 -
error code</p></td>
<td rowspan="2"><p>uint8
-
number
of
elements
encoded</p></td>
<td rowspan="2"><p>uint16
-
UWB
address
in
little
endian</p></td>
<td colspan="3"><p>anchor nr.1</p></td>
<td><p>anchors nr. 2 … nr.15</p></td>
</tr>
<tr class="row-even"><td><p>3 x int32
-
position
coordinates
x, y, z
in little
endian</p></td>
<td><p>int8 -
RSSI</p></td>
<td><div class="line-block">
<div class="line">uint8 - flags</div>
</div>
<div class="line-block">
<div class="line">(bits 0-4) seat number</div>
<div class="line">(bit 5) neighbour network</div>
<div class="line">(bits 6-7) reserved</div>
</div>
</td>
<td><p>…</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x56</p></td>
<td><p>0xE1</p></td>
<td><p>0x0F</p></td>
<td colspan="4"><p>0xAB 0x1E …</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
<div class="line">Type 0x56 means anchor list</div>
</div>
<p><strong>SPI/UART example 2</strong></p>
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
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>Type 0x0B means command dwm_an_list_get</p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV Response   (anchor list is empty)</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x56</p></td>
<td rowspan="2"><p>0x01</p></td>
<td><p>uint8
- number
of
elements
encoded
in the
Value</p></td>
</tr>
<tr class="row-even"><td><p>0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of the previous command</div>
<div class="line">Type 0x56 means anchor list</div>
</div>
</div>


           </div>
