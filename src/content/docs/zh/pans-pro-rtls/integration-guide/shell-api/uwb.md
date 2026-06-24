---
title: "UWB"
lang: zh
slug: "pans-pro-rtls/integration-guide/shell-api/uwb"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/shell-api/uwb/"
order: 161
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uwb">
<h1>UWB</h1>
<hr class="docutils">
<div class="section" id="utpg">
<span id="pp-utpg"></span><h2>utpg</h2>
<p>获取 DW1000 的发射功率。</p>
<p><strong>示例：</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; utpg</span>
<span class="go">utpg: pg_delay=xC5 tx_power=x29496989 (pg_delay=xC4 tx_power=x29496989)</span>
<span class="go">Calibration values from the OTP/settings before the brackets. The current values are displayed in the brackets.</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="utps">
<span id="pp-utps"></span><h2>utps</h2>
<p>设置 DW1000 的发射功率。</p>
<p><strong>示例：</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; utps</span>
<span class="go">Usage: utps &lt;pg_delay&gt; &lt;tx_power&gt;</span>
<span class="go">dwm&gt; utps 0xc2 0x28486888</span>
<span class="go">utps: pg_delay=xC2 tx_power=x28486888</span>
</pre></div>
</div>
</div>
</div>


           </div>
