<h1 align="center">Deep-Live-Cam</h1>

<p align="center">
  一键实时人脸替换和视频深度伪造，仅需单张图片。
</p>

<p align="center">
<a href="https://trendshift.io/repositories/11395" target="_blank"><img src="https://trendshift.io/api/badge/repositories/11395" alt="hacksider%2FDeep-Live-Cam | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
  <img src="media/demo.gif" alt="演示 GIF" width="800">
</p>

## 免责声明

这款深度伪造软件旨在成为 AI 生成媒体行业的生产力工具。它可以帮助艺术家制作自定义角色动画、创建引人入胜的内容，甚至用于服装设计的模特展示。

我们意识到可能存在不道德应用的风险，并致力于采取预防措施。内置检查功能可防止程序处理不当媒体（裸体、暴力内容、战争镜头等敏感材料）。我们将继续负责任地开发这个项目，遵守法律和道德规范。如果法律要求，我们可能会关闭项目或添加水印。

- 道德使用：用户应负责任且合法地使用此软件。如果使用真人面孔，请获得其同意，并在网上分享时明确标注任何输出为深度伪造内容。

- 内容限制：软件包含内置检查功能，防止处理不当媒体，如裸体、暴力内容或敏感材料。

- 法律合规：我们遵守所有相关法律和道德准则。如果法律要求，我们可能会关闭项目或在输出中添加水印。

- 用户责任：我们不对最终用户的行为负责。用户必须确保其使用软件的方式符合道德标准和法律要求。

使用此软件即表示您同意这些条款，并承诺以尊重他人权利和尊严的方式使用它。

用户应负责任且合法地使用此软件。如果使用真人面孔，请获得其同意，并在网上分享时明确标注任何输出为深度伪造内容。我们不对最终用户的行为负责。

## 独家 v2.3 快速开始 - 预构建版本（Windows/Mac Silicon）

  <a href="https://deeplivecam.net/index.php/quickstart"> <img src="media/Download.png" width="285" height="77" />

##### 如果您拥有独立的 NVIDIA 或 AMD GPU 或 Mac Silicon，这是您能获得的最快构建版本，并且您将获得特殊优先支持。
 
###### 这些预构建版本非常适合非技术用户或没有时间或无法手动安装所有要求的用户。提醒一下：这是一个开源项目，所以您也可以手动安装。

## 简而言之：仅需 3 次点击即可实现实时深度伪造
![简单步骤](https://github.com/user-attachments/assets/af825228-852c-411b-b787-ffd9aac72fc6)
1. 选择一张面孔
2. 选择要使用的摄像头
3. 按下实时！

## 功能和用途 - 一切都是实时的

### 嘴部遮罩

**使用嘴部遮罩保留您的原始嘴部以实现准确的动作**

<p align="center">
  <img src="media/ludwig.gif" alt="可调整大小的gif">
</p>

### 人脸映射

**在多个主体上同时使用不同的面孔**

<p align="center">
  <img src="media/streamers.gif" alt="人脸映射源">
</p>

### 您的电影，您的面孔

**实时观看任何面孔的电影**

<p align="center">
  <img src="media/movie.gif" alt="电影">
</p>

### 现场表演

**运行现场表演和演出**

<p align="center">
  <img src="media/live_show.gif" alt="表演">
</p>

### 表情包

**创建您最病毒式的表情包**

<p align="center">
  <img src="media/meme.gif" alt="表演" width="450"> 
  <br>
  <sub>使用 Deep-Live-Cam 的多面孔功能创建</sub>
</p>

### Omegle

**在 Omegle 上给人们惊喜**

<p align="center">
  <video src="https://github.com/user-attachments/assets/2e9b9b82-fa04-4b70-9f56-b1f68e7672d0" width="450" controls></video>
</p>

## 安装（手动）

**请注意，安装需要技术技能，不适合初学者。请考虑下载快速开始版本。**

<details>
<summary>点击查看过程</summary>

### 安装

这更可能在您的计算机上工作，但会更慢，因为它使用 CPU。

**1. 设置您的平台**

-   Python（推荐 3.11）
-   pip
-   git
-   [ffmpeg](https://www.youtube.com/watch?v=OlNWCpFdVMA) - ```iex (irm ffmpeg.tc.ht)```
-   [Visual Studio 2022 运行时（Windows）](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

**2. 克隆仓库**

```bash
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam
```

**3. 下载模型**

1. [GFPGANv1.4](https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth)
2. [inswapper\_128\_fp16.onnx](https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx)

将这些文件放在"**models**"文件夹中。

**4. 安装依赖项**

我们强烈建议使用 `venv` 来避免问题。

对于 Windows：
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
对于 Linux：
```bash
# 确保您使用已安装的 Python 3.10
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**对于 macOS：**

Apple Silicon（M1/M2/M3）需要特定设置：

```bash
# 安装 Python 3.11（特定版本很重要）
brew install python@3.11

# 安装 tkinter 包（GUI 所需）
brew install python-tk@3.10

# 使用 Python 3.11 创建并激活虚拟环境
python3.10 -m venv venv
source venv/bin/activate

# 安装依赖项
pip install -r requirements.txt
```

** 如果出现问题需要重新安装虚拟环境 **

```bash
# 停用虚拟环境
rm -rf venv

# 重新安装虚拟环境
python -m venv venv
source venv/bin/activate

# 再次安装依赖项
pip install -r requirements.txt

# gfpgan 和 basicsrs 问题修复
pip install git+https://github.com/xinntao/BasicSR.git@master
pip uninstall gfpgan -y
pip install git+https://github.com/TencentARC/GFPGAN.git@master
```

**运行：** 如果您没有 GPU，可以使用 `python run.py` 运行 Deep-Live-Cam。请注意，首次执行将下载模型（约 300MB）。

### GPU 加速

**CUDA 执行提供程序（Nvidia）**

1. 安装 [CUDA Toolkit 12.8.0](https://developer.nvidia.com/cuda-12-8-0-download-archive)
2. 安装 [cuDNN v8.9.7 for CUDA 12.x](https://developer.nvidia.com/rdp/cudnn-archive)（onnxruntime-gpu 所需）：
   - 下载 cuDNN v8.9.7 for CUDA 12.x
   - 确保 cuDNN bin 目录在您的系统 PATH 中
3. 安装依赖项：

```bash
pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu==1.21.0
```

3. 使用：

```bash
python run.py --execution-provider cuda
```

**CoreML 执行提供程序（Apple Silicon）**

Apple Silicon（M1/M2/M3）特定安装：

1. 确保您已使用 Python 3.11 完成上述 macOS 设置。
2. 安装依赖项：

```bash
pip uninstall onnxruntime onnxruntime-silicon
pip install onnxruntime==1.21.0
```

3. 使用：

```bash
python3.11 run.py --execution-provider coreml
```

**macOS 重要注意事项：**
- 您**必须**使用 Python 3.11，这是推荐的版本
- 如果您遇到 `_tkinter` 缺失错误，请重新安装 tkinter 包：`brew reinstall python-tk@3.11`
- 如果您遇到模型加载错误，请检查您的模型是否在正确的文件夹中
- 如果您遇到与其他 Python 版本的冲突，请考虑卸载它们：
  ```bash
  # 列出所有已安装的 Python 版本
  brew list | grep python
  
  # 如果需要，卸载冲突版本
  brew uninstall --ignore-dependencies python@3.10 python@3.13
  
  # 仅保留 Python 3.11
  brew cleanup
  ```

**CoreML 执行提供程序（Apple Legacy）**

1. 安装依赖项：

```bash
pip uninstall onnxruntime onnxruntime-coreml
pip install onnxruntime-coreml==1.21.0
```

2. 使用：

```bash
python run.py --execution-provider coreml
```

**DirectML 执行提供程序（Windows）**

1. 安装依赖项：

```bash
pip uninstall onnxruntime onnxruntime-directml
pip install onnxruntime-directml==1.21.0
```

2. 使用：

```bash
python run.py --execution-provider directml
```

**OpenVINO™ 执行提供程序（Intel）**

1. 安装依赖项：

```bash
pip uninstall onnxruntime onnxruntime-openvino
pip install onnxruntime-openvino==1.21.0
```

2. 使用：

```bash
python run.py --execution-provider openvino
```
</details>

## 使用方法

**1. 图像/视频模式**

-   执行 `python run.py`。
-   选择源面孔图像和目标图像/视频。
-   点击"开始"。
-   输出将保存在以目标视频命名的目录中。

**2. 网络摄像头模式**

-   执行 `python run.py`。
-   选择源面孔图像。
-   点击"实时"。
-   等待预览出现（10-30 秒）。
-   使用 OBS 等屏幕捕获工具进行流媒体传输。
-   要更改面孔，请选择新的源图像。

## 命令行参数（未维护）

```
选项：
  -h, --help                                               显示此帮助消息并退出
  -s SOURCE_PATH, --source SOURCE_PATH                     选择源图像
  -t TARGET_PATH, --target TARGET_PATH                     选择目标图像或视频
  -o OUTPUT_PATH, --output OUTPUT_PATH                     选择输出文件或目录
  --frame-processor FRAME_PROCESSOR [FRAME_PROCESSOR ...]  帧处理器（选择：face_swapper、face_enhancer 等）
  --keep-fps                                               保持原始 fps
  --keep-audio                                             保持原始音频
  --keep-frames                                            保持临时帧
  --many-faces                                             处理每张面孔
  --map-faces                                              映射源目标面孔
  --mouth-mask                                             遮罩嘴部区域
  --video-encoder {libx264,libx265,libvpx-vp9}             调整输出视频编码器
  --video-quality [0-51]                                   调整输出视频质量
  --live-mirror                                            实时摄像头显示如您在前置摄像头框架中看到的那样
  --live-resizable                                         实时摄像头框架可调整大小
  --max-memory MAX_MEMORY                                  最大 RAM 量（GB）
  --execution-provider {cpu} [{cpu} ...]                   可用执行提供程序（选择：cpu 等）
  --execution-threads EXECUTION_THREADS                    执行线程数
  -v, --version                                            显示程序版本号并退出
```

寻找 CLI 模式？使用 -s/--source 参数将使运行程序进入 cli 模式。

## 媒体报道

**我们始终对批评持开放态度，并准备改进，这就是为什么我们没有挑选任何内容。**

 - [*"Deep-Live-Cam 走红，让任何人都能成为数字分身"*](https://arstechnica.com/information-technology/2024/08/new-ai-tool-enables-real-time-face-swapping-on-webcams-raising-fraud-concerns/) - Ars Technica
 - [*"感谢 Deep Live Cam，变形者现在就在我们中间"*](https://dataconomy.com/2024/08/15/what-is-deep-live-cam-github-deepfake/) - Dataconomy
 - [*"这个免费的 AI 工具让您在视频通话中成为任何人"*](https://www.newsbytesapp.com/news/science/deep-live-cam-ai-impersonation-tool-goes-viral/story) - NewsBytes
 - [*"好吧，这个病毒式 AI 直播软件真的很可怕"*](https://www.creativebloq.com/ai/ok-this-viral-ai-live-stream-software-is-truly-terrifying) - Creative Bloq
 - [*"深度伪造 AI 工具让您用单张照片在视频通话中成为任何人"*](https://petapixel.com/2024/08/14/deep-live-cam-deepfake-ai-tool-lets-you-become-anyone-in-a-video-call-with-single-photo-mark-zuckerberg-jd-vance-elon-musk/) - PetaPixel
 - [*"Deep-Live-Cam 使用 AI 实时变换您的面孔，包括名人"*](https://www.techeblog.com/deep-live-cam-ai-transform-face/) - TechEBlog
 - [*"一个让您在视频通话中'看起来像任何人'的 AI 工具在网上走红"*](https://telegrafi.com/en/a-tool-that-makes-you-look-like-anyone-during-a-video-call-is-going-viral-on-the-Internet/) - Telegrafi
 - [*"这个将图像转换为直播的深度伪造工具正在 GitHub 排行榜上名列前茅"*](https://decrypt.co/244565/this-deepfake-tool-turning-images-into-livestreams-is-topping-the-github-charts) - Emerge
 - [*"新的实时人脸替换 AI 允许任何人模仿名人面孔"*](https://www.digitalmusicnews.com/2024/08/15/face-swapping-ai-real-time-mimic/) - Digital Music News
 - [*"这个实时网络摄像头深度伪造工具引发了对身份盗用未来的担忧"*](https://www.diyphotography.net/this-real-time-webcam-deepfake-tool-raises-alarms-about-the-future-of-identity-theft/) - DIYPhotography
 - [*"太疯狂了，天哪。太他妈诡异了兄弟...太狂野了兄弟"*](https://www.youtube.com/watch?time_continue=1074&v=py4Tc-Y8BcY) - SomeOrdinaryGamers
 - [*"好吧看看看，现在看聊天，我们可以做任何我们想要看起来像的面孔聊天"*](https://www.youtube.com/live/mFsCe7AIxq8?feature=shared&t=2686) - IShowSpeed
 - [*"他们在匹配姿势、表情甚至光线方面做得很好"*](https://www.youtube.com/watch?v=wnCghLjqv3s&t=551s) - TechLinked (LTT)
 - [*"Als Sean Connery an der Redaktionskonferenz teilnahm"*](https://www.golem.de/news/deepfakes-als-sean-connery-an-der-redaktionskonferenz-teilnahm-2408-188172.html) - Golem.de（德语）

## 致谢

-   [ffmpeg](https://ffmpeg.org/)：使视频相关操作变得简单
-   [deepinsight](https://github.com/deepinsight)：感谢他们的 [insightface](https://github.com/deepinsight/insightface) 项目，提供了制作精良的库和模型。请注意，[模型的使用仅限于非商业研究目的](https://github.com/deepinsight/insightface?tab=readme-ov-file#license)。
-   [havok2-htwo](https://github.com/havok2-htwo)：分享网络摄像头代码
-   [GosuDRM](https://github.com/GosuDRM)：提供 roop 的开放版本
-   [pereiraroland26](https://github.com/pereiraroland26)：多面孔支持
-   [vic4key](https://github.com/vic4key)：支持/贡献此项目
-   [kier007](https://github.com/kier007)：改善用户体验
-   [qitianai](https://github.com/qitianai)：多语言支持
-   以及此项目中使用的库背后的[所有开发者](https://github.com/hacksider/Deep-Live-Cam/graphs/contributors)。
-   脚注：请注意，代码的基础作者是 [s0md3v](https://github.com/s0md3v/roop)
-   所有通过为仓库加星来帮助这个项目走红的精彩用户 ❤️

[![Stargazers](https://reporoster.com/stars/hacksider/Deep-Live-Cam)](https://github.com/hacksider/Deep-Live-Cam/stargazers)

## 贡献

![Alt](https://repobeats.axiom.co/api/embed/fec8e29c45dfdb9c5916f3a7830e1249308d20e1.svg "Repobeats 分析图像")

## 星星飞向月球 🚀

<a href="https://star-history.com/#hacksider/deep-live-cam&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=hacksider/deep-live-cam&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=hacksider/deep-live-cam&type=Date" />
   <img alt="星星历史图表" src="https://api.star-history.com/svg?repos=hacksider/deep-live-cam&type=Date" />
 </picture>
</a>