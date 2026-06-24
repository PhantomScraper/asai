---
title: "UWB"
lang: en
slug: "leaps-rtls/integration-guide/shell-api/uwb"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/shell-api/uwb/"
order: 139
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uwb">
<h1>UWB</h1>
<hr class="docutils">
<div class="section" id="ucs">
<span id="id1"></span><h2>ucs</h2>
<p>Set UWB channel and compliance</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ucs</span>

<span class="go">Usage: ucs &lt;ch&gt; &lt;cpl&gt; &lt;pcode&gt;</span>
</pre></div>
</div>
<p>Where:</p>
<blockquote>
<div><ul class="simple">
<li><p>ch: 5,9</p></li>
<li><p>cpl: 0 = FCC/ETSI, 1 = ETSI+10dB and 2 = ARIB only for ch 9</p></li>
<li><p>pcode: 9,10,11,12</p></li>
</ul>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The &lt;pcode&gt; argument for the ucs command is optional. If the user does not provide an input,
the default value specified below will be used.</p>
<blockquote>
<div><ul class="simple">
<li><p>Channel 2: Tx/Rx Preamble Code = 11</p></li>
<li><p>Channel 3: Tx/Rx Preamble Code = 12</p></li>
<li><p>Channel 5: Tx/Rx Preamble Code = 9</p></li>
<li><p>Channel 9: Tx/Rx Preamble Code = 11</p></li>
</ul>
</div></blockquote>
<p>Channel 2 and channel 3 support ‘0 = FCC/ETSI’ only</p>
</div>
</div></blockquote>
<p>Example (DW3000)</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ucs 9 2</span>

<span class="go">ucs: ch=9 cpl=2</span>

<span class="go">leaps&gt; ucs 5 2</span>

<span class="go">ucs: failed</span>

<span class="go">leaps&gt; ucs 5 1</span>

<span class="go">ucs: ch=5 cpl=1</span>

<span class="go">leaps&gt; ucs 5 0</span>

<span class="go">ucs: ch=5 cpl=0</span>

<span class="go">leaps&gt; ucs 5 4</span>

<span class="go">ucs: failed</span>

<span class="go">leaps&gt; ucs 5 9</span>

<span class="go">ucs: failed</span>

<span class="go">leaps&gt; ucs 5 0</span>

<span class="go">ucs: ch=5 cpl=0</span>

<span class="go">leaps&gt; ucs 2 0</span>

<span class="go">ucs: failed</span>
</pre></div>
</div>
</div></blockquote>
<p>Example (DW1000):</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ucs 5 0</span>

<span class="go">ucs: ch=5 cpl=0</span>

<span class="go">leaps&gt; ucs 5 2</span>

<span class="go">ucs: failed</span>

<span class="go">leaps&gt; ucs 2 1</span>

<span class="go">ucs: ch=2 cpl=1</span>
</pre></div>
</div>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="utpg">
<span id="id2"></span><h2>utpg</h2>
<p>Get transmit power.</p>
<p>Example:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; utpg</span>

<span class="go">utpg: pg_delay=xC5 tx_power=x29496989 (pg_delay=xC4 tx_power=x29496989)</span>

<span class="go">Calibration values from the OTP/settings before the brackets. The current values are displayed in the brackets.</span>
</pre></div>
</div>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="utps">
<span id="id3"></span><h2>utps</h2>
<p>Set transmit power.</p>
<p>Example:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; utps</span>

<span class="go">Usage: utps &lt;pg_delay&gt; &lt;tx_power&gt;</span>

<span class="go">leaps&gt; utps 0xc2 0x28486888</span>

<span class="go">utps: pg_delay=xC2 tx_power=x28486888</span>
</pre></div>
</div>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="ufs">
<span id="id4"></span><h2>ufs</h2>
<p>UWB Frontend Set</p>
<p>Example:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ufs</span>
<span class="go">Usage: ufs &lt;lna&gt; &lt;pa&gt; &lt;rf1&gt; &lt;rf2&gt;</span>
</pre></div>
</div>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="ucls">
<span id="id5"></span><h2>ucls</h2>
<p>Set BLE Adv UWB counter low water mark</p>
<p>Example:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ucls 0</span>
<span class="go">ucls: ok</span>
</pre></div>
</div>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="uclg">
<span id="id6"></span><h2>uclg</h2>
<p>Get BLE Adv UWB counter low water mark</p>
<p>Example:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; uclg</span>
<span class="go">uclg: lwmark=0</span>
</pre></div>
</div>
</div></blockquote>
</div>
</div>


           </div>
