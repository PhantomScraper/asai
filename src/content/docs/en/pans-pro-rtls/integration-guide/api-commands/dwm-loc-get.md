---
title: "dwm_loc_get"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-loc-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-loc-get/"
order: 198
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-loc-get">
<span id="id1"></span><h1>dwm_loc_get</h1>
<p>Gets the last distances to the ranging anchors and gets the position.
The event is generated, the status changes when all TWR measurements are completed,
and new location data is available for the user. When low-power mode is used, it will certainly work in the same way.</p>
<p>For the anchor node, the position and distances are available only if the auto-positioning procedure has been done.
The auto-positioning procedure is carried out via the BLE interface.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_loc_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_loc_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_loc_data_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">loc</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a>, [position], [cnt, {an_pos, addr, distance, pqf}]</p></li>
<li><p><strong>cnt</strong> – 0,1,2,3,4 (<em>number of distances to the anchors</em>)</p></li>
<li><p><strong>an_pos</strong> – position (<em>position of the anchor , that correspond with the distance</em>)</p></li>
<li><p><strong>addr</strong> – 16-bit integer (<em>UWB address/id of the particular anchor</em>)</p></li>
<li><p><strong>distance</strong> – 32-bit integer (<em>distance to particular anchor in millimeters</em>)</p></li>
<li><p><strong>pqf</strong> – 8-bit integer (<em>quality factor</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Prameter <strong>an_pos</strong> is applicable for <strong>Tag node</strong> only</p>
</div>
<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_loc_data_t</span><span class="w"> </span><span class="n">loc</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="cm">/* if pos_available is false, position data are not read, and the function returns without error */</span>
<span class="nl">rv</span><span class="p">:</span><span class="w"> </span><span class="n">dwm_loc_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">loc</span><span class="p">);</span>

<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="mi">0</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">rv</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">loc</span><span class="p">.</span><span class="n">pos_available</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"[%ld,%ld,%ld,%u] "</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">y</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">z</span><span class="p">,</span>
<span class="w">                     </span><span class="n">loc</span><span class="p">.</span><span class="n">pos</span><span class="p">.</span><span class="n">qf</span><span class="p">);</span>
<span class="p">}</span>
<span class="w">     </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="o">:</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">cnt</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"%u)"</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">);</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"0x%04x"</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">addr</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">             </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">cnt</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"[%ld,%ld,%ld,%u]"</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">x</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">y</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">z</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">an_pos</span><span class="p">.</span><span class="n">pos</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">qf</span><span class="p">);</span>
<span class="w">             </span><span class="p">}</span>
<span class="w">             </span><span class="n">printf</span><span class="p">(</span><span class="s">"=%lu,%u "</span><span class="p">,</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">dist</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="w"> </span><span class="n">loc</span><span class="p">.</span><span class="n">anchors</span><span class="p">.</span><span class="n">dist</span><span class="p">.</span><span class="n">qf</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">     </span><span class="p">}</span>
<span class="w">     </span><span class="n">printf</span><span class="p">(</span><span class="s">"</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">     </span><span class="n">printf</span><span class="p">(</span><span class="s">"err code: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART example 1 (tag node)</strong></p>
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
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x0C means command loc_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 7%">
<col style="width: 7%">
<col style="width: 0%">
<col style="width: 7%">
<col style="width: 0%">
<col style="width: 8%">
<col style="width: 3%">
<col style="width: 3%">
<col style="width: 7%">
<col style="width: 7%">
<col style="width: 0%">
<col style="width: 7%">
<col style="width: 0%">
<col style="width: 8%">
<col style="width: 13%">
<col style="width: 8%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="21"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="6"><p>Value</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="8"><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x40</p></td>
<td rowspan="3"><p>0x01</p></td>
<td rowspan="3"><p>0x00</p></td>
<td rowspan="3"><p>0x41</p></td>
<td rowspan="3"><p>0x0D</p></td>
<td rowspan="2"><p>int32 -
x coordinate
in
millimeters</p></td>
<td colspan="2" rowspan="2"><p>int32 -
y coordinate
in
millimeters</p></td>
<td colspan="2" rowspan="2"><p>int32 -
z coordinate
in
millimeters</p></td>
<td rowspan="2"><p>uint8 -
position
quality
factor
in percents</p></td>
<td rowspan="3"><p>0x49</p></td>
<td rowspan="3"><p>0x51</p></td>
<td rowspan="2"><p>uint8 -
number of
distances</p></td>
<td colspan="6"><p>position and distance nr. 1</p></td>
<td><p>position and
distance
nr.2,3,4</p></td>
</tr>
<tr class="row-even"><td colspan="2"><p>int16 -
UWB address</p></td>
<td colspan="2"><p>uint32 -
distance
in
millimeters</p></td>
<td><p>uint8 -
distance
quality
factor
in percents</p></td>
<td><p>3 x int32 + uint8 -
x, y, z in millimeters
+ quality factor in
percents</p></td>
<td><p>…</p></td>
</tr>
<tr class="row-odd"><td colspan="6"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00         0x9c
0x0e         0x00
0x00         0x64</p></td>
<td><p>0x04</p></td>
<td colspan="2"><p>0xab 0xbc</p></td>
<td colspan="2"><p>0x0e 0x03
0x00 0x00</p></td>
<td><p>0x64</p></td>
<td><p>…</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of previous command</div>
<div class="line">Type 0x41 means position</div>
<div class="line">Type 0x49 means position and distances of ranging anchors</div>
</div>
<p><strong>SPI/UART example 2 (anchor node)</strong></p>
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
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x0C means command loc_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 0%">
<col style="width: 8%">
<col style="width: 0%">
<col style="width: 9%">
<col style="width: 4%">
<col style="width: 4%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 0%">
<col style="width: 8%">
<col style="width: 0%">
<col style="width: 9%">
<col style="width: 11%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="20"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="6"><p>Value</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="7"><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x40</p></td>
<td rowspan="3"><p>0x01</p></td>
<td rowspan="3"><p>0x00</p></td>
<td rowspan="3"><p>0x41</p></td>
<td rowspan="3"><p>0x0D</p></td>
<td rowspan="2"><p>int32 -
x coordinate
in
millimeters</p></td>
<td colspan="2" rowspan="2"><p>int32 -
y coordinate
in
millimeters</p></td>
<td colspan="2" rowspan="2"><p>int32 -
z coordinate
in
millimeters</p></td>
<td rowspan="2"><p>uint8 -
position
quality
factor
in percents</p></td>
<td rowspan="3"><p>0x48</p></td>
<td rowspan="3"><p>0x63</p></td>
<td rowspan="2"><p>uint8 -
number of
distances</p></td>
<td colspan="5"><p>distance nr. 1</p></td>
<td><p>distance
nr.2,…, nr. 14</p></td>
</tr>
<tr class="row-even"><td colspan="2"><p>int16 -
UWB address</p></td>
<td colspan="2"><p>uint32 -
distance
in
millimeters</p></td>
<td><p>uint8 -
distance
quality
factor
in percents</p></td>
<td><p>…</p></td>
</tr>
<tr class="row-odd"><td colspan="6"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00         0x9c
0x0e         0x00
0x00         0x64</p></td>
<td><p>0x0E</p></td>
<td colspan="2"><p>0xab 0xbc</p></td>
<td colspan="2"><p>0x0e 0x03
0x00 0x00</p></td>
<td><p>0x64</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a> of previous command</div>
<div class="line">Type 0x41 means position</div>
<div class="line">Type 0x48 means distances of ranging anchors</div>
</div>
</div>


           </div>
