---
title: "SYS"
lang: en
slug: "pans-pro-rtls/integration-guide/shell-api/sys"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/shell-api/sys/"
order: 159
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="sys">
<h1>SYS</h1>
<hr class="docutils">
<div class="section" id="f">
<span id="pp-f"></span><h2>f</h2>
<p>Shows free memory on the heap.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; f</span>
<span class="go">[000014.560 INF] mem: free=3888 alloc=9184 tot=13072</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="reset">
<span id="pp-reset"></span><h2>reset</h2>
<p>Reboots the system.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; reset</span>
<span class="go">/* node resets and boots in binary mode */</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="si">
<span id="pp-si"></span><h2>si</h2>
<p>System info</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; si</span>
<span class="go">[001762.590 INF] sys: fw2 fw_ver=x01020001 cfg_ver=x00010700</span>
<span class="go">[001762.590 INF] uwb0: panid=x1234 addr=xDECADF01465011E4</span>
<span class="go">[001762.590 INF] mode: ani (act,real)</span>
<span class="go">[001762.600 INF] uwbmac: connected</span>
<span class="go">[001762.600 INF] uwbmac: bh connected</span>
<span class="go">[001762.610 INF] cfg: sync=1 fwup=0 ble=1 leds=1 init=1 bh=0 upd_rate_stat=64 label=DW11E4</span>
<span class="go">[001762.620 INF] enc: off</span>
<span class="go">[001762.630 INF] ble: addr=CB:65:C2:DD:D3:D4</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ut">
<span id="pp-ut"></span><h2>ut</h2>
<p>Shows device uptime.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; ut</span>
<span class="go">[000003.680 INF] uptime: 00:07:49.210 0 days (469210 ms)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="frst">
<span id="pp-frst"></span><h2>frst</h2>
<p>Factory reset.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; frst</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="sbl">
<span id="pp-sbl"></span><h2>sbl</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 75%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p>Description</p></td>
<td><p>Set the battery voltage level.</p></td>
</tr>
<tr class="row-even"><td><p>Parameters (In)</p></td>
<td><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">low</span></code>: Voltage threshold for Empty / Low battery detection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">med</span></code>: Voltage threshold for Low → Mid-transition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">high</span></code>: Voltage threshold for Mid → Full transition.</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>Parameters (Out)</p></td>
<td><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">SUCCESSED</span></code> if successful, <code class="docutils literal notranslate"><span class="pre">UNSUCCESSED</span></code> otherwise.</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>Example</p></td>
<td><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; sbl 3800 3900 4200</span>
<span class="go">[INFO]: Update the battery levels: SUCCESSED</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>


           </div>
