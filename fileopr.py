#!/usr/bin/env python3
"""fileopr.py
简单演示 Python 中文件的打开/读取/写入与关闭（with 与手动 open/close）。
用法示例：
  python fileopr.py --mode read                  # 用 with 读取并打印
  python fileopr.py --mode manual                # 手动 open/close 读取并打印
  python fileopr.py --mode write --text "hi"   # 覆盖写入
  python fileopr.py --mode append --text "hi"  # 追加写入
"""

from pathlib import Path
import argparse
import sys


def read_with_context(path: Path, encoding: str = 'utf-8') -> str:
    """使用 with 上下文管理器读取文件并返回内容（自动 close）。"""
    with open(path, 'r', encoding=encoding) as f:
        return f.read()


def read_manual(path: Path, encoding: str = 'utf-8') -> str:
    """手动 open 然后确保 finally 中 close（演示显式关闭）。"""
    f = open(path, 'r', encoding=encoding)
    try:
        return f.read()
    finally:
        f.close()


def write_with_context(path: Path, text: str, encoding: str = 'utf-8') -> None:
    with open(path, 'w', encoding=encoding) as f:
        f.write(text)


def append_with_context(path: Path, text: str, encoding: str = 'utf-8') -> None:
    with open(path, 'a', encoding=encoding) as f:
        f.write(text)


def main():
    parser = argparse.ArgumentParser(description='文件打开/关闭示例程序')
    parser.add_argument('--path', '-p', default=r'd:\Environment\Python_Class\helloworld.txt',
                        help='要操作的文件路径（默认 workspace 中的 helloworld.txt）')
    parser.add_argument('--mode', '-m', choices=['read', 'manual', 'write', 'append'], default='read',
                        help='操作模式：read(with)，manual(显式open/close)，write(覆盖)，append(追加)')
    parser.add_argument('--text', '-t', default='Hello from fileopr.py\n', help='写入或追加的文本')
    args = parser.parse_args()

    path = Path(args.path)

    if args.mode in ('read', 'manual') and not path.exists():
        print(f"文件不存在: {path}")
        sys.exit(1)

    if args.mode == 'read':
        print('--- 使用 with 上下文读取文件（自动 close） ---')
        content = read_with_context(path)
        print(content)

    elif args.mode == 'manual':
        print('--- 手动 open/close 读取（确保 finally 中 close） ---')
        content = read_manual(path)
        print(content)

    elif args.mode == 'write':
        print(f"--- 写入（覆盖）到 {path} ---")
        write_with_context(path, args.text)
        print('写入完成。')

    elif args.mode == 'append':
        print(f"--- 追加写入到 {path} ---")
        append_with_context(path, args.text)
        print('追加完成。')


if __name__ == '__main__':
    main()
