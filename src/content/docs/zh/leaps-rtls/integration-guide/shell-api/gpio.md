---
title: "GPIO"
lang: zh
slug: "leaps-rtls/integration-guide/shell-api/gpio"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/shell-api/gpio/"
order: 135
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
<p>清除 GPIO 引脚。</p>
<p>示例:</p>
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
<p>读取 GPIO 引脚。 将引脚设置为输入模式。</p>
<p>示例:</p>
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
<p>将 GPIO 设置为输出并设置其值。</p>
<p>示例:</p>
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
<p>切换 GPIO 引脚（必须为输出）。</p>
<p>示例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; gt</span>

<span class="go">Usage: gt &lt;pin&gt;</span>

<span class="go">leaps&gt; gt 13</span>

<span class="go">gpio13: 0</span>
</pre></div>
</div>
</div>
</div>


           </div>
