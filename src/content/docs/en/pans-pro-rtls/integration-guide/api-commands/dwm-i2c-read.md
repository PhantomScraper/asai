---
title: "dwm_i2c_read"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-i2c-read"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-i2c-read/"
order: 192
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-i2c-read">
<span id="id1"></span><h1>dwm_i2c_read</h1>
<p>Reads data from I2C slave.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_i2c_read">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_i2c_read</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">uint8_t</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – addr, data, len</p></li>
<li><p><strong>addr</strong> – 8-bit integer (<em>Address of a slave device (only 7 LSB)</em>)</p></li>
<li><p><strong>data</strong> – 8-bit integer (<em>Pointer to a receive buffer</em>)</p></li>
<li><p><strong>len</strong> – 8-bit integer (<em>Number of bytes to be received</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">data</span><span class="p">[</span><span class="mi">2</span><span class="p">];</span>
<span class="k">const</span><span class="w"> </span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">addr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="c1">// some address of the slave device**</span>
<span class="n">dwm_i2c_read</span><span class="p">(</span><span class="n">addr</span><span class="w"> </span><span class="p">,</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<p>Not available on these interfaces.</p>
</div>


           </div>
