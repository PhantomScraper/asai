---
title: "dwm_i2c_write"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-i2c-write"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-i2c-write/"
order: 193
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-i2c-write">
<span id="id1"></span><h1>dwm_i2c_write</h1>
<p>Writes data to I2C slave.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_i2c_write">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_i2c_write</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span>, <span class="n"><span class="pre">boolean_t</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – addr, data, len, no_stop</p></li>
<li><p><strong>addr</strong> – 8-bit integer (<em>Address of a slave device (only 7 LSB)</em>)</p></li>
<li><p><strong>data</strong> – 8-bit integer (<em>Pointer to a transmit buffer</em>)</p></li>
<li><p><strong>len</strong> – 8-bit integer (<em>Number of bytes to send</em>)</p></li>
<li><p><strong>no_stop</strong> – ‘0’ | ‘1’ (<em>If set, the stop condition is not generated on the bus after the transfer has been completed successfully (allowing for a repeated    :param start in the next transfer)</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">data</span><span class="p">[</span><span class="mi">2</span><span class="p">];</span>
<span class="k">const</span><span class="w"> </span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">addr</span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="c1">// some address of the slave device</span>
<span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">=</span><span class="w"> </span><span class="mh">0xAA</span><span class="p">;</span>
<span class="n">data</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">=</span><span class="w"> </span><span class="mh">0xBB</span><span class="p">;</span>
<span class="n">dwm_i2c_write</span><span class="p">(</span><span class="n">addr</span><span class="p">,</span><span class="w"> </span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="nb">true</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<p>not available on these interfaces</p>
</div>


           </div>
