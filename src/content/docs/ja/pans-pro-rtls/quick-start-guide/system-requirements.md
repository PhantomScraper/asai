---
title: "システム要件"
lang: ja
slug: "pans-pro-rtls/quick-start-guide/system-requirements"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/quick-start-guide/system-requirements/"
order: 87
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="qsg-system-requirements"></span><h1>システム要件</h1>
<p>システム要件 以下のセクションでは <a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> の RTLS (Real-time Location System) デモを開始する前に必要なソフトウェアとハードウェアの詳細を説明します。一部の項目はオプションであり、すべてのデモで必須ではないことをご了承ください。</p>
<div class="section" id="hardware">
<h2>ハードウェア</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>アイテム</strong></p></th>
<th class="head"><p><strong>数量</strong></p></th>
<th class="head"><p><strong>必要量</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWBデバイス</p></td>
<td><p>6+</p></td>
<td><p>必須</p></td>
<td><ul class="simple">
<li><p>必須 最低4台の <code class="docutils literal notranslate"><span class="pre">LC4</span> <span class="pre">デバイス</span></code> (アンカーノード)</p></li>
<li><p>少なくとも1台の <code class="docutils literal notranslate"><span class="pre">LC8</span> <span class="pre">デバイス</span></code> (タグノード)</p></li>
<li><p>至少一个``LC5 device``（标签节点）</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">マイクロUSB</div>
<div class="line">ケーブル</div>
</div>
</td>
<td><p>5</p></td>
<td><p>必須</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/micro-usb.webp"><img alt="../../../_images/micro-usb.webp" class="align-right" src="/docs-assets/ja/_images/micro-usb.webp" style="width: 89.94px; height: 89.94px;"></a>
</div></blockquote>
<p>デバイスへの電源供給、PCとのデータ交換、ファームウェアの再フラッシュを行います。ボードの再フラッシュはオプションです。</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">USB-C</div>
<div class="line">ケーブル</div>
</div>
</td>
<td><p>1</p></td>
<td><p>オプション</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/usb-c.jpg"><img alt="../../../_images/usb-c.jpg" class="align-right" src="/docs-assets/ja/_images/usb-c.jpg" style="width: 91.0px; height: 91.0px;"></a>
</div></blockquote>
<p>デバイスへの電源供給、PCとのデータ交換、ファームウェアの再フラッシュを行います。ボードの再フラッシュはオプションです。</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">USBウォール</div>
<div class="line">アダプター</div>
</div>
</td>
<td><p>5+</p></td>
<td><p>おすすめだ</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/usb-wall-charger.jpg"><img alt="../../../_images/usb-wall-charger.jpg" class="align-right" src="/docs-assets/ja/_images/usb-wall-charger.jpg" style="width: 96.0px; height: 96.0px;"></a>
</div></blockquote>
<p>標準的な壁の電源コンセントに接続し、電子機器を充電または給電するための1つまたは複数のUSBポートを提供するコンパクトなデバイスです。</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">アンドロイド</div>
<div class="line">デバイス</div>
<div class="line"><br></div>
</div>
</td>
<td><p>1</p></td>
<td><p>おすすめだ</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/samsung-a7.png"><img alt="../../../_images/samsung-a7.png" class="align-right" src="/docs-assets/ja/_images/samsung-a7.png" style="width: 99.80000000000001px; height: 99.80000000000001px;"></a>
</div></blockquote>
<p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a> を実行するために使用します。このアプリケーションはBluetoothまたはMQTTを使用してデバイスを設定し、ネットワークを視覚化するために使用できます。Android OSバージョン6.0以上が必要です。</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">デスクトップ</div>
<div class="line">デバイス</div>
</div>
</td>
<td><p>1</p></td>
<td><p>オプション</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/desktop-device.png"><img alt="../../../_images/desktop-device.png" class="align-right" src="/docs-assets/ja/_images/desktop-device.png" style="width: 99.89999999999999px; height: 88.02px;"></a>
</div></blockquote>
<p>デスクトップ ウェブサーバアプリケーション (<a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a>, <a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a>, MQTT Broker) を含む VirtualBox イメージを実行し、Windows、macOS、Linux オペレーティングシステムをサポートします。そのほか、USB/UART/Bluetoothを使用したデバイスのアップデートや、USB/UART/Bluetoothを使用したデバイスとの通信にも使用できます。</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">ラズベリー</div>
<div class="line">Pi 3B</div>
<div class="line">または新しい</div>
</div>
</td>
<td><p>1</p></td>
<td><p>オプション</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ras-pi-device.jpg"><img alt="../../../_images/ras-pi-device.jpg" class="align-right" src="/docs-assets/ja/_images/ras-pi-device.jpg" style="width: 100.0px; height: 100.0px;"></a>
</div></blockquote>
<p>LEAPS Server、LEAPS Center、MQTTブローカーを含むウェブサーバーアプリケーションでゲートウェイを素早くセットアップするために使用します。また、USB/UART/Bluetoothを使ったデバイスのアップデートにも使用できます。</p>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="software">
<h2>ソフトウェア</h2>
<p>以下は、デモンストレーションのために不可欠なすべてのソフトウェアアプリケーションとツールのリストです。</p>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>アイテム</p></th>
<th class="head"><p>アイテム バージョン</p></th>
<th class="head"><p>バージョン 必要性</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/pans-pro-uwbs#pans-pro-uwbs"><span class="std std-ref">PANS PRO UWBS</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>PANS PRO Ultra-Wideband Sus-System ファームウェアです。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>BluetoothまたはMQTTを使用してデバイスの設定やネットワークの視覚化に使用できるAndroidアプリケーションです。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>UWB ネットワークの中央データハブとして機能する Linux デーモンアプリケーションで、MQTT Broker を介して外部システムとの間でデータの集約と送信を行います。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>UWB ネットワークの設定と可視化のための Web アプリケーション。</p></td>
</tr>
</tbody>
</table>
<div class="section" id="third-party-applications-and-tools">
<h3>サードパーティのアプリケーションとツール</h3>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>アイテム</p></th>
<th class="head"><p>アイテム バージョン</p></th>
<th class="head"><p>バージョン 必要性</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://mosquitto.org/download/">Mosquitto MQTT Broker</a></p></td>
<td><p>2.0.11</p></td>
<td><p>オプション</p></td>
<td><p>Mosquitto はMQTT v5.0/v3.1.1/v3.1ブローカーです。Mosquittoの推奨バージョンは2.0.11です。</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
