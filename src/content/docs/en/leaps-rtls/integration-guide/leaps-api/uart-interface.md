---
title: "UART Interface"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/uart-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/uart-interface/"
order: 133
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uart-interface">
<h1>UART Interface</h1>
<hr class="docutils">
<p>Users should wait at least 1 second after resetting before using the UART API interface. The UART can operate in a binary or a shell mode. After reset for the UART, The default mode can be configured by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set#leaps-serial-cfg-set"><span class="std std-ref">leaps_serial_cfg_set</span></a>. Press “ENTER” twice within one second to switch from binary mode to shell mode. Use shell command <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/base#quit"><span class="std std-ref">quit</span></a> to switch from shell mode to binary mode.</p>
<a class="reference internal image-reference" href="../../../../_images/image8.png"><img alt="../../../../_images/image8.png" class="align-center" src="/docs-assets/_images/image8.png" style="width: 384.0px; height: 265.0px;"></a>
<hr class="docutils">
<div class="section" id="example-leaps-gpio-cfg-output">
<h2>Example leaps_gpio_cfg_output</h2>
<a class="reference internal image-reference" href="../../../../_images/image9.png"><img alt="../../../../_images/image9.png" class="align-center" src="/docs-assets/_images/image9.png" style="width: 384.0px; height: 279.0px;"></a>
<hr class="docutils">
<div class="section" id="wakeup-via-uart">
<h3>Wakeup via UART</h3>
<p>If the module sleeps (in low-power mode), the wakeup procedure has to be executed before SPI/UART starts accepting commands. At least, 35
microsecond wide pulse has to be generated on the CS pin of the SPI or at least one byte has to be sent on the UART interface to wake
up from the sleep (only in low-power mode).</p>
</div>
</div>
</div>


           </div>
