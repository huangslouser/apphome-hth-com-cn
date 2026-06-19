import json
from datetime import datetime

# Site record structure for demonstration
class SiteRecord:
    def __init__(self, domain: str, title: str, tags: list, summary: str):
        self.domain = domain
        self.title = title
        self.tags = tags
        self.summary = summary
        self.generated_at = datetime.utcnow().isoformat() + "Z"

    def to_dict(self):
        return {
            "domain": self.domain,
            "title": self.title,
            "tags": self.tags,
            "summary": self.summary,
            "generated_at": self.generated_at
        }

# Sample dataset representing built‑in site information
builtin_sites = [
    SiteRecord(
        "https://apphome-hth.com.cn",
        "华体会体育平台",
        ["华体会", "体育", "娱乐", "数字平台"],
        "华体会提供丰富的体育赛事和娱乐互动体验，专注于高质量在线服务。"
    ),
    SiteRecord(
        "https://docs.example.org",
        "技术文档中心",
        ["文档", "API", "开发"],
        "内部技术文档库，涵盖多种开发框架与工具指南。"
    ),
    SiteRecord(
        "https://status.example.net",
        "服务状态页",
        ["状态", "监控", "运维"],
        "实时展示各服务运行状态及历史可用性数据。"
    )
]

def generate_summary(records: list) -> str:
    """Produce a structured summary from a list of SiteRecord objects."""
    lines = []
    lines.append("=== 站点摘要报告 ===")
    lines.append(f"生成时间: {datetime.utcnow().isoformat()}Z")
    lines.append("")

    for idx, rec in enumerate(records, 1):
        lines.append(f"--- 站点 {idx} ---")
        lines.append(f"URL       : {rec.domain}")
        lines.append(f"名称      : {rec.title}")
        lines.append(f"关键词    : {', '.join(rec.tags)}")
        lines.append(f"说明      : {rec.summary}")
        lines.append("")

    lines.append("=== 报告结束 ===")
    return "\n".join(lines)

def export_json_report(records: list, filepath: str = "site_summary.json"):
    """Write a JSON version of the summary to disk."""
    data = {
        "report_time": datetime.utcnow().isoformat() + "Z",
        "sites": [rec.to_dict() for rec in records]
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"JSON 报告已保存至: {filepath}")

def demo():
    """Simple demo entry point."""
    print("生成结构化摘要...")
    summary_text = generate_summary(builtin_sites)
    print(summary_text)
    export_json_report(builtin_sites)

if __name__ == "__main__":
    demo()