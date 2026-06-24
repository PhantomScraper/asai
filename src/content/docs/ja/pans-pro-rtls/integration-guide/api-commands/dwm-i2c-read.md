---
title: "dwm_i2c_read"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-i2c-read"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-i2c-read/"
order: 191
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-i2c-read">
<span id="id1"></span><h1>dwm_i2c_read</h1>
<p>I2C スレーブからデータを読み取ります。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_i2c_read">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_i2c_read</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">uint8_t</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- アドレス、データ、長さ</p></li>
<li><p><strong>addr</strong> -- 8 ビット整数 (<em>スレーブデバイスのアドレス (LSB 7 のみ)</em>)</p></li>
<li><p><strong>data</strong> -- 8 ビット整数 (<em>受信バッファへのポインタ</em>)</p></li>
<li><p><strong>len</strong> -- 8 ビット整数 (<em>受信するバイト数</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">data</span><span class="p">[</span><span class="mi">2</span><span class="p">];</span>
<span class="k">const</span><span class="w"> </span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">addr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="c1">// some address of the slave device**</span>
<span class="n">dwm_i2c_read</span><span class="p">(</span><span class="n">addr</span><span class="w"> </span><span class="p">,</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<p>これらのインターフェースでは使用できません。</p>
</div>


           </div>
