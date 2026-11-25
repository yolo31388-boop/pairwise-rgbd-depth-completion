# pairwise-rgbd-depth-completion

## 领域

游戏、图形与多媒体

## 主题

RGB-D 深度补全与彩色引导

## 说明

时空对齐、孔洞置信传播、边缘感知引导。

初始状态下 `imaging/rgbd_depth.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
