---
title: "SENS"
lang: en
slug: "pans-pro-rtls/integration-guide/shell-api/sens"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/shell-api/sens/"
order: 160
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="sens">
<h1>SENS</h1>
<hr class="docutils">
<div class="section" id="twi">
<span id="pp-twi"></span><h2>twi</h2>
<p>General purpose I2C/TWI read.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; twi</span>
<span class="go">Usage: twi &lt;addr&gt; &lt;reg&gt; [bytes to read (1 or 2)]</span>
<span class="go">dwm&gt; twi 0x33 0x0f</span>
<span class="go">twi: addr=0x33, reg[0x0f]=0x33</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="aid">
<span id="pp-aid"></span><h2>aid</h2>
<p>Reads ACC device ID</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; aid</span>
<span class="go">acc: 0x33</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="av">
<span id="pp-av"></span><h2>av</h2>
<p>Reads ACC values.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; av</span>
<span class="go">acc: x = 240, y = -3792, z = 16240</span>
<span class="go">dwm&gt; av</span>
<span class="go">acc: x = 32, y = -3504, z = 15872</span>
<span class="go">dwm&gt; av</span>
<span class="go">acc: x = 160, y = -3600, z = 16144</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="scs">
<span id="pp-scs"></span><h2>scs</h2>
<p>Stationary configuration set. Sets sensitivity (valid args are 0,1,2).</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; scs 1</span>
<span class="go">ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="scg">
<span id="pp-scg"></span><h2>scg</h2>
<p>Stationary configuration get.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; scg</span>
<span class="go">sensitivity=1</span>
</pre></div>
</div>
</div>
</div>


           </div>
