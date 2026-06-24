---
title: "ファームウェアのアップデート"
lang: ja
slug: "pans-pro-rtls/quick-start-guide/firmware-update"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/quick-start-guide/firmware-update/"
order: 89
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="qsg-firmware-update"></span><h1>ファームウェアのアップデート</h1>
<p>このセクションでは、ファームウェアのアップデート方法について説明します。<span class="red-text">Bluetooth</span>、<span class="red-text">SWD</span>、<span class="red-text">OpenOCD</span>、<span class="red-text">UWB</span> など、様々な方法をサポートしています。</p>
<p>より詳細な情報については、以下からご希望の方法を選択してください：</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Bluetooth</label><div class="sd-tab-content docutils">
<p><strong>Bluetooth インターフェース経由</strong></p>
<p>ネットワークが稼働している状態でネットワーク全体を新しいファームウェアイメージにアップデートしたい場合は、イニシエーターを Bluetooth 経由でアップデートするだけで十分です。イニシエーターは、UWB 無線リンクを介して他のすべてのデバイスに新しいファームウェアを自動的に伝播します。イニシエーターが最初にアップデートされると、ネットワークが再起動され、各デバイスがネットワークに再接続すると、そのファームウェアが更新されることに注意してください。そのため、FW アップデート中は、アップデートを実行しているノードは “オフライン” になります。</p>
<p>開始するには、<a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> アプリケーションをダウンロードしてください（<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.panspro&amp;hl=en">Google Play</a> で入手可能）。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/panspro-manager-qr-code.png"><img alt="../../../_images/panspro-manager-qr-code.png" src="/docs-assets/ja/_images/panspro-manager-qr-code.png" style="width: 344.4px; height: 344.4px;"></a>
</div>
<ul class="simple">
<li><p>デフォルトのログインアカウントは、ユーザー名が <span class="red-text">admin</span>、パスワードが <span class="red-text">admin</span> です（設定でユーザー管理が有効になっている場合）。</p></li>
<li><p>ファームウェアステータスにアクセスします。 アプリケーション内の <span class="red-text">オプションメニュー</span> をタップします。 (<em>縦に3つの点で表示</em>) をタップします。 <span class="red-text">Firmware status</span> オプションを探し、選択します。</p></li>
<li><p><span class="red-text">ファームウェアステータス</span> オプションを探して選択します。</p></li>
<li><p>更新するデバイスを選択します。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/ppm-network-menu.jpg"><img alt="../../../_images/ppm-network-menu.jpg" src="/docs-assets/ja/_images/ppm-network-menu.jpg" style="width: 40%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-firmware-update.jpg"><img alt="../../../_images/ppm-firmware-update.jpg" src="/docs-assets/ja/_images/ppm-firmware-update.jpg" style="width: 40%;"></a>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
SWD</label><div class="sd-tab-content docutils">
<p><strong>SWD プログラマを使用したファームウェアのアップデート</strong></p>
<blockquote>
<div><img alt="../../../_images/image92.png" src="/docs-assets/ja/_images/image92.png">
</div></blockquote>
<p>LC4/LC5 上の DWM1001C</p>
<blockquote>
<div><img alt="../../../_images/image101.png" src="/docs-assets/ja/_images/image101.png">
</div></blockquote>
<p>名前のないボード</p>
<blockquote>
<div><img alt="../../../_images/image111.png" src="/docs-assets/ja/_images/image111.png">
</div></blockquote>
<p><strong>バイナリのプログラミング</strong></p>
<p>ボードにファクトリーイメージを書き込むために必要な手順を以下に示します。再フラッシュするには、J-Link または CMSIS-DAP プログラマを使用する必要があります。プログラマコネクタからは電源が供給されないため、再フラッシュ中はボードに USB またはバッテリーから電源を供給する必要があります。</p>
<p>J-Flash Light ソフトウェアツールを使用してイメージをフラッシュできます。この方法については後述します。別の方法として、様々なプラットフォームで利用可能なオープンソースツール OpenOCD を使用することもできます。PANS PRO ソフトウェアパッケージには、OpenOCD で使用する再フラッシュスクリプトが含まれています。</p>
<ol class="arabic">
<li><p>Segger J-Flash Lite (J-Link ソフトウェアスイート) をダウンロードしてインストールします: <a class="reference external" href="https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack">https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack</a></p></li>
<li><p>以下に示すように、モジュールを Micro USB データケーブルで接続します。</p>
<ol class="arabic">
<li><p>LC5 Gateway 上の DWM1001C モジュールのファームウェア再フラッシュ用接続</p>
<a class="reference internal image-reference" href="../../../_images/image131.png"><img alt="../../../_images/image131.png" src="/docs-assets/ja/_images/image131.png" style="width: 320.0px; height: 240.0px;"></a>
</li>
<li><p>LC5 Gateway 上のホスト MCU SAME70 のファームウェア再フラッシュ用接続</p>
<a class="reference internal image-reference" href="../../../_images/image141.png"><img alt="../../../_images/image141.png" src="/docs-assets/ja/_images/image141.png" style="width: 320.0px; height: 240.0px;"></a>
</li>
</ol>
</li>
<li><p>J-Flash Lite を開きます。</p></li>
<li><p>DWM1001Cのデバイスとしてnrf52832_XXAA、インターフェースとしてSWDを選択します。ホストMCUはATSAME70N19を使用します。デフォルトの速度1000を使用し、<strong>OK</strong> をクリックします。</p>
<a class="reference internal image-reference" href="../../../_images/image15.png"><img alt="../../../_images/image15.png" src="/docs-assets/ja/_images/image15.png" style="width: 384.40000000000003px; height: 126.80000000000001px;"></a>
</li>
<li><p>“チップ消去” をクリックして、チップ全体を消去します。</p>
<a class="reference internal image-reference" href="../../../_images/image16.png"><img alt="../../../_images/image16.png" src="/docs-assets/ja/_images/image16.png" style="width: 371.5px; height: 327.0px;"></a>
</li>
<li><p>データファイルで “...” をクリックし、フラッシュするPANS PROソフトウェアパッケージに含まれる16進ファイルを参照します。その後、 <strong>“Program Device”</strong> をクリックします。ファームウェアバイナリの互換性</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ダウンロード パッケージについては、<a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> までお問い合わせください。</p></li>
</ul>
</div></blockquote>
<table class="docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 36%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>ファームウェアファイル</strong></p></th>
<th class="head"><p><strong>ターゲット</strong></p></th>
<th class="head"><p><strong>リフラッシュアドレス</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>pan-pro-all-dwm1001c-vY.XX.hex</p></td>
<td><p>LC4タグおよびLC5ゲートウェイ上のDWM1001Cモジュール</p></td>
<td><p>0x00000000</p></td>
</tr>
<tr class="row-odd"><td><p>pans-pro-all-lc5s-vY.XX.hex</p></td>
<td><p>LC5ゲートウェイ上のホストMCU SAME70</p></td>
<td><p>0x00400000</p></td>
</tr>
</tbody>
</table>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
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
<li><p>パッケージをダウンロードしてPCに解凍します。WinZipや7-Zipのようなプログラムを使ってダウンロードしたファイルを解凍します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ダウンロード パッケージについては、<a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> までお問い合わせください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
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
<li><p><span class="red-text">cd</span> to <span class="red-text">/path/to/PANSPRO-Firmware-OpenOCD</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Micro USBデータケーブルを使用して、デバイスの``Micro USBデータポート``とPCを接続する。</p></li>
<li><p>スクリプトを実行して、ファームウェアを自動的に更新します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>linuxまたはmacOSでは、<span class="red-text">reflash-panspro-rtls-2ab.sh</span> コマンドを使用します。</p></li>
<li><p>Windows では、 <span class="red-text">reflash-panspro-rtls-2ab.bat</span> コマンドを使用します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>更新が完了すると、デバイスは更新の成功を示すビープ音を鳴らします。ボードはプロセスの一部として自動的にリセットされます。</p></li>
</ol>
<p>デバイスはファームウェアを正常に更新しました。最新の機能と改良点をお楽しみください。</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
UWB</label><div class="sd-tab-content docutils">
<p>RTLS ネットワークを形成する際、イニシエータアンカーはネットワークに必要なファームウェアバージョンを指定します。自動ファームウェアアップデートが有効になっている場合、ネットワークに参加したいデバイスは同じファームウェア（バージョン番号とチェックサム）を持っていなければなりません。新しいデバイスが正しいファームウェアを持っていない場合、以下のサブセクションに従って更新されます。</p>
<p><strong>UWBインターフェース経由</strong></p>
<p>DWM1001 システム概要 [4]で紹介されているように、ノードは自分のファームウェア・ バージョンを参加したいネットワークと比較します。ファームウェアのバージョンが異なる場合、ノードは参加する前にファームウェアのアップデートを試みます。このファームウェア・アップデート機能は、コンフィギュレーションで有効/無効を設定できます。ここでは、ノードが従う機能のルールを示します。</p>
<p><strong>タグ:</strong></p>
<ul class="simple">
<li><p>有効にすると、タグは常にファームウェアバージョンを確認し、測距を開始する前にネットワーク内の近くのアンカーノードに更新要求を送信することで、ファームウェアバージョンをネットワークと同期しようとします。</p></li>
<li><p>無効にすると、タグはファームウェアバージョンを確認せずに測距を開始します。これはバージョン互換性の問題を引き起こす可能性があるため、慎重に扱う必要があります。</p></li>
</ul>
<p><strong>アンカー：</strong></p>
<ul class="simple">
<li><p>有効にすると、アンカーはネットワークに参加する前にファームウェアバージョンを確認し、近くのアンカーノードに更新要求を送信してネットワークとファームウェアバージョンの同期を試みます。ネットワークに参加した後、アンカーは近くのノードからのファームウェア更新要求に応答します。</p></li>
<li><p>無効にすると、アンカーはネットワークに参加する前にファームウェアバージョンを確認せずに直接参加要求を送信します。これはバージョン互換性の問題を引き起こす可能性があるため、慎重に扱う必要があります。ネットワークに参加した後、アンカーは近くのノードからのファームウェア更新要求を無視します。</p></li>
</ul>
</div>
</div>
</div>


           </div>
