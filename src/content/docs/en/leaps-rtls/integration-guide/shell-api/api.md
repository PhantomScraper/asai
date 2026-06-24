---
title: "API"
lang: en
slug: "leaps-rtls/integration-guide/shell-api/api"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/shell-api/api/"
order: 141
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api">
<h1>API</h1>
<hr class="docutils">
<div class="section" id="urs">
<span id="id1"></span><h2>urs</h2>
<p>set the position propagation rate.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; urs</span>

<span class="go">Usage urs &lt;nom&gt; &lt;stat&gt;</span>

<span class="go">leaps&gt; urs 10 20</span>

<span class="go">err code: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="urg">
<span id="id2"></span><h2>urg</h2>
<p>Get propagation rate.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; urg</span>

<span class="go">err code: 0, upd rate: 10, 20(stat)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="tcs">
<span id="id3"></span><h2>tcs</h2>
<p>Configure node as tag with given options. This command requires reset
for new configuration to take effect.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; tcs</span>

<span class="go">usage: tcs &lt;opt&gt; &lt;val&gt; ...</span>

<span class="go">opt: stat_det,lp,le,enc,leds,ble,fwup(0,1) mode(0-twr,1-ul-tdoa,2-dl-tdoa)</span>
<span class="go">uwb(0-off,1-pasv,2-act)</span>
</pre></div>
</div>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; tcs le 1 leds 1 uwb 2</span>

<span class="go">ok(0)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="tlv">
<span id="id4"></span><h2>tlv</h2>
<p>Parses given TLV frame. It accepts both decimal and hexadecimal format.</p>
<p>Example: Read user data from the node (<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-usr-data-read#leaps-usr-data-read"><span class="std std-ref">leaps_usr_data_read</span></a>)</p>
<p>Decimal format:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; tlv 25 01 02</span>

<span class="go">CRC: 0x26</span>

<span class="go">OUTPUT(hex):</span>

<span class="go">40 01 00 06 58 00 d0</span>
</pre></div>
</div>
<p>Hexadecimal format:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; tlv 0x19 0x01 0x02</span>

<span class="go">CRC: 0x26</span>

<span class="go">OUTPUT(hex):</span>

<span class="go">40 01 00 06 58 00 d0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="tlvr">
<span id="id5"></span><h2>tlvr</h2>
<p>Cmd as TLV frame with manual CRC. It accepts both decimal and hexadecimal format.</p>
<p>Example: Read user data from the node (<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-usr-data-read#leaps-usr-data-read"><span class="std std-ref">leaps_usr_data_read</span></a>)</p>
<p>Decimal format:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; tlv 25 01 02 38</span>

<span class="go">OUTPUT FRAME:</span>

<span class="go">40 01 00 06 58 00 d0</span>
</pre></div>
</div>
<p>Hexadecimal format:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; tlv 0x19 0x01 0x02 0x26</span>

<span class="go">OUTPUT FRAME:</span>

<span class="go">40 01 00 06 58 00 d0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ums">
<span id="id6"></span><h2>ums</h2>
<p>Set default UART mode</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ums 1</span>

<span class="go"> Low Energy Accurate Positioning System</span>

<span class="go"> Copyright :  2016-2024 LEAPS</span>
<span class="go"> License   :  Please visit https://www.leapslabs.com/leaps-rtls-license</span>
<span class="go"> Compiled  :  Mar 26 2024 09:19:46 (v0.16.2-14d8a4)</span>

<span class="go"> Help      :  ? or help</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ana">
<span id="id7"></span><h2>ana</h2>
<p>Set MAC address</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This sets a temporary MAC address only. It is not permanent and can be overwritten or reset.</p>
</div>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ana 0 2:3:4:5:6:8</span>
<span class="go">ana: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="amlg">
<span id="id8"></span><h2>amlg</h2>
<p>Get MAC address list</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; amlg</span>
<span class="go">mac0=00:00:00:00:00:02 (usr)</span>
<span class="go">mac1=F1:7C:5C:D8:28:55 (def, mutable, rand)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="mrs">
<span id="id9"></span><h2>mrs</h2>
<p>Set mesh random timing</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; mrs</span>
<span class="go">Usage: mrs &lt;rand (ms)&gt;</span>
<span class="go">leaps&gt; mrs 10</span>
<span class="go">mrs: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="mrg">
<span id="id10"></span><h2>mrg</h2>
<p>Get mesh random timing</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; mrg</span>
<span class="go">mrg: rand:10</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="dacs">
<span id="id11"></span><h2>dacs</h2>
<p>Configures distance alarm event.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; dacs</span>

<span class="go">Usage: dacs &lt;thold_1&gt; &lt;thold_2&gt; &lt;mincon&gt; &lt;minnocon&gt; &lt;opt&gt;</span>

<span class="go">opt: bit 0,1,2 enables leds,buzzer,motor respectively</span>

<span class="go">leaps&gt; dacs 500 2000 0 0 7</span>

<span class="go">dacs: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="dacg">
<span id="id12"></span><h2>dacg</h2>
<p>Reads configuration of distance alarm event.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; dacg</span>

<span class="go">Usage: dacs &lt;thold_1&gt; &lt;thold_2&gt; &lt;thold_3&gt;</span>

<span class="go">leaps&gt; dacg</span>

<span class="go">dacg: thold_1=1000 thold_2=2000 thold_3=3000</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="acs">
<span id="id13"></span><h2>acs</h2>
<p>Configure node as anchor with given options. This command requires reset
for new configuration to take effect.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; acs</span>

<span class="go">*[Output when UWB routing backhaul is disabled]*</span>

<span class="go">usage: acs &lt;opt&gt; &lt;val&gt; ...</span>

<span class="go">opt: inr,gn,enc,leds,ble,fwup,cr,uab(0,1) uwb(0-off,1-pasv,2-act)</span>

<span class="go">*[Output when UWB routing backhaul is enabled]*</span>

<span class="go">usage: acs &lt;opt&gt; &lt;val&gt; ...</span>

<span class="go">opt: inr,gn,enc,leds,ble,fwup,cr,uab(0,1) bh(0-off,1-on,2-auto)</span>
<span class="go">uwb(0-off,1-pasv,2-act)</span>
</pre></div>
</div>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; acs leds 1 uwb 2</span>

<span class="go">ok(0)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="pg">
<span id="id14"></span><h2>pg</h2>
<p>Get the position.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; pg</span>

<span class="go">x:100 y:120 z:2500 qf:100</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ps">
<span id="id15"></span><h2>ps</h2>
<p>Set the position.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ps</span>

<span class="go">Usage ps &lt;x&gt; &lt;y&gt; &lt;z&gt;</span>

<span class="go">leaps&gt; ps 100 120 2500</span>

<span class="go">err code: 0</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="fls">
<span id="id16"></span><h2>fls</h2>
<p>Configures filters, e.g. measurement filter, location filter,
measurement select strategy etc.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; fls</span>

<span class="go">leaps&gt; usage: fls &lt;id&gt; &lt;param(byte array, max len:8)&gt;</span>

<span class="go">id: 0=meas, 1=loc, 2=meas strtg</span>

<span class="go">leaps&gt; fls 2 1</span>

<span class="go">fls: ok</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If id = 1 - loc, the param(byte[0]) specifies whether the moving average filter for position is enabled or disabled.</p>
</div>
<hr class="docutils">
</div>
<div class="section" id="flg">
<span id="id17"></span><h2>flg</h2>
<p>Get filters, e.g. measurement filter, location filter, measurement select strategy etc.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; flg</span>

<span class="go">leaps&gt; usage: flg &lt;id&gt;</span>

<span class="go">id: 0=meas, 1=loc, 2=meas strtg</span>

<span class="go">leaps&gt; flg 2</span>

<span class="go">flg: id:2(meas strtg) param(hex):01 00 00 00 00 00 00 00</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ahs">
<span id="id18"></span><h2>ahs</h2>
<p>Set HW version once</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ahs</span>
<span class="go">usage: ahs &lt;hw_ver&gt; | &lt;board_name&gt;</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="eks">
<span id="id19"></span><h2>eks</h2>
<p>Sets encryption key, takes encryption key as argument.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; eks 00112233445566778899aabbccddeeff</span>

<span class="go">key_set: 00112233445566778899AABBCCDDEEFF</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="ekc">
<span id="id20"></span><h2>ekc</h2>
<p>Clears encryption key and disables encryption.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ekc</span>

<span class="go">ekc : ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="amls">
<span id="id21"></span><h2>amls</h2>
<p>Set MAC addr list once (permanent OTP write - irreversible)</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This command permanently writes to OTP (One-Time Programmable) memory.</p>
<p>Once executed:</p>
<ul class="simple">
<li><p>The data cannot be overwritten or modified</p></li>
<li><p>Previous MAC address entries cannot be changed</p></li>
<li><p>Exercise caution as this action is irreversible</p></li>
</ul>
<p>Recommendation: Verify the MAC addresses carefully before executing this command</p>
</div>
<hr class="docutils">
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; amls</span>
<span class="go">usage: amls &lt;hex_0&gt; ... &lt;hex_3&gt;</span>
</pre></div>
</div>
</div>
</div>


           </div>
