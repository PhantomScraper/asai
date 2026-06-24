---
title: "SENS"
lang: ja
slug: "leaps-rtls/integration-guide/shell-api/sens"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/shell-api/sens/"
order: 136
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="sens">
<h1>SENS</h1>
<hr class="docutils">
<div class="section" id="twi">
<span id="id1"></span><h2>twi</h2>
<p>汎用 I2C/TWI 読み取り。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; twi</span>

<span class="go">Usage: twi &lt;addr&gt; &lt;reg&gt; [bytes to read (1 or 2)]</span>

<span class="go">leaps&gt; twi 0x33 0x0f</span>

<span class="go">twi: addr=0x33, reg[0x0f]=0x33</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="aid">
<span id="id2"></span><h2>aid</h2>
<p>ACC デバイス ID を読み取ります</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; aid</span>

<span class="go">acc: 0x33</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="av">
<span id="id3"></span><h2>av</h2>
<p>ACC 値の読み取り</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; av</span>

<span class="go">acc: x = 240, y = -3792, z = 16240</span>

<span class="go">leaps&gt; av</span>

<span class="go">acc: x = 32, y = -3504, z = 15872</span>

<span class="go">leaps&gt; av</span>

<span class="go">acc: x = 160, y = -3600, z = 16144</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="scs">
<span id="id4"></span><h2>scs</h2>
<p>固定構成セット。感度を設定します (有効な引数は 0、1、2)。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; scs 1</span>

<span class="go">ok</span>

<span class="go">leaps&gt; scs 4</span>

<span class="go">error: invalid arg</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="scg">
<span id="id5"></span><h2>scg</h2>
<p>固定構成を取得します。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; scg</span>

<span class="go">sensitivity=1</span>
</pre></div>
</div>
</div>
</div>


           </div>
