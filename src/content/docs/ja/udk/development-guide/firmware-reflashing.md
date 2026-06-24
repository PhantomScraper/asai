---
title: "ファームウェアのプログラミング/アップグレード"
lang: ja
slug: "udk/development-guide/firmware-reflashing"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/development-guide/firmware-reflashing/"
order: 46
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="programming-upgrading-firmware">
<span id="flashingfirmware"></span><h1>ファームウェアのプログラミング/アップグレード</h1>
<p>このセクションでは、ファームウェアのアップデート方法について説明します。red:<cite>MSD</cite>、<span class="red-text">WebUSB</span>、<span class="red-text">Serial-COM</span>、<span class="red-text">OpenOCD</span>、<span class="red-text">SEGGER J-Link</span> など、様々な方法をサポートしています。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>更新プロセス中は接続を維持し、正しい <span class="red-text">デバイス</span> と <span class="red-text">インターフェース</span> を使用してください。</p>
</div>
<p>より詳細な情報については、以下からご希望の方法を選択してください：</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>接続すると、LEAPS MSD ドライブが PC 上に表示されます。 LEAPS MSD ドライブを開きます。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Windows の場合:</p>
<a class="styled-image reference internal image-reference" href="../../../_images/msd-win-01.png"><img alt="../../../_images/msd-win-01.png" class="styled-image align-center" src="/docs-assets/ja/_images/msd-win-01.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p><a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> ファイルを PC にダウンロードします。 WinZip や 7-Zip などのプログラムを使用して、ダウンロードしたファイルの内容を抽出します。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.bin</span></code> でバイナリ ファイルを見つけます。このファイルを LEAPS MSD ドライブにコピーします。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Windows の場合:</p>
<a class="styled-image reference internal image-reference" href="../../../_images/msd-win-02.png"><img alt="../../../_images/msd-win-02.png" class="styled-image align-center" src="/docs-assets/ja/_images/msd-win-02.png" style="width: 60%;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>コピーが成功するまで、コピーとフラッシュのプロセスを待ちます。ボードはプロセスの一部として自動的にリセットされ、RGB LED が点灯し、ハードウェアからビープ音が鳴り、更新が成功したことが示されます。</p></li>
</ol>
<p>デバイスはファームウェアを正常に更新しました。最新の機能と改良点をお楽しみください。</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>パッケージをダウンロードして PC に解凍します。WinZip や 7-Zip などのプログラムを使用して、ダウンロードした <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> ファイルを解凍します。</p></li>
<li><p>ウェブサイト <a class="reference external" href="https://armmbed.github.io/dapjs/examples/daplink-flash/web.html">DAPLink Flash</a> を開きます。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web02.png"><img alt="../../../_images/daplink-flash-web02.png" class="styled-image align-center" src="/docs-assets/ja/_images/daplink-flash-web02.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p><span class="red-text">ファームウェア イメージを選択</span> をクリックし、 <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.hex</span></code> でバイナリ ファイルを選択します。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web03.png"><img alt="../../../_images/daplink-flash-web03.png" class="styled-image align-center" src="/docs-assets/ja/_images/daplink-flash-web03.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p><span class="red-text">SELECT DEVICE</span> ボタンをクリックして、PC に接続されている DAPLink CMSIS-DAP ポートを選択します。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web05.png"><img alt="../../../_images/daplink-flash-web05.png" class="styled-image align-center" src="/docs-assets/ja/_images/daplink-flash-web05.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>ファームウェア イメージを選択すると、バイナリ ファイルのフラッシュ プロセスが開始されます。プロセス全体を通じてハードウェアが接続されていることを確認してください。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web06.png"><img alt="../../../_images/daplink-flash-web06.png" class="styled-image align-center" src="/docs-assets/ja/_images/daplink-flash-web06.png" style="width: 90%;"></a>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>予期しない問題が発生する可能性があります。ボードをコンピュータから取り外して、再度起動してください。</p>
</div>
<ol class="arabic simple">
<li><p><span class="red-text">フラッシュが完了しました!</span> の後。ボードはプロセスの一部として自動的にリセットされ、RGB LED が点灯し、ハードウェアからビープ音が鳴り、更新が成功したことが示されます。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web07.png"><img alt="../../../_images/daplink-flash-web07.png" class="styled-image align-center" src="/docs-assets/ja/_images/daplink-flash-web07.png" style="width: 90%;"></a>
</div></blockquote>
<p>デバイスはファームウェアを正常に更新しました。最新の機能と改良点をお楽しみください。</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
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
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
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
<p>次に、<code class="docutils literal notranslate"><span class="pre">./udk-leaps-uwbs-firmware.sh</span></code> の実行を続けます。</p>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
SEGGER J-Link</label><div class="sd-tab-content docutils">
<p><strong>セットアップの準備</strong></p>
<ul class="simple">
<li><p>少なくともデバイスがあります。</p></li>
<li><p>更新するバイナリファイル。(.hex または .bin)</p></li>
<li><p><a class="reference external" href="https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack">SEGGER J-Link</a> をインストールしました。</p></li>
</ul>
<p><strong>SEGGER J-Linkを使ったアップデート方法のステップバイステップの説明</strong></p>
<ol class="arabic simple">
<li><p>SEGGER J-Linkをインストールします。</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
Windows</label><div class="sd-tab-content docutils">
<p>Windows用のダウンロードファイル <code class="docutils literal notranslate"><span class="pre">JLink_Windows_V766_x86_64.exe</span></code> を探してください。</p>
<ul class="simple">
<li><p>ファイルをダブルクリックしてインストールを開始します。</p></li>
<li><p>プロンプトが表示されたら、管理者パスワードを入力してください。</p></li>
<li><p>ライセンス条項を読み、同意してください。</p></li>
<li><p>デフォルトのインストール先フォルダは、通常 <code class="docutils literal notranslate"><span class="pre">C:∕Program</span> <span class="pre">Files</span> <span class="pre">(x86)∕SEGGERJLink</span></code> にあります。</p></li>
<li><p>デフォルトのUSBドライバを承認してください。</p></li>
</ul>
<p>インストールが完了すると、システムフォルダにフォルダとドライバファイル一式がインストールされます。新しくインストールするたびに、これらのファイルは上書きされますのでご注意ください。</p>
</div>
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
macOS</label><div class="sd-tab-content docutils">
<p><code class="docutils literal notranslate"><span class="pre">JLink_macOSX_V766_x86_64.pkg</span></code> という名前の macOS ダウンロードファイルを探してください。</p>
<blockquote>
<div><ul class="simple">
<li><p>ファイルをダブルクリックしてインストールを開始します。</p></li>
<li><p>ライセンス条項を読み、同意してください。</p></li>
<li><p>プロンプトが表示されたら、管理者パスワードを入力してください。このパスワードはアプリケーションフォルダに書き込むのに必要です。</p></li>
</ul>
</div></blockquote>
<p>インストール後、次の場所にフォルダができます: <code class="docutils literal notranslate"><span class="pre">/Applications/SEGGER/JLink_V766/</span></code>. バージョンごとにフォルダが異なることを覚えておいてください。このフォルダにはアプリケーションに関連するすべての実行ファイルとライブラリが保存されます。</p>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
GNU/Linux</label><div class="sd-tab-content docutils">
<p>GNU/Linux用のSEGGERダウンロードサイトにアクセスし、目的のパッケージを見つけてください。32/64ビット版から選択してください。</p>
<blockquote>
<div><ul class="simple">
<li><p>.tgzファイルをダウンロードし、コンピュータに保存してください。</p></li>
<li><p>ターミナルウィンドウを開きます。</p></li>
</ul>
</div></blockquote>
<p>例えば、Ubuntu (Linux) で64ビットの .tgz ファイルをインストールするには、以下のコマンドを使ってください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mkdir</span> <span class="o">-</span><span class="n">p</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span>
<span class="n">cd</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span>
<span class="n">tar</span> <span class="n">xf</span> <span class="o">~/</span><span class="n">Downloads</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span><span class="o">.</span><span class="n">tgz</span>
<span class="n">chmod</span> <span class="n">a</span><span class="o">-</span><span class="n">w</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span>
<span class="n">ls</span> <span class="o">-</span><span class="n">l</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span>
</pre></div>
</div>
<p>上記のコマンドを実行した後：</p>
<blockquote>
<div><ul class="simple">
<li><p><cite>~/opt/SEGGER</cite> にフォルダが作成されます。</p></li>
<li><p>ダウンロードした .tgz ファイルの内容が <cite>~/opt/SEGGER</cite> フォルダに展開されます。</p></li>
<li><p>JLink_Linux_V766_x86_64` ファイルのパーミッションが変更されます。</p></li>
<li><p><cite>~/opt/SEGGER/JLink_Linux_V766_x86_64</cite> フォルダの内容をチェックすることでインストールを確認できます。</p></li>
</ul>
</div></blockquote>
<p>新規インストール時にシステムフォルダ内の既存のファイルを上書きすることに注意してください。</p>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>SEGGER J-Linkを開き、バイナリファイルをフラッシュしてください。</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
J-Link GUI (J-Flash Lite)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>最新の J-Link ソフトウェア＆ドキュメントパックがインストールされていることを確認してください。</p></li>
<li><p>J-LinkをPCに接続してください。</p></li>
<li><p>ターゲットシステムをJ-Linkに接続</p></li>
<li><p>J-Flash Liteの起動</p></li>
</ul>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe01.png"><img alt="../../../_images/jflashliteexe01.png" class="styled-image align-center" src="/docs-assets/ja/_images/jflashliteexe01.png" style="width: 542.0px; height: 114.0px;"></a>
<ul class="simple">
<li><p>デバイス、デバッグインターフェイス、通信速度の選択</p></li>
<li><p>ファイルを選択し、[デバイスをプログラム]をクリックするか、[チップを消去]をクリックします。</p></li>
<li><p>J-Flash Liteは要求された操作を実行します</p></li>
</ul>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe02.png"><img alt="../../../_images/jflashliteexe02.png" class="styled-image align-center" src="/docs-assets/ja/_images/jflashliteexe02.png" style="width: 511.0px; height: 576.0px;"></a>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
J-Linkコマンダー (JLink.exe / JLinkExe)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>最新の J-Link ソフトウェア＆ドキュメントパックがインストールされていることを確認してください。</p></li>
<li><p>J-LinkをPCに接続します。</p></li>
<li><p>ターゲットシステムをJ-Linkに接続</p></li>
<li><p>J-Link Commanderを起動してください。</p></li>
<li><p>以下のコマンドを入力してください：</p></li>
<li><p>J-Link&gt; device &lt;devicename&gt; // 既知のデバイスのリストについては、ここを参照してください。</p></li>
<li><p>J-Link&gt; r</p></li>
<li><p>J-Link&gt; h</p></li>
<li><p>J-Link&gt; loadbin &lt;PathToBinFile&gt;, &lt;programmingaddress&gt;</p></li>
<li><p>J-Link Commander はフラッシュダウンロードを実行し、成功したら時間統計を出力します。</p></li>
</ul>
</div>
</div>
<p>更新が完了すると、ボードは自動的にリセットされます。</p>
</div></blockquote>
</div>
</div>
<p><strong>ファームウェアを確認し、成功を確認してください</strong></p>
<blockquote>
<div><p>お好きなターミナル・アプリケーションを開いてください、</p>
<blockquote>
<div><ul class="simple">
<li><p>GNU/LinuxまたはmacOSでは <span class="red-text">Terminal</span> アプリケーションのようになります。</p></li>
<li><p>Windowsでは <span class="red-text">Powershell</span> アプリケーションのようなものです。</p></li>
</ul>
</div></blockquote>
<p>例えば、Ubuntu（Linux）では、minicomを開いてダブルエンターを押す：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe05.png"><img alt="../../../_images/jflashliteexe05.png" class="styled-image align-center" src="/docs-assets/ja/_images/jflashliteexe05.png" style="width: 663.0px; height: 418.0px;"></a>
</div></blockquote>
</div>


           </div>
