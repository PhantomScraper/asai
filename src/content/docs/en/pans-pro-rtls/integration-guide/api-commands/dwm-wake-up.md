---
title: "dwm_wake_up"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-wake-up"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-wake-up/"
order: 220
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-wake-up">
<span id="id1"></span><h1>dwm_wake_up</h1>
<p>Prevents the system from entering sleep mode if it is in low-power mode.
This function should only be called from within a thread context.
See also <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a>.</p>
<p><strong>C code example</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="cm">/* THREAD 1: sleep and block*/</span>
<span class="n">dwm_sleep</span><span class="p">();</span>
<span class="cm">/*do something*/</span>
<span class="p">...</span>
<span class="cm">/*THREAD 2: wait until event */</span>
<span class="n">dwm_evt_wait</span><span class="p">(</span><span class="o">&amp;</span><span class="n">evt</span><span class="p">);</span>
<span class="cm">/*unblock dwm_sleep()*/</span>
<span class="n">dwm_wake_up</span><span class="p">();</span>
</pre></div>
</div>
<p><strong>SPI/UART example</strong></p>
<p>Not available on these interfaces.</p>
</div>


           </div>
