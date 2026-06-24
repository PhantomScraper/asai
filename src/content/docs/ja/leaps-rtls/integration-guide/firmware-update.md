---
title: "ファームウェアのアップデート"
lang: ja
slug: "leaps-rtls/integration-guide/firmware-update"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/firmware-update/"
order: 68
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="lr-firmware-update"></span><h1>ファームウェアのアップデート</h1>
<p>このセクションでは、ファームウェアのアップデート方法について説明します。私たちは <span class="red-text">SEGGER J-Link</span>、<span class="red-text">OpenOCD</span> や <span class="red-text">Serial-COM</span> 経由など、様々な方法をサポートしています。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>更新プロセス中は接続を維持し、正しい <span class="red-text">デバイス</span> と <span class="red-text">インターフェース</span> を使用してください。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a> はBLE経由でのファームウェアアップデートもサポートしており、より詳細な情報については <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leaps-manager-fup-over-ble"><span class="std std-ref">BLE経由のファームウェア更新</span></a> を参照してください。</p></li>
</ul>
</div>
<p>より詳細な情報については、以下からご希望の方法を選択してください：</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
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
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
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
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
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
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
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
<li><p>SEGGER J-Link を開き、バイナリファイルをフラッシュします。</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
J-Link GUI (J-Flash Lite)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>最新の J-Link ソフトウェア＆ドキュメントパックがインストールされていることを確認してください。</p></li>
<li><p>J-LinkをPCに接続してください。</p></li>
<li><p>ターゲットシステムをJ-Linkに接続</p></li>
<li><p>J-Flash Liteの起動</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe03.png"><img alt="../../../_images/jflashliteexe03.png" class="align-center" src="/docs-assets/ja/_images/jflashliteexe03.png" style="width: 541.0px; height: 114.0px;"></a>
<ul class="simple">
<li><p>デバイス、デバッグインターフェイス、通信速度の選択</p></li>
<li><p>ファイルを選択し、[デバイスをプログラム]をクリックするか、[チップを消去]をクリックします。</p></li>
<li><p>J-Flash Liteは要求された操作を実行します</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe04.png"><img alt="../../../_images/jflashliteexe04.png" class="align-center" src="/docs-assets/ja/_images/jflashliteexe04.png" style="width: 513.0px; height: 588.0px;"></a>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
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
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
OpenOCD</label><div class="sd-tab-content docutils">
<p><strong>セットアップの準備</strong></p>
<ul class="simple">
<li><p>少なくとも 1 つのデバイス。</p></li>
<li><p>パッケージには、アップデート用のスクリプトとバイナリが含まれています。</p></li>
<li><p>Installed <a class="reference external" href="https://openocd.org/pages/getting-openocd.html">OpenOCD</a>.</p></li>
</ul>
<p><strong>OpenOCD (Open On-Chip Debugger) 経由でのアップデート方法を順を追って説明します。</strong></p>
<ol class="arabic simple">
<li><p>OpenOCD デバッガのインストール</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-8" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
Windows</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>Windows 用の <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">xPack OpenOCD package</a> をダウンロードする。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1</span></code> フォルダーに解凍します。</p></li>
<li><p>パスを追加します： Windows ユーザーパス環境変数に <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1\bin</span></code> というパスを追加してください。</p></li>
</ul>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
macOS</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>macOS 用の <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">xPack OpenOCD package</a> をダウンロードする。</p></li>
<li><p>tarball を解凍してローカルにインストールします。</p></li>
</ul>
<p>例えば、xpack-openocd-0.11.0-1-linux-arm.tar.gz ファイルをインストールするには、以下のコマンドを使います：</p>
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
</div>
<input id="sd-tab-item-10" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
GNU/Linux</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>GNU/Linux用の`xPack OpenOCD package &lt;<a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">https://github.com/xpack-dev-tools/openocd-xpack/releases</a>&gt;`_をダウンロードしてください。</p></li>
<li><p>tarball を解凍してローカルにインストールします。</p></li>
</ul>
<p>例えば、Ubuntu (Linux)では、xpack-openocd-0.11.0-1-linux-arm.tar.gzファイルをインストールするには、以下のコマンドを使用します：</p>
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
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>OpenOCDのバージョンを確認する</p></li>
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
<li><p>パッケージをダウンロードしてPCに解凍します。</p></li>
</ol>
<blockquote>
<div><p>UDKボードの例： WinZip や 7-Zip のようなプログラムを使って、ダウンロードした <cite>to be defined</cite> ファイルを解凍します。</p>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>お気に入りのターミナル アプリケーションを開きます。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Linux または macOS では、<span class="red-text">ターミナル</span> アプリケーションのように。</p></li>
<li><p>Windowsでは <span class="red-text">Powershell</span> アプリケーションのようなものです。</p></li>
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
<li><p>ケーブルを使用してデバイスを PC に接続します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>UDK ボードの例： USB-Cデータケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> をPCに接続します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>スクリプトを実行して、ファームウェアを自動的に更新します。</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-11" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
Windows</label><div class="sd-tab-content docutils">
<p>Windows では、<span class="red-text">udk-leaps-uwbs-firmware.bat</span> コマンドを使用します。</p>
</div>
<input id="sd-tab-item-12" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-12">
macOS</label><div class="sd-tab-content docutils">
<p>macOSでは、 <span class="red-text">udk-leaps-uwbs-firmware.sh</span> コマンドを使用する。</p>
</div>
<input id="sd-tab-item-13" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-13">
GNU/Linux</label><div class="sd-tab-content docutils">
<p>GNU/Linuxでは、<span class="red-text">udk-leaps-uwbs-firmware.sh</span> コマンドを使用する。</p>
</div>
</div>
<p>たとえば、Ubuntu (Linux) の場合:</p>
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
Info : high-speed (adapter speed 10000) may be limited by adapter firmware.
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
<li><p>更新が完了すると、ボードは自動的にリセットされます。</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
LEAPS-COM</label><div class="sd-tab-content docutils">
<p><strong>Install LEAPS-COM tool</strong></p>
<p>Follow instructions in section describing <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-com/how-to-install#install-leapscom"><span class="std std-ref">how to install LEAPS-COM</span></a>.</p>
<p><strong>You will need</strong></p>
<ul class="simple">
<li><p>At least one device connected via the USB port or the serial port, alternatively, the device advertises on the BLE interface if enabled.</p></li>
<li><p>The firmware binary included in the package.</p></li>
<li><p>The <a class="reference external" href="https://www.python.org/downloads/">python3</a> installed on you system.</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-14" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-14">
USB</label><div class="sd-tab-content docutils">
<p>Connect USB data cable to the <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB port</span></a>.
Execute following command to update Firmware and Extended-Loader on the available devices that are connected on the USB interface.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
<p>In order to update only certain devices you need to specify serial number.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>630D46F2D51482FC<span class="w"> </span>7E1C5859C2ECF343<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
<input id="sd-tab-item-15" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-15">
BLE</label><div class="sd-tab-content docutils">
<p>Before update, make sure that BLE is enabled on the devices (see section <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution#discovering-leaps-devices"><span class="std std-ref">Discovering devices</span></a> for more details).
Execute following command to update Firmware and Extended-Loader of all the devices that are advertising on the BLE interface.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--ble<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
<p>In order to update only certain devices you need to specify the BLE address.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--ble<span class="w"> </span>FE:40:B4:BC:D3:42<span class="w"> </span>E0:05:86:49:A9:40<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
<input id="sd-tab-item-16" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-16">
Serial port</label><div class="sd-tab-content docutils">
<p>Connect USB data cable to the <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">Serial port</span></a>.
Execute following command to update Firmware and Extended-Loader over the serial ports.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--dev<span class="w"> </span>/dev/ttyACM0<span class="w"> </span>/dev/ttyACM1<span class="w"> </span>/dev/ttyACM2<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
</div>
</div>
</div>
<p><strong>ファームウェアを確認し、成功を確認してください</strong></p>
<blockquote>
<div><p>お好きなターミナル・アプリケーションを開いてください、</p>
<blockquote>
<div><ul class="simple">
<li><p>GNU/LinuxまたはmacOSでは、<span class="red-text">Terminal</span> アプリケーションのようにする。</p></li>
<li><p>Windowsでは <span class="red-text">Powershell</span> アプリケーションのようなものです。</p></li>
</ul>
</div></blockquote>
<p>例えば、Ubuntu（Linux）では、minicomを開いてダブルエンターを押す：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe05.png"><img alt="../../../_images/jflashliteexe05.png" class="align-center" src="/docs-assets/ja/_images/jflashliteexe05.png" style="width: 663.0px; height: 418.0px;"></a>
</div></blockquote>
<hr class="docutils">
<p>接続のために、まず <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001-DEV">DWM1001-DEV</a> と <a class="reference external" href="https://www.qorvo.com/products/p/DWM3001CDK">DWM3001CDK</a> 開発キットの主なコンポーネントの概要を見てみましょう。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>UDKキットについては、 <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">ハードウェアインターフェイス</span></a> セクションの詳細情報を参照してください。</p>
</div>
<a class="reference internal image-reference" href="../../../_images/dwm1001_io.png"><img alt="../../../_images/dwm1001_io.png" class="align-center" src="/docs-assets/ja/_images/dwm1001_io.png" style="width: 696.8000000000001px; height: 357.6px;"></a>
<a class="reference internal image-reference" href="../../../_images/dwm3001c_io.png"><img alt="../../../_images/dwm3001c_io.png" class="align-center" src="/docs-assets/ja/_images/dwm3001c_io.png" style="width: 630.0px; height: 630.0px;"></a>
</div>


           </div>
