---
title: "LE"
lang: ja
slug: "pans-pro-rtls/integration-guide/shell-api/le"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/shell-api/le/"
order: 160
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="le">
<h1>LE</h1>
<hr class="docutils">
<div class="section" id="les">
<span id="pp-les"></span><h2>les</h2>
<p>測距アンカーまでの距離と位置エンジンが有効な場合は位置を表示します。</p>
<p><strong>例:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; les</span>
<span class="go">1151[5.00,8.00,2.25]=6.48 0CA8[0.00,8.00,2.25]=6.51 111C[5.00,0.00,2.25]=3.18 1150[0.00,0.00,2.25]=3.16 le_us=2576 est[2.57,1.98,1.68,100]</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="lec">
<span id="pp-lec"></span><h2>lec</h2>
<p>測距アンカーまでの距離と、位置エンジンが有効になっている場合の位置を CSV 形式で表示します。</p>
<p><strong>例:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; lec</span>
<span class="go">DIST,4,AN0,1151,5.00,8.00,2.25,6.44,AN1,0CA8,0.00,8.00,2.25,6.50,AN2,111C,5.00,0.00,2.25,3.24,AN3,1150,0.00,0.00,2.25,3.19,POS,2.55,2.01,1.71,98</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="lep">
<span id="pp-lep"></span><h2>lep</h2>
<p>位置を CSV 形式で表示します。</p>
<p><strong>例:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; lep</span>
<span class="go">POS,2.57,2.00,1.67,97</span>
</pre></div>
</div>
</div>
</div>


           </div>
