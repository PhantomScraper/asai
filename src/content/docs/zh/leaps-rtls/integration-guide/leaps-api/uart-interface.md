---
title: "UART接口"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/uart-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/uart-interface/"
order: 132
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uart-interface">
<h1>UART接口</h1>
<hr class="docutils">
<p>用户应在重置后等待至少1秒，然后才能使用UART API接口。UART可以在二进制或shell模式下运行。UART重置后，可以通过以下方式配置默认模式 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set#leaps-serial-cfg-set"><span class="std std-ref">leaps_serial_cfg_set</span></a>。在一秒钟内按两次 “ENTER” 键，从二进制模式切换到shell模式。使用shell命令 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/base#quit"><span class="std std-ref">退出</span></a> 从shell模式切换到二进制模式。</p>
<a class="reference internal image-reference" href="../../../../_images/image8.png"><img alt="../../../../_images/image8.png" class="align-center" src="/docs-assets/zh-cn/_images/image8.png" style="width: 384.0px; height: 265.0px;"></a>
<hr class="docutils">
<div class="section" id="example-leaps-gpio-cfg-output">
<h2>示例 leaps_gpio_cfg_output</h2>
<a class="reference internal image-reference" href="../../../../_images/image9.png"><img alt="../../../../_images/image9.png" class="align-center" src="/docs-assets/zh-cn/_images/image9.png" style="width: 384.0px; height: 279.0px;"></a>
<hr class="docutils">
<div class="section" id="wakeup-via-uart">
<h3>通过UART唤醒</h3>
<p>如果模块处于休眠状态（低功耗模式），则必须在SPI/UART开始接受命令之前执行唤醒过程。至少，必须在SPI的CS引脚上产生35微秒宽的脉冲，或者必须在UART接口上发送至少一个字节才能从睡眠中唤醒（仅在低功耗模式下）。</p>
</div>
</div>
</div>


           </div>
