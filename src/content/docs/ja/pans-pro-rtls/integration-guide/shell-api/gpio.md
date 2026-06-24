---
title: "GPIO"
lang: ja
slug: "pans-pro-rtls/integration-guide/shell-api/gpio"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/shell-api/gpio/"
order: 157
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="gpio">
<h1>GPIO</h1>
<hr class="docutils">
<div class="section" id="gc">
<span id="pp-gc"></span><h2>gc</h2>
<p>GPIO ピンをクリアします。</p>
<p><strong>例:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; gc</span>
<span class="go">Usage: gc &lt;pin&gt;</span>
<span class="go">dwm&gt; gc 13</span>
<span class="go">gpio13: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="gg">
<span id="pp-gg"></span><h2>gg</h2>
<p>GPIO ピンを読み取ります。端子を入力モードに設定します。</p>
<p><strong>例:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; gg</span>
<span class="go">Usage: gg &lt;pin&gt;</span>
<span class="go">dwm&gt; gg 13</span>
<span class="go">gpio13: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="gs">
<span id="pp-gs"></span><h2>gs</h2>
<p>GPIO を出力として設定し、その値を設定します。</p>
<p><strong>例:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; gs</span>
<span class="go">Usage: gs &lt;pin&gt;</span>
<span class="go">dwm&gt; gs 13</span>
<span class="go">gpio13: 1</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="gt">
<span id="pp-gt"></span><h2>gt</h2>
<p>GPIO ピンを切り替えます (出力する必要があります)。</p>
<p><strong>例:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; gt</span>
<span class="go">Usage: gt &lt;pin&gt;</span>
<span class="go">dwm&gt; gt 13</span>
<span class="go">gpio13: 0</span>
</pre></div>
</div>
</div>
</div>


           </div>
