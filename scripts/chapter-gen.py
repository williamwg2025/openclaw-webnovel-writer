#!/usr/bin/env python3
"""
Chapter Generator
Usage: python3 chapter-gen.py --chapter 1 --outline "退婚现场"
"""

import argparse
import sys
from pathlib import Path

class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text:^60}{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.NC}\n")

def generate_chapter(chapter_num: int, outline: str):
    """生成章节内容框架"""
    print(f"{Colors.BOLD}章节:{Colors.NC} 第{chapter_num}章")
    print(f"{Colors.BOLD}主题:{Colors.NC} {outline}\n")
    
    print(f"{Colors.BOLD}{Colors.MAGENTA}【章节结构】{Colors.NC}\n")
    print(f"  {Colors.GREEN}开篇 (500 字):{Colors.NC}")
    print(f"    - 环境描写，营造氛围")
    print(f"    - 主角出场，展示当前处境")
    print(f"    - 引出冲突/事件")
    print()
    
    print(f"  {Colors.GREEN}发展 (1000 字):{Colors.NC}")
    print(f"    - 冲突升级")
    print(f"    - 配角反应（嘲讽/担忧/看戏）")
    print(f"    - 主角内心活动")
    print()
    
    print(f"  {Colors.GREEN}高潮 (1000 字):{Colors.NC}")
    print(f"    - 主角爆发/展现实力")
    print(f"    - 众人震惊")
    print(f"    - 打脸反派")
    print()
    
    print(f"  {Colors.GREEN}结尾 (500 字):{Colors.NC}")
    print(f"    - 收尾，留下悬念")
    print(f"    - 为下一章铺垫")
    print(f"    - 简短有力，让人想看下一章")
    print()
    
    print(f"{Colors.BOLD}{Colors.CYAN}【写作提示】{Colors.NC}\n")
    print(f"  ✓ 多用短句，节奏要快")
    print(f"  ✓ 对话要符合人物性格")
    print(f"  ✓ 爽点要足，但不要过度")
    print(f"  ✓ 结尾留钩子，吸引读者继续看")
    print(f"  ✓ 字数控制在 2000-3000 字")

def main():
    parser = argparse.ArgumentParser(description='生成章节内容')
    parser.add_argument('--chapter', type=int, required=True, help='章节号')
    parser.add_argument('--outline', type=str, required=True, help='章节大纲/主题')
    args = parser.parse_args()
    
    print_header("📝 章节生成器")
    generate_chapter(args.chapter, args.outline)

if __name__ == '__main__':
    main()
