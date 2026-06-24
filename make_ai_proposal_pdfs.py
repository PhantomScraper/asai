# -*- coding: utf-8 -*-
"""Generate AI adoption proposal PDFs (Vietnamese + English), v0.2."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as canvas_mod
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, HRFlowable, Flowable)

FD = "/System/Library/Fonts/Supplemental"
pdfmetrics.registerFont(TTFont("Arial", os.path.join(FD, "Arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold", os.path.join(FD, "Arial Bold.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic", os.path.join(FD, "Arial Italic.ttf")))
pdfmetrics.registerFont(TTFont("Arial-BoldItalic", os.path.join(FD, "Arial Bold Italic.ttf")))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold",
                              italic="Arial-Italic", boldItalic="Arial-BoldItalic")

NAVY = colors.HexColor("#1a3a5c")
BLUE = colors.HexColor("#2c6fad")
LIGHT = colors.HexColor("#eef3f8")
GREY = colors.HexColor("#666666")
LINE = colors.HexColor("#c5d3e0")

S = {}
S["title"] = ParagraphStyle("title", fontName="Arial-Bold", fontSize=20, leading=25,
                            textColor=NAVY, spaceAfter=4)
S["subtitle"] = ParagraphStyle("subtitle", fontName="Arial", fontSize=11, leading=15,
                               textColor=GREY, spaceAfter=8)
S["h1"] = ParagraphStyle("h1", fontName="Arial-Bold", fontSize=14, leading=18,
                         textColor=NAVY, spaceBefore=16, spaceAfter=6)
S["h2"] = ParagraphStyle("h2", fontName="Arial-Bold", fontSize=11.5, leading=15,
                         textColor=BLUE, spaceBefore=10, spaceAfter=4)
S["p"] = ParagraphStyle("p", fontName="Arial", fontSize=9.5, leading=14,
                        spaceAfter=6, alignment=TA_LEFT)
S["li"] = ParagraphStyle("li", parent=S["p"], leftIndent=14, bulletIndent=4, spaceAfter=3)
S["cell"] = ParagraphStyle("cell", fontName="Arial", fontSize=8.5, leading=11.5)
S["cellb"] = ParagraphStyle("cellb", parent=S["cell"], fontName="Arial-Bold")
S["cellh"] = ParagraphStyle("cellh", parent=S["cell"], fontName="Arial-Bold",
                            textColor=colors.white)
S["src"] = ParagraphStyle("src", fontName="Arial", fontSize=7.5, leading=10.5,
                          textColor=GREY, spaceAfter=1, leftIndent=10)
S["note"] = ParagraphStyle("note", parent=S["p"], fontName="Arial-Italic",
                           fontSize=8.5, textColor=GREY)

PAGE_W, PAGE_H = A4
MARG = 2 * cm
CONTENT_W = PAGE_W - 2 * MARG


def LK(url, label=None):
    """Clickable link markup."""
    return f"<link href='{url}'><font color='#2c6fad'>{label or url}</font></link>"


def clean(t):
    """No em/en dashes in document text."""
    return t.replace("—", "-").replace("–", "-")


def make_table(headers, rows, widths=None):
    data = [[Paragraph(clean(h), S["cellh"]) for h in headers]]
    for r in rows:
        row = []
        for j, c in enumerate(r):
            st = S["cellb"] if j == 0 else S["cell"]
            row.append(Paragraph(clean(c), st))
        data.append(row)
    if widths:
        widths = [w * CONTENT_W for w in widths]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ]))
    return t


class ArchDiagram(Flowable):
    """Horizontal box-and-arrow architecture diagram."""

    def __init__(self, boxes, width=CONTENT_W, height=1.9 * cm):
        super().__init__()
        self.boxes = boxes
        self.width = width
        self.height = height

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        n = len(self.boxes)
        gap = 0.55 * cm
        bw = (self.width - gap * (n - 1)) / n
        bh = self.height - 0.2 * cm
        y = 0.1 * cm
        for i, (title, subs) in enumerate(self.boxes):
            x = i * (bw + gap)
            c.setFillColor(LIGHT)
            c.setStrokeColor(NAVY)
            c.setLineWidth(1)
            c.roundRect(x, y, bw, bh, 4, stroke=1, fill=1)
            c.setFillColor(NAVY)
            c.setFont("Arial-Bold", 8.5)
            cy = y + bh / 2 + (4 if subs else -3)
            c.drawCentredString(x + bw / 2, cy, title)
            c.setFont("Arial", 6.6)
            c.setFillColor(GREY)
            for j, sub in enumerate(subs):
                c.drawCentredString(x + bw / 2, cy - 11 - j * 8, sub)
            if i < n - 1:
                ax0 = x + bw + 2
                ax1 = x + bw + gap - 2
                ay = y + bh / 2
                c.setStrokeColor(BLUE)
                c.setLineWidth(1.2)
                c.line(ax0, ay, ax1 - 4, ay)
                c.setFillColor(BLUE)
                p = c.beginPath()
                p.moveTo(ax1, ay)
                p.lineTo(ax1 - 5, ay + 2.6)
                p.lineTo(ax1 - 5, ay - 2.6)
                p.close()
                c.drawPath(p, stroke=0, fill=1)


class BarChart(Flowable):
    """Horizontal bar chart with labels and values."""

    def __init__(self, items, width=CONTENT_W, bar_h=0.42 * cm, gap=0.28 * cm, max_val=100.0):
        super().__init__()
        self.items = items
        self.width = width
        self.bar_h = bar_h
        self.gap = gap
        self.max_val = max_val
        self.height = len(items) * (bar_h + gap) + 0.2 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        label_w = 5.6 * cm
        area_w = self.width - label_w - 1.4 * cm
        y = self.height - 0.2 * cm
        for i, (name, sub, val) in enumerate(self.items):
            y -= self.bar_h + self.gap
            cy = y + self.bar_h / 2
            c.setFillColor(NAVY)
            c.setFont("Arial-Bold", 8)
            c.drawRightString(label_w - 8, cy + 1.5, name)
            c.setFillColor(GREY)
            c.setFont("Arial", 6.5)
            c.drawRightString(label_w - 8, cy - 6.5, sub)
            bw = area_w * val / self.max_val
            c.setFillColor(BLUE if i % 2 == 0 else NAVY)
            c.roundRect(label_w, y, bw, self.bar_h, 2, stroke=0, fill=1)
            c.setFillColor(NAVY)
            c.setFont("Arial-Bold", 8)
            c.drawString(label_w + bw + 5, cy - 2.5, f"{val:.1f}")


class DocCanvas(canvas_mod.Canvas):
    """Canvas with page-number-only footer."""
    page_label = "Trang {page}/{total}"

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            self.setFont("Arial", 8)
            self.setFillColor(GREY)
            self.drawCentredString(PAGE_W / 2, 1.05 * cm,
                                   self.page_label.format(page=self._pageNumber, total=total))
            self.setFillColor(NAVY)
            self.rect(0, PAGE_H - 0.45 * cm, PAGE_W, 0.45 * cm, stroke=0, fill=1)
            super().showPage()
        super().save()


def build_pdf(filename, story, page_label, title):
    doc = BaseDocTemplate(filename, pagesize=A4,
                          leftMargin=MARG, rightMargin=MARG,
                          topMargin=1.6 * cm, bottomMargin=1.7 * cm, title=title)
    frame = Frame(MARG, 1.7 * cm, CONTENT_W, PAGE_H - 1.6 * cm - 1.7 * cm, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame])])

    class C(DocCanvas):
        pass
    C.page_label = page_label
    doc.build(story, canvasmaker=C)


def H1(s, txt): s.append(Paragraph(clean(txt), S["h1"]))
def H2(s, txt): s.append(Paragraph(clean(txt), S["h2"]))
def P(s, txt): s.append(Paragraph(clean(txt), S["p"]))
def NOTE(s, txt): s.append(Paragraph(clean(txt), S["note"]))
def UL(s, items):
    for it in items:
        s.append(Paragraph(clean(it), S["li"], bulletText="•"))
    s.append(Spacer(1, 4))
def SRC(s, label, urls):
    s.append(Paragraph(f"<b>{clean(label)}</b>", S["src"]))
    for u in urls:
        s.append(Paragraph("- " + LK(u), S["src"]))
    s.append(Spacer(1, 6))


# URLs
U_NV5090 = "https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/"
U_NVPRO6000 = "https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/"
U_RUNPOD = "https://www.runpod.io/articles/guides/nvidia-rtx-5090"
U_BIZON = "https://bizon-tech.com/blog/best-gpu-llm-training-inference"
U_APPLE = "https://www.apple.com/mac-studio/specs/"
U_M3LLM = "https://medium.com/@billynewport/apples-m3-ultra-mac-studio-misses-the-mark-for-llm-inference-f57f1f10a56f"
U_OWUI = "https://docs.openwebui.com/"
U_VLLM = "https://docs.vllm.ai/en/latest/deployment/frameworks/open-webui/"
U_LITELLM = "https://docs.litellm.ai/"
U_TAILSCALE = "https://tailscale.com/pricing"
U_WIREGUARD = "https://www.wireguard.com/"
U_BENCHLM = "https://benchlm.ai/blog/posts/best-open-source-llm"
U_HFBLOG = "https://huggingface.co/blog/daya-shankar/open-source-llms"
U_QWEN3 = "https://huggingface.co/Qwen/Qwen3-32B"
U_QWENCODER = "https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct"
U_DSR1 = "https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"
U_GEMMA = "https://huggingface.co/google/gemma-3-27b-it"
U_OSS20 = "https://huggingface.co/openai/gpt-oss-20b"
U_OSS120 = "https://huggingface.co/openai/gpt-oss-120b"
U_LLAMA = "https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct"
U_GPTPRICE = "https://openai.com/business/chatgpt-pricing/"
U_CLAUDEPRICE = "https://claude.com/pricing"
U_CURSORPRICE = "https://cursor.com/pricing"
U_COPILOT = "https://github.com/features/copilot/plans"
U_CLAUDELIMIT = "https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work"
U_GPTLIMIT = "https://help.openai.com/en/articles/11909943"
U_GPTBIZLIMIT = "https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits"
U_CURSORBLOG = "https://cursor.com/blog/june-2025-pricing"
U_PROMPT_A = "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview"
U_PROMPT_O = "https://platform.openai.com/docs/guides/prompt-engineering"
U_PROMPT_G = "https://www.promptingguide.ai/"
U_UWB1 = "https://www.strategicmarketresearch.com/market-report/ultrawideband-rtls-market"
U_UWB2 = "https://www.marketsandmarkets.com/PressReleases/ultra-wideband.asp"
U_FIRA = "https://www.firaconsortium.org/"
U_UWBA = "https://uwballiance.org/"
U_OMLOX = "https://omlox.com/"
U_RFIDJ = "https://www.rfidjournal.com/"
U_EVRF = "https://www.everythingrf.com/news"
U_NXP = "https://www.nxp.com/company/about-nxp/newsroom:NEWSROOM"
U_QORVO = "https://www.qorvo.com/newsroom"
U_SEWIO = "https://www.sewio.net/blog/"
U_MNM_UWB = "https://www.marketsandmarkets.com/Market-Reports/ultra-wideband-market-200905786.html"
U_GVR_UWB = "https://www.grandviewresearch.com/industry-analysis/ultra-wideband-market-report"
U_GNEWS = "https://news.google.com/rss/search?q=UWB+OR+RTLS"
U_FEEDPARSER = "https://feedparser.readthedocs.io/"
U_BSOUP = "https://www.crummy.com/software/BeautifulSoup/"
U_N8N = "https://n8n.io/"
U_SWEBENCH = "https://www.swebench.com/"
U_AIDER = "https://aider.chat/docs/leaderboards/"
U_LIVECODE = "https://livecodebench.github.io/leaderboard.html"
U_EVALPLUS = "https://evalplus.github.io/leaderboard.html"
U_LMARENA = "https://lmarena.ai/leaderboard"
U_LEAPSDOCS = "https://docs.leapslabs.com/"
U_LLAMAINDEX = "https://docs.llamaindex.ai/"
U_LANGCHAIN = "https://python.langchain.com/docs/"
U_BENCHSWE = "https://benchlm.ai/benchmarks/sweVerified"


# ============================ VIETNAMESE ============================
def build_vi():
    s = []
    s.append(Paragraph("Đề xuất triển khai AI nội bộ", S["title"]))
    s.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceAfter=10))

    H1(s, "1. Mục đích và yêu cầu")
    P(s, "Tài liệu trả lời các câu hỏi:"
         "<br/>(1) Phương án chạy AI server local với model mã nguồn mở, truy cập qua VPN, kèm cấu hình phần cứng;"
         "<br/>(2) Nếu dùng dịch vụ trả phí thì có những lựa chọn nào và việc dùng chung tài khoản trong team "
         "thực tế ra sao;"
         "<br/>(3) Phương án khác;"
         "<br/>(4) Kế hoạch triển khai và đào tạo.")
    P(s, "<b>Các nhu cầu sử dụng AI đã xác định:</b>")
    UL(s, [
        "Testing, validation và tóm tắt trạng thái (status summary) tự động.",
        "Phân tích vấn đề kỹ thuật (analyze).",
        "Review code, chuẩn hoá coding style, bổ sung comment.",
        "Hỗ trợ khách hàng (customer support).",
        "Thu thập thông tin thị trường định kỳ: UWB, RTLS, xu hướng và nhu cầu theo lĩnh vực.",
    ])

    H1(s, "2. Option 1 — AI server local với model mã nguồn mở")
    P(s, "Phương án bảo mật nhất: toàn bộ dữ liệu (mã nguồn, tài liệu khách hàng) không rời khỏi hạ tầng của công ty. "
         "Nhân viên truy cập qua VPN từ văn phòng hoặc từ xa.")

    H2(s, "2.1. Kiến trúc")
    s.append(Spacer(1, 4))
    s.append(ArchDiagram([
        ("User", ["laptop"]),
        ("VPN", ["WireGuard /", "Tailscale"]),
        ("Open WebUI", ["giao diện chat", "nhiều người dùng"]),
        ("vLLM", ["inference engine"]),
        ("GPU server", ["model mã nguồn mở"]),
    ]))
    NOTE(s, "Hình 1: Kiến trúc truy cập AI server local qua VPN.")
    UL(s, [
        "<b>Hệ điều hành:</b> Ubuntu Server 24.04 LTS + Docker.",
        "<b>Inference engine:</b> vLLM cho môi trường nhiều người dùng đồng thời (PagedAttention, throughput cao); "
        "Ollama chỉ phù hợp thử nghiệm cá nhân.",
        "<b>Giao diện:</b> Open WebUI — mã nguồn mở, nhiều người dùng, phân quyền admin/user, tách riêng hội thoại "
        "từng người, RAG tích hợp (hỏi đáp trên tài liệu nội bộ), hỗ trợ SSO/LDAP.",
        "<b>API gateway (tuỳ chọn):</b> LiteLLM proxy — cấp key ảo cho từng người, đặt hạn mức, gom model local "
        "và cloud về một endpoint.",
        "<b>VPN:</b> Tailscale (gần như không cần cấu hình, miễn phí tới 3 user/100 thiết bị) hoặc WireGuard tự dựng "
        "(miễn phí hoàn toàn).",
    ])
    SRC(s, "Nguồn / tài liệu hướng dẫn:",
        [U_OWUI, U_VLLM, U_LITELLM, U_TAILSCALE, U_WIREGUARD])

    H2(s, "2.2. Model mã nguồn mở tiêu biểu")
    P(s, "Bảng xếp hạng các model mã nguồn mở hàng đầu theo benchmark tổng hợp (Top open source LLMs "
         "ranked by benchmarks, benchlm.ai, 06/2026):")
    s.append(make_table(
        ["Hạng", "Model", "Nhà phát triển", "Điểm tổng (Overall)", "Context"],
        [
            ["1", "DeepSeek V4 Pro (Max)", "DeepSeek", "87", "1M"],
            ["2", "Kimi K2.6", "Moonshot AI", "84", "256K"],
            ["3", "GLM-5 (Reasoning)", "Zhipu AI", "81", "200K"],
            ["4", "GLM-5.1", "Zhipu AI", "83", "203K"],
            ["5", "DeepSeek V4 Pro (High)", "DeepSeek", "83", "1M"],
            ["6", "Qwen3.5 397B (Reasoning)", "Alibaba", "77", "128K"],
            ["7", "DeepSeek V4 Flash (Max)", "DeepSeek", "77", "1M"],
            ["8", "Qwen3.6-27B", "Alibaba", "75", "262K"],
        ],
        widths=[0.1, 0.34, 0.2, 0.21, 0.15]))
    s.append(Spacer(1, 4))
    NOTE(s, "Các model top đầu có quy mô hàng trăm tỷ tham số nên cần hạ tầng GPU lớn; với cấu hình server ở mục "
            "2.3, phù hợp là các bản nhỏ (ví dụ Qwen3.6-27B) hoặc bản distill/quantized của các model trên.")
    P(s, "So sánh nhanh khả năng coding của các model mở (điểm càng cao càng tốt, nguồn: benchlm.ai):")
    s.append(make_table(
        ["Model", "Điểm coding tổng hợp", "LiveCodeBench", "SWE-bench Verified"],
        [
            ["DeepSeek V4 Pro (Max)", "89.8", "93.5", "-"],
            ["Kimi K2.6", "88.7", "89.6", "-"],
            ["DeepSeek V4 Pro (High)", "88.7", "-", "-"],
            ["Qwen3.5 397B (Reasoning)", "86.7", "-", "-"],
            ["GLM-5.1", "84.1", "-", "77.8"],
            ["GLM-5 (Reasoning)", "-", "-", "77.8"],
            ["DeepSeek V4 Flash (Max)", "-", "91.6", "-"],
        ],
        widths=[0.34, 0.24, 0.21, 0.21]))
    s.append(Spacer(1, 4))
    SRC(s, "Tham khảo từ:", [U_BENCHLM, U_HFBLOG])
    SRC(s, "Dẫn chứng so sánh khả năng coding giữa các model (leaderboard cập nhật liên tục, "
           "gồm cả model mở và model thương mại):",
        [U_SWEBENCH, U_AIDER, U_LIVECODE, U_EVALPLUS])

    H2(s, "2.3. Cấu hình phần cứng tham khảo")
    s.append(make_table(
        ["Hạng mục", "Tier A — Khởi điểm", "Tier B — Tầm trung", "Tier C — Phương án Mac"],
        [
            ["GPU", "1× NVIDIA RTX 5090 32 GB GDDR7", "2× RTX 5090 (64 GB tổng) hoặc 1× RTX PRO 6000 Blackwell 96 GB",
             "Apple M3 Ultra, GPU 80 nhân, unified memory"],
            ["CPU", "Ryzen 9 7950X / Core i9 (8+ nhân)", "Threadripper / Xeon W (đủ lane PCIe cho 2 GPU)", "—"],
            ["RAM", "64 GB DDR5", "128–256 GB DDR5 ECC", "256–512 GB unified memory"],
            ["Lưu trữ", "NVMe 2 TB", "NVMe 4 TB (model + dữ liệu RAG)", "2–4 TB SSD"],
            ["Nguồn / khác", "PSU 1000 W", "PSU 1600 W, vỏ máy thoáng khí, UPS", "Tiêu thụ điện rất thấp"],
            ["Model chạy được", "≤ 32B Q4 (Qwen3 32B, Gemma 3 27B, gpt-oss-20b)",
             "70B Q4, gpt-oss-120b, Qwen3 235B-A22B (bản quantized)",
             "Model rất lớn (DeepSeek R1 671B ~17–18 token/giây)"],
            ["Người dùng đồng thời", "~3–5", "~10–20 với vLLM", "1–3 (yếu khi nhiều người dùng đồng thời)"],
            ["Dẫn chứng phần cứng phù hợp model",
             f"RTX 5090 32 GB đủ chạy các model quantized cỡ ~30B: "
             f"{LK(U_RUNPOD, 'runpod.io (RTX 5090 LLM guide)')}",
             f"70B Q4 cần ~40 GB VRAM, 2× RTX 5090 hoặc card 96 GB đáp ứng: "
             f"{LK(U_RUNPOD, 'runpod.io (RTX 5090 LLM guide)')}, {LK(U_BIZON, 'bizon-tech.com (best GPU for LLM)')}",
             f"M3 Ultra 512 GB chạy DeepSeek R1 671B ~17-18 token/giây: "
             f"{LK(U_M3LLM, 'medium.com (M3 Ultra LLM inference)')}, {LK(U_APPLE, 'apple.com/mac-studio/specs')}"],
            ["Chi phí ước tính", "≈ 2.500–3.500 USD", "≈ 7.000–12.000 USD", "≈ 5.600 USD (256 GB) – 9.500 USD (512 GB)"],
        ],
        widths=[0.14, 0.27, 0.31, 0.28]))
    s.append(Spacer(1, 4))
    P(s, "Cơ sở tính toán: model 70B ở FP16 cần ~140 GB VRAM, quantize 4-bit (Q4_K_M) còn ~40 GB — vượt 32 GB "
         "của một card RTX 5090 nên cần 2 GPU hoặc card 96 GB. Mac Studio chạy được model rất lớn nhờ unified memory "
         "nhưng tốc độ xử lý prompt dài (prefill) và khả năng phục vụ đồng thời kém hơn GPU NVIDIA.")
    SRC(s, "Tham khảo từ:",
        [U_NV5090, U_NVPRO6000, U_RUNPOD, U_BIZON, U_APPLE, U_M3LLM])

    H2(s, "2.4. Đánh giá")
    s.append(make_table(
        ["Ưu điểm", "Hạn chế"],
        [
            ["Dữ liệu 100% trong nội bộ; không phí thuê bao theo người dùng; không giới hạn số lượt dùng; "
             "chủ động tuỳ biến (RAG tài liệu nội bộ, fine-tune).",
             "Chất lượng model mở 32B–120B vẫn thấp hơn model thương mại hàng đầu ở tác vụ khó; cần người vận hành "
             "(cập nhật model, backup, giám sát); không tự tìm kiếm web nếu không tích hợp thêm; chi phí đầu tư ban đầu."],
        ],
        widths=[0.5, 0.5]))
    s.append(Spacer(1, 6))

    H1(s, "3. Option 2 — Dịch vụ AI trả phí (theo tháng / theo năm)")
    H2(s, "3.1. Các lựa chọn")
    s.append(make_table(
        ["Dịch vụ", "Giá/người/tháng", "Ghi chú"],
        [
            [f"ChatGPT Business (OpenAI)<br/>{LK(U_GPTPRICE, 'openai.com/chatgpt-pricing')}",
             "25 USD (theo tháng) / 20 USD (theo năm)",
             "Tối thiểu 2 chỗ; workspace riêng; dữ liệu không bị dùng để huấn luyện"],
            [f"Claude Team Standard (Anthropic)<br/>{LK(U_CLAUDEPRICE, 'claude.com/pricing')}",
             "25 USD (theo tháng) / 20 USD (theo năm)",
             "Tối thiểu 5 chỗ; SSO, quản trị tập trung; không huấn luyện trên dữ liệu team"],
            [f"Claude Team Premium<br/>{LK(U_CLAUDEPRICE, 'claude.com/pricing')}",
             "125 USD (theo tháng) / 100 USD (theo năm)",
             "Như Standard + Claude Code (agent lập trình trong terminal/IDE)"],
            [f"Cursor Pro / Teams<br/>{LK(U_CURSORPRICE, 'cursor.com/pricing')}",
             "20 USD (Pro) / 40 USD (Teams)",
             "IDE lập trình có AI; mỗi tháng kèm hạn mức sử dụng model tương ứng giá gói"],
            [f"GitHub Copilot Business<br/>{LK(U_COPILOT, 'github.com/copilot/plans')}",
             "19 USD",
             "Gợi ý code trong IDE; bổ trợ chứ không thay thế chat AI"],
        ],
        widths=[0.3, 0.24, 0.46]))
    s.append(Spacer(1, 4))
    s.append(BarChart([
        ("Claude Fable 5", "Claude Team", 95.0),
        ("GPT-5.5", "ChatGPT Business", 88.7),
        ("Claude Opus 4.8", "Claude Team", 88.6),
        ("Gemini 3.1 Pro", "Google Gemini", 80.6),
    ]))
    NOTE(s, "Hình 2: Khả năng coding của model đứng sau từng dịch vụ - điểm SWE-bench Verified "
            "(% issue GitHub thật được giải đúng), 06/2026. Cursor và Copilot chạy chính các model trên nên khả "
            "năng coding phụ thuộc model được chọn.")
    SRC(s, "Dẫn chứng so sánh khả năng coding của các model thương mại (Claude, GPT, Gemini...) "
           "trên leaderboard độc lập:",
        [U_BENCHSWE, U_SWEBENCH, U_AIDER, U_LMARENA, U_LIVECODE])
    s.append(Spacer(1, 2))

    H2(s, "3.2. Dùng chung tài khoản trong team — được, nhưng chạm giới hạn rất nhanh")
    P(s, "Về kỹ thuật, nhiều người có thể đăng nhập chung một tài khoản, nhưng <b>giới hạn sử dụng tính trên "
         "tài khoản</b> nên sẽ cạn rất nhanh khi dùng chung:")
    UL(s, [
        f"<b>Claude (Pro/Max):</b> giới hạn theo <b>phiên 5 giờ</b> (tính từ prompt đầu tiên) cộng thêm "
        f"<b>giới hạn theo tuần</b>; mọi kênh (web, IDE, Claude Code) trừ chung một quota. Gói Pro chỉ khoảng "
        f"10–45 prompt mỗi phiên 5 giờ tuỳ độ dài. Nguồn: {LK(U_CLAUDELIMIT, 'support.claude.com — How do usage and length limits work')}.",
        f"<b>ChatGPT Plus:</b> khoảng <b>160 tin nhắn GPT-5.5 mỗi 3 giờ</b>; vượt giới hạn thì tự rơi xuống bản mini. "
        f"Nguồn: {LK(U_GPTLIMIT, 'help.openai.com — GPT-5.5 in ChatGPT')}. Gói Business: gần như không giới hạn với "
        f"model cơ bản, nhưng tính theo seat từng người. Nguồn: {LK(U_GPTBIZLIMIT, 'help.openai.com — ChatGPT Business Models & Limits')}.",
        f"<b>Cursor:</b> giới hạn theo <b>tháng</b> — gói Pro 20 USD kèm ~20 USD chi phí model mỗi tháng, "
        f"dùng hết thì dừng (hoặc trả thêm theo nhu cầu nếu bật spend limit). "
        f"Nguồn: {LK(U_CURSORPRICE, 'cursor.com/pricing')}, {LK(U_CURSORBLOG, 'cursor.com/blog/june-2025-pricing')}.",
        "<b>Giới hạn phụ thuộc context/token, không phải số câu hỏi:</b> các nhà cung cấp đo quota theo lượng token "
        "xử lý. Hội thoại dài, đính kèm file lớn, đưa nhiều code vào context sẽ tiêu tốn quota nhanh gấp nhiều lần — "
        "nên càng nhiều người dùng chung một tài khoản thì càng chạm trần sớm.",
        "Ngoài ra, chia sẻ tài khoản cá nhân nằm ngoài phạm vi điều khoản sử dụng của các dịch vụ; "
        "hình thức chính thức cho team là gói Business/Team theo seat.",
    ])

    H1(s, "4. Phương án khác")
    H2(s, "4.1. Thuê GPU cloud")
    P(s, "Thuê GPU theo giờ để chạy chính các model mã nguồn mở ở mục 2. Ưu điểm:")
    UL(s, [
        "Không cần vốn đầu tư ban đầu — trả theo giờ sử dụng thực tế.",
        "Thử được nhiều cấu hình GPU khác nhau trước khi quyết định mua phần cứng.",
        "Nâng/hạ cấu hình linh hoạt theo nhu cầu; có việc nặng thì thuê máy mạnh hơn vài giờ.",
        "Dùng được ngay trong lúc chờ mua máy, không gián đoạn kế hoạch.",
    ])
    H2(s, "4.2. Bảng so sánh các phương án")
    s.append(make_table(
        ["Tiêu chí", "Option 1 — Server local", "Option 2 — Dịch vụ trả phí", "Thuê GPU cloud"],
        [
            ["Bảo mật dữ liệu", "Cao nhất — dữ liệu không rời công ty", "Phụ thuộc nhà cung cấp (có cam kết không train)",
             "Dữ liệu đi qua hạ tầng bên thuê"],
            ["Chất lượng AI", "Khá (model mở 32B–120B)", "Cao nhất (model thương mại mới nhất)", "Như Option 1 (cùng model mở)"],
            ["Chi phí ban đầu", "2.500–12.000 USD tuỳ tier", "0", "0"],
            ["Chi phí hằng tháng", "Điện + bảo trì", "20–125 USD/người tuỳ gói", "Theo giờ sử dụng"],
            ["Giới hạn sử dụng", "Không", "Theo phiên/tuần/tháng tuỳ dịch vụ (mục 3.2)", "Không (trong giờ đã thuê)"],
            ["Tìm kiếm web", "Phải tích hợp thêm", "Có sẵn", "Phải tích hợp thêm"],
            ["Công sức vận hành", "Cần người phụ trách", "Không đáng kể", "Trung bình"],
        ],
        widths=[0.18, 0.28, 0.29, 0.25]))
    s.append(Spacer(1, 6))

    H1(s, "5. Kế hoạch triển khai")
    s.append(make_table(
        ["Thời gian", "Công việc chính", "Kết quả"],
        [
            ["Tuần 1, ngày 1–2", "Chốt phương án và ngân sách; quy định dữ liệu nào được/không được đưa lên cloud; "
             "tạo tài khoản; dựng Open WebUI (+ LiteLLM nếu dùng API) trên máy tạm; cấu hình VPN Tailscale/WireGuard",
             "Cả nhóm bắt đầu dùng được AI qua web nội bộ"],
            ["Tuần 1, ngày 3–5", "Dựng server model mở: cài Ubuntu + Docker + vLLM, tải model (Qwen3 32B, "
             "Qwen2.5-Coder); nếu chưa có phần cứng thì thuê GPU cloud chạy tạm",
             "Model mã nguồn mở hoạt động, truy cập qua VPN"],
            ["Tuần 2", "Tích hợp use case: AI review code trên Git, RAG tài liệu nội bộ, script tóm tắt kết quả test, "
             "agent tổng hợp tin thị trường UWB/RTLS; quay video demo hướng dẫn (mục 6); ban hành quy định sử dụng AI",
             "AI gắn vào quy trình hằng ngày, có tài liệu hướng dẫn"],
        ],
        widths=[0.16, 0.56, 0.28]))
    s.append(Spacer(1, 4))
    NOTE(s, "Nếu phải đặt mua phần cứng, thời gian chờ hàng nằm ngoài 2 tuần này — trong lúc chờ dùng GPU thuê.")

    H1(s, "6. Đào tạo cho nhóm")
    UL(s, [
        "<b>Quay video demo cách setup</b> (5–10 phút/video, quay màn hình): cài và kết nối VPN, đăng nhập "
        "Open WebUI, kết nối agent trong IDE/terminal, cấu hình API key nội bộ — lưu vào drive nội bộ để nhân viên "
        "mới tự setup được bất cứ lúc nào.",
        "<b>Tổng hợp link tài liệu viết prompt</b> gửi cả nhóm:",
    ])
    SRC(s, "Tài liệu hướng dẫn viết prompt:",
        [U_PROMPT_A, U_PROMPT_O, U_PROMPT_G])
    UL(s, [
        "Cheat sheet 1 trang: các mẫu prompt dùng ngay cho công việc của công ty.",
    ])

    H1(s, "7. Ánh xạ nhu cầu sử dụng → giải pháp")
    s.append(make_table(
        ["Nhu cầu", "Giải pháp", "Model/Công cụ"],
        [
            ["Testing, validation, tóm tắt trạng thái", "Script gọi model qua API nội bộ: đọc log test/CI, sinh báo cáo "
             "tóm tắt hằng ngày gửi vào kênh chat", "Qwen3 32B (local) — dữ liệu nội bộ"],
            ["Phân tích vấn đề", "Chat trực tiếp; vấn đề khó dùng model mạnh hơn",
             "Claude/GPT (cloud) hoặc DeepSeek-R1-Distill (local)"],
            ["Review code, coding style, comment", "Tích hợp vào Git: AI review tự động từng merge request; "
             "kỹ sư dùng agent trong terminal/IDE", "Qwen2.5-Coder (local), Claude Code / Cursor (cloud)"],
            ["Hỗ trợ khách hàng", "Chatbot hỏi đáp trên tài liệu docs.leapslabs.com theo mô hình RAG "
             "(chi tiết mục 9)", "Open WebUI Knowledge (local)"],
            ["Theo dõi thị trường UWB/RTLS", "Script crawl tin từ danh sách nguồn cố định; AI chỉ tóm tắt và "
             "phân loại; gửi notification (chi tiết mục 8)", "Script crawl + model local hoặc API"],
            ["Phát triển ứng dụng mới", "Làm thử 1 ứng dụng nhỏ trong 2 tuần bằng AI pair-programming để đánh giá "
             "tốc độ thực tế — bàn riêng để chọn ứng dụng thí điểm", "Claude Code / Cursor + khung dự án chuẩn"],
        ],
        widths=[0.22, 0.48, 0.3]))
    s.append(Spacer(1, 6))

    H1(s, "8. Theo dõi thông tin thị trường UWB/RTLS")
    P(s, "Chúng ta xây script crawl tin từ danh sách website cố định; AI đảm nhận phần <b>tóm tắt và phân loại</b>; "
         "cuối cùng hệ thống gửi thông báo. Quy trình 4 bước:")
    UL(s, [
        "<b>Bước 1 - Chốt danh sách nguồn:</b> các website/RSS ở bảng dưới, có thể thêm bớt theo thời gian.",
        f"<b>Bước 2 - Script crawl tin:</b> Python ({LK(U_FEEDPARSER, 'feedparser')} đọc RSS; "
        f"requests + {LK(U_BSOUP, 'BeautifulSoup')} cho trang không có RSS), chạy cron mỗi ngày, lưu bài mới vào "
        f"database và loại bài trùng. Ai không muốn code có thể dùng {LK(U_N8N, 'n8n')} (no-code, self-host được).",
        "<b>Bước 3 - AI tóm tắt và phân loại:</b> với mỗi bài mới, model tóm tắt 3-5 câu tiếng Việt và gắn nhãn "
        "(UWB / RTLS / chip và phần cứng / đối thủ / báo cáo thị trường / ứng dụng ngành: ô tô, y tế, logistics...), "
        "chấm điểm mức liên quan 1-5 và bỏ qua bài dưới ngưỡng. Tin tức là dữ liệu công khai nên dùng model local "
        "(Qwen3 32B) hay API đều được.",
        "<b>Bước 4 - Notification:</b> bản tin tổng hợp hằng tuần gửi qua email/Slack/Teams; bài điểm liên quan cao "
        "gửi ngay trong ngày.",
    ])
    P(s, "<b>Danh sách website nguồn đề xuất:</b>")
    s.append(make_table(
        ["Nguồn", "Nội dung chính"],
        [
            [f"FiRa Consortium<br/>{LK(U_FIRA, 'firaconsortium.org')}",
             "Tổ chức chuẩn hoá UWB: tin chứng nhận, thành viên mới, use case chuẩn"],
            [f"UWB Alliance<br/>{LK(U_UWBA, 'uwballiance.org')}",
             "Hệ sinh thái UWB, vận động chính sách tần số"],
            [f"omlox<br/>{LK(U_OMLOX, 'omlox.com')}",
             "Chuẩn định vị mở cho công nghiệp (UWB là công nghệ lõi)"],
            [f"RFID Journal<br/>{LK(U_RFIDJ, 'rfidjournal.com')}",
             "Tin RTLS, định vị tài sản, case study triển khai thực tế trong kho vận, y tế, sản xuất"],
            [f"everything RF<br/>{LK(U_EVRF, 'everythingrf.com/news')}",
             "Tin chip/module RF và UWB mới ra mắt"],
            [f"NXP Newsroom<br/>{LK(U_NXP, 'nxp.com (newsroom)')}",
             "Chip UWB Trimension, hợp tác với ngành ô tô và điện thoại"],
            [f"Qorvo Newsroom<br/>{LK(U_QORVO, 'qorvo.com/newsroom')}",
             "Dòng chip UWB DW3000 (gốc Decawave) và tin ngành"],
            [f"Sewio Blog<br/>{LK(U_SEWIO, 'sewio.net/blog')}",
             "RTLS UWB trong nhà máy; bài so sánh công nghệ định vị (theo dõi đối thủ)"],
            [f"MarketsandMarkets / Grand View Research<br/>{LK(U_MNM_UWB, 'marketsandmarkets.com (UWB report)')}, "
             f"{LK(U_GVR_UWB, 'grandviewresearch.com (UWB report)')}",
             "Báo cáo quy mô và dự báo thị trường UWB cập nhật định kỳ"],
            [f"Google News RSS<br/>{LK(U_GNEWS, 'news.google.com/rss/search?q=UWB+OR+RTLS')}",
             "Quét rộng theo từ khoá, miễn phí, dễ thêm từ khoá mới (ví dụ: tên đối thủ, tên ngành)"],
        ],
        widths=[0.4, 0.6]))
    s.append(Spacer(1, 6))

    H1(s, "9. Hỗ trợ khách hàng: chatbot hỏi đáp trên tài liệu docs.leapslabs.com")
    P(s, f"Xây chatbot cho phép người dùng hỏi đáp trực tiếp, với toàn bộ kiến thức lấy từ "
         f"{LK(U_LEAPSDOCS, 'docs.leapslabs.com')}. Chatbot hoạt động theo mô hình <b>RAG</b> "
         f"(Retrieval-Augmented Generation): chỉ trả lời dựa trên nội dung tài liệu, kèm link trích dẫn tới trang "
         f"docs liên quan; nếu không tìm thấy trong tài liệu thì trả lời 'không có trong tài liệu' thay vì bịa.")
    P(s, "<b>Cách làm (pipeline):</b>")
    UL(s, [
        f"<b>Bước 1 - Ingest tài liệu:</b> script tải toàn bộ trang {LK(U_LEAPSDOCS, 'docs.leapslabs.com')} "
        f"(theo sitemap), chuyển sang markdown và chia nhỏ theo đoạn (chunking); chạy lại tự động hằng tuần bằng "
        f"cron để cập nhật khi docs thay đổi.",
        "<b>Bước 2 - Đánh index:</b> tạo embedding cho từng đoạn và lưu vào vector database. Open WebUI có sẵn "
        "tính năng Knowledge (RAG built-in) nên không phải tự dựng.",
        "<b>Bước 3 - Hỏi đáp:</b> khi user đặt câu hỏi, hệ thống tìm các đoạn docs liên quan nhất, đưa vào context "
        "và model trả lời kèm link nguồn.",
        "<b>Bước 4 - Triển khai 2 giai đoạn:</b> (a) dùng nội bộ trước: team support dùng chatbot để soạn câu trả "
        "lời cho khách (người duyệt trước khi gửi); (b) khi chất lượng đã ổn định, nhúng widget chat công khai lên "
        "website/docs cho khách tự hỏi đáp, câu khó tự động chuyển sang người phụ trách.",
        "Log lại toàn bộ câu hỏi của khách: vừa đo chất lượng trả lời, vừa biết phần docs nào thiếu để bổ sung.",
        "Nội dung docs là công khai nên dùng model local (Qwen3 32B) hay API đều được; chạy local thì không tốn "
        "phí theo lượt hỏi.",
    ])
    SRC(s, "Công cụ / framework dựng RAG chatbot:",
        [U_OWUI, U_LLAMAINDEX, U_LANGCHAIN])

    H1(s, "10. Rủi ro và biện pháp")
    s.append(make_table(
        ["Rủi ro", "Biện pháp"],
        [
            ["Lộ dữ liệu nhạy cảm lên dịch vụ cloud", "Quy định phân loại dữ liệu; dữ liệu mật chỉ dùng model local"],
            ["AI trả lời sai (hallucination)", "Người duyệt trước khi gửi khách hàng; yêu cầu AI trích nguồn"],
            ["Chi phí vượt kiểm soát", "Hạn mức theo người dùng; xem lại chi phí hằng tuần"],
            ["Phần cứng lỗi/quá tải", "UPS, backup cấu hình; theo dõi GPU; tạm chuyển sang cloud khi bảo trì"],
            ["Ít người dùng sau đào tạo", "Video demo dễ xem lại; đưa AI review vào quy trình merge request"],
        ],
        widths=[0.38, 0.62]))
    s.append(Spacer(1, 6))
    NOTE(s, "Giá và thông số trong tài liệu tra cứu tháng 06/2026, có thể thay đổi; cần xác nhận lại khi mua sắm.")
    return s


# ============================ ENGLISH ============================
def build_en():
    s = []
    s.append(Paragraph("Internal AI Adoption Proposal", S["title"]))
    s.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceAfter=10))

    H1(s, "1. Purpose and requirements")
    P(s, "This document answers:"
         "<br/>(1) Options for a local AI server on open-source models, accessed over VPN, with hardware "
         "configurations;"
         "<br/>(2) The paid-service options and what sharing one account across a team really looks like;"
         "<br/>(3) Other options;"
         "<br/>(4) An implementation and training plan.")
    P(s, "<b>Identified AI use cases:</b>")
    UL(s, [
        "Testing, validation and automated status summaries.",
        "Analysis of technical problems.",
        "Code review, coding-style fixes, adding comments.",
        "Customer support.",
        "Recurring market intelligence: UWB, RTLS, market progress and demand by industry.",
    ])

    H1(s, "2. Option 1 — Local AI server with open-source models")
    P(s, "The most secure option: all data (source code, customer documents) never leaves company infrastructure. "
         "Staff connect over VPN from the office or remotely.")

    H2(s, "2.1. Architecture")
    s.append(Spacer(1, 4))
    s.append(ArchDiagram([
        ("User", ["laptop"]),
        ("VPN", ["WireGuard /", "Tailscale"]),
        ("Open WebUI", ["multi-user", "chat front-end"]),
        ("vLLM", ["inference engine"]),
        ("GPU server", ["open-source models"]),
    ]))
    NOTE(s, "Figure 1: Access architecture for the local AI server over VPN.")
    UL(s, [
        "<b>OS:</b> Ubuntu Server 24.04 LTS + Docker.",
        "<b>Inference engine:</b> vLLM for multi-user serving (PagedAttention, high throughput); Ollama only suits "
        "personal experiments.",
        "<b>Front-end:</b> Open WebUI — open source, multi-user with role-based access, per-user conversation "
        "isolation, built-in RAG (Q&amp;A over internal documents), SSO/LDAP support.",
        "<b>API gateway (optional):</b> LiteLLM proxy — virtual keys per person with budgets, one endpoint combining "
        "local and cloud models.",
        "<b>VPN:</b> Tailscale (near zero-config, free up to 3 users/100 devices) or self-hosted WireGuard "
        "(completely free).",
    ])
    SRC(s, "Sources / setup guides:",
        [U_OWUI, U_VLLM, U_LITELLM, U_TAILSCALE, U_WIREGUARD])

    H2(s, "2.2. Notable open-source models")
    P(s, "Top open-source LLMs ranked by aggregated benchmarks (benchlm.ai, June 2026):")
    s.append(make_table(
        ["Rank", "Model", "Creator", "Overall", "Context"],
        [
            ["1", "DeepSeek V4 Pro (Max)", "DeepSeek", "87", "1M"],
            ["2", "Kimi K2.6", "Moonshot AI", "84", "256K"],
            ["3", "GLM-5 (Reasoning)", "Zhipu AI", "81", "200K"],
            ["4", "GLM-5.1", "Zhipu AI", "83", "203K"],
            ["5", "DeepSeek V4 Pro (High)", "DeepSeek", "83", "1M"],
            ["6", "Qwen3.5 397B (Reasoning)", "Alibaba", "77", "128K"],
            ["7", "DeepSeek V4 Flash (Max)", "DeepSeek", "77", "1M"],
            ["8", "Qwen3.6-27B", "Alibaba", "75", "262K"],
        ],
        widths=[0.1, 0.34, 0.2, 0.21, 0.15]))
    s.append(Spacer(1, 4))
    NOTE(s, "The top-ranked models have hundreds of billions of parameters and need large GPU infrastructure; "
            "for the server configurations in section 2.3, the smaller variants (e.g. Qwen3.6-27B) or "
            "distilled/quantized versions of these models are the practical fit.")
    P(s, "Quick coding-capability comparison of the open models (higher is better, source: benchlm.ai):")
    s.append(make_table(
        ["Model", "Blended coding score", "LiveCodeBench", "SWE-bench Verified"],
        [
            ["DeepSeek V4 Pro (Max)", "89.8", "93.5", "-"],
            ["Kimi K2.6", "88.7", "89.6", "-"],
            ["DeepSeek V4 Pro (High)", "88.7", "-", "-"],
            ["Qwen3.5 397B (Reasoning)", "86.7", "-", "-"],
            ["GLM-5.1", "84.1", "-", "77.8"],
            ["GLM-5 (Reasoning)", "-", "-", "77.8"],
            ["DeepSeek V4 Flash (Max)", "-", "91.6", "-"],
        ],
        widths=[0.34, 0.24, 0.21, 0.21]))
    s.append(Spacer(1, 4))
    SRC(s, "Reference:", [U_BENCHLM, U_HFBLOG])
    SRC(s, "Evidence comparing coding capability across models (continuously updated leaderboards, "
           "covering both open and commercial models):",
        [U_SWEBENCH, U_AIDER, U_LIVECODE, U_EVALPLUS])

    H2(s, "2.3. Reference hardware configurations")
    s.append(make_table(
        ["Item", "Tier A — Entry", "Tier B — Mid-range", "Tier C — Mac alternative"],
        [
            ["GPU", "1× NVIDIA RTX 5090 32 GB GDDR7", "2× RTX 5090 (64 GB total) or 1× RTX PRO 6000 Blackwell 96 GB",
             "Apple M3 Ultra, 80-core GPU, unified memory"],
            ["CPU", "Ryzen 9 7950X / Core i9 (8+ cores)", "Threadripper / Xeon W (enough PCIe lanes for 2 GPUs)", "—"],
            ["RAM", "64 GB DDR5", "128–256 GB DDR5 ECC", "256–512 GB unified memory"],
            ["Storage", "2 TB NVMe", "4 TB NVMe (models + RAG data)", "2–4 TB SSD"],
            ["PSU / misc", "1000 W PSU", "1600 W PSU, well-ventilated case, UPS", "Very low power draw"],
            ["Models it can run", "≤ 32B Q4 (Qwen3 32B, Gemma 3 27B, gpt-oss-20b)",
             "70B Q4, gpt-oss-120b, quantized Qwen3 235B-A22B",
             "Very large models (DeepSeek R1 671B at ~17–18 tokens/s)"],
            ["Concurrent users", "~3–5", "~10–20 with vLLM", "1–3 (weak under concurrency)"],
            ["Evidence that the hardware fits the models",
             f"An RTX 5090's 32 GB is enough for quantized ~30B models: "
             f"{LK(U_RUNPOD, 'runpod.io (RTX 5090 LLM guide)')}",
             f"70B Q4 needs ~40 GB VRAM; 2× RTX 5090 or a 96 GB card covers it: "
             f"{LK(U_RUNPOD, 'runpod.io (RTX 5090 LLM guide)')}, {LK(U_BIZON, 'bizon-tech.com (best GPU for LLM)')}",
             f"The M3 Ultra 512 GB runs DeepSeek R1 671B at ~17-18 tokens/s: "
             f"{LK(U_M3LLM, 'medium.com (M3 Ultra LLM inference)')}, {LK(U_APPLE, 'apple.com/mac-studio/specs')}"],
            ["Estimated cost", "≈ US$2,500–3,500", "≈ US$7,000–12,000", "≈ US$5,600 (256 GB) – $9,500 (512 GB)"],
        ],
        widths=[0.14, 0.27, 0.31, 0.28]))
    s.append(Spacer(1, 4))
    P(s, "Basis: a 70B model at FP16 needs ~140 GB of VRAM; 4-bit quantization (Q4_K_M) reduces this to ~40 GB — "
         "more than one RTX 5090's 32 GB, hence two GPUs or a 96 GB card. The Mac Studio can hold very large models "
         "thanks to unified memory, but its long-prompt (prefill) speed and concurrency are weaker than NVIDIA GPUs.")
    SRC(s, "Reference:",
        [U_NV5090, U_NVPRO6000, U_RUNPOD, U_BIZON, U_APPLE, U_M3LLM])

    H2(s, "2.4. Assessment")
    s.append(make_table(
        ["Strengths", "Limitations"],
        [
            ["Data stays 100% on-premises; no per-seat subscription fees; unlimited usage; full control and "
             "customization (internal-document RAG, fine-tuning).",
             "Open 32B–120B models still trail top commercial models on hard tasks; needs an operator (model updates, "
             "backups, monitoring); no built-in web search unless integrated; upfront hardware investment."],
        ],
        widths=[0.5, 0.5]))
    s.append(Spacer(1, 6))

    H1(s, "3. Option 2 — Paid AI services (monthly / yearly)")
    H2(s, "3.1. The options")
    s.append(make_table(
        ["Service", "Price/user/month", "Notes"],
        [
            [f"ChatGPT Business (OpenAI)<br/>{LK(U_GPTPRICE, 'openai.com/chatgpt-pricing')}",
             "US$25 (monthly) / US$20 (annual)",
             "Minimum 2 seats; dedicated workspace; data not used for training"],
            [f"Claude Team Standard (Anthropic)<br/>{LK(U_CLAUDEPRICE, 'claude.com/pricing')}",
             "US$25 (monthly) / US$20 (annual)",
             "Minimum 5 seats; SSO, central admin; no training on team data"],
            [f"Claude Team Premium<br/>{LK(U_CLAUDEPRICE, 'claude.com/pricing')}",
             "US$125 (monthly) / US$100 (annual)",
             "Standard + Claude Code (terminal/IDE coding agent)"],
            [f"Cursor Pro / Teams<br/>{LK(U_CURSORPRICE, 'cursor.com/pricing')}",
             "US$20 (Pro) / US$40 (Teams)",
             "AI coding IDE; each month includes a model-usage allowance matching the plan price"],
            [f"GitHub Copilot Business<br/>{LK(U_COPILOT, 'github.com/copilot/plans')}",
             "US$19",
             "In-IDE code completion; complements rather than replaces AI chat"],
        ],
        widths=[0.3, 0.24, 0.46]))
    s.append(Spacer(1, 4))
    s.append(BarChart([
        ("Claude Fable 5", "Claude Team", 95.0),
        ("GPT-5.5", "ChatGPT Business", 88.7),
        ("Claude Opus 4.8", "Claude Team", 88.6),
        ("Gemini 3.1 Pro", "Google Gemini", 80.6),
    ]))
    NOTE(s, "Figure 2: Coding capability of the model behind each service - SWE-bench Verified score "
            "(% of real GitHub issues solved), June 2026. Cursor and Copilot run these same models, so coding "
            "ability follows the chosen model.")
    SRC(s, "Evidence comparing coding capability of commercial models (Claude, GPT, Gemini...) "
           "on independent leaderboards:",
        [U_BENCHSWE, U_SWEBENCH, U_AIDER, U_LMARENA, U_LIVECODE])
    s.append(Spacer(1, 2))

    H2(s, "3.2. Sharing one account across the team — possible, but limits hit fast")
    P(s, "Technically several people can log into one account, but <b>usage limits are counted per account</b>, "
         "so a shared account runs dry very quickly:")
    UL(s, [
        f"<b>Claude (Pro/Max):</b> a rolling <b>5-hour session limit</b> (starting from the first prompt) plus a "
        f"<b>weekly limit</b>; every channel (web, IDE, Claude Code) draws from the same quota. Pro allows only "
        f"roughly 10–45 prompts per 5-hour session depending on length. Source: "
        f"{LK(U_CLAUDELIMIT, 'support.claude.com — How do usage and length limits work')}.",
        f"<b>ChatGPT Plus:</b> about <b>160 GPT-5.5 messages every 3 hours</b>; beyond that it falls back to the mini "
        f"model. Source: {LK(U_GPTLIMIT, 'help.openai.com — GPT-5.5 in ChatGPT')}. The Business plan is virtually "
        f"unlimited on base models, but is billed per seat. Source: "
        f"{LK(U_GPTBIZLIMIT, 'help.openai.com — ChatGPT Business Models & Limits')}.",
        f"<b>Cursor:</b> limited <b>per month</b> — the US$20 Pro plan includes ~US$20 of model usage each month; "
        f"when it is used up, it stops (or continues on-demand at extra cost if a spend limit is set). Sources: "
        f"{LK(U_CURSORPRICE, 'cursor.com/pricing')}, {LK(U_CURSORBLOG, 'cursor.com/blog/june-2025-pricing')}.",
        "<b>Limits depend on context/tokens, not message count:</b> providers meter quota by tokens processed. "
        "Long conversations, large file attachments and big code contexts burn quota many times faster — so the more "
        "people share one account, the sooner it hits the ceiling.",
        "Also, sharing a personal account falls outside the services' terms of use; the official way for a team is a "
        "per-seat Business/Team plan.",
    ])

    H1(s, "4. Other options")
    H2(s, "4.1. Renting cloud GPUs")
    P(s, "Rent GPUs by the hour to run the same open-source models from section 2. Advantages:")
    UL(s, [
        "No upfront investment — pay only for hours actually used.",
        "Try several GPU configurations before committing to a hardware purchase.",
        "Scale up or down flexibly; rent a bigger machine for a few hours when a heavy job comes up.",
        "Usable immediately while waiting for purchased hardware to arrive.",
    ])
    H2(s, "4.2. Comparison matrix")
    s.append(make_table(
        ["Criterion", "Option 1 — Local server", "Option 2 — Paid services", "Cloud GPU rental"],
        [
            ["Data security", "Highest — data never leaves the company", "Depends on vendor (no-training commitments)",
             "Data passes through the rental provider"],
            ["AI quality", "Good (open 32B–120B models)", "Best (latest commercial models)", "Same as Option 1 (same open models)"],
            ["Upfront cost", "US$2,500–12,000 by tier", "0", "0"],
            ["Monthly cost", "Power + maintenance", "US$20–125/user by plan", "Per hour of use"],
            ["Usage limits", "None", "Session/weekly/monthly depending on service (3.2)", "None (within rented hours)"],
            ["Web search", "Requires extra integration", "Built-in", "Requires extra integration"],
            ["Operating effort", "Needs an owner", "Negligible", "Moderate"],
        ],
        widths=[0.18, 0.28, 0.29, 0.25]))
    s.append(Spacer(1, 6))

    H1(s, "5. Implementation plan")
    s.append(make_table(
        ["Timeline", "Key activities", "Outcome"],
        [
            ["Week 1, days 1–2", "Confirm option and budget; define which data may/may not go to cloud; open "
             "accounts; deploy Open WebUI (+ LiteLLM if using APIs) on an interim machine; set up Tailscale/WireGuard VPN",
             "Whole team starts using AI via an internal web app"],
            ["Week 1, days 3–5", "Stand up the open-model server: Ubuntu + Docker + vLLM, pull models (Qwen3 32B, "
             "Qwen2.5-Coder); if hardware is not yet available, run on a rented cloud GPU",
             "Open-source models live, reachable over VPN"],
            ["Week 2", "Integrate use cases: AI code review on Git, internal-document RAG, test-summary scripts, "
             "weekly UWB/RTLS market-watch agent; record demo videos (section 6); publish the AI usage policy",
             "AI embedded in daily workflows, guides available"],
        ],
        widths=[0.16, 0.56, 0.28]))
    s.append(Spacer(1, 4))
    NOTE(s, "If hardware must be ordered, shipping time falls outside these 2 weeks — use rented GPUs meanwhile.")

    H1(s, "6. Team training")
    UL(s, [
        "<b>Record setup demo videos</b> (5–10 min screen recordings): installing and connecting the VPN, logging "
        "into Open WebUI, connecting the IDE/terminal agent, configuring internal API keys — stored on the internal "
        "drive so new staff can set themselves up anytime.",
        "<b>Share a curated list of prompt-writing guides</b> with the team:",
    ])
    SRC(s, "Prompt-engineering guides:",
        [U_PROMPT_A, U_PROMPT_O, U_PROMPT_G])
    UL(s, [
        "A one-page cheat sheet of ready-to-use prompts for company work.",
    ])

    H1(s, "7. Mapping use cases → solutions")
    s.append(make_table(
        ["Use case", "Solution", "Model / tool"],
        [
            ["Testing, validation, status summaries", "Scripts calling the internal model API: read test/CI logs, "
             "generate a daily summary posted to chat", "Qwen3 32B (local) — internal data"],
            ["Problem analysis", "Direct chat; escalate hard problems to a stronger model",
             "Claude/GPT (cloud) or DeepSeek-R1-Distill (local)"],
            ["Code review, style, comments", "Wired into Git: automatic AI review on every merge request; engineers "
             "use a terminal/IDE agent", "Qwen2.5-Coder (local), Claude Code / Cursor (cloud)"],
            ["Customer support", "A Q&amp;A chatbot over the docs.leapslabs.com documentation using RAG "
             "(details in section 9)", "Open WebUI Knowledge (local)"],
            ["UWB/RTLS market watch", "A script crawls news from a fixed source list; AI only summarizes and "
             "classifies; notifications are sent (details in section 8)", "Crawl script + local model or API"],
            ["New application development", "Build one small app in a 2-week pilot with AI pair-programming to "
             "measure real speed — separate discussion to pick the pilot", "Claude Code / Cursor + standard project template"],
        ],
        widths=[0.22, 0.48, 0.3]))
    s.append(Spacer(1, 6))

    H1(s, "8. UWB/RTLS market intelligence monitoring")
    P(s, "We build a script that crawls news from a fixed list of websites; AI handles <b>summarization and "
         "classification</b>; the system then sends notifications. A 4-step pipeline:")
    UL(s, [
        "<b>Step 1 - Fix the source list:</b> the websites/RSS feeds in the table below; adjustable over time.",
        f"<b>Step 2 - News crawl script:</b> Python ({LK(U_FEEDPARSER, 'feedparser')} for RSS; "
        f"requests + {LK(U_BSOUP, 'BeautifulSoup')} for pages without RSS), run daily by cron, storing new articles "
        f"in a database with de-duplication. A no-code alternative is {LK(U_N8N, 'n8n')} (self-hostable).",
        "<b>Step 3 - AI summarization and classification:</b> for each new article, the model writes a 3-5 sentence "
        "summary and assigns labels (UWB / RTLS / chips and hardware / competitors / market reports / industry "
        "applications: automotive, healthcare, logistics...), scores relevance 1-5 and drops articles below the "
        "threshold. News is public data, so either the local model (Qwen3 32B) or an API works.",
        "<b>Step 4 - Notification:</b> a weekly digest via email/Slack/Teams; highly relevant articles forwarded "
        "the same day.",
    ])
    P(s, "<b>Suggested source websites:</b>")
    s.append(make_table(
        ["Source", "Main content"],
        [
            [f"FiRa Consortium<br/>{LK(U_FIRA, 'firaconsortium.org')}",
             "UWB standards body: certification news, new members, standard use cases"],
            [f"UWB Alliance<br/>{LK(U_UWBA, 'uwballiance.org')}",
             "UWB ecosystem, spectrum policy advocacy"],
            [f"omlox<br/>{LK(U_OMLOX, 'omlox.com')}",
             "Open locating standard for industry (UWB at its core)"],
            [f"RFID Journal<br/>{LK(U_RFIDJ, 'rfidjournal.com')}",
             "RTLS and asset-tracking news, real deployment case studies in logistics, healthcare, manufacturing"],
            [f"everything RF<br/>{LK(U_EVRF, 'everythingrf.com/news')}",
             "Newly released RF and UWB chips/modules"],
            [f"NXP Newsroom<br/>{LK(U_NXP, 'nxp.com (newsroom)')}",
             "Trimension UWB chips, automotive and smartphone partnerships"],
            [f"Qorvo Newsroom<br/>{LK(U_QORVO, 'qorvo.com/newsroom')}",
             "DW3000 UWB chip line (ex-Decawave) and industry news"],
            [f"Sewio Blog<br/>{LK(U_SEWIO, 'sewio.net/blog')}",
             "UWB RTLS in factories; positioning-technology comparisons (competitor watch)"],
            [f"MarketsandMarkets / Grand View Research<br/>{LK(U_MNM_UWB, 'marketsandmarkets.com (UWB report)')}, "
             f"{LK(U_GVR_UWB, 'grandviewresearch.com (UWB report)')}",
             "Periodically updated UWB market sizing and forecast reports"],
            [f"Google News RSS<br/>{LK(U_GNEWS, 'news.google.com/rss/search?q=UWB+OR+RTLS')}",
             "Broad keyword sweep, free, easy to add new keywords (e.g. competitor or industry names)"],
        ],
        widths=[0.4, 0.6]))
    s.append(Spacer(1, 6))

    H1(s, "9. Customer support: a Q&amp;A chatbot over docs.leapslabs.com")
    P(s, f"Build a chatbot that lets users ask questions directly, with all of its knowledge taken from "
         f"{LK(U_LEAPSDOCS, 'docs.leapslabs.com')}. The chatbot works on the <b>RAG</b> "
         f"(Retrieval-Augmented Generation) pattern: it answers only from the documentation content, citing links "
         f"to the relevant docs pages; when the answer is not in the docs it says 'not covered in the "
         f"documentation' instead of making something up.")
    P(s, "<b>How to build it (pipeline):</b>")
    UL(s, [
        f"<b>Step 1 - Ingest the docs:</b> a script downloads all pages of {LK(U_LEAPSDOCS, 'docs.leapslabs.com')} "
        f"(via the sitemap), converts them to markdown and splits them into chunks; re-run automatically every "
        f"week by cron so updates to the docs are picked up.",
        "<b>Step 2 - Index:</b> create embeddings for each chunk and store them in a vector database. Open WebUI "
        "ships with a built-in Knowledge (RAG) feature, so nothing has to be built from scratch.",
        "<b>Step 3 - Q&amp;A:</b> when a user asks a question, the system retrieves the most relevant doc chunks, "
        "puts them into context, and the model answers with source links.",
        "<b>Step 4 - Two-stage rollout:</b> (a) internal first: the support team uses the chatbot to draft replies "
        "to customers (human approves before sending); (b) once quality is stable, embed a public chat widget on "
        "the website/docs so customers can ask directly, with hard questions automatically handed over to a human.",
        "Log every customer question: it both measures answer quality and shows which parts of the docs are "
        "missing and should be added.",
        "The docs content is public, so either the local model (Qwen3 32B) or an API works; running locally means "
        "no per-question cost.",
    ])
    SRC(s, "Tools / frameworks for building the RAG chatbot:",
        [U_OWUI, U_LLAMAINDEX, U_LANGCHAIN])

    H1(s, "10. Risks and mitigations")
    s.append(make_table(
        ["Risk", "Mitigation"],
        [
            ["Sensitive data leaking to cloud services", "Data classification policy; confidential data restricted to local models"],
            ["Incorrect AI answers (hallucination)", "Human review before anything reaches customers; require sources"],
            ["Costs running out of control", "Per-user limits; weekly cost review"],
            ["Hardware failure / overload", "UPS and config backups; GPU monitoring; temporary cloud fallback during maintenance"],
            ["Low adoption after training", "Replayable demo videos; AI review built into the merge-request process"],
        ],
        widths=[0.38, 0.62]))
    s.append(Spacer(1, 6))
    NOTE(s, "Prices and specifications researched in June 2026 and subject to change; re-confirm at purchase time.")
    return s


if __name__ == "__main__":
    out = "/Users/hienvuong/Desktop/leaps"
    build_pdf(os.path.join(out, "De-xuat-trien-khai-AI_VI.pdf"), build_vi(),
              "Trang {page}/{total}", "Đề xuất triển khai AI nội bộ")
    build_pdf(os.path.join(out, "AI-Adoption-Proposal_EN.pdf"), build_en(),
              "Page {page}/{total}", "Internal AI Adoption Proposal")
    print("done")
