"""Remove the MathJax v2 scripts plotly injects into every figure embed.

plotly's notebook renderer hardcodes include_mathjax="cdn", but MathJax v2 is
incompatible with the plotly.js 3.x bundle and silently suppresses in-chart
text (e.g. bar value labels). No page on this site uses LaTeX math, so the
scripts are safe to strip. Runs as a Quarto post-render hook.
"""

import re
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / "_site"

MATHJAX_SRC = re.compile(
    r'<script[^>]*src="[^"]*mathjax[^"]*"[^>]*>\s*</script>', re.IGNORECASE
)
MATHJAX_CONFIG = re.compile(
    r"<script>\s*if \(window\.MathJax[^<]*</script>", re.IGNORECASE
)


def main():
    for page in SITE.rglob("*.html"):
        html = page.read_text()
        stripped = MATHJAX_CONFIG.sub("", MATHJAX_SRC.sub("", html))
        if stripped != html:
            page.write_text(stripped)
            print(f"stripped MathJax from {page.relative_to(SITE)}")


if __name__ == "__main__":
    main()
