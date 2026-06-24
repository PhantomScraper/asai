---
title: "GPIO"
lang: en
slug: "leaps-rtls/integration-guide/shell-api/gpio"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/shell-api/gpio/"
order: 136
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="gpio">
<h1>GPIO</h1>
<hr class="docutils">
<div class="section" id="gc">
<span id="id1"></span><h2>gc</h2>
<p>Clears GPIO pin.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; gc</span>

<span class="go">Usage: gc &lt;pin&gt;</span>

<span class="go">leaps&gt; gc 13</span>

<span class="go">gpio13: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="gg">
<span id="id2"></span><h2>gg</h2>
<p>Reads GPIO pin. Sets pin into input mode.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; gg</span>

<span class="go">Usage: gg &lt;pin&gt;</span>

<span class="go">leaps&gt; gg 13</span>

<span class="go">gpio13: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="gs">
<span id="id3"></span><h2>gs</h2>
<p>Sets GPIO as output and sets its value.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; gs</span>

<span class="go">Usage: gs &lt;pin&gt;</span>

<span class="go">leaps&gt; gs 13</span>

<span class="go">gpio13: 1</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="gt">
<span id="id4"></span><h2>gt</h2>
<p>Toggles GPIO pin (must be output).</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; gt</span>

<span class="go">Usage: gt &lt;pin&gt;</span>

<span class="go">leaps&gt; gt 13</span>

<span class="go">gpio13: 0</span>
</pre></div>
</div>
</div>
</div>


           </div>
