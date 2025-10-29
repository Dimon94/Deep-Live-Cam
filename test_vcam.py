#!/usr/bin/env python3
"""
虚拟摄像头功能测试脚本

用途：
1. 验证 VirtualCameraOutput 是否正常工作
2. 测试 UDP 流是否正常发送
3. 生成测试模式视频帧

使用方法：
    python test_vcam.py

验证方法：
    # 在另一个终端运行 ffplay 接收：
    ffplay -fflags nobuffer -flags low_delay udp://127.0.0.1:1234
"""

import sys
import time
import numpy as np
import cv2

# 导入虚拟摄像头模块
from modules.outputs import VirtualCameraOutput


def generate_test_frame(width: int, height: int, frame_number: int) -> np.ndarray:
    """
    生成测试模式帧

    Args:
        width: 帧宽度
        height: 帧高度
        frame_number: 帧序号（用于动画）

    Returns:
        BGR24 格式的帧
    """
    # 创建黑色背景
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # 绘制彩色条纹（模拟电视测试卡）
    colors = [
        (255, 255, 255),  # 白色
        (0, 255, 255),    # 黄色
        (255, 255, 0),    # 青色
        (0, 255, 0),      # 绿色
        (255, 0, 255),    # 品红
        (0, 0, 255),      # 红色
        (255, 0, 0),      # 蓝色
        (0, 0, 0),        # 黑色
    ]

    stripe_width = width // len(colors)
    for i, color in enumerate(colors):
        x1 = i * stripe_width
        x2 = (i + 1) * stripe_width if i < len(colors) - 1 else width
        frame[:, x1:x2] = color

    # 绘制移动的白色圆圈（验证帧更新）
    circle_x = int((frame_number * 10) % width)
    circle_y = height // 2
    cv2.circle(frame, (circle_x, circle_y), 50, (255, 255, 255), -1)

    # 绘制帧计数文本
    text = f"Frame: {frame_number}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 2, 3)[0]
    text_x = (width - text_size[0]) // 2
    text_y = height - 100

    # 黑色描边
    cv2.putText(frame, text, (text_x, text_y), font, 2, (0, 0, 0), 8)
    # 白色文字
    cv2.putText(frame, text, (text_x, text_y), font, 2, (255, 255, 255), 3)

    return frame


def test_virtual_camera(
    width: int = 1280,
    height: int = 720,
    fps: int = 30,
    duration: int = 30,
    addr: str = "127.0.0.1",
    port: int = 1234,
) -> None:
    """
    测试虚拟摄像头输出

    Args:
        width: 分辨率宽度
        height: 分辨率高度
        fps: 帧率
        duration: 测试持续时间（秒）
        addr: UDP 地址
        port: UDP 端口
    """
    print("=" * 80)
    print("Deep-Live-Cam 虚拟摄像头测试")
    print("=" * 80)
    print(f"\n配置:")
    print(f"  分辨率: {width}x{height}")
    print(f"  帧率: {fps} fps")
    print(f"  UDP: {addr}:{port}")
    print(f"  持续时间: {duration} 秒")
    print(f"\n验证方法:")
    print(f"  在另一个终端运行:")
    print(f"  $ ffplay -fflags nobuffer -flags low_delay udp://{addr}:{port}")
    print("\n" + "=" * 80)

    # 创建虚拟摄像头输出
    print("\n[1/3] 初始化 VirtualCameraOutput...")
    try:
        vcam = VirtualCameraOutput(
            width=width,
            height=height,
            addr=addr,
            port=port,
            fps=fps,
        )
        print("  ✅ VirtualCameraOutput 创建成功")
    except Exception as e:
        print(f"  ❌ 初始化失败: {e}")
        return

    # 启动 FFmpeg 进程
    print("\n[2/3] 启动 FFmpeg 进程...")
    try:
        vcam.start()
        print("  ✅ FFmpeg 进程启动成功")
    except Exception as e:
        print(f"  ❌ FFmpeg 启动失败: {e}")
        return

    # 推送测试帧
    print(f"\n[3/3] 推送测试帧 ({duration} 秒)...")
    print("  提示: 按 Ctrl+C 提前停止\n")

    frame_interval = 1.0 / fps
    total_frames = duration * fps
    frame_number = 0

    try:
        start_time = time.time()
        next_frame_time = start_time

        while frame_number < total_frames:
            # 生成测试帧
            frame = generate_test_frame(width, height, frame_number)

            # 推送到虚拟摄像头
            try:
                vcam.push_frame(frame)
            except Exception as e:
                print(f"  ⚠️  推送帧失败: {e}")
                break

            frame_number += 1

            # 进度显示
            if frame_number % (fps * 5) == 0:
                elapsed = time.time() - start_time
                progress = (frame_number / total_frames) * 100
                print(f"  进度: {progress:.1f}% ({frame_number}/{total_frames} 帧, "
                      f"{elapsed:.1f}s)")

            # 帧率控制
            next_frame_time += frame_interval
            sleep_time = next_frame_time - time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)

        # 统计信息
        elapsed = time.time() - start_time
        actual_fps = frame_number / elapsed if elapsed > 0 else 0

        print(f"\n  ✅ 测试完成")
        print(f"  总帧数: {frame_number}")
        print(f"  总时长: {elapsed:.2f} 秒")
        print(f"  实际帧率: {actual_fps:.2f} fps (目标: {fps} fps)")

    except KeyboardInterrupt:
        print("\n\n  ⚠️  用户中断测试")
    except Exception as e:
        print(f"\n  ❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # 停止虚拟摄像头
        print("\n[清理] 停止 FFmpeg 进程...")
        vcam.stop()
        print("  ✅ 清理完成")

    print("\n" + "=" * 80)
    print("测试结束")
    print("=" * 80)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="测试虚拟摄像头功能")
    parser.add_argument(
        "--width",
        type=int,
        default=1280,
        help="分辨率宽度 (默认: 1280)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=720,
        help="分辨率高度 (默认: 720)",
    )
    parser.add_argument(
        "--fps",
        type=int,
        default=30,
        help="帧率 (默认: 30)",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=30,
        help="测试持续时间（秒，默认: 30）",
    )
    parser.add_argument(
        "--addr",
        type=str,
        default="127.0.0.1",
        help="UDP 地址 (默认: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=1234,
        help="UDP 端口 (默认: 1234)",
    )

    args = parser.parse_args()

    test_virtual_camera(
        width=args.width,
        height=args.height,
        fps=args.fps,
        duration=args.duration,
        addr=args.addr,
        port=args.port,
    )
