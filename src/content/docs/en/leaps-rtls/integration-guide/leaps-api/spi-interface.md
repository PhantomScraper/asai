---
title: "SPI Interface"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/spi-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/spi-interface/"
order: 132
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="spi-interface">
<h1>SPI Interface</h1>
<hr class="docutils">
<p>The module responds with 0xFF in an idle state. The minimum delay between SPI transactions must be at least five milliseconds. The module acts as a SPI slave on the SPI bus. Maximum number of bytes supported by the slave in one transfer is 255. The User should wait at least 1 second after reset before using the SPI API interface.</p>
<hr class="docutils">
<div class="section" id="using-polling">
<h2>Using polling</h2>
<a class="reference internal image-reference" href="../../../../_images/image3.png"><img alt="../../../../_images/image3.png" class="align-center" src="/docs-assets/_images/image3.png" style="width: 615.0px; height: 352.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="example-polling-leaps-gpio-cfg-output">
<h2>Example polling leaps_gpio_cfg_output</h2>
<a class="reference internal image-reference" href="../../../../_images/image4.png"><img alt="../../../../_images/image4.png" class="align-center" src="/docs-assets/_images/image4.png" style="width: 614.0px; height: 312.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="using-interrupt-gpio-when-command-is-issued-from-the-master">
<h2>Using interrupt (GPIO) when command is issued from the master</h2>
<a class="reference internal image-reference" href="../../../../_images/image5.png"><img alt="../../../../_images/image5.png" class="align-center" src="/docs-assets/_images/image5.png" style="width: 615.0px; height: 464.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="using-core-int-gpio-pin-to-notify-master-about-the-status-change">
<h2>Using CORE_INT GPIO pin to notify master about the status change</h2>
<p>This interrupt is postponed if it happens during the TLV Request
response procedure described above.</p>
<a class="reference internal image-reference" href="../../../../_images/image6.png"><img alt="../../../../_images/image6.png" class="align-center" src="/docs-assets/_images/image6.png" style="width: 614.0px; height: 291.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="example-interrupt-leaps-bh-xfer">
<h2>Example interrupt leaps_bh_xfer</h2>
<p>The maximum payload size of a single TLV frame is 253 bytes (Max TLV frame supported by the slave - TLV header = 255 - 2 = 253). A number of bytes which the master wants to transfer to the slave (downlink) using the command leaps_bh_xfer is encoded in the argument of the command. Slave takes the number of downlink data and uplink data ready to be transferred to the master and decides the size and the number of transactions to transfer both the downlink and the uplink in the sequence of the SPI transfers.</p>
<p>Let’s say that the master wants to transfer 299 bytes of downlink data, and the slave has 1124 bytes of uplink data ready.</p>
<ul class="simple">
<li><p>downlink bytes: 299 (at least 2 TLV frames)</p></li>
<li><p>uplink bytes: 1124 (at least 5 TLV frames)</p></li>
</ul>
<p>The master executes the command leaps_bh_xfer with argument == 299. The slave responds with size == 255 and number of transactions == 5 (5 * 253 = 1265). Both downlink and uplink TLV data chunks are encoded using reserved TLV types that can be used to serialize the data encoded in multiple TLV frames. At most, 5 TLV frames are supported for now. TLV types 100-104 (0x64-0x68) are reserved for uplink data chunks. TLV types 110-114 (0x6E-0x72) are reserved for downlink data chunks.</p>
<a class="reference internal image-reference" href="../../../../_images/image7.png"><img alt="../../../../_images/image7.png" class="align-center" src="/docs-assets/_images/image7.png" style="width: 615.0px; height: 440.0px;"></a>
<hr class="docutils">
<div class="section" id="wakeup-via-spi">
<h3>Wakeup via SPI</h3>
<p>If the module sleeps (in low-power mode), the wakeup procedure has to be executed before SPI/UART starts accepting commands. At least, 35
microsecond wide pulse has to be generated on the CS pin of the SPI or at least one byte has to be sent on the UART interface to wake
up from the sleep (only in low-power mode).</p>
</div>
</div>
</div>


           </div>
