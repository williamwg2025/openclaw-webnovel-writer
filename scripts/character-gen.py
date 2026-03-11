#!/usr/bin/env python3
"""
Character Generator
Usage: python3 character-gen.py --role 主角 --genre 都市
"""

import argparse
import random
import sys
from pathlib import Path

class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    NC = '\033[0m'
    BOLD = '\033[1m'

SCRIPT_DIR = Path(__file__).parent

# 人物数据库
CHARACTERS = {
    '主角': {
        '玄幻': {
            '名字': ['萧炎', '林动', '叶凡', '石昊', '楚风'],
            '身份': ['废柴少爷', '宗门弟子', '散修', '转世大能', '异界来客'],
            '性格': ['坚毅', '腹黑', '低调', '热血', '杀伐果断'],
            '金手指': ['药老', '系统', '神秘血脉', '上古功法', '神秘宝物'],
            '目标': ['成为斗帝', '复仇', '保护家人', '探索真相', '长生']
        },
        '都市': {
            '名字': ['林凡', '叶辰', '陈凡', '苏铭', '秦风'],
            '身份': ['大学生', '保安', '医生', '兵王', '富二代'],
            '性格': ['低调', '腹黑', '热血', '冷静', '重情义'],
            '金手指': ['神豪系统', '医术传承', '透视眼', '修仙记忆', '未来知识'],
            '目标': ['赚钱', '复仇', '保护家人', '走上巅峰', '找到真爱']
        },
        '言情': {
            '名字': ['苏浅', '林晚', '夏沫', '安然', '顾念'],
            '身份': ['设计师', '医生', '老师', '小透明', '重生女配'],
            '性格': ['独立', '温柔', '坚强', '聪慧', '洒脱'],
            '金手指': ['重生记忆', '空间', '医术', '预知能力', '系统'],
            '目标': ['逆袭', '找到真爱', '事业成功', '复仇', '守护家人']
        }
    },
    '反派': {
        '玄幻': {
            '类型': ['世家子弟', '宗门天骄', '邪修', '魔道巨擘', '异域强者'],
            '动机': ['嫉妒主角', '利益冲突', '理念不同', '宿命对决', '误会'],
            '结局': ['被反杀', '臣服', '洗白', '逃遁', '同归于尽']
        },
        '都市': {
            '类型': ['富二代', '商业对手', '黑道大佬', '情敌', '腐败官员'],
            '动机': ['争夺利益', '争夺女人', '面子问题', '家族恩怨', '理念冲突'],
            '结局': ['破产', '入狱', '臣服', '逃亡', '洗心革面']
        }
    },
    '女主': {
        '玄幻': {
            '身份': ['圣女', '公主', '仙子', '妖女', '神秘强者'],
            '性格': ['高冷', '温柔', '活泼', '傲娇', '神秘'],
            '与主角关系': ['师徒', '青梅竹马', '救命恩人', '竞争对手', '命中注定']
        },
        '都市': {
            '身份': ['校花', '总裁', '明星', '医生', '警察'],
            '性格': ['高冷御姐', '温柔知性', '活泼可爱', '傲娇千金', '神秘女郎'],
            '与主角关系': ['上司', '同学', '邻居', '病人', '救命恩人']
        },
        '言情': {
            '身份': ['总裁', '明星', '设计师', '医生', '老师'],
            '性格': ['霸道', '温柔', '专一', '傲娇', '宠溺'],
            '与主角关系': ['契约婚姻', '青梅竹马', '上下级', '师生', '陌生人']
        }
    }
}

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text:^60}{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.NC}\n")

def generate_character(role: str, genre: str):
    """生成人物设定"""
    if role not in CHARACTERS:
        print(f"{Colors.RED}未知角色类型：{role}{Colors.NC}")
        print(f"可用角色：{', '.join(CHARACTERS.keys())}")
        return
    
    if genre not in CHARACTERS[role]:
        print(f"{Colors.RED}{genre}题材暂无{role}模板{Colors.NC}")
        print(f"可用题材：{', '.join(CHARACTERS[role].keys())}")
        return
    
    data = CHARACTERS[role][genre]
    
    print(f"{Colors.BOLD}角色类型:{Colors.NC} {role}")
    print(f"{Colors.BOLD}题材:{Colors.NC} {genre}\n")
    
    print(f"{Colors.BOLD}{Colors.MAGENTA}【人物设定】{Colors.NC}\n")
    
    for key, values in data.items():
        value = random.choice(values)
        print(f"  {Colors.YELLOW}{key}:{Colors.NC} {value}")
    
    print()
    
    # 详细设定
    print(f"{Colors.BOLD}{Colors.CYAN}【详细设定】{Colors.NC}\n")
    
    if role == '主角':
        print(f"  {Colors.GREEN}外貌描写:{Colors.NC}")
        print(f"    - 剑眉星目，气质不凡")
        print(f"    - 平时低调，爆发时气势惊人")
        print(f"    - 有独特的个人标志（伤疤/饰品/气息）")
        print()
        
        print(f"  {Colors.GREEN}经典台词:{Colors.NC}")
        quotes = [
            '"三十年河东，三十年河西，莫欺少年穷！"',
            '"我命由我不由天！"',
            '"动我家人者，虽远必诛！"',
            '"今天，我要让所有人知道，谁才是真正的主角！"'
        ]
        for quote in quotes:
            print(f"    {quote}")
        print()
        
        print(f"  {Colors.GREEN}成长路线:{Colors.NC}")
        print(f"    初期：被看不起→获得金手指")
        print(f"    中期：展现实力→震惊众人")
        print(f"    后期：成为传奇→创造神话")
        print()
    
    elif role == '反派':
        print(f"  {Colors.GREEN}人物弧光:{Colors.NC}")
        print(f"    - 不是纯粹的坏，有自己的坚持")
        print(f"    - 可能与主角有相似之处")
        print(f"    - 有让人同情的一面")
        print()
        
        print(f"  {Colors.GREEN}与主角冲突:{Colors.NC}")
        print(f"    - 第一次：小摩擦，主角隐忍")
        print(f"    - 第二次：正面冲突，主角小胜")
        print(f"    - 第三次：生死对决，主角反杀")
        print()
    
    elif role == '女主':
        print(f"  {Colors.GREEN}感情线发展:{Colors.NC}")
        print(f"    - 初遇：误会/冲突/救命")
        print(f"    - 发展：逐渐了解，产生好感")
        print(f"    - 波折：误会/分离/第三者")
        print(f"    - 结局：在一起/开放式")
        print()
        
        print(f"  {Colors.GREEN}经典场景:{Colors.NC}")
        print(f"    - 英雄救美")
        print(f"    - 雨中告白")
        print(f"    - 生死与共")
        print(f"    - 久别重逢")
        print()

def main():
    parser = argparse.ArgumentParser(description='生成人物设定')
    parser.add_argument('--role', type=str, required=True,
                       help='角色类型 (主角，反派，女主)')
    parser.add_argument('--genre', type=str, default='玄幻',
                       help='题材 (玄幻，都市，言情，科幻)')
    args = parser.parse_args()
    
    print_header("👥 人物设定生成器")
    generate_character(args.role, args.genre)

if __name__ == '__main__':
    main()
