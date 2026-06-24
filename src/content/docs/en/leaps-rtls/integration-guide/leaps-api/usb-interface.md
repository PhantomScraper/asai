---
title: "USB interface"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/usb-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/usb-interface/"
order: 134
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="usb-interface">
<h1>USB interface</h1>
<p>USB interface of LEAPS RTLS devices provides a composite USB device. The interface provides an  ACM class to support shell access, similar to the UART interface. It also provides a  Leaps proprietary class to support binary mode. On a linux host, the ACM class would be recognized as a tty device (/dev/ttyACM…), and the proprietary class could be accessed using libusb. Data transfer with proprietary class would be directly over in/out endpoints (0x81, 0x01).</p>
</div>


           </div>
