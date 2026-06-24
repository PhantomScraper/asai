---
title: "USB 接口"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/usb-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/usb-interface/"
order: 133
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="usb-interface">
<h1>USB 接口</h1>
<p>LEAPS RTLS 设备的 USB 接口提供了一个复合 USB 设备. 该接口提供一个 ACM 类，以支持 shell 访问，类似于 UART 接口. 它还提供了一个 Leaps 专有类，以支持二进制模式. 在 linux 主机上，ACM 类将被识别为 tty 设备（/dev/ttyACM…），并可使用 libusb 访问专有类. 专有类的数据传输将直接通过输入/输出端点（0x81, 0x01）进行。</p>
</div>


           </div>
