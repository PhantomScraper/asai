---
title: "USB インターフェース"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/usb-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/usb-interface/"
order: 133
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="usb-interface">
<h1>USB インターフェース</h1>
<p>LEAPS RTLS デバイスの USB インターフェイスは、複合 USB デバイスを提供します。このインターフェイスは、UART インターフェイスと同様に、シェル アクセスをサポートする ACM クラスを提供します。また、バイナリ モードをサポートするための Leaps 独自のクラスも提供します。 Linux ホストでは、ACM クラスは tty デバイス (/dev/ttyACM…) として認識され、独自クラスは libusb を使用してアクセスできます。独自クラスによるデータ転送は、in/out エンドポイント (0x81、0x01) を介して直接行われます。</p>
</div>


           </div>
