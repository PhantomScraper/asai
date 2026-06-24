---
title: "dwm_i2c_read"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-i2c-read"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-i2c-read/"
order: 191
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-i2c-read">
<span id="id1"></span><h1>dwm_i2c_read</h1>
<p>从 I2C 从站读取数据。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_i2c_read">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_i2c_read</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">uint8_t</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – 地址, 数据, len</p></li>
<li><p><strong>addr</strong> – 8 位整数 (<em>从属设备的地址 (只有 7 LSB)</em>)</p></li>
<li><p><strong>data</strong> – 8 位整数 (<em>接收缓冲区的指针</em>)</p></li>
<li><p><strong>len</strong> – 8 位整数 (<em>要接收的字节数</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">data</span><span class="p">[</span><span class="mi">2</span><span class="p">];</span>
<span class="k">const</span><span class="w"> </span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">addr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="c1">// some address of the slave device**</span>
<span class="n">dwm_i2c_read</span><span class="p">(</span><span class="n">addr</span><span class="w"> </span><span class="p">,</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<p>这些接口不可用。</p>
</div>


           </div>
