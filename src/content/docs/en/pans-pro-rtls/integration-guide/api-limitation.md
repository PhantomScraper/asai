---
title: "API Limitations"
lang: en
slug: "pans-pro-rtls/integration-guide/api-limitation"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-limitation/"
order: 125
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api-limitations">
<h1>API Limitations</h1>
<p>API on the SPI/UART interface might not work properly when node configuration is being changed via the BLE interface while API commands are being executed on the SPI/UART interface at the same time. Either the BLE or SPI/UART should be used at the time for now to avoid potential errors. Certain shell commands also write data into FLASH memory. Therefore,they can cause problems on the UART/SPI and BLE if these interfaces are being used at the same time. It is caused by the fact that the CPU is halted while FLASH is being erased or written.</p>
</div>


           </div>
