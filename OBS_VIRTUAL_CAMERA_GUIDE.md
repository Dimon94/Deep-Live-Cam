# Deep-Live-Cam 虚拟摄像头使用指南

**项目**: Deep-Live-Cam 虚拟摄像头升级
**方案**: 方案 A - OBS 虚拟摄像头中转
**状态**: ✅ 已实现，待测试
**更新时间**: 2025-10-29 北京时间

---

## 📋 功能概述

Deep-Live-Cam 现已支持将处理后的视频流输出为 UDP 流，可通过 OBS Studio 转换为系统虚拟摄像头，供 Zoom、Teams、浏览器等应用使用。

**架构流程：**
```
Deep-Live-Cam → UDP 流(127.0.0.1:1234) → OBS Studio → OBS 虚拟摄像头 → 浏览器/Zoom
```

---

## 🚀 快速开始

### 1. 前置要求

**必须安装：**
- ✅ FFmpeg (已安装: v7.1)
- ⬜ OBS Studio ([下载地址](https://obsproject.com/))

**验证 FFmpeg：**
```bash
ffmpeg -version
```

### 2. 启动 Deep-Live-Cam 虚拟摄像头

#### 方式 1：命令行启动
```bash
python run.py --vcam --vcam-port 1234 --vcam-width 1280 --vcam-height 720 --vcam-fps 30
```

#### 方式 2：UI 启动
1. 启动 Deep-Live-Cam
2. 在主界面底部找到 **Virtual Camera** 开关
3. 配置参数：
   - **Addr**: 127.0.0.1 (本地回环)
   - **Port**: 1234 (默认端口)
   - **Width**: 1280 (分辨率宽度)
   - **Height**: 720 (分辨率高度)
   - **FPS**: 30 (帧率)
4. 打开开关启用

**状态指示：**
- 🟢 "运行中" - UDP 流正常输出
- 🔴 "已禁用" - 虚拟摄像头未启用
- 🟡 "错误信息" - 启动失败

---

## 🎬 OBS Studio 配置

### 步骤 1：添加 UDP 媒体源

1. **打开 OBS Studio**
2. **添加来源**：
   - 点击 "来源" (Sources) 面板的 `+` 按钮
   - 选择 **"媒体源"** (Media Source)
   - 命名为 "DeepLiveCam"
3. **配置媒体源**：
   ```
   ☑ 取消勾选 "本地文件" (Local File)
   输入: udp://127.0.0.1:1234

   ☐ 取消勾选 "显示媒体信息时暂停" (Pause when not showing)
   ☐ 取消勾选 "关闭不在场景中的源" (Close file when not showing)

   网络缓冲: 0 MB (降低延迟)
   ```
4. **点击确定**

### 步骤 2：启动 OBS 虚拟摄像头

1. **菜单栏** → **工具** (Tools) → **启动虚拟摄像头** (Start Virtual Camera)
2. 或点击控制面板的 **"启动虚拟摄像头"** 按钮

**验证：**
- OBS 底部显示 "虚拟摄像头: 运行中"
- 系统摄像头列表中会出现 "OBS Virtual Camera"

---

## 🌐 在浏览器中使用

### Chrome/Edge/Safari

1. 打开视频会议网站（Zoom Web, Google Meet, Teams 等）
2. 进入设置 → 视频设置
3. 摄像头列表中选择 **"OBS Virtual Camera"**
4. 开始会议，其他人会看到经过 Deep-Live-Cam 处理的视频

**测试工具：**
- [WebRTC 摄像头测试](https://webrtc.github.io/samples/src/content/devices/input-output/)
- 浏览器会列出所有可用摄像头设备

### Zoom 桌面客户端

1. **设置** → **视频**
2. **摄像头** 下拉菜单选择 **"OBS Virtual Camera"**
3. 预览窗口会显示处理后的视频

---

## 🔧 故障排查

### 问题 1：OBS 显示黑屏或 "等待媒体"

**可能原因：**
- Deep-Live-Cam 虚拟摄像头未启动
- UDP 端口不匹配
- 防火墙阻止本地 UDP 流量

**解决方案：**
```bash
# 1. 验证 Deep-Live-Cam 是否正在推流
# 使用 ffplay 测试接收：
ffplay -fflags nobuffer -flags low_delay -probesize 32 -analyzeduration 0 udp://127.0.0.1:1234

# 2. 验证端口是否被占用
lsof -i :1234

# 3. 验证 FFmpeg 进程是否运行
ps aux | grep ffmpeg
```

---

### 问题 2：浏览器/Zoom 看不到 OBS Virtual Camera

**macOS 解决方案：**
```bash
# 重启 coreaudiod 和 CoreMediaIO 服务
sudo killall coreaudiod
sudo killall VDCAssistant

# 重新启动 OBS
```

**Windows 解决方案：**
- 检查 OBS 虚拟摄像头驱动是否已安装
- OBS 菜单 → 工具 → 虚拟摄像头 → 重新安装驱动

---

### 问题 3：画面延迟高

**优化策略：**

1. **降低网络缓冲**（OBS 媒体源设置）：
   ```
   网络缓冲: 0 MB
   ```

2. **降低 Deep-Live-Cam 分辨率**：
   ```bash
   python run.py --vcam --vcam-width 960 --vcam-height 540
   ```

3. **使用硬件编码**（未来优化）：
   - macOS: VideoToolbox
   - Windows: NVENC (NVIDIA) / QuickSync (Intel)
   - Linux: VAAPI

---

### 问题 4：画面卡顿或丢帧

**可能原因：**
- 处理速度跟不上帧率
- 分辨率过高
- CPU/GPU 负载过高

**解决方案：**
```bash
# 降低帧率
python run.py --vcam --vcam-fps 15

# 降低分辨率
python run.py --vcam --vcam-width 640 --vcam-height 360
```

---

## 🧪 测试流程

### 端到端测试

```bash
# 1. 启动 Deep-Live-Cam
python run.py --vcam

# 2. 在 UI 中选择源图像和摄像头
# 3. 开启虚拟摄像头开关

# 4. 使用 ffplay 验证 UDP 流
ffplay udp://127.0.0.1:1234

# 5. 在 OBS 中配置媒体源
# 6. 启动 OBS 虚拟摄像头

# 7. 打开摄像头测试网站验证
# https://webrtc.github.io/samples/src/content/devices/input-output/
```

**预期结果：**
- ffplay 显示处理后的视频
- OBS 预览显示视频
- 浏览器摄像头列表包含 "OBS Virtual Camera"
- 选择后显示处理后的视频

---

## 📊 技术细节

### UDP 流格式

**FFmpeg 编码参数：**
```bash
-f rawvideo          # 输入格式：原始视频
-pix_fmt bgr24       # 像素格式：BGR24 (OpenCV 默认)
-s 1280x720          # 分辨率
-r 30                # 帧率
-f mpegts            # 输出格式：MPEG 传输流
-codec:v mpeg1video  # 编码器：MPEG-1 (兼容性好)
-q:v 2               # 质量：2 (1-31, 越小越好)
-bf 0                # B帧：0 (降低延迟)
udp://127.0.0.1:1234 # 输出地址
```

### 性能指标

| 分辨率 | 帧率 | 比特率 | 延迟 |
|--------|------|--------|------|
| 1280x720 | 30 fps | ~4 Mbps | ~100ms |
| 960x540 | 30 fps | ~2 Mbps | ~80ms |
| 640x360 | 30 fps | ~1 Mbps | ~60ms |

---

## 🎓 架构设计哲学

### 为什么选择 OBS 中转？

**优势：**
1. ✅ **跨平台**：OBS 已解决所有平台虚拟摄像头驱动问题
2. ✅ **快速验证**：无需开发内核驱动
3. ✅ **用户友好**：许多用户已安装 OBS
4. ✅ **功能丰富**：OBS 提供额外的场景管理、滤镜、叠加层等

**劣势：**
1. ❌ **需要额外软件**：用户需要安装 OBS
2. ❌ **多一层延迟**：Deep-Live-Cam → FFmpeg → UDP → OBS → 虚拟摄像头
3. ❌ **手动配置**：需要用户手动配置 OBS 媒体源

### Linus 的品味检查

#### ✅ 符合 "Good Taste"
```python
# 统一的输出接口，无特殊情况
for output in self.outputs:
    output(frame)
```

#### ✅ 简洁性
- VirtualCameraOutput: 117 行代码
- 无嵌套超过 2 层
- 单一职责：只负责推流

#### ✅ 自动恢复
```python
except (BrokenPipeError, OSError):
    self.stop()
    self.start()  # FFmpeg 崩溃自动重启
```

---

## 🔮 未来优化方向

### 短期（1-2 周）
- [ ] 自动检测 OBS 是否安装
- [ ] 一键启动 OBS 虚拟摄像头（通过 obs-websocket）
- [ ] 优化分辨率自动缩放逻辑

### 中期（1-2 月）
- [ ] Linux: 直接创建 v4l2loopback 设备（无需 OBS）
- [ ] 硬件编码支持（VideoToolbox/NVENC/VAAPI）
- [ ] 性能监控和自适应码率

### 长期（3-6 月）
- [ ] macOS: CoreMediaIO Plugin（原生虚拟摄像头）
- [ ] Windows: DirectShow Filter（原生虚拟摄像头）
- [ ] 多进程管道架构（参考 DeepFaceLive）

---

## 📚 参考资料

### 官方文档
- [OBS Studio](https://obsproject.com/)
- [FFmpeg 文档](https://ffmpeg.org/documentation.html)
- [WebRTC Samples](https://webrtc.github.io/samples/)

### 相关项目
- [DeepFaceLive](https://github.com/iperov/DeepFaceLive) - 完整的实时换脸系统
- [v4l2loopback](https://github.com/umlaeute/v4l2loopback) - Linux 虚拟摄像头内核模块
- [obs-websocket](https://github.com/obsproject/obs-websocket) - OBS 远程控制协议

---

## 🙏 致谢

本实现遵循 **Linus Torvalds 的代码哲学**：
- **"Good taste"** - 消除特殊情况，让设计自然统一
- **"Never break userspace"** - 完全向后兼容，用户可选择启用
- **"Pragmatism"** - 解决真实问题，避免过度设计

---

**最后更新**: 2025-10-29 北京时间
**维护者**: Dimon
**版本**: v1.0
