---
title: "システム要件"
lang: ja
slug: "udk/development-guide/system-requirements"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/development-guide/system-requirements/"
order: 44
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="anchor-dev-sr"></span><h1>システム要件</h1>
<p>以下のセクションでは、UDK デバイスで SDK を使用する前に必要なソフトウェアとハードウェアについて詳しく説明します。</p>
<hr class="docutils">
<div class="section" id="hardware-software">
<h2>ハードウェアとソフトウェア</h2>
<p>開発段階に入る前に、以下のソフトウェア ツールをインストールしてください：</p>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 80%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>アイテム</p></th>
<th class="head"><p>アイテム バージョン</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.14.2">Zephyr SDK</a></p></td>
<td><p>0.14.2</p></td>
<td><p>必須。RTOS には、UDK デバイスに対応した BSP パッケージが含まれています。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference external" href="https://openocd.org/pages/getting-openocd.html">OpenOCD</a></p></td>
<td><p>--</p></td>
<td><p>システムのファームウェアアップグレード、デバッグ、プログラミングを提供することを目的とする。詳しいインストール方法は <a class="reference internal" href="/docs/ja/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">ファームウェアのプログラミング/アップグレード</span></a> のセクションを参照。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference external" href="https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack">SEGGER J-Link</a></p></td>
<td><p>--</p></td>
<td><p>システムのファームウェアアップグレード、デバッグ、プログラミングを提供することを目的とする。詳細なインストール方法については、 <a class="reference internal" href="/docs/ja/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">ファームウェアのプログラミング/アップグレード</span></a> のセクションを参照してください。</p></td>
</tr>
<tr class="row-odd"><td><p>デスクトップデバイス</p></td>
<td><p>--</p></td>
<td><p>必須、推奨：ガイドラインに沿ったLinux環境をサポートする。</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="environment-setup">
<h2>環境セットアップ</h2>
<a class="reference internal image-reference" href="../../../_images/development_tools.png"><img alt="../../../_images/development_tools.png" class="align-right" src="/docs-assets/ja/_images/development_tools.png" style="width: 339.25px; height: 203.75px;"></a>
<p>各デバイスにはUSB DAPLinkが搭載されており、ターゲットマイコンのシームレスなプログラミングやデバッグが可能です。</p>
<p>ボードにファームウェアをプログラムするには、USB DAPLinkをPCに接続する必要があります。</p>
<p>下図は、ファームウェアのプログラミングに必要な絶縁接続を示しています。</p>
</div>
</div>


           </div>
