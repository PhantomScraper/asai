---
title: "ファームウェアのアップデート"
lang: ja
slug: "pans-pro-rtls/integration-guide/firmware-update"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/firmware-update/"
order: 94
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="pans-pro-fw-update"></span><h1>ファームウェアのアップデート</h1>
<p>RTLS ネットワークを形成する際、イニシエータアンカーはネットワークに必要なファームウェアバージョンを指定します。自動ファームウェアアップデートが有効になっている場合、ネットワークに参加したいデバイスは同じファームウェア（バージョン番号とチェックサム）を持っていなければなりません。新しいデバイスが正しいファームウェアを持っていない場合、以下のサブセクションに従って更新されます。</p>
<div class="section" id="firmware-update-via-bluetooth">
<h2>Bluetoothによるファームウェア・アップデート</h2>
<p>ネットワークが動作している間にネットワーク全体を新しいファームウェア・イメ ージにアップデートしたい場合は、Bluetooth経由でイニシエータをアップデートすれば 十分です。イニシエータは、UWB無線リンクを介して、他の全てのデバイスに新しいファームウェアを自動的に伝搬します。イニシエータが最初にアップデートされると、ネットワークが再スタートし、各デバイスがネットワークに再参加すると、そのファームウェアがアップデートされることに注意してください。従って、ファームウェア・アップデートの間、アップデートを実行するノードは ”オフライン” になります。</p>
</div>
<div class="section" id="firmware-update-via-uwb">
<h2>UWB を介したファームウェア・アップデート</h2>
<p>DWM1001 システム概要 [4]で紹介されているように、ノードは自分のファームウェア・ バージョンを参加したいネットワークと比較します。ファームウェアのバージョンが異なる場合、ノードは参加する前にファームウェアのアップデートを試みます。このファームウェア・アップデート機能は、コンフィギュレーションで有効/無効を設定できます。ここでは、ノードが従う機能のルールを示します。</p>
<p><strong>タグ:</strong></p>
<ul class="simple">
<li><p>有効の場合、タグは常にファームウェアバージョンをチェックし、レンジングを開始する前にネットワーク内の近くのアンカーノードに更新要求を送信することにより、ファームウェアバージョンをネットワークと同期させようとします。</p></li>
<li><p>無効の場合、タグはファームウェアバージョンをチェックせずにレンジングを開始します。 無効にすると、タグはファームウェアのバージョンをチェックせずにレンジングを開始します。</p></li>
</ul>
<p><strong>アンカー：</strong></p>
<ul class="simple">
<li><p>有効にすると、ネットワークに参加する前に、アンカーはファームウェア・バージョンをチェックし、近くのアンカー・ノードに更新要求を送信することで、ファームウェア・バージョンをネットワークと同期させようとする。ネットワークに参加した後、アンカーは近くのノードからのファームウェア更新要求に応答します。</p></li>
<li><p>無効の場合、ネットワークに参加する前に、アンカーは直接参加要求を送信し、ファームウェアのバージョンを確認しません。これはバージョンの互換性の問題につながる可能性があるため、慎重に対処する必要があります。ネットワークに参加した後、アンカーは近くのノードからのファームウェア更新要求を無視します。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="firmware-update-via-uart">
<h2>UART 経由でのファームウェア・アップデート</h2>
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
</div>


           </div>
