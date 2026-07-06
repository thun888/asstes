import json
from pathlib import Path

def get_longest_common_prefix(strings):
    """
    计算字符串列表的最大公共前缀
    """
    if not strings:
        return ""

    sorted_strs = sorted(strings, key=len)
    shortest = sorted_strs[0]

    for i, char in enumerate(shortest):
        for s in sorted_strs[1:]:
            if s[i] != char:
                return shortest[:i]
    return shortest

def get_longest_common_suffix(strings):
    """
    计算字符串列表的最大公共后缀（通过反转字符串来计算前缀）
    """
    if not strings:
        return ""

    reversed_strs = [s[::-1] for s in strings]
    prefix = get_longest_common_prefix(reversed_strs)
    return prefix[::-1]

def main():
    script_dir = Path(__file__).parent
    json_path = script_dir / "main.json"

    print(f"读取文件：{json_path}")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    modified_count = 0
    for pack in data:
        if pack.get('type') == 'image':
            items = pack.get('items', [])
            if not items:
                continue

            vals = [item['val'] for item in items]

            # 计算最大公共前缀和后缀
            prefix = get_longest_common_prefix(vals)
            suffix = get_longest_common_suffix(vals)

            if not prefix and not suffix:
                continue

            pack['basePrefix'] = prefix
            pack['baseSuffix'] = suffix

            # 从每个 val 中移除前后缀
            for item in items:
                original_val = item['val']
                new_val = original_val

                if prefix and new_val.startswith(prefix):
                    new_val = new_val[len(prefix):]

                if suffix and new_val.endswith(suffix):
                    new_val = new_val[:-len(suffix)]

                item['val'] = new_val

            modified_count += 1

            print(f"分类：{pack['name']} (共{len(items)}个表情)")
            print(f"  basePrefix: {prefix}")
            print(f"  baseSuffix: {suffix}")
            print(f"  示例 val: {items[0]['val']}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n处理完成！共修改 {modified_count} 个 image 类型分类")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n处理完成！共修改 {modified_count} 个 image 类型分类")

if __name__ == '__main__':
    main()
