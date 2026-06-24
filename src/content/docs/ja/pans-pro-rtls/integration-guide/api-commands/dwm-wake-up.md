---
title: "dwm_wake_up"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-wake-up"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-wake-up/"
order: 219
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-wake-up">
<span id="id1"></span><h1>dwm_wake_up</h1>
<p>システムが低電力モードの場合、システムがスリープ モードに移行しないようにします。この関数はスレッド コンテキスト内からのみ呼び出す必要があります。 <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a> も参照してください。</p>
<p><strong>Cコード例</strong></p>
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
<p><strong>SPI/UART 例</strong></p>
<p>これらのインターフェースでは使用できません。</p>
</div>


           </div>
