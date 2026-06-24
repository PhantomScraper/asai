---
title: "dwm_gpio_irq_dis"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-gpio-irq-dis"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-irq-dis/"
order: 188
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-gpio-irq-dis">
<span id="id1"></span><h1>dwm_gpio_irq_dis</h1>
<p>Disables interrupts for GPIO pin.</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_gpio_irq_dis">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_gpio_irq_dis</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">gpio_idx</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>gpio_idx</strong> – 8-bit integer (see the section gpio_idx for allowed values)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_gpio_irq_dis</span><span class="p">(</span><span class="n">DWM_GPIO_IDX_13</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<p>not available on these interfaces</p>
</div>


           </div>
