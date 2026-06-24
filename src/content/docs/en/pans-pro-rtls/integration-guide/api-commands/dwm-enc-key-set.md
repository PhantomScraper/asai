---
title: "dwm_enc_key_set"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-set/"
order: 180
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-enc-key-set">
<span id="id1"></span><h1>dwm_enc_key_set</h1>
<p>Sets encryption key. The key is stored in a non-volatile memory. The key that
consists of just zeros is considered invalid. If the key is set, the node will
automatically enable encryption. Automatic enabling of the encryption is triggered
via the UWB network when the node detects encrypted messages and can decrypt the messages with the key.
The BLE option is disabled when encryption is enabled automatically.
The encryption can be disabled by clearing the key (see <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-clear#dwm-enc-key-clear"><span class="std std-ref">dwm_enc_key_clear</span></a>).</p>
<div class="admonition caution">
<p class="admonition-title">Caution</p>
<p>Normally, this call writes to internal flash when setting a new value.
Hence, it should not be used frequently and can take hundreds of milliseconds in the worst case!
Reset is requires for the new configuration to take effect.</p>
</div>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_enc_key_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_enc_key_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_enc_key_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">key</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – key</p></li>
<li><p><strong>key</strong> – 16-bytes (<em>the encryption key</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_enc_key_t</span><span class="w"> </span><span class="n">key</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x00</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x11</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x22</span><span class="p">;</span>
<span class="cm">/* ... */</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">15</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0xFF</span><span class="p">;</span>
<span class="n">dwm_enc_key_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">key</span><span class="p">)</span>
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
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x3C</p></td>
<td><p>0x10</p></td>
<td><p>0x00 0x11 0x22
0x33 0x44 0x55
0x66 0x77 0x88
0x99 0xAA 0xBB
0xCC 0xDD 0xEE
0xFF</p></td>
</tr>
</tbody>
</table>
<p>Type 0x3C means command <a class="reference internal" href="#dwm-enc-key-set"><span class="std std-ref">dwm_enc_key_set</span></a></p>
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
