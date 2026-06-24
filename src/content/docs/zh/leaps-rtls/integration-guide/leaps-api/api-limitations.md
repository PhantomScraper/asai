---
title: "API 限制"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/api-limitations"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/api-limitations/"
order: 116
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api-limitations">
<h1>API 限制</h1>
<p>当通过 BLE 接口更改节点配置，同时在 SPI/UART 接口上执行 API 命令时，SPI/UART 接口上的 API 可能无法正常工作。 目前应同时使用 BLE 或 SPI/UART，以避免潜在错误。 某些 shell 命令也会将数据写入闪存，因此如果同时使用 UART/SPI 和 BLE 接口，可能会导致问题。 这是因为在擦除或写入 FLASH 时，CPU 会停止运行。</p>
</div>


           </div>
