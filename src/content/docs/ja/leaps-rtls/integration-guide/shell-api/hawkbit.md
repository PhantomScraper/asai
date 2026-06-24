---
title: "HAWKBIT"
lang: ja
slug: "leaps-rtls/integration-guide/shell-api/hawkbit"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/shell-api/hawkbit/"
order: 142
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="hawkbit">
<h1>HAWKBIT</h1>
<hr class="docutils">
<div class="section" id="hb-peer">
<span id="id1"></span><h2>hb_peer</h2>
<p>Set Hawkbit server IPv4</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; hb_peer</span>

<span class="go">Usage: hb_peer [host STRING] [port NUM]</span>
</pre></div>
</div>
<p>[host STRING] [port NUM] The Hawkbit server's IP address and Port number.</p>
</div></blockquote>
<p>Example:</p>
<blockquote>
<div><p>Suppose, Hawkbit server is deployed at IP 192.168.10.102 and port 8081. The shell command to configure the Hawkbit IP address for gateway is as follows:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; hb_peer host 192.168.10.102 port 8081</span>
<span class="go">hb_peer (Success)</span>
</pre></div>
</div>
<p>Check the configuration again with the <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#si"><span class="std std-ref">si</span></a> command.</p>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="hb-token">
<span id="id2"></span><h2>hb_token</h2>
<p>hb_token: Set Hawkbit auth token</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; hb_token</span>

<span class="go">Usage: hb_token [auth_token : STRING]</span>
</pre></div>
</div>
<p>[auth_token : STRING] The security token obtained in the previous step.</p>
</div></blockquote>
<p>Example:</p>
<blockquote>
<div><p>The command line syntax to configure a security token on gateway is as follows:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; hb_token 772118077bc13af93f7f590693ef5215</span>
<span class="go">hb_token (Success)</span>
</pre></div>
</div>
<p>Check the configuration again with the <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#si"><span class="std std-ref">si</span></a> command.</p>
</div></blockquote>
</div>
</div>


           </div>
