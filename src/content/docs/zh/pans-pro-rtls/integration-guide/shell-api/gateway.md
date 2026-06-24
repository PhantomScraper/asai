---
title: "网关"
lang: zh
slug: "pans-pro-rtls/integration-guide/shell-api/gateway"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/shell-api/gateway/"
order: 126
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="gateway">
<h1>网关</h1>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>请注意，以下命令仅适用于 Gateway MCU。</p>
</div>
<hr class="docutils">
<div class="section" id="ana">
<span id="pp-ana"></span><h2>ana</h2>
<p>ana: 设置节点的 UWB, BLE, 以太网或 Wi-Fi 地址. (参见 dwm_mac_addr_set)</p>
<p>示例:</p>
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
<p>amls: 设置一次 MAC 地址列表</p>
<p>示例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; amls 0xaabbccddeeff 0x112233445566</span>
<span class="go">amls(ok)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="amlg">
<span id="pp-amlg"></span><h2>amlg</h2>
<p>获取 MAC 地址列表，并参考 dwm_mac_addr_get 进行描述。</p>
<ul class="simple">
<li><p>usr - 用户指定的自定义 MAC 地址</p></li>
<li><p>pub, rand - 公共或随机 BLE 地址</p></li>
<li><p>def - 默认地址</p></li>
<li><p>def, mutable - 可修改的默认地址。 如果默认地址是可变的，则只能更改一次。</p></li>
</ul>
<p>示例:</p>
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
<p class="admonition-title">注解</p>
<p>Before executing the AHS command, follow these steps:</p>
<ul class="simple">
<li><p>Set the node to offline mode using the <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmo"><span class="std std-ref">nmo</span></a> command.</p></li>
<li><p>Run the command ahs 0x0b100111 (execute only once).</p></li>
<li><p>Execute <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sys#pp-reset"><span class="std std-ref">重置</span></a> twice.</p></li>
<li><p>Verify that the changes were applied successfully using the <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sys#pp-si"><span class="std std-ref">si</span></a> command.</p></li>
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
<p>仅在以太网网关上可用，它配置节点。</p>
<p>示例:</p>
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
<p>仅在以太网网关上可用，设置默认 UART 模式（二进制或 shell）。</p>
<p>示例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; ums 1</span>
<span class="go">...</span>
<span class="go">dwm&gt; ums 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ipv4">
<span id="pp-ipv4"></span><h2>ipv4</h2>
<p>仅在以太网网关上可用，可设置本地 IPv4 网络配置. 连接互联网时，默认 DNS 服务器为 8.8.8.8 和 4.4.4.4. 默认的 NTP 时间服务器是 time.google.com。</p>
<p>示例:</p>
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
<p>仅适用于以太网网关，可配置 DNS 服务器。 它只有在使用静态 IP 地址或 DHCP 服务器不提供 DNS 设置时才会生效。</p>
<p>示例:</p>
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
<p>仅适用于以太网网关，可配置 WIFI SSID, PSK 和扫描区域。 请勿在 SSID 和 PSK 中使用空白字符。</p>
<p>示例:</p>
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
