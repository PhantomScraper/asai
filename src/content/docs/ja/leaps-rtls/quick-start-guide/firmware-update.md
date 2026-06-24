---
title: "ファームウェアのアップデート"
lang: ja
slug: "leaps-rtls/quick-start-guide/firmware-update"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/quick-start-guide/firmware-update/"
order: 62
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="leaps-qsg-fw-update"></span><h1>ファームウェアのアップデート</h1>
<p>このセクションでは、ファームウェアを更新する方法について説明します。私たちは、<span class="red-text">Bluetooth</span>、<span class="red-text">MSD</span>、<span class="red-text">WebUSB</span>、<span class="red-text">Serial-COM</span>、または <span class="red-text">OpenOCD</span> 経由など、さまざまな方法をサポートしています。</p>
<p>より詳細な情報については、以下からご希望の方法を選択してください：</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Bluetooth</label><div class="sd-tab-content docutils">
<div class="figure align-right" id="id4">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-qr-code.png"><img alt="../../../_images/leaps-manager-qr-code.png" src="/docs-assets/ja/_images/leaps-manager-qr-code.png" style="width: 112.5px; height: 112.5px;"></a>
<p class="caption"><span class="caption-text"><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> on <a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.leaps&amp;hl=en_GB&amp;gl=US">Google Play</a></span></p>
</div>
<p><strong>セットアップの準備</strong></p>
<ul class="simple">
<li><p>少なくとも 1 つのデバイス。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> アプリケーションが Android デバイスにインストールされています。</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>更新プロセス中に接続を確認し、接続が Bluetooth の場合は遠くに移動しないようにします。</p></li>
<li><p>ファームウェアの更新速度は Bluetooth デバイスによって異なります。たとえば、Bluetooth 4.2 と Bluetooth 5.0 のデータ速度は、それぞれ 1Mbps と 2Mbps です。</p></li>
</ul>
</div>
<p><strong>Bluetooth 経由でアップデートする方法の詳しい手順:</strong></p>
<p>1. Open the <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> application, then navigate to the <span class="red-text">Demo Selector</span>.
Additionally, you can navigate to the created network to update the devices in the network.</p>
<ol class="arabic" start="2">
<li><p>ファームウェアステータスにアクセスします。 アプリケーション内の <span class="red-text">オプションメニュー</span> をタップします。 (<em>縦に3つの点で表示</em>) をタップします。 <span class="red-text">Firmware status</span> オプションを探し、選択します。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update9.jpg"><img alt="../../../_images/firmware-update9.jpg" src="/docs-assets/ja/_images/firmware-update9.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update10.jpg"><img alt="../../../_images/firmware-update10.jpg" src="/docs-assets/ja/_images/firmware-update10.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</div></blockquote>
</li>
<li><p>更新するデバイスを選択します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>表示されたデバイスのリストから、ファームウェアを更新するデバイスを選択します。</p></li>
<li><p><span class="red-text">Update</span> ボタンは、アプリのインターフェースの左下隅にあります。それをクリックして、選択したデバイスのファームウェア更新プロセスを開始します。</p>
<a class="reference internal image-reference" href="../../../_images/firmware-update8.jpg"><img alt="../../../_images/firmware-update8.jpg" src="/docs-assets/ja/_images/firmware-update8.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update5.jpg"><img alt="../../../_images/firmware-update5.jpg" src="/docs-assets/ja/_images/firmware-update5.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic" start="4">
<li><p>アプリは、更新の進行状況を示す視覚的なインジケーターまたは進行状況バーを提供します。アップデートプロセスが完了するまで、辛抱強く待ってください。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update7.jpg"><img alt="../../../_images/firmware-update7.jpg" src="/docs-assets/ja/_images/firmware-update7.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update1.jpg"><img alt="../../../_images/firmware-update1.jpg" src="/docs-assets/ja/_images/firmware-update1.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</div></blockquote>
</li>
<li><p>更新が完了すると、 <span class="red-text">ステータスは完了しました</span> と表示されます。さらに、デバイスは更新が成功したことを示すビープ音を鳴らします。ボードはプロセスの一部として自動的にリセットされます。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update3.jpg"><img alt="../../../_images/firmware-update3.jpg" src="/docs-assets/ja/_images/firmware-update3.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update2.jpg"><img alt="../../../_images/firmware-update2.jpg" src="/docs-assets/ja/_images/firmware-update2.jpg" style="width: 45%;"></a>
</div></blockquote>
</li>
</ol>
<p>デバイスはファームウェアを正常に更新しました。最新の機能と改良点をお楽しみください。</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
MSD</label><div class="sd-tab-content docutils">
<p><strong>セットアップの準備</strong></p>
<ul class="simple">
<li><p>少なくとも 1 つのデバイス。</p></li>
<li><p>更新するバイナリ ファイル。</p></li>
</ul>
<p><strong>MSD 経由で更新する方法の詳しい手順</strong></p>
<ol class="arabic simple">
<li><p>USB-C データ ケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 2</span></a> を PC に接続します。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>接続すると、LEAPS MSD ドライブが PC 上に表示されます。 LEAPS MSD ドライブを開きます。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Windows の場合:</p>
<a class="reference internal image-reference" href="../../../_images/msd-win-01.png"><img alt="../../../_images/msd-win-01.png" class="align-center" src="/docs-assets/ja/_images/msd-win-01.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p><a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> ファイルを PC にダウンロードします。 WinZip や 7-Zip などのプログラムを使用して、ダウンロードしたファイルの内容を抽出します。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.bin</span></code> でバイナリ ファイルを見つけます。このファイルを LEAPS MSD ドライブにコピーします。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Windows の場合:</p>
<a class="reference internal image-reference" href="../../../_images/msd-win-02.png"><img alt="../../../_images/msd-win-02.png" class="align-center" src="/docs-assets/ja/_images/msd-win-02.png" style="width: 60%;"></a>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>コピーが成功するまで、コピーとフラッシュのプロセスを待ちます。ボードはプロセスの一部として自動的にリセットされ、RGB LED が点灯し、ハードウェアからビープ音が鳴り、更新が成功したことが示されます。</p></li>
</ol>
<p>デバイスはファームウェアを正常に更新しました。最新の機能と改良点をお楽しみください。</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
WebUSB</label><div class="sd-tab-content docutils">
<p><strong>セットアップの準備</strong></p>
<ul class="simple">
<li><p>少なくとも 1 つのデバイス。</p></li>
<li><p>更新するバイナリ ファイル。</p></li>
</ul>
<p><strong>WebUSB 経由でアップデートする方法をステップバイステップで説明します</strong></p>
<ol class="arabic simple">
<li><p>Node.js をダウンロードしてインストールします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请访问 Node.js 官方网站 <a class="reference external" href="https://nodejs.org/en/download">https://nodejs.org/en/download</a>。</p></li>
<li><p>下载推荐的 Node.js 版本。</p></li>
<li><p>公式 Node.js Web サイト (<a class="reference external" href="https://nodejs.org/en/download">https://nodejs.org/en/download</a>) にアクセスします。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>依存関係をインストールします。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>コンピューターでお好きなターミナル・アプリケーションを開いてください。</p>
<ul class="simple">
<li><p>Linux または macOS では、<span class="red-text">ターミナル</span> アプリケーションのように。</p></li>
<li><p>Windows では、<span class="red-text">Powershell</span> のように。</p></li>
</ul>
</li>
<li><p>webusb 依存関係をインストールするには、次のコマンドを実行します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">webusb</span>
</pre></div>
</div>
</li>
<li><p>次に、次のコマンドを実行して USB 依存関係をインストールします。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">usb</span>
</pre></div>
</div>
</li>
<li><p>最後に、次のコマンドを使用して、node-hid 依存関係をインストールします。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">node</span><span class="o">-</span><span class="n">hid</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>USB-C データ ケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 2</span></a> を PC に接続します。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>パッケージをダウンロードして PC に解凍します。WinZip や 7-Zip などのプログラムを使用して、ダウンロードした <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> ファイルを解凍します。</p></li>
<li><p>ウェブサイト <a class="reference external" href="https://armmbed.github.io/dapjs/examples/daplink-flash/web.html">DAPLink Flash</a> を開きます。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web02.png"><img alt="../../../_images/daplink-flash-web02.png" class="align-center" src="/docs-assets/ja/_images/daplink-flash-web02.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p><span class="red-text">ファームウェア イメージを選択</span> をクリックし、 <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.hex</span></code> でバイナリ ファイルを選択します。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web03.png"><img alt="../../../_images/daplink-flash-web03.png" class="align-center" src="/docs-assets/ja/_images/daplink-flash-web03.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p><span class="red-text">SELECT DEVICE</span> ボタンをクリックして、PC に接続されている DAPLink CMSIS-DAP ポートを選択します。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web05.png"><img alt="../../../_images/daplink-flash-web05.png" class="align-center" src="/docs-assets/ja/_images/daplink-flash-web05.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>ファームウェア イメージを選択すると、バイナリ ファイルのフラッシュ プロセスが開始されます。プロセス全体を通じてハードウェアが接続されていることを確認してください。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web06.png"><img alt="../../../_images/daplink-flash-web06.png" class="align-center" src="/docs-assets/ja/_images/daplink-flash-web06.png" style="width: 90%;"></a>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>予期しない問題が発生する可能性があります。ボードをコンピュータから取り外して、再度起動してください。</p>
</div>
<ol class="arabic simple" start="7">
<li><p><span class="red-text">フラッシュが完了しました!</span> の後。ボードはプロセスの一部として自動的にリセットされ、RGB LED が点灯し、ハードウェアからビープ音が鳴り、更新が成功したことが示されます。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web07.png"><img alt="../../../_images/daplink-flash-web07.png" class="align-center" src="/docs-assets/ja/_images/daplink-flash-web07.png" style="width: 90%;"></a>
</div></blockquote>
<p>デバイスはファームウェアを正常に更新しました。最新の機能と改良点をお楽しみください。</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
シリアルCOM</label><div class="sd-tab-content docutils">
<p><strong>必要なもの:</strong></p>
<ul class="simple">
<li><p>少なくとも 1 つのデバイスが USB ポート経由で接続されています。</p></li>
<li><p>パッケージに含まれるスクリプトとファームウェアのバイナリ。</p></li>
<li><p>システムにインストールされている <a class="reference external" href="https://www.python.org/downloads/">python3</a>。</p></li>
</ul>
<p><strong>シリアル COM 経由で更新する方法に関する詳しい説明:</strong></p>
<ol class="arabic simple">
<li><p>パッケージをダウンロードして PC に解凍します。WinZip や 7-Zip などのプログラムを使用して、ダウンロードした <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> ファイルを解凍します。</p></li>
<li><p>お気に入りのターミナル アプリケーションを開きます。</p></li>
</ol>
<ul class="simple">
<li><p>Linux または macOS では、<span class="red-text">ターミナル</span> アプリケーションのように。</p></li>
<li><p>Windows では、<span class="red-text">Powershell</span> のように。</p></li>
</ul>
<ol class="arabic simple" start="3">
<li><p>抽出されたパッケージが含まれるフォルダーに移動します。</p></li>
<li><p>Python の依存関係をインストールします。</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>pip<span class="w"> </span>install<span class="w"> </span>pyserial<span class="w"> </span>libusb<span class="w"> </span>tqdm
</pre></div>
</div>
<p>もし <code class="docutils literal notranslate"><span class="pre">libusb</span></code> でエラーが発生する場合は、次のようにしてみてください: <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">pip</span> <span class="pre">install</span> <span class="pre">libusb</span>&nbsp; <span class="pre">--break-system-package</span></code></p>
<ol class="arabic simple" start="5">
<li><p>更新に 2 つのポートのうち 1 つを使用することを選択できます。</p></li>
</ol>
<p><a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> を使用している場合は、ELDR バイナリと MAIN バイナリを個別に更新できます。逆に、 <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> を使用すると、複数のデバイスを同時に連続的に更新できます。</p>
<ol class="upperalpha">
<li><p>USB-C データ ケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 1</span></a> に接続します。</p>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port1.gif">
<p>次のコマンドを実行して、ELDR および MAIN バイナリを更新します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>~/LEAPS-UWBS-Firmware-Serial-COM$ sudo python3 ./udk-leaps-uwbs-serial-com.py --main ./udk-leaps-uwbs-fira-v0.15.0-rc8.bin --eldr ./udk-leaps-uwbs-eldr-v0.15.0-rc8.bin
03:11:55 Device 01/02 (SerialNumber=3DB15A2CCB8053C8): Reset
03:11:55 Device 02/02 (SerialNumber=904AD29FD29D2452): Reset
15:12:15 Device 01/02 (SerialNumber=904AD29FD29D2452): Uploading MAIN: 100%|████████████████████████████| 716192/716192 [00:16&lt;00:00, 44623.94it/s]
15:12:15 Device 02/02 (SerialNumber=3DB15A2CCB8053C8): Uploading MAIN: 100%|████████████████████████████| 716192/716192 [00:16&lt;00:00, 44630.31it/s]
15:12:37 Device 01/02 (SerialNumber=904AD29FD29D2452): Uploading ELDR: 100%|████████████████████████████| 235748/235748 [00:05&lt;00:00, 42419.44it/s]
15:12:37 Device 02/02 (SerialNumber=3DB15A2CCB8053C8): Uploading ELDR: 100%|████████████████████████████| 235748/235748 [00:05&lt;00:00, 42498.01it/s]
03:12:43 Resetting devices
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>USB-C データ ケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 2</span></a> に接続します。次のコマンドを実行して、ELDR または MAIN バイナリを更新します。</p>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p><a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 2</span></a> 経由でファームウェアを更新できるようにするには、udev ルールをインストールする必要がある場合があります。 Debian 風のディストリビューションについては、 <a class="reference external" href="https://github.com/NordicSemiconductor/nrf-udev/tree/main">udev ルールのインストール</a> を参照してください。</p>
</div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>~/LEAPS-UWBS-Firmware-Serial-COM$ python3 ./udk-leaps-uwbs-serial-com.py -d /dev/ttyACM0 --eldr ./udk-leaps-uwbs-eldr-v0.15.0-rc8.bin
02:54:30 Resetting device
02:54:33 Uploading file /home/leaps/LEAPS-UWBS-Firmware-v0.15.0/LEAPS-UWBS-Firmware-Serial-COM/udk-leaps-uwbs-eldr-v0.15.0-rc8.bin (235748 bytes)
100%|████████████████████████████| 235748/235748 [00:28&lt;00:00, 8129.43it/s]
02:55:07 Ok (upload time = 34.70 seconds)
02:55:10 Resetting device

~/LEAPS-UWBS-Firmware-Serial-COM$ python3 ./udk-leaps-uwbs-serial-com.py -d /dev/ttyACM0 --main ./udk-leaps-uwbs-fira-v0.15.0-rc8.bin
02:56:25 Resetting device
02:56:28 Uploading file /home/leaps/LEAPS-UWBS-Firmware-v0.15.0/LEAPS-UWBS-Firmware-Serial-COM/udk-leaps-uwbs-fira-v0.15.0-rc8.bin (716192 bytes)
100%|████████████████████████████| 716192/716192 [01:27&lt;00:00, 8175.81it/s]
02:58:11 Ok (upload time = 102.74 seconds)
02:58:14 Resetting device
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
<ol class="arabic simple" start="6">
<li><p>更新が完了するまで待ちます。</p></li>
<li><p>更新が完了すると、ボードはプロセスの一部として自動的にリセットされます。</p></li>
</ol>
<p>デバイスはファームウェアを正常に更新しました。最新の機能と改良点をお楽しみください。</p>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
OpenOCD</label><div class="sd-tab-content docutils">
<p><strong>セットアップの準備</strong></p>
<ul class="simple">
<li><p>少なくとも 1 つのデバイス。</p></li>
<li><p>パッケージには、アップデート用のスクリプトとバイナリが含まれています。</p></li>
<li><p><a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">OpenOCD</a> がインストールされました。</p></li>
</ul>
<p><strong>OpenOCD (Open On-Chip Debugger) 経由で更新する方法に関するステップバイステップの手順:</strong></p>
<ol class="arabic simple">
<li><p>OpenOCD デバッガーをインストールしています。</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>Windows に OpenOCD をインストールしています。</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>Windows 用のバイナリ zip ファイルをダウンロードします。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1</span></code> フォルダーに解凍します。</p></li>
<li><p>パスを追加します： Windows ユーザーパス環境変数に <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1\bin</span></code> というパスを追加してください。</p></li>
</ol>
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p>Linux または macOS に OpenOCD をインストールします。</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p><a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">Linux 用バイナリ tarball</a> をダウンロードします。</p></li>
<li><p>tarball を解凍してローカルにインストールします。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>mkdir -p ~/.local/xPacks/openocd
cd ~/.local/xPacks/openocd
tar -zxvf ~/Downloads/xpack-openocd-0.11.0-1-linux-arm.tar.gz (with PC’s AMD core, using … linux-x64.tar.gz with PC’s Intel core)
....
sudo chmod -R -w xpack-openocd-0.11.0-1/
~/.local/xPacks/openocd/xpack-openocd-0.11.0-1/bin/openocd --version
export PATH="~/.local/xPacks/openocd/xpack-openocd-0.11.0-1/bin/:$PATH"
cd ~
source .bashrc
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>OpenOCD のバージョンを確認します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">openocd</span> <span class="o">--</span><span class="n">version</span>
<span class="n">xPack</span> <span class="n">OpenOCD</span><span class="p">,</span> <span class="n">x86_64</span> <span class="n">Open</span> <span class="n">On</span><span class="o">-</span><span class="n">Chip</span> <span class="n">Debugger</span> <span class="mf">0.11.0</span><span class="o">-</span><span class="mi">00155</span><span class="o">-</span><span class="n">ge392e485e</span> <span class="p">(</span><span class="mi">2021</span><span class="o">-</span><span class="mi">03</span><span class="o">-</span><span class="mi">15</span><span class="o">-</span><span class="mi">16</span><span class="p">:</span><span class="mi">43</span><span class="p">)</span>
<span class="n">Licensed</span> <span class="n">under</span> <span class="n">GNU</span> <span class="n">GPL</span> <span class="n">v2</span>
<span class="n">For</span> <span class="n">bug</span> <span class="n">reports</span><span class="p">,</span> <span class="n">read</span>
  <span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">openocd</span><span class="o">.</span><span class="n">org</span><span class="o">/</span><span class="n">doc</span><span class="o">/</span><span class="n">doxygen</span><span class="o">/</span><span class="n">bugs</span><span class="o">.</span><span class="n">html</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>パッケージをダウンロードして PC に解凍します。WinZip や 7-Zip などのプログラムを使用して、ダウンロードした <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> ファイルを解凍します。</p></li>
<li><p>お気に入りのターミナル アプリケーションを開きます。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Linux または macOS では、<span class="red-text">ターミナル</span> アプリケーションのように。</p></li>
<li><p>Windows では、<span class="red-text">Powershell</span> のように。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>抽出されたパッケージが含まれるフォルダーに移動します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><span class="red-text">cd</span> から <span class="red-text">/path/to/LEAPS-UWBS-Firmware-OpenOCD</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>USB-C データ ケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 2</span></a> を PC に接続します。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>スクリプトを実行して、ファームウェアを自動的に更新します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Linux または macOS では、<span class="red-text">udk-leaps-uwbs-firmware.sh</span> コマンドを使用します。</p></li>
<li><p>Windows では、<span class="red-text">udk-leaps-uwbs-firmware.bat</span> コマンドを使用します。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>./udk-leaps-uwbs-firmware.sh
xPack OpenOCD, x86_64 Open On-Chip Debugger 0.11.0-00155-ge392e485e (2021-03-15-16:43)
Licensed under GNU GPL v2
For bug reports, read
  http://openocd.org/doc/doxygen/bugs.html
DEPRECATED! use 'adapter speed' not 'adapter_khz'
set_test_mode
Info : Using CMSIS-DAPv2 interface with VID:PID=0x0d28:0x0204, serial=01100E003602002e003f4146570120313238
Info : CMSIS-DAP: SWD Supported
Info : CMSIS-DAP: FW Version = 2.1.0
Info : CMSIS-DAP: Serial# = 01100E003602002e003f4146570120313238
Info : CMSIS-DAP: Interface Initialised (SWD)
Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1
Info : CMSIS-DAP: Interface ready
Info : High speed (adapter speed 10000) may be limited by adapter firmware.
Info : clock speed 10000 kHz
Info : SWD DPIDR 0x2ba01477
Info : nrf52.cpu: hardware has 6 breakpoints, 4 watchpoints
Info : starting gdb server for nrf52.cpu on 3333
Info : Listening on port 3333 for gdb connections
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x000031ec msp: 0x20003488
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0xfffffffe msp: 0xfffffffc
Info : nRF52840-CKAA(build code: D0) 1024kB Flash, 256kB RAM
auto erase enabled
wrote 1048576 bytes from file leaps-rtls-all-2ab-v0.14-rc25.hex in 38.776192s (26.408 KiB/s)
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>更新が完了すると、デバイスは更新の成功を示すビープ音を鳴らします。ボードはプロセスの一部として自動的にリセットされます。</p></li>
</ol>
<p>デバイスはファームウェアを正常に更新しました。最新の機能と改良点をお楽しみください。</p>
<p><strong>トラブルシューティング</strong></p>
<p>"エラー: コアを制御する MEM-AP が見つかりませんでした" の場合。</p>
<blockquote>
<div><img alt="../../../_images/firmware-update-error.png" class="align-center" src="/docs-assets/ja/_images/firmware-update-error.png">
</div></blockquote>
<p>次のコマンドを実行して復元してください。</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">openocd</span> <span class="o">-</span><span class="n">f</span> <span class="o">./</span><span class="n">openocd</span><span class="o">-</span><span class="n">swd</span><span class="o">-</span><span class="n">nrf52</span><span class="o">.</span><span class="n">cfg</span> <span class="o">-</span><span class="n">c</span> <span class="s2">"init;nrf52833_workaround;exit_debug_mode;shutdown;sleep 250"</span>
</pre></div>
</div>
</div></blockquote>
<p>次に、 <code class="docutils literal notranslate"><span class="pre">./udk-leaps-uwbs-firmware.sh</span></code> の実行を続けます。</p>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>弊社製品に関するご意見やご質問については、<a class="reference external" href="https://forum.leapslabs.com">LEAPS フォーラム</a> にアクセスすることをお勧めします。</p></li>
<li><p>既知の制限と問題リストの詳細については、セクション <a class="reference internal" href="/docs/ja/udk/release#udk-releases"><span class="std std-ref">リリース</span></a> を参照してください。</p></li>
</ul>
</div>
</div>


           </div>
