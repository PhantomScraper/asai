---
title: "UWBMAC"
lang: en
slug: "leaps-rtls/integration-guide/shell-api/uwbmac"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/shell-api/uwbmac/"
order: 140
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uwbmac">
<h1>UWBMAC</h1>
<hr class="docutils">
<div class="section" id="nmo">
<span id="id1"></span><h2>nmo</h2>
<p>Set UWB mode to off.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmo</span>

<span class="go">/\* press enter twice to switch to shell mode after reset*/</span>

<span class="go">Low Energy Accurate Positioning System</span>

<span class="go">FOR DEMO PURPOSE ONLY, NOT FOR SALE.</span>

<span class="go">Copyright : 2016-2020 LEAPS</span>

<span class="go">License : Please visit https://www.leapslabs.com/leaps_license</span>

<span class="go">Compiled : Jul 13 2020 09:30:07</span>

<span class="go">Help : ? or help</span>

<span class="go">leaps&gt; si</span>
<span class="go">/\*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: tn (off,twr,np,le)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmp">
<span id="id2"></span><h2>nmp</h2>
<p>Set UWB mode to passive.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmp</span>

<span class="go">/\* press enter twice to switch to shell mode after reset*/</span>

<span class="go">Low Energy Accurate Positioning System</span>

<span class="go">FOR DEMO PURPOSE ONLY, NOT FOR SALE.</span>

<span class="go">Copyright : 2016-2020 LEAPS</span>

<span class="go">License : Please visit https://www.leapslabs.com/leaps_license</span>

<span class="go">Compiled : Jul 13 2020 09:30:07</span>

<span class="go">Help : ? or help</span>

<span class="go">leaps&gt; si</span>
<span class="go">/\*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: tn (pasv,twr,np,nole)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nma">
<span id="id3"></span><h2>nma</h2>
<p>Set mode to AN.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nma</span>

<span class="go">/\* press Enter twice \*/</span>

<span class="go">Low Energy Accurate Positioning System</span>

<span class="go">FOR DEMO PURPOSE ONLY, NOT FOR SALE.</span>

<span class="go">Copyright : 2016-2020 LEAPS</span>

<span class="go">License : Please visit https://www.leapslabs.com/leaps_license</span>

<span class="go">Compiled : Jul 13 2020 09:30:07</span>

<span class="go">Help : ? or help</span>

<span class="go">leaps&gt; si</span>
<span class="go">/\*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: an (act,-,-)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmi">
<span id="id4"></span><h2>nmi</h2>
<p>Set mode to ANI</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmi</span>

<span class="go">/\* press enter twice \*/</span>

<span class="go">Low Energy Accurate Positioning System</span>

<span class="go">FOR DEMO PURPOSE ONLY, NOT FOR SALE.</span>

<span class="go">Copyright : 2016-2020 LEAPS</span>

<span class="go">License : Please visit https://www.leapslabs.com/leaps_license</span>

<span class="go">Compiled : Jul 13 2020 09:30:07</span>

<span class="go">Help : ? or help</span>

<span class="go">leaps&gt; si</span>
<span class="go">/\*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: ain (act,real,-)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmt">
<span id="id5"></span><h2>nmt</h2>
<p>Set mode to TN</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmt</span>

<span class="go">/\* press enter twice \*/</span>

<span class="go">Low Energy Accurate Positioning System</span>

<span class="go">FOR DEMO PURPOSE ONLY, NOT FOR SALE.</span>

<span class="go">Copyright : 2016-2020 LEAPS</span>

<span class="go">License : Please visit https://www.leapslabs.com/leaps_license</span>

<span class="go">Compiled : Jul 13 2020 09:30:07</span>

<span class="go">Help : ? or help</span>

<span class="go">leaps&gt; si</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmtl">
<span id="id6"></span><h2>nmtl</h2>
<p>Set mode to TN-LP</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmtl</span>

<span class="go">/\* press enter twice \*/</span>

<span class="go">Low Energy Accurate Positioning System</span>

<span class="go">FOR DEMO PURPOSE ONLY, NOT FOR SALE.</span>

<span class="go">Copyright : 2016-2020 LEAPS</span>

<span class="go">License : Please visit https://www.leapslabs.com/leaps_license</span>

<span class="go">Compiled : Jul 13 2020 09:30:07</span>

<span class="go">Help : ? or help</span>

<span class="go">leaps&gt; si</span>
<span class="go">/\*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: tn (act,twr,lp,le)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmg">
<span id="id7"></span><h2>nmg</h2>
<p>Set mode to GN</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmg</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ln">
<span id="id8"></span><h2>ln</h2>
<p>Show node list</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ln</span>
<span class="go">[000214.375 INF] TN: cnt=0 size=0</span>
<span class="go">[000214.375 INF]</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="la">
<span id="id9"></span><h2>la</h2>
<p>Show AN list.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt;la</span>

<span class="go">[007582.110 INF] AN: cnt=5 seq=x15</span>

<span class="go">[007582.110 INF] 0) id=DECAA6429C750997 seat=0 idl=1 seens=90 rssi=-79</span>
<span class="go">fl=0001</span>

<span class="go">[007582.120 INF] 1) id=DECA5AA932A3D482 seat=1 idl=1 seens=35 rssi=-79</span>
<span class="go">fl=0001</span>

<span class="go">[007582.120 INF] 2) id=DECAA19F7B23CAAB seat=2 idl=1 seens=21 rssi=-79</span>
<span class="go">fl=0001</span>

<span class="go">[007582.130 INF] 3) id=DECA97E24B94C5B7 seat=3 idl=0 seens=254 rssi=-79</span>
<span class="go">fl=0001</span>

<span class="go">[007582.140 INF] 4) id=DECA1DAB42E4C62F seat=4 idl=1 seens=47 rssi=-79</span>
<span class="go">fl=0001</span>
</pre></div>
</div>
<hr class="docutils">
<span class="target" id="bns"></span><span class="target" id="lb"></span><span class="target" id="lr"></span><span class="target" id="lrn"></span></div>
<div class="section" id="nis">
<span id="id10"></span><h2>nis</h2>
<p>Set Network ID, Mask, and Zone ID with flags option</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nis</span>
<span class="go">usage: nis PANID [FLAGS] [PANID_MASK] [ZONE_ID]</span>
</pre></div>
</div>
<p>Example 1:</p>
<p>Set the PANID only with writing the value to the environment</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nis 0x6666</span>
<span class="go">nis: ok</span>
</pre></div>
</div>
<p>Set the PANID only with <strong>skipping</strong> writing the value to the environment - Flags bit 0 set to 1</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nis 0x6666 1</span>
<span class="go">nis: ok</span>
</pre></div>
</div>
<p>Example 2:</p>
<p>If the device is TN and the UWB profile is 0, 1, 2, or 3, set the PANID mask using a hexadecimal value</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nis 0x6666 0 0xFFF0</span>
<span class="go">nis: ok</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">0xFFF0</span></code>: accept the PANID from <code class="docutils literal notranslate"><span class="pre">0x6660</span></code> to <code class="docutils literal notranslate"><span class="pre">0x666F</span></code>.</div>
<div class="line">If no PANID mask is provided, the default mask is <code class="docutils literal notranslate"><span class="pre">0xFFFF</span></code>.</div>
<div class="line"><em>Flags</em> bit 0 is set to 0: write to the environment.</div>
</div>
</div>
<p>Example 3:</p>
<p>Alternatively, use <a class="reference external" href="https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/">CIDR notation</a> to set the PANID MASK</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nis 0x6666 0 /12</span>
<span class="go">nis: ok</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code class="docutils literal notranslate"><span class="pre">/12</span></code> is equivalent to the mask <code class="docutils literal notranslate"><span class="pre">0xFFF0</span></code>.</p>
</div>
<hr class="docutils">
</div>
<div class="section" id="nls">
<span id="id11"></span><h2>nls</h2>
<p>Set node label</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nls MAIN</span>
<span class="go">nls: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nps">
<span id="id12"></span><h2>nps</h2>
<p>Set network profile</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nps 2</span>
<span class="go">nps: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="udi">
<span id="id13"></span><h2>udi</h2>
<p>Show incoming IoT data</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; udi</span>

<span class="go">dl: show on</span>

<span class="go">dl: len=8: 01 23 45 67 89 AB CD EF</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="uui">
<span id="id14"></span><h2>uui</h2>
<p>Send IoT data</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; uui</span>

<span class="go">usage: uui &lt;hex_string&gt; [cnt]</span>

<span class="go">leaps&gt; uui 11223344 100</span>

<span class="go">ul: len=4 cnt=100 rv=4: 11 22 33 44</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="usps">
<span id="id15"></span><h2>usps</h2>
<p>Set pulse per superframe cycle. Example: 50 means 1 pulse per 50 superframe</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; usps 50</span>
<span class="go">usps: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="uspg">
<span id="id16"></span><h2>uspg</h2>
<p>Get pulse per superframe cycle.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; uspg</span>
<span class="go">uspg: 50</span>
</pre></div>
</div>
</div>
</div>


           </div>
