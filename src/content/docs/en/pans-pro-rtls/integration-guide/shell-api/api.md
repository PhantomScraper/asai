---
title: "API"
lang: en
slug: "pans-pro-rtls/integration-guide/shell-api/api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/shell-api/api/"
order: 164
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api">
<h1>API</h1>
<hr class="docutils">
<div class="section" id="tlv">
<span id="pp-tlv"></span><h2>tlv</h2>
<p>Parses given TLV frame.</p>
<p>Example:
read node configuration</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; tlv 8 0</span>
<span class="go">OUTPUT FRAME:</span>
<span class="go">40 01 00 46 02 b0 00</span>
<span class="go">toggles GPIO pin 13</span>
<span class="go">dwm&gt; tlv 44 1 13</span>
<span class="go">OUTPUT FRAME:</span>
<span class="go">40 01 00</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="aurs">
<span id="pp-aurs"></span><h2>aurs</h2>
<p>Set update rate.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; aurs</span>
<span class="go">Usage aurs &lt;ur&gt; &lt;urs&gt;</span>
<span class="go">dwm&gt; aurs 10 20</span>
<span class="go">err code: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="aurg">
<span id="pp-aurg"></span><h2>aurg</h2>
<p>Get update rate.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; aurg</span>
<span class="go">err code: 0, upd rate: 10, 20(stat)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="apg">
<span id="pp-apg"></span><h2>apg</h2>
<p>Gets the position of the node.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; apg</span>
<span class="go">x:100 y:120 z:2500 qf:100</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="aps">
<span id="pp-aps"></span><h2>aps</h2>
<p>sets the position of the node.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; aps</span>
<span class="go">Usage aps &lt;x&gt; &lt;y&gt; &lt;z&gt;</span>
<span class="go">dwm&gt; aps 100 120 2500</span>
<span class="go">err code: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="acas">
<span id="pp-acas"></span><h2>acas</h2>
<p>Set anchor config. This command requires reset for new configuration to take effect.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; acas</span>
<span class="go">[Output when UWB routing backhaul is disabled]</span>
<span class="go">Usage acas &lt;inr&gt; &lt;gateway&gt; &lt;enc&gt; &lt;leds&gt; &lt;ble&gt; &lt;uwb&gt; &lt;fw_upd&gt;</span>
<span class="go">dwm&gt; acas 0 0 0 1 1 2 1</span>
<span class="go">err code: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="acts">
<span id="pp-acts"></span><h2>acts</h2>
<p>Set tag config. This command requires reset for new configuration to take effect.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; acts</span>
<span class="go">Usage acts &lt;meas_mode&gt; &lt;stnry_en&gt; &lt;low_pwr&gt; &lt;loc_en&gt; &lt;enc&gt; &lt;leds&gt; &lt;ble&gt; &lt;uwb&gt; &lt;fw_upd&gt;</span>
<span class="go">dwm&gt; acts 0 1 0 1 0 0 1 2 1</span>
<span class="go">err code: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="aks">
<span id="pp-aks"></span><h2>aks</h2>
<p>Sets encryption key, takes encryption key as argument.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; aks 00112233445566778899aabbccddeeff</span>
<span class="go">key_set: 00112233445566778899AABBCCDDEEFF</span>
<span class="go">dwm&gt;</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="akc">
<span id="pp-akc"></span><h2>akc</h2>
<p>Clears encryption key and disables encryption.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; akc</span>
<span class="go">Ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ans">
<span id="pp-ans"></span><h2>ans</h2>
<p>Writes user data to non-volatile memory.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; ans 00112233445566778899aabbccddeeff00112233</span>

<span class="go">data: 00112233445566778899AABBCCDDEEFF00112233</span>
<span class="go">len=20</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ang">
<span id="pp-ang"></span><h2>ang</h2>
<p>Reads data from non-volatile memory.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; ang</span>
<span class="go">data: 00112233445566778899AABBCCDDEEFF00112233</span>
<span class="go">len=20</span>
<span class="go">dwm&gt;</span>
</pre></div>
</div>
</div>
</div>


           </div>
