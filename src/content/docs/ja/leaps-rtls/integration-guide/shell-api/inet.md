---
title: "INET"
lang: ja
slug: "leaps-rtls/integration-guide/shell-api/inet"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/shell-api/inet/"
order: 141
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="inet">
<h1>INET</h1>
<hr class="docutils">
<div class="section" id="ipv4">
<span id="id1"></span><h2>ipv4</h2>
<p>Set local IPv4. This command is used to configure the local IPv4 network settings for either an Ethernet or Wi-Fi connection.</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4</span>

<span class="go">Usage: ipv4 [static|dynamic] [eth|wifi] [addr STRING] [mask STRING] [gw STRING]</span>
</pre></div>
</div>
<p>static | dynamic</p>
<blockquote>
<div><ul class="simple">
<li><p>static — Manually set the IP address information</p></li>
<li><p>dynamic — Automatically obtain IP settings (DHCP)</p></li>
</ul>
</div></blockquote>
<p>eth | wifi</p>
<blockquote>
<div><ul class="simple">
<li><p>eth — Apply settings to the Ethernet interface</p></li>
<li><p>wifi — Apply settings to the Wi-Fi interface</p></li>
</ul>
</div></blockquote>
<p>addr STRING (static only)</p>
<blockquote>
<div><ul class="simple">
<li><p>The IPv4 address to assign (example: 192.168.1.100)</p></li>
</ul>
</div></blockquote>
<p>mask STRING (static only)</p>
<blockquote>
<div><ul class="simple">
<li><p>The subnet mask (example: 255.255.255.0)</p></li>
</ul>
</div></blockquote>
<p>gw STRING (static only)</p>
<blockquote>
<div><ul class="simple">
<li><p>The default gateway address (example: 192.168.1.1)</p></li>
</ul>
</div></blockquote>
</div></blockquote>
<p>Example:</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>Set a static IPv4 address for Ethernet</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 static eth addr 192.168.1.100 mask 255.255.255.0 gw 192.168.1.1</span>
<span class="go">ipv4 (Success)</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>Set a static IPv4 address for Wi-Fi</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 static wifi addr 10.0.0.50 mask 255.255.255.0 gw 10.0.0.1</span>
<span class="go">ipv4 (Success)</span>
</pre></div>
</div>
<ol class="arabic simple" start="3">
<li><p>Enable dynamic (DHCP) configuration for Ethernet</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 dynamic eth</span>
<span class="go">ipv4 (Success)</span>
</pre></div>
</div>
<ol class="arabic simple" start="4">
<li><p>Enable dynamic (DHCP) configuration for Wi-Fi</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 dynamic wifi</span>
<span class="go">ipv4 (Success)</span>
</pre></div>
</div>
</div></blockquote>
<p>Notes:</p>
<blockquote>
<div><ul class="simple">
<li><p>When using dynamic, the addr, mask, and gw parameters are not required.</p></li>
<li><p>When using static, all three (addr, mask, gw) must be provided.</p></li>
<li><p>Make sure the IP address and gateway are within the same network range.</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="peer">
<span id="id2"></span><h2>peer</h2>
<p>Set server IPv4. This command configures the server (peer) IPv4 connection settings, including the server address, port, TLS security level, and message filtering.</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer</span>

<span class="go">Usage: peer [host STRING] [port NUM] [tls 0|1|2|3|4] [mflt 0|1]</span>
<span class="go">tls 0-off, 1-on, 2-on(mutual authentication), 3-on(check CN), 4-on(mutual authentication, check CN)</span>
</pre></div>
</div>
<p>host STRING</p>
<blockquote>
<div><ul class="simple">
<li><p>The server’s IPv4 address or hostname</p></li>
<li><p>Example: 192.168.1.10</p></li>
</ul>
</div></blockquote>
<p>port NUM</p>
<blockquote>
<div><ul class="simple">
<li><p>The server port number</p></li>
<li><p>Example: 1883, 7777</p></li>
</ul>
</div></blockquote>
<p>tls 0|1|2|3|4</p>
<blockquote>
<div><ul>
<li><p>Defines the TLS security mode:</p>
<p>0 — TLS off</p>
<p>1 — TLS on</p>
<p>2 — TLS on (mutual authentication)</p>
<p>3 — TLS on (check Common Name / CN)</p>
<p>4 — TLS on (mutual authentication + check CN)</p>
</li>
</ul>
</div></blockquote>
<p>mflt 0|1</p>
<blockquote>
<div><ul>
<li><p>Message filtering option:</p>
<p>0 — Message filtering disabled</p>
<p>1 — Message filtering enabled</p>
</li>
</ul>
</div></blockquote>
</div></blockquote>
<p>Example:</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>Set server with no TLS</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer host 192.168.1.10 port 1883 tls 0 mflt 0</span>
<span class="go">peer (Success)</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>Set server with TLS enabled</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer host server.example.com port 7777 tls 1 mflt 0</span>
<span class="go">peer (Success)</span>
</pre></div>
</div>
<ol class="arabic simple" start="3">
<li><p>Set server with TLS and mutual authentication</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer host 10.0.0.5 port 7777 tls 2 mflt 1</span>
<span class="go">peer (Success)</span>
</pre></div>
</div>
<ol class="arabic simple" start="4">
<li><p>Set server with TLS, CN check</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer host secure.example.com port 7777 tls 3 mflt 1</span>
<span class="go">peer (Success)</span>
</pre></div>
</div>
<ol class="arabic simple" start="5">
<li><p>Set server with maximum security (mutual authentication + CN check)</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer host secure.example.com port 7777 tls 4 mflt 1</span>
<span class="go">peer (Success)</span>
</pre></div>
</div>
</div></blockquote>
<p>Notes</p>
<blockquote>
<div><ul class="simple">
<li><p>Use higher TLS modes (2–4) for better security in production environments.</p></li>
<li><p>Mutual authentication requires valid client and server certificates.</p></li>
<li><p>CN checking ensures the server certificate matches the specified host.</p></li>
<li><p>Make sure the selected port matches the server’s configuration.</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="wifi">
<span id="id3"></span><h2>wifi</h2>
<p>Set WIFI configuration. This command configures the device’s Wi-Fi connection by setting the network name and password.</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; wifi</span>

<span class="go">Usage: wifi [ssid] [pwd]</span>
</pre></div>
</div>
<p>ssid</p>
<blockquote>
<div><ul class="simple">
<li><p>The name of the Wi-Fi network to connect to</p></li>
<li><p>Example: HomeNetwork</p></li>
</ul>
</div></blockquote>
<p>pwd</p>
<blockquote>
<div><ul class="simple">
<li><p>The password for the Wi-Fi network</p></li>
<li><p>Example: SecurePassword123</p></li>
</ul>
</div></blockquote>
</div></blockquote>
<p>Example:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; wifi HomeNetwork SecurePassword123</span>
<span class="go">wifi (Success)</span>
</pre></div>
</div>
</div></blockquote>
<p>Notes</p>
<blockquote>
<div><ul class="simple">
<li><p>The SSID and password are case-sensitive.</p></li>
<li><p>Ensure the Wi-Fi network is within range and supports the device.</p></li>
<li><p>If the password is incorrect, the connection will fail.</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="dns">
<span id="id4"></span><h2>dns</h2>
<p>Set DNS server IP address list. This command configures the DNS (Domain Name System) server IP addresses used for name resolution.</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; dns</span>

<span class="go">Usage: dns [PRIMARY SECONDARY]</span>
</pre></div>
</div>
<p>PRIMARY</p>
<blockquote>
<div><ul class="simple">
<li><p>The primary DNS server IP address</p></li>
<li><p>Example: 8.8.8.8</p></li>
</ul>
</div></blockquote>
<p>SECONDARY</p>
<blockquote>
<div><ul class="simple">
<li><p>The secondary (backup) DNS server IP address</p></li>
<li><p>Example: 8.8.4.4</p></li>
</ul>
</div></blockquote>
</div></blockquote>
<p>Example:</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; dns 8.8.8.8 8.8.4.4</span>
<span class="go">dns (Success)</span>
</pre></div>
</div>
</div></blockquote>
<p>Notes</p>
<blockquote>
<div><ul class="simple">
<li><p>Both DNS server addresses must be valid IPv4 addresses.</p></li>
<li><p>The secondary DNS server is used if the primary server is unavailable.</p></li>
</ul>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="switch">
<span id="id5"></span><h2>switch</h2>
<p>Set net switch configuration. This command is used to enable or disable automatic switching between Ethernet and Wi-Fi connections.</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; switch</span>
<span class="go">switch: 1 (enabled)</span>
<span class="go">usage: switch [0|1]</span>
</pre></div>
</div>
</div></blockquote>
<p>Example:</p>
<ol class="arabic simple">
<li><p>Check the current state of the network switch.</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; switch</span>
<span class="go">switch: 0 (disabled)</span>
<span class="go">usage: switch [0|1]</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Enable to switch automatically.</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; switch 1</span>
<span class="go">switch (Success)</span>
<span class="go">leaps&gt; switch</span>
<span class="go">switch: 1</span>
<span class="go">usage: switch [0|1]</span>
</pre></div>
</div>
</div></blockquote>
</div>
</div>


           </div>
