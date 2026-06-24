---
title: "TLV API"
lang: ja
slug: "pans-pro-rtls/integration-guide/tlv-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/tlv-api/"
order: 121
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="tlv-api">
<h1>TLV API</h1>
<p>TLV (Type-Length-Value) 形式は、DWM モジュール API で使用されます。TLV 形式のデータは常に、タイプ バイトで始まり、長さバイトが続き、長さバイトで指定された可変数の値バイト (0 ～ 253 の範囲) が続きます。表 1 は、TLV 形式のデータの例を示しています。タイプ バイトは 0x28、長さバイトは 0x02 で、長さバイトで宣言されているように、値フィールドは 0x0D と 0x01 の 2 つのバイトで構成されます。</p>
<p>DWM1001 ファームウェアでは、SPI と UART API の両方がデータ転送用の TLV 形式。タイプ バイトの意味を理解するには、TLV タイプ リストを参照する必要があります。特定のコマンドまたは応答ごとに、対応する情報を提供するために値フィールドの長さが異なります。</p>
<p><strong>TLV 形式のデータの例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 63%">
<col style="width: 11%">
<col style="width: 13%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p><strong>ピン指数</strong></p></td>
<td><p><strong>引脚值</strong></p></td>
</tr>
<tr class="row-even"><td><p>0x28</p></td>
<td><p>0x02</p></td>
<td><p>0x0D</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>各 API の詳細情報については、次のページを参照してください。</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information">一般的な API 情報</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-command-list">API コマンドリスト</a></li>
</ul>
</div>
</div>


           </div>
