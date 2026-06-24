---
title: "SDKで起動"
lang: ja
slug: "udk/development-guide/udk-sdk-getting-started"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/development-guide/udk-sdk-getting-started/"
order: 45
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="udk-sdk-getting-started">
<span id="udksdk"></span><h1>SDKで起動</h1>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>サードパーティ アプリケーションの開発は UDK の提供範囲外であるため、プリペイドの UDK サポートの一部ではないことに注意してください。</p>
</div>
<p>このセクションでは、Zephyr RTOSプラットフォーム用に設計されたLEAPSサンプルプロジェクトの選択および起動に関する包括的なガイダンスを提供します。これらのサンプルは、<strong>UWB（Ultra-Wideband）技術</strong> とUDKキットの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">ハードウェアインターフェイス</span></a> をより深く理解するためのものです。</p>
<p>これらの知識を活用すれば、UDK キットでカスタム アプリケーションを自信を持って開発することができます。</p>
<p><strong>ガイダンスは以下の手順で行われます:</strong></p>
<ol class="arabic simple">
<li><p>Linux、macOS、または Windows 上で <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> RTOS 用の開発環境をセットアップします。</p></li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> ベースのサンプルアプリケーションパッケージであるUDKのSDKを入手する。</p></li>
<li><p>ホストPCへのデバイスの接続と必要なツール。</p></li>
<li><p>サンプル・アプリケーションを選択し、ビルド、フラッシュ、実行します。</p></li>
</ol>
<hr class="docutils">
<div class="section" id="zephyr-s-getting-started-guide">
<h2>ゼファー入門ガイド</h2>
<p>このガイドに従ってください：</p>
<ul class="simple">
<li><p>Ubuntu、macOS、Windows上でコマンドラインZephyr開発環境をセットアップする (他のLinuxディストリビューションの手順は <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/installation_linux.html#installation-linux">installation_linux</a> で説明されています)</p></li>
<li><p>ZephyrのSDKパッケージ(必要なツールチェーンを含む)をインストールする。</p></li>
</ul>
<div class="section" id="select-and-update-os">
<h3>OS の選択と更新</h3>
<p>お使いのOSをクリックしてください。</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-0">
Ubuntu</label><div class="sd-tab-content docutils">
<p>このガイドはUbuntuバージョン20.04 LTS以降を対象としています。</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>update
sudo<span class="w"> </span>apt<span class="w"> </span>upgrade
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-1">
macOS</label><div class="sd-tab-content docutils">
<p>macOS Mojave以降では、<em>システム環境設定</em> &gt; <em>ソフトウェア・アップデート</em> を選択します。必要に応じて、 <em>今すぐ更新</em> をクリックします。</p>
<p>他のバージョンについては、<a class="reference external" href="https://support.apple.com/en-us/HT201541">この Apple サポートトピック</a> を参照してください。</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-2">
Windows</label><div class="sd-tab-content docutils">
<p><em>スタート</em> &gt; <em>設定</em> &gt; <em>更新とセキュリティ</em> &gt; <em>Windows Update</em>。 <em>を選択します更新プログラムのチェック</em> をクリックし、利用可能なすべての更新プログラムをインストールします。</p>
</div>
</div>
</div>
<div class="section" id="install-dependencies">
<h3>依存関係のインストール</h3>
<p>次に、パッケージマネージャーを使ってホストの依存関係をいくつかインストールします。</p>
<p>主な依存関係の現在の最小必要バージョンは以下の通りです：</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>ツール</p></th>
<th class="head"><p>最小 バージョン</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://cmake.org/">CMake</a></p></td>
<td><p>3.20.5</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference external" href="https://www.python.org/">Python</a></p></td>
<td><p>3.10</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference external" href="https://www.devicetree.org/">Devicetreeコンパイラ</a></p></td>
<td><p>1.4.6</p></td>
</tr>
</tbody>
</table>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-3">
Ubuntu</label><div class="sd-tab-content docutils">
<ol class="arabic" id="install-dependencies-ubuntu">
<li><p>22.04より古いバージョンのUbuntuを使用している場合、上記の主な依存関係の最低必要バージョンを満たすために、追加のリポジトリを追加する必要があります。その場合、Kitware APT リポジトリをソースリストに追加するために、Kitware アーカイブスクリプトをダウンロード、検査、実行してください。<code class="docutils literal notranslate"><span class="pre">kitware-archive.sh</span></code> の詳細な説明は、こちら <a class="reference external" href="https://apt.kitware.com/">kitware third-party apt repository</a> にあります：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>wget<span class="w"> </span>https://apt.kitware.com/kitware-archive.sh
sudo<span class="w"> </span>bash<span class="w"> </span>kitware-archive.sh
</pre></div>
</div>
</li>
<li><p>必要な依存関係をインストールするには <code class="docutils literal notranslate"><span class="pre">apt</span></code> を使ってください：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>install<span class="w"> </span>--no-install-recommends<span class="w"> </span>git<span class="w"> </span>cmake<span class="w"> </span>ninja-build<span class="w"> </span>gperf<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>ccache<span class="w"> </span>dfu-util<span class="w"> </span>device-tree-compiler<span class="w"> </span>wget<span class="w"> </span>minicom<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>python3-dev<span class="w"> </span>python3-pip<span class="w"> </span>python3-setuptools<span class="w"> </span>python3-tk<span class="w"> </span>python3-wheel<span class="w"> </span>xz-utils<span class="w"> </span>file<span class="w"> </span><span class="se">\</span>
<span class="w">  </span>make<span class="w"> </span>gcc<span class="w"> </span>gcc-multilib<span class="w"> </span>g++-multilib<span class="w"> </span>libsdl2-dev<span class="w"> </span>libmagic1
</pre></div>
</div>
</li>
<li><p>システムにインストールされている主な依存関係のバージョンを入力して確認してください：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--version
python3<span class="w"> </span>--version
dtc<span class="w"> </span>--version
</pre></div>
</div>
<p>このセクションの最初にある表のバージョンと照らし合わせてください。手動で依存関係を更新するための追加情報については <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/installation_linux.html#installation-linux">installation_linux</a> page を参照してください。</p>
</li>
</ol>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-4">
macOS</label><div class="sd-tab-content docutils">
<ol class="arabic" id="install-dependencies-macos">
<li><p><a class="reference external" href="https://brew.sh/">Homebrew</a> をインストールしてください：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>/bin/bash<span class="w"> </span>-c<span class="w"> </span><span class="s2">"</span><span class="k">$(</span>curl<span class="w"> </span>-fsSL<span class="w"> </span>https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh<span class="k">)</span><span class="s2">"</span>
</pre></div>
</div>
</li>
<li><p>Homebrew インストールスクリプトが完了したら、画面の指示に従って Homebrew インストールをパスに追加してください。</p>
<ul>
<li><p>Apple Silicon上で動作するmacOSでは、次のようにします：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="o">(</span>echo<span class="p">;</span><span class="w"> </span><span class="nb">echo</span><span class="w"> </span><span class="s1">'eval "$(/opt/homebrew/bin/brew shellenv)"'</span><span class="o">)</span><span class="w"> </span>&gt;&gt;<span class="w"> </span>~/.zprofile
<span class="nb">source</span><span class="w"> </span>~/.zprofile
</pre></div>
</div>
</li>
<li><p>Intel 上で動作している macOS では、Apple Silicon 用のコマンドを使用しますが、<code class="docutils literal notranslate"><span class="pre">/opt/homebrew/</span></code> を <code class="docutils literal notranslate"><span class="pre">/usr/local/</span></code> に置き換えてください。</p></li>
</ul>
</li>
<li><p>必要な依存関係をインストールするには <code class="docutils literal notranslate"><span class="pre">brew</span></code> を使用してください：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>brew<span class="w"> </span>install<span class="w"> </span>cmake<span class="w"> </span>ninja<span class="w"> </span>gperf<span class="w"> </span>python3<span class="w"> </span>ccache<span class="w"> </span>qemu<span class="w"> </span>dtc<span class="w"> </span>libmagic<span class="w"> </span>wget<span class="w"> </span>openocd<span class="w"> </span>minicom
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">python</span></code> と <code class="docutils literal notranslate"><span class="pre">pip</span></code> だけでなく <code class="docutils literal notranslate"><span class="pre">python3</span></code> と <code class="docutils literal notranslate"><span class="pre">pip3</span></code> も実行できるように、Homebrew Python フォルダーをパスに追加します。</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="o">(</span>echo<span class="p">;</span><span class="w"> </span><span class="nb">echo</span><span class="w"> </span><span class="s1">'export PATH="'</span><span class="k">$(</span>brew<span class="w"> </span>--prefix<span class="k">)</span><span class="s1">'/opt/python/libexec/bin:$PATH"'</span><span class="o">)</span><span class="w"> </span>&gt;&gt;<span class="w"> </span>~/.zprofile
<span class="nb">source</span><span class="w"> </span>~/.zprofile
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-5">
Windows</label><div class="sd-tab-content docutils">
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>実行ファイルが見つからないという問題があるため、Zephyr Project は現在 <a class="reference external" href="https://msdn.microsoft.com/en-us/commandline/wsl/install_guide">Windows Subsystem for Linux (WSL)</a> (WSL) を使ったアプリケーションのフラッシュをサポートしていません。</p>
<p>そのため、Zephyrを始めるときにWSLを使うことはお勧めしません。</p>
</div>
<p>これらの手順は <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> コマンドプロンプトのターミナルウィンドウで実行する必要があります。Windowsの最新バージョン（10以降）では、マイクロソフトストアからWindowsターミナルアプリケーションをインストールすることをお勧めします。必要なコマンドはPowerShellによって異なります。</p>
<p>これらの手順は <a class="reference external" href="https://chocolatey.org/">Chocolatey</a> に依存しています。Chocolateyが使えない場合は、それぞれのウェブサイトから依存関係をインストールし、コマンドラインツールが <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-PATH">PATH</a> <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#env-vars">environment variable</a> にあることを確認してください。</p>
<ol class="arabic" id="install-dependencies-windows">
<li><p><a class="reference external" href="https://chocolatey.org/install">Install chocolatey</a></p></li>
<li><p><strong>管理者</strong> として <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> ターミナルウィンドウを開きます。Windows キーを押しながら <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> と入力し、 <span class="guilabel">Command Prompt</span> の検索結果を右クリックし、 <span class="guilabel">Run as Administrator</span> を選択する。</p></li>
<li><p>グローバル確認を無効にすると、個々のプログラムのインストールを確認する必要がなくなります：</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>choco feature enable -n allowGlobalConfirmation
</pre></div>
</div>
</li>
<li><p>必要な依存関係をインストールするには <code class="docutils literal notranslate"><span class="pre">choco</span></code> を使ってください：</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>choco install cmake --installargs 'ADD_CMAKE_TO_PATH=System'
choco install ninja gperf python311 git dtc-msys2 wget 7zip unzip
</pre></div>
</div>
<div class="admonition warning">
<p class="admonition-title">警告</p>
<p>2023年11月現在、Python 3.12はWindowsでのZephyr開発には推奨されていません。</p>
</div>
</li>
<li><p>ターミナ</p></li>
</ol>
</div>
</div>
</div>
<div class="section" id="install-west">
<h3>Westのインストール</h3>
<p><a class="reference external" href="https://docs.zephyrproject.org/latest/develop/west/index.html">West</a> は <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 用の swiss-army knife コマンドラインツールです：</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-6">
Ubuntu</label><div class="sd-tab-content docutils">
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
仮想環境内にインストールする</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Python <code class="docutils literal notranslate"><span class="pre">venv</span></code> パッケージをインストールするには <code class="docutils literal notranslate"><span class="pre">apt</span></code> を使用してください：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>install<span class="w"> </span>python3-venv
</pre></div>
</div>
</li>
<li><p>新しい仮想環境を作成します：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>~/udk-sdk/.venv
</pre></div>
</div>
</li>
<li><p>仮想環境をアクティブにします：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">source</span><span class="w"> </span>~/udk-sdk/.venv/bin/activate
</pre></div>
</div>
<p>アクティブにするとシェルの先頭に <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code> が付きます。仮想環境は <code class="docutils literal notranslate"><span class="pre">deactivate</span></code> を実行することでいつでも無効化することができます。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>作業を開始するたびに仮想環境を有効にすることを忘れないでください。</p>
</div>
</li>
<li><p>ウェストをインストールする</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
グローバルにインストールする</label><div class="sd-tab-content docutils">
<p>west をインストールし、<code class="file docutils literal notranslate"><span class="pre">~/.local/bin</span></code> が <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-PATH">PATH</a> <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/env_vars.html#env-vars">environment variable</a> にあることを確認してください：</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip3<span class="w"> </span>install<span class="w"> </span>--user<span class="w"> </span>-U<span class="w"> </span>west
<span class="nb">echo</span><span class="w"> </span><span class="s1">'export PATH=~/.local/bin:"$PATH"'</span><span class="w"> </span>&gt;&gt;<span class="w"> </span>~/.bashrc
<span class="nb">source</span><span class="w"> </span>~/.bashrc
</pre></div>
</div>
</div></blockquote>
</div>
</div>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-7">
macOS</label><div class="sd-tab-content docutils">
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-11" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
仮想環境内にインストールする</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>新しい仮想環境を作成します：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>~/udk-sdk/.venv
</pre></div>
</div>
</li>
<li><p>仮想環境をアクティブにします：</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">source</span><span class="w"> </span>~/udk-sdk/.venv/bin/activate
</pre></div>
</div>
<p>アクティブにするとシェルの先頭に <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code> が付きます。仮想環境は <code class="docutils literal notranslate"><span class="pre">deactivate</span></code> を実行することでいつでも無効化することができます。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>作業を開始するたびに仮想環境を有効にすることを忘れないでください。</p>
</div>
</li>
<li><p>ウェストをインストールする</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-12" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-12">
グローバルにインストールする</label><div class="sd-tab-content docutils">
<p>ウェストをインストールする</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip3<span class="w"> </span>install<span class="w"> </span>-U<span class="w"> </span>west
</pre></div>
</div>
</div></blockquote>
</div>
</div>
</div>
<input id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-8">
Windows</label><div class="sd-tab-content docutils">
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-13" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-13">
仮想環境内にインストールする</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>ターミナルウィンドウ <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> を開きます <strong>一般ユーザー</strong> として</p></li>
<li><p>新しい仮想環境を作成します：</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span><span class="k">cd</span> <span class="nv">%HOMEPATH%</span>
python -m venv udk-sdk\.venv
</pre></div>
</div>
</li>
<li><p>仮想環境をアクティブにします：</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>udk-sdk\.venv\Scripts\activate.bat
</pre></div>
</div>
<p>アクティブにするとシェルの先頭に <code class="docutils literal notranslate"><span class="pre">(.venv)</span></code> が付きます。仮想環境は <code class="docutils literal notranslate"><span class="pre">deactivate</span></code> を実行することでいつでも無効化することができます。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>作業を開始するたびに仮想環境を有効にすることを忘れないでください。</p>
</div>
</li>
<li><p>ウェストをインストールする</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>pip install west
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-14" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-14">
グローバルにインストールする</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>ターミナルウィンドウ <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> を開きます <strong>一般ユーザー</strong> として</p></li>
<li><p>ウェストをインストールする</p>
<div class="highlight-bat notranslate"><div class="highlight"><pre><span></span>pip3 install -U west
</pre></div>
</div>
</li>
</ol>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="install-the-zephyr-sdk">
<span id="installthezephyrsdk"></span><h3>Zephyr SDK をインストールする。</h3>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>SDKをアンインストールしたい場合は、SDKをインストールしたディレクトリを削除してください。</p>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-15" name="sd-tab-set-6" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-15">
Ubuntu</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p><a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a> をダウンロードして確認してください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">~</span>
<span class="n">wget</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_linux</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
<span class="n">wget</span> <span class="o">-</span><span class="n">O</span> <span class="o">-</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">sha256</span><span class="o">.</span><span class="n">sum</span> <span class="o">|</span> <span class="n">shasum</span> <span class="o">--</span><span class="n">check</span> <span class="o">--</span><span class="n">ignore</span><span class="o">-</span><span class="n">missing</span>
</pre></div>
</div>
<p>ホストアーキテクチャが 64-bit ARM (例: Raspberry Pi) の場合、64-bit ARM Linux SDK をダウンロードするには <code class="docutils literal notranslate"><span class="pre">x86_64</span></code> を <code class="docutils literal notranslate"><span class="pre">aarch64</span></code> に置き換えてください。</p>
</li>
<li><p>Zephyr SDK バンドルアーカイブを解凍してください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">tar</span> <span class="n">xvf</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_linux</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Zephyr SDK バンドルは以下のいずれかの場所で展開することをお勧めします：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/bin</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/usr/local</span></code></p></li>
</ul>
<p>Zephyr SDK バンドルアーカイブには <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code> ディレクトリが含まれており、<code class="docutils literal notranslate"><span class="pre">$HOME</span></code> の下に展開すると、インストールパスは <code class="docutils literal notranslate"><span class="pre">$HOME/zephyr-sdk-&lt;version&gt;</span></code> になります。</p>
</div>
</li>
<li><p>Zephyr SDK バンドルセットアップスクリプトを実行してください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="o">./</span><span class="n">setup</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Zephyr SDK バンドルを展開した後、セットアップスクリプトを一度だけ実行する必要があります。</p>
<p>初期セットアップ後に Zephyr SDK バンドルディレクトリを再配置した場合は、セットアップスクリプトを再実行する必要があります。</p>
</div>
</li>
<li><p><a class="reference external" href="https://en.wikipedia.org/wiki/Udev">udev</a> ルールをインストールすると、ほとんどの Zephyr ボードを一般ユーザーとしてフラッシュできるようになります：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">cp</span> <span class="o">~/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="o">/</span><span class="n">sysroots</span><span class="o">/</span><span class="n">x86_64</span><span class="o">-</span><span class="n">pokysdk</span><span class="o">-</span><span class="n">linux</span><span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">share</span><span class="o">/</span><span class="n">openocd</span><span class="o">/</span><span class="n">contrib</span><span class="o">/</span><span class="mi">60</span><span class="o">-</span><span class="n">openocd</span><span class="o">.</span><span class="n">rules</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">udev</span><span class="o">/</span><span class="n">rules</span><span class="o">.</span><span class="n">d</span>
<span class="n">sudo</span> <span class="n">udevadm</span> <span class="n">control</span> <span class="o">--</span><span class="n">reload</span>
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-16" name="sd-tab-set-6" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-16">
macOS</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p><a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a> をダウンロードして確認してください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">~</span>
<span class="n">curl</span> <span class="o">-</span><span class="n">L</span> <span class="o">-</span><span class="n">O</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_macos</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
<span class="n">curl</span> <span class="o">-</span><span class="n">L</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">sha256</span><span class="o">.</span><span class="n">sum</span> <span class="o">|</span> <span class="n">shasum</span> <span class="o">--</span><span class="n">check</span> <span class="o">--</span><span class="n">ignore</span><span class="o">-</span><span class="n">missing</span>
</pre></div>
</div>
<p>ホストアーキテクチャが64-bit ARM (Apple Silicon, M1としても知られています) の場合、64-bit ARM macOS SDKをダウンロードするために <code class="docutils literal notranslate"><span class="pre">x86_64</span></code> を <code class="docutils literal notranslate"><span class="pre">aarch64</span></code> に置き換えてください。</p>
</li>
<li><p>Zephyr SDK バンドルアーカイブを解凍してください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">tar</span> <span class="n">xvf</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_macos</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">tar</span><span class="o">.</span><span class="n">gz</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Zephyr SDK バンドルは以下のいずれかの場所で展開することをお勧めします：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/.local/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">$HOME/bin</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/opt</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">/usr/local</span></code></p></li>
</ul>
<p>Zephyr SDK バンドルアーカイブには <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code> ディレクトリが含まれており、<code class="docutils literal notranslate"><span class="pre">$HOME</span></code> の下に展開すると、インストールパスは <code class="docutils literal notranslate"><span class="pre">$HOME/zephyr-sdk-&lt;version&gt;</span></code> になります。</p>
</div>
</li>
<li><p>Zephyr SDK バンドルセットアップスクリプトを実行してください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="o">./</span><span class="n">setup</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Zephyr SDK バンドルを展開した後、セットアップスクリプトを一度だけ実行する必要があります。</p>
<p>初期セットアップ後に Zephyr SDK バンドルディレクトリを再配置した場合は、セットアップスクリプトを再実行する必要があります。</p>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-17" name="sd-tab-set-6" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-17">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>ターミナルウィンドウ <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> を開きます <strong>一般ユーザー</strong> として</p></li>
<li><p>下载 <a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/tree/v0.14.2">Zephyr SDK bundle</a>：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="o">%</span><span class="n">HOMEPATH</span><span class="o">%</span>
<span class="n">wget</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">zephyrproject</span><span class="o">-</span><span class="n">rtos</span><span class="o">/</span><span class="n">sdk</span><span class="o">-</span><span class="n">ng</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">v0</span><span class="mf">.14.2</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_windows</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">zip</span>
</pre></div>
</div>
</li>
<li><p>Zephyr SDK バンドルアーカイブを解凍してください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">unzip</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span><span class="n">_windows</span><span class="o">-</span><span class="n">x86_64</span><span class="o">.</span><span class="n">zip</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Zephyr SDK バンドルは以下のいずれかの場所で展開することをお勧めします：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">%HOMEPATH%</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">%PROGRAMFILES%</span></code>.</p></li>
</ul>
<p>Zephyr SDK バンドルアーカイブには <code class="docutils literal notranslate"><span class="pre">zephyr-sdk-&lt;version&gt;</span></code> ディレクトリが含まれており、<code class="docutils literal notranslate"><span class="pre">%HOMEPATH%</span></code> で展開するとインストールパスは <code class="docutils literal notranslate"><span class="pre">%HOMEPATH%%zephyr-sdk-&lt;version&gt;</span></code> となります。</p>
</div>
</li>
<li><p>Zephyr SDK バンドルセットアップスクリプトを実行してください：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">sdk</span><span class="o">-</span><span class="mf">0.14.2</span>
<span class="n">setup</span><span class="o">.</span><span class="n">cmd</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Zephyr SDK バンドルを展開した後、セットアップスクリプトを一度だけ実行する必要があります。</p>
<p>初期セットアップ後に Zephyr SDK バンドルディレクトリを再配置した場合は、セットアップスクリプトを再実行する必要があります。</p>
</div>
</li>
</ol>
</div>
</div>
</div>
</div>
<div class="section" id="install-udk-sdk-package">
<h2>UDK-SDK パッケージのインストール</h2>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>UDK SDKもZephyrベースのサンプルアプリケーションです。より深く理解するには、この <a class="reference external" href="https://github.com/zephyrproject-rtos/example-application">example-application</a> ページを参照してください。</p>
</div>
<p>最初のステップでは、ワークスペースフォルダ <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code> を初期化し、そこに <code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> と全てのZephyrモジュールをクローンします。以下の手順に従ってください：</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-18" name="sd-tab-set-7" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-18">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>ターミナルを開く</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> の <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code> ワークスペースをメインリビジョンで初期化する。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> ソース（バージョン 3.1.0）とそのモジュールをクローンしてください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake パッケージをエクスポートしてください。これにより、Zephyrアプリケーションのビルドに必要なボイラープレートコードをCMakeが自動的にロードするようになります。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> のscripts/requirements.txtファイルは追加のPython依存を宣言しています。pip を使ってインストールしてください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="o">./</span><span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>ZEPHYR_BASE 環境を設定してください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">zephyr</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">env</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-19" name="sd-tab-set-7" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-19">
macOS</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>ターミナルを開く</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> の <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code> ワークスペースをメインリビジョンで初期化する。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
<div class="admonition caution">
<p class="admonition-title">注意</p>
<p>公開されている <code class="docutils literal notranslate"><span class="pre">udk-sdk</span> <span class="pre">repository</span></code> は近日中に提供される予定です。ご期待ください！</p>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> ソース（バージョン 3.1.0）とそのモジュールをクローンしてください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake パッケージをエクスポートしてください。これにより、Zephyrアプリケーションのビルドに必要なボイラープレートコードをCMakeが自動的にロードするようになります。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> のscripts/requirements.txtファイルは追加のPython依存を宣言しています。pip を使ってインストールしてください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="o">./</span><span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>ZEPHYR_BASE 環境を設定してください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">zephyr</span><span class="o">/</span><span class="n">zephyr</span><span class="o">-</span><span class="n">env</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-20" name="sd-tab-set-7" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-20">
Windows</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>一般ユーザーとして <code class="docutils literal notranslate"><span class="pre">cmd.exe</span></code> ターミナルウィンドウを開く</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">leaps-udk-examples</span></code> の <code class="docutils literal notranslate"><span class="pre">udk-sdk</span></code> ワークスペースをメインリビジョンで初期化する。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">init</span> <span class="o">-</span><span class="n">m</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">leapslabs</span><span class="o">/</span><span class="n">udk</span><span class="o">-</span><span class="n">sdk</span><span class="o">.</span><span class="n">git</span> <span class="o">--</span><span class="n">mr</span> <span class="n">main</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> ソース（バージョン 3.1.0）とそのモジュールをクローンしてください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">udk</span><span class="o">-</span><span class="n">sdk</span>
<span class="n">west</span> <span class="n">update</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> CMake パッケージをエクスポートしてください。これにより、Zephyrアプリケーションのビルドに必要なボイラープレートコードをCMakeが自動的にロードするようになります。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">west</span> <span class="n">zephyr</span><span class="o">-</span><span class="n">export</span>
</pre></div>
</div>
</li>
<li><p><a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> のscripts/requirements.txtファイルは追加のPython依存を宣言しています。pip を使ってインストールしてください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="n">zephyr</span><span class="o">/</span><span class="n">scripts</span><span class="o">/</span><span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div>
</div>
</li>
<li><p>ZEPHYR_BASE 環境を設定してください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">cd</span> <span class="n">zephyr</span>
<span class="n">zephyr</span><span class="o">-</span><span class="n">env</span><span class="o">.</span><span class="n">cmd</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
</div>
</div>
<div class="section" id="device-setup">
<span id="devicesetup"></span><h2>デバイスのセットアップ</h2>
<p>サンプル・アプリケーションを実行する前に、デバイスが接続されていることを確認し、以下の手順でコンソール・ウィンドウを開いてください：</p>
<ol class="arabic">
<li><p>USB-C データケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データポート 2</span></a> とホスト PC を接続します。</p>
<img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port2.gif">
</li>
<li><p><a class="reference internal" href="/docs/ja/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">ファームウェアのプログラミング/アップグレード</span></a> セクションのOpenOCDタブを参照し、OpenOCDツールをインストールする。このセクションにはファームウェアをフラッシュするための他のソリューションも含まれています。</p></li>
<li><p>以下のコマンドを実行して minicom (Linux と macOs) または <a class="reference external" href="https://teratermproject.github.io/index-en.html">Tera Term</a> (Windows) を開き、接続されたシリアルポートにアクセスします。</p></li>
</ol>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-21" name="sd-tab-set-8" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-21">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>ターミナルを開く</p></li>
<li><p>以下のコマンドを ttyACM&lt;X&gt; (0 は最初に接続されたデバイスのデフォルトポート) で実行する。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">minicom -b 115200 -D /dev/ttyACM0</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>以下のコマンドを使用して、再フラッシュしようとしているすべての接続デバイス(ttyACM&lt;X&gt;)を確認してください</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">ls ../../dev/</span>
</pre></div>
</div>
</div></blockquote>
</div>
</li>
<li><p>デバイスに正常に接続された場合</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">Welcome to minicom 2.8</span>

<span class="go">OPTIONS: I18n</span>
<span class="go">Port /dev/ttyACM0, 04:49:57</span>

<span class="go">Press CTRL-A Z for help on special keys</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-22" name="sd-tab-set-8" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-22">
macOS</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p>ターミナルを開く</p></li>
<li><p>dev/tty.usb&lt;xxx&gt;で以下のコマンドを実行します(モデム1410の例)</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">minicom -b 115200 -D /dev/tty.usbmodem1410</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>以下のコマンドを使って、再フラッシュしようとしている接続デバイス (tty.usb&lt;xxx&gt;) を確認してください。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">ls ../../dev/</span>
</pre></div>
</div>
</div>
</li>
<li><p>デバイスに正常に接続された場合</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">Welcome to minicom 2.8</span>

<span class="go">OPTIONS:</span>
<span class="go">Compiled on Jan  4 2021, 00:04:46.</span>
<span class="go">Port /dev/tty.usbmodem1410, 19:42:45</span>

<span class="go">Press Meta-Z for help on special keys</span>
</pre></div>
</div>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-23" name="sd-tab-set-8" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-23">
Windows</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p><a class="reference external" href="https://teratermproject.github.io/index-en.html">Tera Term</a> ツールを開く</p></li>
<li><p>設定 &gt; シリアルポート</p>
<a class="reference internal image-reference" href="../../../_images/setup.png"><img alt="../../../_images/setup.png" src="/docs-assets/ja/_images/setup.png" style="width: 523.2px; height: 268.0px;"></a>
</li>
<li><p>デバイスの接続ポートを選択 (例: Port 5 がデバイスに接続されている)</p>
<a class="reference internal image-reference" href="../../../_images/port.png"><img alt="../../../_images/port.png" src="/docs-assets/ja/_images/port.png" style="width: 373.6px; height: 359.20000000000005px;"></a>
</li>
<li><p>速度を 115200 に選択してください</p>
<a class="reference internal image-reference" href="../../../_images/speed.png"><img alt="../../../_images/speed.png" src="/docs-assets/ja/_images/speed.png" style="width: 372.0px; height: 361.6px;"></a>
</li>
<li><p>Close と New Open を選択する(または New Open)</p></li>
</ol>
</div></blockquote>
</div>
</div>
</div>
<div class="section" id="coordinated-examples-execution">
<h2>調整された例の実行</h2>
<p>UDK-SDKパッケージの <span class="sd-sphinx-override sd-badge sd-outline-info sd-text-info">@yourdir/udk-sdk/leaps-udk-examples/app/006_ex_uwb</span> に、さまざまなサンプルがあります。ウルトラワイドバンドの協調動作を実現するには、以下の表に示すように2つの例をペアリングする必要があります。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 51%">
<col style="width: 49%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>例 1</p></th>
<th class="head"><p>例 2</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ex_01a_simple_tx/simple_tx.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_01b_tx_sleep/tx_sleep_idleRC.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_01b_tx_sleep/tx_sleep.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_01c_tx_sleep_auto/tx_sleep_auto.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_01d_tx_timed_sleep/tx_timed_sleep.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_01e_tx_with_cca/tx_with_cca.c</p></td>
<td><p>ex_02a_simple_rx/simple_rx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_01g_simple_tx_sts_sdc/simple_tx_sts_sdc.c</p></td>
<td><p>ex_02g_simple_rx_sts_sdc/simple_rx_sts_sdc.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_01h_simple_tx_pdoa/simple_tx_pdoa.c</p></td>
<td><p>ex_02h_simple_rx_pdoa/simple_rx_pdoa.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_01i_simple_tx_aes/simple_tx_aes.c</p></td>
<td><p>ex_02i_simple_rx_aes/simple_rx_aes.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_02a_simple_rx/simple_rx_nlos.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_02c_rx_diagnostics/rx_diagnostics.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_02d_rx_sniff/rx_sniff.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_02e_rx_dbl_buff/double_buffer_rx.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_02f_rx_with_crystal_trim/rx_with_xtal_trim.c</p></td>
<td><p>ex_01a_simple_tx/simple_tx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_03a_tx_wait_resp/tx_wait_resp.c</p></td>
<td><p>ex_03b_rx_send_resp/rx_send_resp.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_03d_tx_wait_resp_interrupts/tx_wait_resp_int.c</p></td>
<td><p>ex_03b_rx_send_resp/rx_send_resp.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_05a_ds_twr_init/ds_twr_initiator.c</p></td>
<td><p>ex_05b_ds_twr_resp/ds_twr_responder.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_05a_ds_twr_init/ds_twr_initiator_sts.c</p></td>
<td><p>ex_05b_ds_twr_resp/ds_twr_responder_sts.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_05c_ds_twr_init_sts_sdc/ds_twr_sts_sdc_initiator.c</p></td>
<td><p>ex_05d_ds_twr_resp_sts_sdc/ds_twr_sts_sdc_responder.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_06a_ss_twr_initiator/ss_twr_initiator_sts_no_data.c</p></td>
<td><p>ex_06b_ss_twr_responder/ss_twr_responder_sts_no_data.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_06a_ss_twr_initiator/ss_twr_initiator_sts.c</p></td>
<td><p>ex_06b_ss_twr_responder/ss_twr_responder_sts.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_06a_ss_twr_initiator/ss_twr_initiator.c</p></td>
<td><p>ex_06b_ss_twr_responder/ss_twr_responder.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_06e_AES_ss_twr_initiator/ss_aes_twr_initiator.c</p></td>
<td><p>ex_06f_AES_ss_twr_responder/ss_aes_twr_responder.c</p></td>
</tr>
<tr class="row-odd"><td><p>ex_07a_ack_data_tx/ack_data_tx.c</p></td>
<td><p>ex_07b_ack_data_rx/ack_data_rx.c</p></td>
</tr>
<tr class="row-even"><td><p>ex_15_le_pend/le_pend_rx.c</p></td>
<td><p>ex_15_le_pend/le_pend_tx.c</p></td>
</tr>
</tbody>
</table>
<p>詳細な説明は、各例のソース∕*.c ファイルに記載されている説明を参照してください。</p>
<p><strong>例:</strong> ex_01h_simple_tx_pdoa/simple_tx_pdoa.c</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">*  @file    simple_tx_pdoa.c</span>
<span class="go">*  @brief   Simple TX PDOA example code, companion to Simple RX PDOA example.</span>
<span class="go">*           See note 7 regarding information on calibrating the system</span>
</pre></div>
</div>
</div>
<hr class="docutils">
<div class="section" id="build-and-run-the-example">
<h2>サンプルのビルドと実行</h2>
<p>このセクションでは、ソフトウェアのビルドと再フラッシュの方法を説明します。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>もし <a class="reference external" href="https://www.zephyrproject.org/">Zephyr</a> 環境で何らかの問題が発生した場合は、 <a class="reference external" href="https://docs.zephyrproject.org/latest/develop/getting_started/index.html#troubleshooting-installation">トラブルシューティング インストール</a> セクションを参照してください。</p>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-24" name="sd-tab-set-9" type="radio">
<label class="sd-tab-label" data-sync-id="key1" for="sd-tab-item-24">
Ubuntu</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p><a class="reference internal" href="#devicesetup"><span class="std std-ref">デバイスのセットアップ</span></a> ガイドラインを完成させてください。</p></li>
<li><p>サンプルディレクトリに移動します</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</li>
<li><p>(オプション) 古いビルドディレクトリを掃除する。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rm -rf build/</span>
</pre></div>
</div>
</li>
<li><p>サンプルをビルドする</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-27" name="sd-tab-set-10" type="radio">
<label class="sd-tab-label" for="sd-tab-item-27">
選択メニュー付き</label><div class="sd-tab-content docutils">
<p>このセクションは、予想される例を1つ選択して、例を構築する方法をガイドします。</p>
<ol class="arabic">
<li><p>BOARDがleaps_lc14またはleaps_lc13の場合、メニューを表示するには以下のコマンドを実行してください</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p><strong>サンプルアプリケーション</strong> を選択してEnterを押してください。</p>
<a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/ja/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</li>
<li><p>デフォルトの <strong>サンプル</strong> が表示されます。</p>
<a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/ja/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>上下にスクロールして <strong>サンプル</strong> を選択し、Enterを押してください。</p>
<a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/ja/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>ESC と Y を押して選択を保存してください。</p>
<a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/ja/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</li>
<li><p>サンプルをビルドする</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</li>
<li><p>サンプルのビルドに成功しました。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[169/179] Linking C executable zephyr/zephyr_pre0.elf</span>

<span class="go">[173/179] Linking C executable zephyr/zephyr_pre1.elf</span>

<span class="go">[179/179] Linking C executable zephyr/zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       31268 B         1 MB      2.98%</span>
<span class="go">            SRAM:        8568 B       256 KB      3.27%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</li>
</ol>
</div>
<input id="sd-tab-item-28" name="sd-tab-set-10" type="radio">
<label class="sd-tab-label" for="sd-tab-item-28">
選択メニューなし</label><div class="sd-tab-content docutils">
<p>このセクションはデフォルトのサンプルを使ってサンプルをビルドする方法を説明します。</p>
<ol class="arabic">
<li><p>$BOARD が leaps_lc14 または leaps_lc13 の場合、以下のコマンドを実行してください。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p>サンプルのビルドに成功しました。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[169/179] Linking C executable zephyr/zephyr_pre0.elf</span>

<span class="go">[173/179] Linking C executable zephyr/zephyr_pre1.elf</span>

<span class="go">[179/179] Linking C executable zephyr/zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       31268 B         1 MB      2.98%</span>
<span class="go">            SRAM:        8568 B       256 KB      3.27%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</li>
</ol>
</div>
</div>
</li>
<li><p>そしてデバイスに16進ファイルを再フラッシュしてください：</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>ファームウェアの再フラッシュに成功しました。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">Open On-Chip Debugger 0.11.0+dev-00245-gaf169e805 (2022-05-14-14:24)</span>
<span class="go">Licensed under GNU GPL v2</span>
<span class="go">For bug reports, read</span>
<span class="go">        http://openocd.org/doc/doxygen/bugs.html</span>
<span class="go">DEPRECATED! use 'adapter speed' not 'adapter_khz'</span>
<span class="go">exit_debug_mode</span>
<span class="go">Info : Using CMSIS-DAPv2 interface with VID:PID=0x0d28:0x0204, serial=01100E003602002e00354146570120313238</span>
<span class="go">Info : CMSIS-DAP: SWD  Supported</span>
<span class="go">Info : CMSIS-DAP: FW Version = 2.1.0</span>
<span class="go">Info : CMSIS-DAP: Serial# = 01100E003602002e00354146570120313238</span>
<span class="go">Info : CMSIS-DAP: Interface Initialised (SWD)</span>
<span class="go">Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1</span>
<span class="go">Info : CMSIS-DAP: Interface ready</span>
<span class="go">Info : clock speed 10000 kHz</span>
<span class="go">Info : SWD DPIDR 0x2ba01477</span>
<span class="go">Info : nrf52.cpu: hardware has 6 breakpoints, 4 watchpoints</span>
<span class="go">Info : starting gdb server for nrf52.cpu on 3333</span>
<span class="go">Info : Listening on port 3333 for gdb connections</span>
<span class="go">    TargetName         Type       Endian TapName            State</span>
<span class="go">--  ------------------ ---------- ------ ------------------ ------------</span>
<span class="go"> 0* nrf52.cpu          cortex_m   little nrf52.cpu          running</span>

<span class="go">target halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x0000243c msp: 0x20001838</span>
<span class="go">Info : nRF52840-CKAA(build code: D0) 1024kB Flash, 256kB RAM</span>
<span class="go">Warn : Adding extra erase range, 0x00007a24 .. 0x00007fff</span>
<span class="go">auto erase enabled</span>
<span class="go">wrote 31268 bytes from file @/udk-sdk/zephyr/zephyr.hex in     1.151423s             (26.519 KiB/s)</span>

<span class="go">target halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x0000243c msp: 0x20001838</span>
<span class="go">verified 31268 bytes in 0.092640s (329.611 KiB/s)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>TEST_BUTTONSの例題をそれぞれC、B、Aのボタンを押して実行したときの出力例。</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>***<span class="w"> </span>Booting<span class="w"> </span>Zephyr<span class="w"> </span>OS<span class="w"> </span>build<span class="w"> </span>5db7528340ec<span class="w">  </span>***
PRESS<span class="w"> </span>BUTTON<span class="w"> </span>EXAMPLE
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">24778</span>
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">28996</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">76012</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">81454</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">104172</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">109917</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-25" name="sd-tab-set-9" type="radio">
<label class="sd-tab-label" data-sync-id="key2" for="sd-tab-item-25">
macOS</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p><a class="reference internal" href="#devicesetup"><span class="std std-ref">デバイスのセットアップ</span></a> ガイドラインを完成させてください。</p></li>
<li><p>サンプルディレクトリに移動します</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>(オプション) 古いビルドディレクトリを掃除する。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rm -rf build/</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>サンプルをビルドする</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-29" name="sd-tab-set-11" type="radio">
<label class="sd-tab-label" for="sd-tab-item-29">
選択メニュー付き</label><div class="sd-tab-content docutils">
<p>このセクションは、1つの期待される例を選択して、例を構築する方法をガイドします。</p>
<ol class="arabic">
<li><p>BOARDがleaps_lc14またはleaps_lc13の場合、メニューを表示するには以下のコマンドを実行してください</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p><strong>サンプルアプリケーション</strong> を選択してEnterを押してください。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/ja/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</div></blockquote>
</li>
<li><p>デフォルトの <strong>サンプル</strong> が表示されます。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/ja/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>上下にスクロールして <strong>サンプル</strong> を選択し、Enterを押してください。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/ja/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>ESC と Y を押して選択を保存してください。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/ja/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
</li>
<li><p>サンプルをビルドする</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>サンプルのビルドに成功しました。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[169/179] Linking C executable zephyr/zephyr_pre0.elf</span>

<span class="go">[173/179] Linking C executable zephyr/zephyr_pre1.elf</span>

<span class="go">[179/179] Linking C executable zephyr/zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       31268 B         1 MB      2.98%</span>
<span class="go">            SRAM:        8568 B       256 KB      3.27%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div>
<input id="sd-tab-item-30" name="sd-tab-set-11" type="radio">
<label class="sd-tab-label" for="sd-tab-item-30">
選択メニューなし</label><div class="sd-tab-content docutils">
<p>このセクションはデフォルトのサンプルを使ってサンプルをビルドする方法を説明します。</p>
<ol class="arabic">
<li><p>$BOARD が leaps_lc14 または leaps_lc13 の場合、以下のコマンドを実行してください。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>サンプルのビルドに成功しました。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[169/179] Linking C executable zephyr/zephyr_pre0.elf</span>

<span class="go">[173/179] Linking C executable zephyr/zephyr_pre1.elf</span>

<span class="go">[179/179] Linking C executable zephyr/zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       31268 B         1 MB      2.98%</span>
<span class="go">            SRAM:        8568 B       256 KB      3.27%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div>
</div>
</div></blockquote>
</li>
<li><p>そしてデバイスに16進ファイルを再フラッシュしてください：</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>ファームウェアの再フラッシュに成功しました。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">Open On-Chip Debugger 0.11.0+dev-00245-gaf169e805 (2022-05-14-14:24)</span>
<span class="go">Licensed under GNU GPL v2</span>
<span class="go">For bug reports, read</span>
<span class="go">        http://openocd.org/doc/doxygen/bugs.html</span>
<span class="go">DEPRECATED! use 'adapter speed' not 'adapter_khz'</span>
<span class="go">exit_debug_mode</span>
<span class="go">Info : Using CMSIS-DAPv2 interface with VID:PID=0x0d28:0x0204, serial=01100E003602002e00354146570120313238</span>
<span class="go">Info : CMSIS-DAP: SWD  Supported</span>
<span class="go">Info : CMSIS-DAP: FW Version = 2.1.0</span>
<span class="go">Info : CMSIS-DAP: Serial# = 01100E003602002e00354146570120313238</span>
<span class="go">Info : CMSIS-DAP: Interface Initialised (SWD)</span>
<span class="go">Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1</span>
<span class="go">Info : CMSIS-DAP: Interface ready</span>
<span class="go">Info : clock speed 10000 kHz</span>
<span class="go">Info : SWD DPIDR 0x2ba01477</span>
<span class="go">Info : nrf52.cpu: hardware has 6 breakpoints, 4 watchpoints</span>
<span class="go">Info : starting gdb server for nrf52.cpu on 3333</span>
<span class="go">Info : Listening on port 3333 for gdb connections</span>
<span class="go">    TargetName         Type       Endian TapName            State</span>
<span class="go">--  ------------------ ---------- ------ ------------------ ------------</span>
<span class="go"> 0* nrf52.cpu          cortex_m   little nrf52.cpu          running</span>

<span class="go">target halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x0000243c msp: 0x20001838</span>
<span class="go">Info : nRF52840-CKAA(build code: D0) 1024kB Flash, 256kB RAM</span>
<span class="go">Warn : Adding extra erase range, 0x00007a24 .. 0x00007fff</span>
<span class="go">auto erase enabled</span>
<span class="go">wrote 31268 bytes from file @/udk-sdk/zephyr/zephyr.hex in     1.151423s             (26.519 KiB/s)</span>

<span class="go">target halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x0000243c msp: 0x20001838</span>
<span class="go">verified 31268 bytes in 0.092640s (329.611 KiB/s)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>TEST_BUTTONSの例題をそれぞれC、B、Aのボタンを押して実行したときの出力例。</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>***<span class="w"> </span>Booting<span class="w"> </span>Zephyr<span class="w"> </span>OS<span class="w"> </span>build<span class="w"> </span>5db7528340ec<span class="w">  </span>***
PRESS<span class="w"> </span>BUTTON<span class="w"> </span>EXAMPLE
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">24778</span>
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">28996</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">76012</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">81454</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">104172</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">109917</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div></blockquote>
</div>
<input id="sd-tab-item-26" name="sd-tab-set-9" type="radio">
<label class="sd-tab-label" data-sync-id="key3" for="sd-tab-item-26">
Windows</label><div class="sd-tab-content docutils">
<blockquote>
<div><ol class="arabic">
<li><p><a class="reference internal" href="#devicesetup"><span class="std std-ref">デバイスのセットアップ</span></a> ガイドラインを完成させてください。</p></li>
<li><p>サンプルディレクトリに移動します</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps-udk-examples</span>
</pre></div>
</div>
</li>
<li><p>(オプション) 古いビルドディレクトリを削除してYを押してください。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">rd /s build</span>
</pre></div>
</div>
</li>
<li><p>サンプルをビルドする</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-31" name="sd-tab-set-12" type="radio">
<label class="sd-tab-label" for="sd-tab-item-31">
選択メニュー付き</label><div class="sd-tab-content docutils">
<p>このセクションは、予想される例を1つ選択して、例を構築する方法をガイドします。</p>
<ol class="arabic simple">
<li><p>BOARDがleaps_lc14またはleaps_lc13の場合、メニューを表示するには以下のコマンドを実行してください</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -t menuconfig -b $BOARD -s app</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple">
<li><p><strong>サンプルアプリケーション</strong> を選択してEnterを押してください。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/main_menu.png"><img alt="../../../_images/main_menu.png" class="align-center" src="/docs-assets/ja/_images/main_menu.png" style="width: 758.5px; height: 396.0px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>デフォルトの <strong>サンプル</strong> が表示されます。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_default_example.png"><img alt="../../../_images/menu_default_example.png" class="align-center" src="/docs-assets/ja/_images/menu_default_example.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>上下にスクロールして <strong>サンプル</strong> を選択し、Enterを押してください。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_example_list.png"><img alt="../../../_images/menu_example_list.png" class="align-center" src="/docs-assets/ja/_images/menu_example_list.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>ESC と Y を押して選択を保存してください。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/menu_exit_andsave.png"><img alt="../../../_images/menu_exit_andsave.png" class="align-center" src="/docs-assets/ja/_images/menu_exit_andsave.png" style="width: 688.5px; height: 385.5px;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>サンプルをビルドする</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple">
<li><p>サンプルのビルドに成功しました。</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[152/158] Linking C executable zephyr\zephyr_pre1.elf←[K1.dir/dev_handles.c.obj←[Kj←[K</span>

<span class="go">[158/158] Linking C executable zephyr\zephyr.elf←[Kr_final.dir/dev_handles.c.obj←[Kj←[K</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       32668 B         1 MB      3.12%</span>
<span class="go">            SRAM:        4496 B       248 KB      1.77%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</div></blockquote>
</div>
<input id="sd-tab-item-32" name="sd-tab-set-12" type="radio">
<label class="sd-tab-label" for="sd-tab-item-32">
選択メニューなし</label><div class="sd-tab-content docutils">
<p>このセクションはデフォルトのサンプルを使ってサンプルをビルドする方法を説明します。</p>
<ol class="arabic">
<li><p>$BOARD が leaps_lc14 または leaps_lc13 の場合、以下のコマンドを実行してください。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west build -b $BOARD -s app</span>
</pre></div>
</div>
</li>
<li><p>サンプルのビルドに成功しました。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">[1/161] Generating include/generated/version.h</span>
<span class="go">-- Zephyr version: 3.1.0 (@/udk-sdk/zephyr), build: zephyr-v3.1.0</span>
<span class="go">[151/161] Linking C executable zephyr\zephyr_pre0.elf</span>

<span class="go">[155/161] Linking C executable zephyr\zephyr_pre1.elf</span>

<span class="go">[161/161] Linking C executable zephyr\zephyr.elf</span>
<span class="go">Memory region         Used Size  Region Size  %age Used</span>
<span class="go">           FLASH:       91160 B         1 MB      8.69%</span>
<span class="go">            SRAM:        5056 B       248 KB      1.99%</span>
<span class="go">        IDT_LIST:          0 GB         2 KB      0.00%</span>
</pre></div>
</div>
</li>
</ol>
</div>
</div>
</li>
<li><p>そしてデバイスに16進ファイルを再フラッシュしてください：</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">west flash</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>ファームウェアの再フラッシュに成功しました。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">-- west flash: rebuilding</span>
<span class="go">ninja: no work to do.</span>
<span class="go">-- west flash: using runner openocd</span>
<span class="go">-- runners.openocd: Flashing file: D:/01_Work/udk-sdk/udk-sdk/leaps-udk-examples/build/zephyr/zephyr.hex</span>
<span class="go">xPack Open On-Chip Debugger 0.12.0-01004-g9ea7f3d64-dirty (2023-01-30-15:04)</span>
<span class="go">Licensed under GNU GPL v2</span>
<span class="go">For bug reports, read</span>
<span class="go">        http://openocd.org/doc/doxygen/bugs.html</span>
<span class="go">DEPRECATED! use 'adapter speed' not 'adapter_khz'</span>
<span class="go">exit_debug_mode</span>
<span class="go">Info : Using CMSIS-DAPv2 interface with VID:PID=0x0d28:0x0204, serial=01100E003602002d00184146570120313238</span>
<span class="go">Info : CMSIS-DAP: SWD supported</span>
<span class="go">Info : CMSIS-DAP: Atomic commands supported</span>
<span class="go">Info : CMSIS-DAP: Test domain timer supported</span>
<span class="go">Info : CMSIS-DAP: FW Version = 2.1.0</span>
<span class="go">Info : CMSIS-DAP: Serial# = 01100E003602002d00184146570120313238</span>
<span class="go">Info : CMSIS-DAP: Interface Initialised (SWD)</span>
<span class="go">Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1</span>
<span class="go">Info : CMSIS-DAP: Interface ready</span>
<span class="go">Info : clock speed 10000 kHz</span>
<span class="go">Info : SWD DPIDR 0x2ba01477</span>
<span class="go">Info : [nrf52.cpu] Cortex-M4 r0p1 processor detected</span>
<span class="go">Info : [nrf52.cpu] target has 6 breakpoints, 4 watchpoints</span>
<span class="go">Info : starting gdb server for nrf52.cpu on 3333</span>
<span class="go">Info : Listening on port 3333 for gdb connections</span>
<span class="go">    TargetName         Type       Endian TapName            State</span>
<span class="go">--  ------------------ ---------- ------ ------------------ ------------</span>
<span class="go"> 0* nrf52.cpu          cortex_m   little nrf52.cpu          running</span>

<span class="go">[nrf52.cpu] halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x00002e10 msp: 0x20002b10</span>
<span class="go">Info : nRF52840-CKAA(build code: D0) 1024kB Flash, 256kB RAM</span>
<span class="go">Warn : Adding extra erase range, 0x00007f9c .. 0x00007fff</span>
<span class="go">auto erase enabled</span>
<span class="go">wrote 32668 bytes from file D:/01_Work/udk-sdk/udk-sdk/leaps-udk-examples/build/zephyr/zephyr.hex in 1.178412s (27.072 KiB/s)</span>

<span class="go">[nrf52.cpu] halted due to debug-request, current mode: Thread</span>
<span class="go">xPSR: 0x01000000 pc: 0x00002a5c msp: 0x20002850</span>
<span class="go">verified 32668 bytes in 0.099523s (320.552 KiB/s)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>TEST_BUTTONSの例題をそれぞれC、B、Aのボタンを押して実行したときの出力例。</p>
<blockquote>
<div><div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>***<span class="w"> </span>Booting<span class="w"> </span>Zephyr<span class="w"> </span>OS<span class="w"> </span>build<span class="w"> </span>5db7528340ec<span class="w">  </span>***
PRESS<span class="w"> </span>BUTTON<span class="w"> </span>EXAMPLE
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">24778</span>
Button<span class="w"> </span>C<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">28996</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">76012</span>
Button<span class="w"> </span>B<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">81454</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>pressed<span class="w"> </span>at<span class="w"> </span><span class="m">104172</span>
Button<span class="w"> </span>A<span class="w"> </span>is<span class="w"> </span>released<span class="w"> </span>at<span class="w"> </span><span class="m">109917</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
</div></blockquote>
</div>
</div>
</div>
</div>


           </div>
