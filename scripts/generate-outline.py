#!/usr/bin/env python3
"""
Novel Outline Generator
Usage: python3 generate-outline.py --genre 玄幻 --theme 重生
"""

import argparse
import sys
import random
from pathlib import Path

class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    RED = '\033[0;31m'
    NC = '\033[0m'
    BOLD = '\033[1m'

SCRIPT_DIR = Path(__file__).parent

# 爆款套路库
PLOTS = {
    '玄幻': [
        '废柴退婚，获得神秘老爷爷',
        '家族测试，觉醒最强血脉',
        '秘境探险，获得上古传承',
        '宗门大比，一鸣惊人',
        '越级挑战，震惊全场'
    ],
    '都市': [
        '重生回到高考前',
        '获得神豪系统',
        '兵王回归都市',
        '意外获得医术传承',
        '被校花倒追'
    ],
    '言情': [
        '重生回到婚前',
        '总裁契约婚姻',
        '穿越成恶毒女配',
        '带球跑后被发现',
        '竹马vs天降'
    ],
    '科幻': [
        '末世爆发，获得空间',
        '穿越到星际时代',
        '觉醒 S 级异能',
        '机甲大赛夺冠',
        '发现外星文明'
    ]
}

CHARACTER_TEMPLATES = {
    '主角': {
        '性格': ['坚毅', '腹黑', '低调', '热血', '冷静'],
        '金手指': ['系统', '老爷爷', '血脉', '宝物', '知识'],
        '目标': ['成为最强', '复仇', '保护家人', '探索真相', '长生']
    },
    '反派': {
        '类型': ['富二代', '宗门天骄', '世家子弟', '邪修', '外星势力'],
        '动机': ['嫉妒', '利益', '理念冲突', '宿命', '误会']
    },
    '女主': {
        '身份': ['校花', '总裁', '仙子', '公主', '杀手'],
        '性格': ['高冷', '温柔', '活泼', '傲娇', '神秘']
    }
}

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text:^60}{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.NC}\n")

def generate_title(genre: str, theme: str) -> str:
    """生成小说书名"""
    prefixes = {
        '玄幻': ['绝世', '逆天', '至尊', '无上', '万古'],
        '都市': ['神级', '最强', '超级', '极品', '无敌'],
        '言情': ['重生', '总裁', '甜宠', '独家', '命中注定'],
        '科幻': ['星际', '末世', '无限', '维度', '觉醒']
    }
    
    suffixes = {
        '玄幻': ['帝尊', '神王', '剑神', '武帝', '天尊'],
        '都市': ['神豪', '兵王', '医仙', '大佬', '高手'],
        '言情': ['娇妻', '前妻', '新娘', '女友', '夫人'],
        '科幻': ['战甲', '舰队', '领主', '主宰', '纪元']
    }
    
    prefix = random.choice(prefixes.get(genre, ['超级']))
    suffix = random.choice(suffixes.get(genre, ['传奇']))
    
    return f"《{prefix}{theme}{suffix}》"

def generate_outline(genre: str, theme: str, chapters: int = 100):
    """生成小说大纲"""
    print(f"{Colors.BOLD}题材:{Colors.NC} {genre}")
    print(f"{Colors.BOLD}主题:{Colors.NC} {theme}")
    print(f"{Colors.BOLD}预计章节:{Colors.NC} {chapters}章\n")
    
    # 生成书名
    title = generate_title(genre, theme)
    print(f"{Colors.BOLD}{Colors.MAGENTA}推荐书名：{title}{Colors.NC}\n")
    
    # 核心梗
    print(f"{Colors.BOLD}{Colors.CYAN}【核心梗】{Colors.NC}")
    plots = PLOTS.get(genre, PLOTS['玄幻'])
    core_plot = random.choice(plots)
    print(f"  {core_plot}\n")
    
    # 故事大纲
    print(f"{Colors.BOLD}{Colors.CYAN}【故事大纲】{Colors.NC}")
    print(f"  {Colors.GREEN}第一卷：崛起篇 (1-{chapters//4}章){Colors.NC}")
    print(f"    - 主角出场，被看不起/退婚/欺负")
    print(f"    - 获得金手指（系统/传承/宝物）")
    print(f"    - 初次展现实力，震惊周围的人")
    print(f"    - 进入更大舞台（宗门/学校/城市）")
    print()
    
    print(f"  {Colors.GREEN}第二卷：成长篇 ({chapters//4+1}-{chapters//2}章){Colors.NC}")
    print(f"    - 遇到第一个大反派")
    print(f"    - 经历挫折，实力提升")
    print(f"    - 收服小弟/盟友")
    print(f"    - 感情线发展")
    print()
    
    print(f"  {Colors.GREEN}第三卷：高潮篇 ({chapters//2+1}-{chapters*3//4}章){Colors.NC}")
    print(f"    - 身份/秘密曝光")
    print(f"    - 与反派正面冲突")
    print(f"    - 底牌尽出，越级挑战")
    print(f"    - 成为一方霸主")
    print()
    
    print(f"  {Colors.GREEN}第四卷：巅峰篇 ({chapters*3//4+1}-{chapters}章){Colors.NC}")
    print(f"    - 最终 BOSS 出现")
    print(f"    - 揭开世界真相")
    print(f"    - 终极决战")
    print(f"    - 成为传说/新的开始")
    print()
    
    # 人物设定
    print(f"{Colors.BOLD}{Colors.CYAN}【主要人物】{Colors.NC}")
    print(f"  {Colors.YELLOW}主角:{Colors.NC}")
    print(f"    - 性格：{random.choice(CHARACTER_TEMPLATES['主角']['性格'])}")
    print(f"    - 金手指：{random.choice(CHARACTER_TEMPLATES['主角']['金手指'])}")
    print(f"    - 目标：{random.choice(CHARACTER_TEMPLATES['主角']['目标'])}")
    print()
    
    print(f"  {Colors.YELLOW}反派:{Colors.NC}")
    print(f"    - 类型：{random.choice(CHARACTER_TEMPLATES['反派']['类型'])}")
    print(f"    - 动机：{random.choice(CHARACTER_TEMPLATES['反派']['动机'])}")
    print()
    
    print(f"  {Colors.YELLOW}女主:{Colors.NC}")
    print(f"    - 身份：{random.choice(CHARACTER_TEMPLATES['女主']['身份'])}")
    print(f"    - 性格：{random.choice(CHARACTER_TEMPLATES['女主']['性格'])}")
    print()
    
    # 爽点设计
    print(f"{Colors.BOLD}{Colors.CYAN}【爽点设计】{Colors.NC}")
    print(f"  ✓ 每章至少 1 个小爽点")
    print(f"  ✓ 每 3 章一个中爽点")
    print(f"  ✓ 每 10 章一个大爽点")
    print(f"  ✓ 每 50 章一个超爽点")
    print()
    
    # 更新建议
    print(f"{Colors.BOLD}{Colors.CYAN}【更新建议】{Colors.NC}")
    print(f"  - 日更：4000-6000 字/天")
    print(f"  - 章节字数：2000-3000 字/章")
    print(f"  - 更新时间：固定时段（推荐晚 8 点）")
    print(f"  - 存稿建议：至少存 10 章再发书")

def main():
    parser = argparse.ArgumentParser(description='生成小说大纲')
    parser.add_argument('--genre', type=str, default='玄幻',
                       help='题材 (玄幻，都市，言情，科幻，仙侠，历史)')
    parser.add_argument('--theme', type=str, default='重生',
                       help='主题 (重生，穿越，系统，退婚， etc.)')
    parser.add_argument('--chapters', type=int, default=100,
                       help='预计章节数')
    args = parser.parse_args()
    
    print_header("📖 网文小说大纲生成器")
    generate_outline(args.genre, args.theme, args.chapters)

if __name__ == '__main__':
    main()
