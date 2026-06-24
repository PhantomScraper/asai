---
title: "ゲートウェイ"
lang: ja
slug: "pans-pro-rtls/integration-guide/shell-api/gateway"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/shell-api/gateway/"
order: 126
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="gateway">
<h1>ゲートウェイ</h1>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>以下のコマンドはGateway MCUのみに適用されることに注意してください。</p>
</div>
<hr class="docutils">
<div class="section" id="ana">
<span id="pp-ana"></span><h2>ana</h2>
<p>ana: ノードのUWB、BLE、イーサネット、Wi-Fiアドレスを設定する。( dwm_mac_addr_setを参照)</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; ana</span>
<span class="go">dwm&gt; ana</span>
<span class="go">Usage: ana &lt;TYPE&gt; &lt;ADDR&gt;</span>
<span class="go"> TYPE can be 0=UWB, 1=BLE-Random, 2=BLE-Public, 3=ETH, 4=WiFi</span>
<span class="go"> ADDR is 6-byte long hex number</span>
<span class="go">dwm&gt; ana 0 0xaabbccddeeff</span>
<span class="go">ana: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="amls">
<span id="pp-amls"></span><h2>amls</h2>
<p>amls: MACアドレスリストを一度設定する。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; amls 0xaabbccddeeff 0x112233445566</span>
<span class="go">amls(ok)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="amlg">
<span id="pp-amlg"></span><h2>amlg</h2>
<p>MACアドレスのリストを取得し、その説明はdwm_mac_addr_getを参照する。</p>
<ul class="simple">
<li><p>usr - ユーザが指定したカスタムMACアドレス</p></li>
<li><p>pub, rand - パブリックまたはランダムBLEアドレス</p></li>
<li><p>def - デフォルトアドレス</p></li>
<li><p>def, mutable - 変更可能なデフォルトアドレス。デフォルトアドレスが変更可能な場合、デフォルトアドレスは一度しか変更できない。</p></li>
</ul>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; amlg</span>
<span class="go">mac0=68:79:12:90:11:11 (usr)</span>
<span class="go">mac1=68:79:12:90:22:22 (def, pub)</span>
<span class="go">mac2=68:79:12:90:33:33 (def)</span>
<span class="go">mac3=</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ahs">
<span id="pp-ahs"></span><h2>ahs</h2>
<p>Sets the HW version in the OTP memory.</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Before executing the AHS command, follow these steps:</p>
<ul class="simple">
<li><p>Set the node to offline mode using the <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmo"><span class="std std-ref">nmo</span></a> command.</p></li>
<li><p>Run the command ahs 0x0b100111 (execute only once).</p></li>
<li><p>Execute <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sys#pp-reset"><span class="std std-ref">リセット</span></a> twice.</p></li>
<li><p>Verify that the changes were applied successfully using the <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sys#pp-si"><span class="std std-ref">si</span></a> command.</p></li>
</ul>
</div>
<p>Example</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; ahs</span>
<span class="go">Usage: ahs &lt;hw_ver&gt;</span>
<span class="go">dwm&gt; ahs 0x0b100111</span>
<span class="go">ahs: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="acs">
<span id="pp-acs"></span><h2>acs</h2>
<p>イーサネットゲートウェイでのみ使用可能で、ノードの設定を行います。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; acs</span>
<span class="go">usage: acs [leds 0|1] [enc 0|1] [fwup 0|1] [uwb 0|1|2]</span>
<span class="go">uwb 0-off,1-pasv,2-act</span>
<span class="go">leaps&gt; acs leds 0 fwup 0</span>
<span class="go">ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ums">
<span id="pp-ums"></span><h2>ums</h2>
<p>イーサネットゲートウェイでのみ使用可能で、デフォルトのUARTモード（バイナリまたはシェル）を設定します。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; ums 1</span>
<span class="go">...</span>
<span class="go">dwm&gt; ums 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ipv4">
<span id="pp-ipv4"></span><h2>ipv4</h2>
<p>イーサネットゲートウェイでのみ利用可能で、ローカルのIPv4ネットワーク構成を設定します。インターネットに接続されている場合、デフォルトのDNSサーバーは8.8.8.8と4.4.4.4です。デフォルトのNTPタイムサーバーはtime.google.comです。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4</span>
<span class="go">usage: ipv4 [static|dynamic] [eth|wifi] [addr STRING] [mask STRING] [gw STRING]</span>

<span class="go">Use DHCP server to obtain IP address</span>
<span class="go">leaps&gt; ipv4 dynamic</span>
<span class="go">ipv4 (Success)</span>

<span class="go">Use static IP address settings</span>
<span class="go">usage: ipv4 addr 192.168.1.103 mask 255.255.255.0</span>
<span class="go">ipv4 (Success)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="dns">
<span id="pp-dns"></span><h2>dns</h2>
<p>イーサネットゲートウェイでのみ使用可能で、DNSサーバーを設定します。静的IPアドレスを使用している場合、またはDHCPサーバーがDNS設定を提供していない場合にのみ有効になります。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; dns</span>
<span class="go">usage: dns [STRING STRING]</span>

<span class="go">Configure DNS server (up to 2 DNS servers is supported)</span>
<span class="go">leaps&gt; dns 8.8.8.8</span>
<span class="go">dns (Success)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="wifi">
<span id="pp-wifi"></span><h2>wifi</h2>
<p>イーサネットゲートウェイでのみ利用可能で、WIFI SSID、PSK、スキャン地域を設定します。SSIDとPSKには空白文字を使用しないでください。</p>
<p>例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; wifi</span>
<span class="go">usage: wifi [ssid] [pwd] [region]</span>
<span class="go">region 0-europe(default), 1-north-america, 2-asia</span>

<span class="go">Configure SSID, PSK</span>
<span class="go">leaps&gt; wifi MyWifiSSID mywifipassword</span>
<span class="go">wifi (Success)</span>
</pre></div>
</div>
</div>
</div>


           </div>
